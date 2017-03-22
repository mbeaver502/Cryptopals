#-------------------------------------------------------------------------
#
#   Copyright (c) 2017, J. Michael Beaver
#
#   This software may be distributed in accordance with the MIT License.
#   See the accompanying LICENSE or https://opensource.org/licenses/MIT.
#
#-------------------------------------------------------------------------
#
#   This code attempts to solve: https://cryptopals.com/sets/1/challenges/4.
#
#   This version uses simple SHRDLU frequency scoring to determine the key.
#       The guess with the highest score _should_ produce the correct
#       input string and XOR key.
#
#   Answer:
#   7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f
#        Key: 0x35 | Score: 1.3159 | String: nowthatthepartyisjumping
#
#   Note that all the strings in the txt file are the same length,
#       except 1c3df1135321a8e9241a5607f8305d571aa546001e3254555a11511924,
#       which is one byte shorter than the rest.
#
#   No claims are made on the efficiency of this code.
#
#   Changelog:
#       2017 03 20  Initial version.
#
#-------------------------------------------------------------------------

# Courtesy of http://www.rinkworks.com/words/letterfreq.shtml
SHRDLU = {
        'e': 0.1142,
        'a': 0.0856,
        'i': 0.0794,
        'r': 0.0751,
        't': 0.0746,
        'o': 0.0712,
        'n': 0.0641,
        's': 0.0555,
        'l': 0.0552,
        'c': 0.0474,
        'u': 0.0366,
        'p': 0.0327,
        'm': 0.0322,
        'd': 0.0313,
        'h': 0.0276,
        'g': 0.0230,
        'b': 0.0212,
        'y': 0.0200,
        'f': 0.0147,
        'v': 0.0107,
        'w': 0.0094,
        'k': 0.0084,
        'x': 0.0035,
        'z': 0.0024,
        'q': 0.0023,
        'j': 0.0015
        }

#----------------------------------------------------------------------------------

def gen_guesses(_bytes):
    len_bytes = len(_bytes)
    guesses = { }

    # Assuming Latin ASCII alphabet
    # Constant time: 0x80 - 0x20 = 0x60 iterations
    # Worst case O(c * n) => c * O(n) => O(n)
    for key in range(0x20, 0x80):
        guess = [ ]
        score = 0
                
        # Worst case O(n), where n = # of bytes
        for i in range(len_bytes):
            xbyte = int(_bytes[i], 16) ^ key
                        
            # Broad bounds for Latin ASCII alphanumericspecial chars
            if xbyte < 0x20 or xbyte > 0x7E: 
                    break
                        
            letter = chr(xbyte).lower()
            if letter in SHRDLU.keys():
                    score += SHRDLU[letter]
                    guess.append(letter)
                
        if len(guess) > 0 and score > 0: 
                guesses[key] = (score, guess)
                        
    return guesses
		
#----------------------------------------------------------------------------------

def highest_score(guesses):
    key = 0
    high = 0
    for guess in guesses.keys():
        score = guesses[guess][0]
        if score > high: 
                key = guess
                high = score
    return key

#----------------------------------------------------------------------------------

if __name__ == '__main__':
    with open('4.txt', 'r') as f:
        for line in f:
            _input = line.replace('\n', '')
            _input_hex = _input.decode('hex')
            _bytes = [elem.encode('hex') for elem in _input_hex]
            guesses = gen_guesses(_bytes)
            key = highest_score(guesses)
            print _input
            if key > 0 and len(guesses) > 0:
                print "\tKey: {0} | Score: {1} | String: {2}\n".format(hex(key), 
                                                                       guesses[key][0], 
                                                                       ''.join(guesses[key][1]))
            else: print '\tNo solution found!\n'
