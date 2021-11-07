def hash(data):
    dict = {'0':'0000','1':'0001','2':'0010','3':'0011','4':'0100','5':'0101','6':'0110',\
            '7':'0111','8':'1000','9':'1001','a':'1010','b':'1011','c':'1100','d':'1101','e':'1110','f':'1111'}

    pc1=[56, 48, 40, 32, 24, 16,8,
        0, 57, 49, 41, 33, 25, 17,
        9,  1, 58, 50, 42, 34, 26,
        18, 10,  2, 59, 51, 43,35,
        62, 54, 46, 38, 30, 22,14,
        6, 61, 53, 45, 37, 29, 21,
        13,  5, 60, 52, 44, 36,28,
        20, 12,  4, 27, 19, 11, 3]

    pc2=[13, 16, 10, 23, 0, 4,
        2, 27, 14,  5, 20,  9,
        22, 18, 11,  3, 25, 7,
        15,  6, 26, 19, 12, 1,
        40, 51, 30, 36, 46, 54,
        29, 39, 50, 44, 32, 47,
        43, 48, 38, 55, 33, 52,
        45, 41, 49, 35, 28, 31]

    ip=[57, 49, 41, 33, 25, 17, 9,  1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7,
        56, 48, 40, 32, 24, 16, 8,  0,
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6]

    expansion_table = \
    [31,  0,  1,  2,  3,  4,
        3,  4,  5,  6,  7,  8,
        7,  8,  9, 10, 11, 12,
        11, 12, 13, 14, 15, 16,
        15, 16, 17, 18, 19, 20,
        19, 20, 21, 22, 23, 24,
        23, 24, 25, 26, 27, 28,
        27, 28, 29, 30, 31, 0]

    sbox = \
        [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    p=[15, 6, 19, 20, 28, 11,
    27, 16, 0, 14, 22, 25,
    4, 17,30, 9,  1,  7, 23,
    13, 31,26, 2,  8,  18,
    12, 29, 5, 21, 10, 3, 24]

    final_permutation=[39,  7, 47, 15, 55, 23, 63, 31,
        38,  6, 46, 14, 54, 22, 62, 30,
        37,  5, 45, 13, 53, 21, 61, 29,
        36,  4, 44, 12, 52, 20, 60, 28,
        35,  3, 43, 11, 51, 19, 59, 27,
        34,  2, 42, 10, 50, 18, 58, 26,
        33,  1, 41,  9, 49, 17, 57, 25,
        32,  0, 40,  8, 48, 16, 56, 24]

    def shiftbyK(string,k):
        return string[k:]+string[0:k]

    def hexTobin(s):
        string = ''
        for i in s: string += dict[i]
        return string

    def changeBitPositions(text,list):
        string = ""
        for i in list: string += text[i]
        return string

    def xorf(a, b):
        result = ""
        for i in range(len(a)):
            if (a[i] == b[i]): result += "0"
            else: result += "1"
        return result

    def generateKeys(c,d):
        for i in range (1,17):
            if (i==1 or i==2 or i==9 or i==16): k=1 
            else : k=2
            c = shiftbyK(c,k)
            d = shiftbyK(d,k)
            keys16.append(changeBitPositions(c+d,pc2))
        return keys16

    def sixTOfour(list1):
        temp = [] 
        for j in range(8):
            i = list1[j]
            n1 = int(i[0]+i[-1],2)
            n2 = int(i[1:5],2)
            string = bin(sbox[j][n1][n2])[2:]
            string = '0'*(4-len(string)) + bin(sbox[j][n1][n2])[2:]
            temp.append(string)
        return temp  

    def encode(l0,r0,keys16):
        if choice: keys16 = keys16[::-1] #reverese key list while decrypting
        r_prev = r0
        l_prev = l0
        for i in range (16):
            xor = []
            k = keys16[i]
            l_next = r_prev
            xored = xorf(changeBitPositions(r_prev, expansion_table),k)
            for j in range(0,48,6):
                xor.append(xored[j:j+6])
            expanded_bits = "".join(i for i in sixTOfour(xor))
            keyXORr = changeBitPositions(expanded_bits,p)
            r_next = xorf(l_prev,keyXORr)
            l_prev = l_next
            r_prev = r_next
        global l16 
        global r16 
        l16 = l_next
        r16 = r_next

    def modifyKey(key):
        key = hexTobin(key)
        key1 = changeBitPositions(key,pc1)
        c0 = key1[:28]
        d0 = key1[28:]
        generateKeys(c0,d0)

    def encryption(plain_txt):
        if len(plain_txt)!=16:
            plain_txt += '0'*(16-len(plain_txt))
        plain_txt = hexTobin(plain_txt)
        plain_txt = changeBitPositions(plain_txt, ip)
        l0 = plain_txt[:32]
        r0 = plain_txt[32:]
        encode(l0,r0,keys16)
        r16_l16 = r16+l16 
        encoded_message = changeBitPositions(r16_l16, final_permutation)
        cipherText = hex(int(encoded_message, 2)).upper()
        return cipherText

    keys16 = []
    key = "133457799BBCDFF1".lower()
    plain_txt = ("".join([hex(ord(x))[2:] for x in data]))
    choice = 0
    modifyKey(key) 
    Text = encryption(plain_txt)[2:]
    if len(Text)<16 : 
        Text =  (16-len(Text))*'0' + Text

    def shiftby(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff 

    def get_listOf80(text):
        text = list(format(ord(i), '08b') for i in text)
        string = str("".join(text) + '1')
        while len(string)%512 != 448: 
            string += '0'
        filler = bin(len("".join(text)))[2:]
        filler = '0'*(64-len(filler)) + filler
        string += filler  
        list80 = list(string[i:i+32] for i in range(0,512,32))
        for i in range (16, 80):
            list80.append(bin(shiftby(int(list80[i-3],2)^int(list80[i-8],2)^int(list80[i-14],2)^int(list80[i-16],2),1))[2:].zfill(32))
        return list80

    def SHA1():
        h0, h1, h2, h3, h4 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476, 0xC3D2E1F0
        a,b,c,d,e = h0,h1,h2,h3,h4
        for i in range (80):
            if(i<20):
                key = 0x5A827999
                fun = d^(b&(c^d))
            elif (i>19 and i<40):  
                key = 0x6ED9EBA1
                fun = b^c^d
            elif (i>39 and i<60):   
                key = 0x8F1BBCDC
                fun = (b&c) | (b&d) | (c&d)
            else:    
                key = 0xCA62C1D6
                fun = b^c^d
            a, b, c, d, e = ((shiftby(a, 5) + fun + e + key + int(list80[i],2)) & 0xffffffff, a, shiftby(b, 30), c, d)
        h0,h1,h2,h3,h4 = (h0+a) & 0xffffffff, (h1+b) & 0xffffffff, (h2+c) & 0xffffffff,(h3+d) & 0xffffffff,(h4+e) & 0xffffffff
        return '%08x%08x%08x%08x%08x' % (h0,h1,h2,h3,h4)
    text = Text
    for _ in range(20):
        list80 = get_listOf80 (text)
        text = "84B03D034B409D4E" + SHA1().upper() + "E1F53135E559C253" 
        hash_value = SHA1().upper() 
    return hash_value 

def stored():
    return "AA40A88A209AF4F1FC056D2FE12489991402184E"
