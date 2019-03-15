data = {
' ' : [ 0x00 ,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00 ,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00 ,0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'0' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01111100,
          0b10000010,
          0b10000010,
          0b01111100,
          0x00,0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'1' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b10000100,
          0b11111110,
          0b10000000,
          0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'2' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11000100,
          0b10100010,
          0b10010010,
          0b10001100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'3' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01000100,
          0b10010010,
          0b10010010,
          0b01101100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'4' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01110000,
          0b01001100,
          0b11111110,
          0b01000000,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'5' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b10011110,
          0b10010010,
          0b10010010,
          0b01100010,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'6' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01111100,
          0b10010010,
          0b10010010,
          0b01100100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'7' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b00000110,
          0b11100010,
          0b00010010,
          0b00001110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'8' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01101100,
          0b10010010,
          0b10010010,
          0b01101100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'9' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01001100,
          0b10010010,
          0b10010010,
          0b01111100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'A' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111100,
          0b00010010,
          0b00010010,
          0b11111100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'B' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b10010010,
          0b10010010,
          0b01101100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'C' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01111100,
          0b10000010,
          0b10000010,
          0b01000100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'D' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b10000010,
          0b10000010,
          0b01111100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'E' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b10010010,
          0b10010010,
          0b10000010,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'F' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b00010010,
          0b00010010,
          0b00000010,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'G' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b01111100,
          0b10000010,
          0b10000010,
          0b10100010,
          0b01100100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'H' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b00010000,
          0b00010000,
          0b11111110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'I' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b10000010,
          0b11111110,
          0b10000010,
          0x00, 0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'J' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01000010,
          0b10000010,
          0b10000010,
          0b01111110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'K' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b11111110,
          0b00010000,
          0b00101000,
          0b01000100,
          0b10000010,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'L' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b10000000,
          0b10000000,
          0b10000000,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'M' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b11111110,
          0b00000100,
          0b00001000,
          0b00000100,
          0b11111110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'N' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b11111110,
          0b00000100,
          0b00011000,
          0b00100000,
          0b01000000,
          0b11111110,
          0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'O' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b01111100,
          0b10000010,
          0b10000010,
          0b01111100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'P' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,0x00,
          0b11111110,
          0b00010010,
          0b00010010,
          0b00001100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'Q' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b01111100,
          0b10000010,
          0b10000010,
          0b11111100,
          0b10000000,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'R' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11111110,
          0b00110010,
          0b01010010,
          0b10001100,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'S' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b10001100,
          0b10010010,
          0b10010010,
          0b01100010,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'T' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b00000010,
          0b00000010,
          0b11111110,
          0b00000010,
          0b00000010,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'U' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b01111110,
          0b10000000,
          0b10000000,
          0b10000000,
          0b01111110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'V' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b00111110,
          0b01000000,
          0b10000000,
          0b01000000,
          0b00111110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'W' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b11111110,
          0b01000000,
          0b00100000,
          0b01000000,
          0b11111110,
          0x00,0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'X' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b11000011,
          0b00100100,#0b11100110,
          0b00011000,
          0b00011000,#0b00011000,
          0b00100100,#0b00011000,
          0b11000011,#0b11100110,
          0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'Y' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00,
          0b00001110,
          0b00010000,
          0b11100000,
          0b00010000,
          0b00001110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'Z' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
          0x00, 0x00,
          0b11000010,
          0b10100010,
          0b10011010,
          0b10000110,
          0x00, 0x00,
          0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'?' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00000100,
            0b10100010,
            0b00010010,
            0b00001100,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'!' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00,
            0b10111110,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'.' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x80,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

':' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00,
            0b00101000,
            0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

',' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00,
            0b10110000,
            0b01110000,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

';' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00,
            0b10110000,
            0b00000000,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'(' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b01111100,
            0b10000010,
            0b10000010,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

')' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b10000010,
            0b10000010,
            0b01111100,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'[' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b11111110,
            0b10000010,
            0b10000010,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

']' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b10000010,
            0b10000010,
            0b11111110,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

##{} : curly bracket
'{' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00010000,
            0b01101100,
            0b10000010,
            0b10000010,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'}' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b10000010,
            0b10000010,
            0b01101100,
            0b00010000,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

##<> : lace bracket
'<' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00010000,
            0b00101000,
            0b01000100,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'>' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b01000100,
            0b00101000,
            0b00010000,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'#' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 
            0b00100100,
            0b01111110,
            0b00100100,
            0b00100100,
            0b01111110,
            0b00100100,
            0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'+' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00,
            0b00010000,
            0b00010000,
            0b01111100,
            0b00010000,
            0b00010000,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'-' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00010000,
            0b00010000,
            0b00010000,
            0b00010000,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'*' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00000100,
            0b00001110,
            0b00000100,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'/' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b11000000,
            0b00111000,
            0b00000110,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'&' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00,
            0b01101100,
            0b10010010,
            0b10110010,
            0b01001100,
            0b10100000,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'%' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b11000010,
            0b00111000,
            0b10000110,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'=' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00101000,
            0b00101000,
            0b00101000,
            0b00101000,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'^' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00000100,
            0b00000010,
            0b00000100,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'_' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b10000000,
            0b10000000,
            0b10000000,
            0b10000000,
            0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],

'\\' : [ 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00,
            0b00000110,
            0b00111000,
            0b11000000,
            0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
}