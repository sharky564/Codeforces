# Spreadsheets
def alpha(n):
    result = ''
    dig = 1
    while n > 27 ** (dig - 1) * 26:
        dig += 1
    k = n
    while dig > 1:
        num = (k - 1) // (27 ** (dig - 2) * 26)
        char = chr(num + 64)
        result += char
        k -= num * 26 ** (dig - 1)
        dig -= 1
    else:
        char = chr(k + 64)
        result += char
    return result

def splitter(text):
    k = text
    digits = ['0','1','2','3','4','5','6','7','8','9']
    for i in digits:
        k = k.replace(i,'')
    a, b = text.split(k)
    return k,b

def num(text):
    result = 0
    i = 0
    while i < len(text):
        result += 26**(len(text)-i-1) * (ord(text[i]) - 64)
        i += 1
    return result

def coord(text):
    if 'R' in text and 'C' in text and 'RC' not in text and 'CR' not in text:
        text = text[1:]
        r, c = text.split('C')
        result = alpha(int(c)) + r
    else:
        c, r = splitter(text)
        c = str(num(c))
        result = 'R' + r + 'C' + c
    return result

n = int(input())
for i in range(n):
    print(coord(input()))
