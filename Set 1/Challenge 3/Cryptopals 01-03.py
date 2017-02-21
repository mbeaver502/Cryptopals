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
#   https://cryptopals.com/sets/1/challenges/3.
#
#   This version is naive bruteforce. A statistical/frequency version is
#   forthcoming.
#
#   No claims are made on the efficiency of this code.
#
#   Changelog:
#       2017 02 20  Initial version.
#
#-------------------------------------------------------------------------


from xor import XOR


#-------------------------------------------------------------------------


if __name__ == '__main__':
    xor = XOR()
    key     = 0x01 # No need to start at 0x00 since XX XOR 00 = XX
    message = [ 0x1b , 0x37 , 0x37 , 0x33 , 0x31 , 0x36 , 0x3f , 0x78 , 
                0x15 , 0x1b , 0x7f , 0x2b , 0x78 , 0x34 , 0x31 , 0x33 , 
                0x3d , 0x78 , 0x39 , 0x78 , 0x28 , 0x37 , 0x2d , 0x36 , 
                0x3c , 0x78 , 0x37 , 0x3e , 0x78 , 0x3a , 0x39 , 0x3b ,
                0x37 , 0x36 ]

    # Bruteforce method
    try:
        while key <= 0xFF:
            xor_output = []
            for i in range(len(message)):
                xor_output.append(message[i] ^ key)
            print "%X \t %s" % (key, xor.bytes_to_ascii(xor_output))
            key += 0x01
        
    except:
        print 'Failed to encode!'


    
    
    
