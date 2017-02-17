#-------------------------------------------------------------------------
#
#   Copyright (c) 2017, J. Michael Beaver
#
#   This software may be distributed in accordance with the MIT License.
#   See the accompanying LICENSE or https://opensource.org/licenses/MIT.
#
#-------------------------------------------------------------------------
#
#   This code uses a custom implementation of fixed-length XOR to solve:
#   https://cryptopals.com/sets/1/challenges/2.
#
#   No claims are made on the efficiency of this code.
#
#   Changelog:
#       2017 02 16  Initial version.
#
#-------------------------------------------------------------------------


from xor import XOR


#-------------------------------------------------------------------------


if __name__ == '__main__':
    xor = XOR()
    key     = [ 0x1c , 0x01 , 0x11 , 0x00 , 0x1f , 0x01 , 0x01 , 0x00 , 0x06 , 0x1a , 0x02 , 0x4b , 0x53 , 0x53 , 0x50 , 0x09 , 0x18 , 0x1c ]
    message = [ 0x68 , 0x69 , 0x74 , 0x20 , 0x74 , 0x68 , 0x65 , 0x20 , 0x62 , 0x75 , 0x6c , 0x6c , 0x27 , 0x73 , 0x20 , 0x65 , 0x79 , 0x65 ]
    
    try:
        xor_output = xor.xor(message, key)
        print xor.bytes_to_ascii(xor_output)
    except:
        print 'Failed to encode!'

    try:
        message = xor.xor(xor_output, key)
        print xor.bytes_to_ascii(message)
    except:
        print 'Failed to decode!'

    
    
    
