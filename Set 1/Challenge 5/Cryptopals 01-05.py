#-------------------------------------------------------------------------
#
#   Copyright (c) 2017, J. Michael Beaver
#
#   This software may be distributed in accordance with the MIT License.
#   See the accompanying LICENSE or https://opensource.org/licenses/MIT.
#
#-------------------------------------------------------------------------
#
#   This code attempts to solve: https://cryptopals.com/sets/1/challenges/5.
#
#   This is a simple repeating XOR encryption scheme.
#
#   No claims are made on the efficiency of this code.
#
#   Changelog:
#       2017 03 21  Initial version.
#
#-------------------------------------------------------------------------

def repeating_xor(_bytes, key):
    result = [ ]
    
    if len(_bytes) >= len(key) and len(key) > 0: 
        idx     = 0
        bound   = len(_bytes)
        mod     = len(key)
        
        while idx < bound:
            result.append(_bytes[idx] ^ int(key[idx % mod].encode('hex'), 16))
            idx += 1

    return result

#-------------------------------------------------------------------------

if __name__ == '__main__':
    key     = 'ICE'
    _input  = "Burning 'em, if you ain't quick and nimble\n" \
              "I go crazy when I hear a cymbal"
    _bytes  = [int(elem.encode('hex'), 16) for elem in _input]

    output  = repeating_xor(_bytes, key)
    print ''.join([format(x, '02x') for x in output])
    
    output  = repeating_xor(output, key)
    print ''.join([chr(x) for x in output])
