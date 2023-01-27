# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('fileSem5Task4_decoded.txt', 'r') as data:
    textcode = data.read()


def encode_file(code):
    strCode = ''
    prevChar = ''
    count = 1
    for char in code:
        if char != prevChar:
            if prevChar:
                strCode += str(count)+prevChar
            count = 1
            prevChar = char
        else:
            count += 1
    return strCode


strCode = encode_file(textcode)
print(strCode)

with open('fileSem5Task4_encoded.txt', 'r') as data:
    textcode2 = data.read()


def decode_file(code: str):
    count = ''
    strDecode = ''
    for char in code:
        if char.isdigit():
            count += char
        else:
            strDecode += char*int(count)
            count = ''
    return strDecode


strDecode = decode_file(textcode2)
print(strDecode)
