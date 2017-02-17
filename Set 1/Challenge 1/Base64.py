#-------------------------------------------------------------------------
#
#   Copyright (c) 2017, J. Michael Beaver
#
#   This software may be distributed in accordance with the MIT License.
#   See the accompanying LICENSE or https://opensource.org/licenses/MIT.
#
#-------------------------------------------------------------------------
#
#   This code is a basic implementation of Base64. It was created in
#   response to: https://cryptopals.com/sets/1/challenges/1.
#
#   No claims are made on the efficiency of this code. I deduced the
#   bitwise operations/manipulations myself, but I'm sure there are 
#   "better" methods out there.
#
#   Changelog:
#       2017 02 16  Initial version.
#
#-------------------------------------------------------------------------
#
#  +-----------------------------------------------+
#  |               |               |               |
#  |    Input 1    |    Input 2    |    Input 2    |   
#  |               |               |               |
#  +-----------------------------------------------+
#  |0|1|2|3|4|5|6|7|0|1|2|3|4|5|6|7|0|1|2|3|4|5|6|7|
#  +-----------------------------------------------+
#  |           |           |           |           |                 
#  |  Base64 1 |  Base64 1 |  Base64 1 |  Base64 1 |
#  |           |           |           |           |    
#  +-----------------------------------------------+
#
#  Encode: 3 8-bit blocks into 4 6-bit blocks
#  Decode: 4 6-bit blocks into 3 8-bit blocks
#
#-------------------------------------------------------------------------


class Base64:
    
    ascii_table = { ' ': 0x20, '!': 0x21, '"': 0x22, '#': 0x23, '$': 0x24, '%': 0x25, '&': 0x26, 
                    "'": 0x27, '(': 0x28, ')': 0x29, '*': 0x2a, '+': 0x2b, ',': 0x2c, '-': 0x2d, 
                    '.': 0x2e, '/': 0x2f, '0': 0x30, '1': 0x31, '2': 0x32, '3': 0x33, '4': 0x34, 
                    '5': 0x35, '6': 0x36, '7': 0x37, '8': 0x38, '9': 0x39, ':': 0x3a, ';': 0x3b, 
                    '<': 0x3c, '=': 0x3d, '>': 0x3e, '?': 0x3f, '@': 0x40, 'A': 0x41, 'B': 0x42, 
                    'C': 0x43, 'D': 0x44, 'E': 0x45, 'F': 0x46, 'G': 0x47, 'H': 0x48, 'I': 0x49, 
                    'J': 0x4a, 'K': 0x4b, 'L': 0x4c, 'M': 0x4d, 'N': 0x4e, 'O': 0x4f, 'P': 0x50, 
                    'Q': 0x51, 'R': 0x52, 'S': 0x53, 'T': 0x54, 'U': 0x55, 'V': 0x56, 'W': 0x57, 
                    'X': 0x58, 'Y': 0x59, 'Z': 0x5a, '[': 0x5b, '\\': 0x5c, ']': 0x5d, '^': 0x5e, 
                    '_': 0x5f, '`': 0x60, 'a': 0x61, 'b': 0x62, 'c': 0x63, 'd': 0x64, 'e': 0x65, 
                    'f': 0x66, 'g': 0x67, 'h': 0x68, 'i': 0x69, 'j': 0x6a, 'k': 0x6b, 'l': 0x6c, 
                    'm': 0x6d, 'n': 0x6e, 'o': 0x6f, 'p': 0x70, 'q': 0x71, 'r': 0x72, 's': 0x73, 
                    't': 0x74, 'u': 0x75, 'v': 0x76, 'w': 0x77, 'x': 0x78, 'y': 0x79, 'z': 0x7a, 
                    '{': 0x7b, '|': 0x7c, '}': 0x7d, '~': 0x7e } 

    base64_table = [ 0x41 , 0x42 , 0x43 , 0x44 , 0x45 , 0x46 , 0x47 , 0x48 , 0x49 , 0x4a , 0x4b , 0x4c , 0x4d , 0x4e , 0x4f , 0x50 ,
                     0x51 , 0x52 , 0x53 , 0x54 , 0x55 , 0x56 , 0x57 , 0x58 , 0x59 , 0x5a , 0x61 , 0x62 , 0x63 , 0x64 , 0x65 , 0x66 ,
                     0x67 , 0x68 , 0x69 , 0x6a , 0x6b , 0x6c , 0x6d , 0x6e , 0x6f , 0x70 , 0x71 , 0x72 , 0x73 , 0x74 , 0x75 , 0x76 ,
                     0x77 , 0x78 , 0x79 , 0x7a , 0x30 , 0x31 , 0x32 , 0x33 , 0x34 , 0x35 , 0x36 , 0x37 , 0x38 , 0x39 , 0x2b , 0x2f ,
                     0x3D ]


    def __encode_block(self, block):
        """
        Encode a list of bytes (the block). The list should contain between 1 and 3 bytes.
        If the block is too small, it will be padded with null bytes (0x00). Bitwise
        operations are used to group the bits, and the Base64 substitution table is
        used to construct the final encoded output (a list of encoded bytes).
        """
        b64_bytes = [ 0x3D , 0x3D , 0x3D , 0x3D ] # Default to all padding

        bytes = block
        pad_len = 3 - len(bytes)
        while len(bytes) < 3: bytes.append(0x00)

        # Group the bits using bitwise operations
        b64_B1 = bytes[0] >> 0x02
        b64_B2 = ((bytes[0] & 0x03) << 0x04) | (bytes[1] >> 0x04)
        b64_B3 = ((bytes[1] & 0x0F) << 0x02) | ((bytes[2] & 0xC0) >> 0x06)
        b64_B4 = bytes[2] & 0x3F

        # Construct encoded output from Base64 table -- a better pad method certainly exists
        b64_bytes[0] = self.base64_table[b64_B1]
        b64_bytes[1] = self.base64_table[b64_B2]
        if pad_len <= 1: b64_bytes[2] = self.base64_table[b64_B3]
        if pad_len == 0: b64_bytes[3] = self.base64_table[b64_B4]

        return b64_bytes


    def __decode_block(self, block):
        """
        Decode a list of bytes (the block). The list should contain exactly 4 bytes.
        The Base64 substitution table is used to replace bytes with their corresponding
        indices within the table. Bitwise operations are used to group the bits, and the 
        Base64 substitution table is used to construct the final DEcoded output (a list 
        of decoded bytes).
        """
        def get_b64_index(byte):
            idx = 0
            for b in self.base64_table:
                if byte == b:
                    return idx
                idx += 1
            return -1

        asc_bytes = []
        bytes = block

        # Get index of byte in the Base64 substitution table
        for i in range(4):
            idx = get_b64_index(bytes[i])
            if idx >= 0 and idx < 64: bytes[i] = idx
            elif idx == 64: bytes[i] = 0    # Padding character
            else: raise RuntimeError        # Invalid character in Base64 string

        # Group the bits using bitwise operations
        asc_B1 = ((bytes[0] << 0x02) & 0xFF) | (bytes[1] >> 0x04)
        asc_B2 = ((bytes[1] & 0x0F) << 0x04) | (bytes[2] >> 0x02)
        asc_B3 = ((bytes[2] & 0x03) << 0x06) | bytes[3]

        # Construct decoded output
        asc_bytes.append(asc_B1)
        if asc_B2 != 0: asc_bytes.append(asc_B2)
        if asc_B3 != 0: asc_bytes.append(asc_B3)

        return asc_bytes


    def encode(self, bytes):
        """
        Encode a list of bytes. An exception will be thrown if there is no input.
        The output is a list of encoded bytes.
        """
        if len(bytes) < 1: raise RuntimeError
        output = []
        ptr = 0
        while ptr < len(bytes):
            output += self.__encode_block(bytes[ptr:ptr+3])
            ptr += 3
        return output


    def decode(self, bytes):
        """
        Decode a list of bytes. An exception will be thrown if there is no input or
        if the input length is not a multiple of 4. The output is a list of decoded bytes.
        """
        if len(bytes) % 4 != 0 or len(bytes) < 1: raise RuntimeError # Malformed Base64 input
        output = []
        ptr = 0
        while ptr < len(bytes):
            output += self.__decode_block(bytes[ptr:ptr+4])
            ptr += 4
        return output


    def ascii_to_bytes(self, s):
        """ Convert an ASCII string to a list of its corresponding bytes. """
        bytes = []
        for ch in s:
            try:
                bytes.append(self.ascii_table[ch])
            except:
                continue
        return bytes


    def bytes_to_ascii(self, bytes):
        """ Convert a list of bytes to its corresponding ASCII string. """
        output = ''
        for byte in bytes: 
            try:
                output += chr(byte)
            except:
                continue
        return output
    
