#-------------------------------------------------------------------------
#
#   Copyright (c) 2017, J. Michael Beaver
#
#   This software may be distributed in accordance with the MIT License.
#   See the accompanying LICENSE or https://opensource.org/licenses/MIT.
#
#-------------------------------------------------------------------------
#
#   This code uses a custom implementation of Base64 to solve:
#   https://cryptopals.com/sets/1/challenges/1.
#
#   The hex string
#
#      49276d206b696c6c696e6720796f757220627261696e206c
#      696b65206120706f69736f6e6f7573206d757368726f6f6d
#
#   is provided, but it's referred to simply as a 'string'. My
#   implementation of Base64 takes either an ASCII string or a list of
#   bytes, not a string of bytes. It wouldn't know how to distinguish.
#   Thus, the hardcoded string here is the ASCII equivalent of the
#   hex string.
#
#   No claims are made on the efficiency of this code.
#
#   Changelog:
#       2017 02 16  Initial version.
#
#-------------------------------------------------------------------------


from Base64 import Base64


#-------------------------------------------------------------------------


if __name__ == '__main__':
    b64 = Base64()
    bytes = b64.ascii_to_bytes("I'm killing your brain like a poisonous mushroom")
    
    try:
        b64_output = b64.encode(bytes)
        print b64.bytes_to_ascii(b64_output)
    except:
        print 'Failed to encode!'

    try:
        asc_output = b64.decode(b64_output)
        print b64.bytes_to_ascii(asc_output)
    except:
        print 'Failed to decode!'

    
    
    
