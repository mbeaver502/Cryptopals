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
#       2017 02 16  Initial version.
#
#-------------------------------------------------------------------------


class XOR:
    def xor(self, message, key):
        """
        Perform fixed-length XOR encryption and decryption. Input for
        both message and key should be list of bytes. Raises an exception
        if input lengths do not match or if there is no input.
        """
        if ((len(message) < 1 or len(key) < 1) or
            (len(message) != len(key))):
                raise RuntimeError
        
        output = []
        for i in range(len(message)):
            output.append(message[i] ^ key[i])
                
        return output


    def bytes_to_ascii(self, bytes):
        """ Convert a list of bytes to its corresponding ASCII string. """
        output = ''
        for byte in bytes: 
            try:
                output += chr(byte)
            except:
                continue
        return output
    
