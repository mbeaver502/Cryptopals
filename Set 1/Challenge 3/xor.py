#-------------------------------------------------------------------------
#
#   Copyright (c) 2017, J. Michael Beaver
#
#   This software may be distributed in accordance with the MIT License.
#   See the accompanying LICENSE or https://opensource.org/licenses/MIT.
#
#-------------------------------------------------------------------------
#
#   This code is a basic implementation of XOR encryption. It was created
#   in response to: https://cryptopals.com/sets/1/challenges/2.
#
#   No claims are made on the efficiency of this code.
#
#   Changelog:
#       2017 02 20  Modified to XOR individual bytes (redundant given ^).
#       2017 02 16  Initial version.
#
#-------------------------------------------------------------------------


class XOR:
    def xor(self, message, key):
        """
        Perform fixed-length XOR encryption and decryption. Raises an
        exception if input lengths do not match or if there is no input.
        """
        if (message < 0 or key < 0) or (message > 0xFF or key > 0xFF):
            raise RuntimeError
        return message ^ key


    def bytes_to_ascii(self, bytes):
        """ Convert a list of bytes to its corresponding ASCII string. """
        output = ''
        for byte in bytes: 
            try:
                output += chr(byte)
            except:
                continue
        return output
    
