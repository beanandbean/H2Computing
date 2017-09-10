def binToDec(binStr):
    decNum = 0
    for ch in binStr:
        decNum = decNum * 2 + int(ch)
    return decNum
    
def octToDec(octStr):
    decNum = 0
    for ch in octStr:
        decNum = decNum * 8 + int(ch)
    return decNum

def hexToDec(hexStr):
    decNum = 0
    for ch in hexStr.upper():
        if ch in "ABCDEF":
            decNum = decNum * 16 + ord(ch) - ord("A") + 10
        else:
            decNum = decNum * 16 + int(ch)
    return decNum
    
def decToBin(decNum):
    binStr = ""
    while decNum > 0:
        binStr = str(decNum % 2) + binStr
        decNum = decNum // 2
    return binStr
    
def decToOct(decNum):
    octStr = ""
    while decNum > 0:
        octStr = str(decNum % 8) + octStr
        decNum = decNum // 8
    return octStr
        
def decToHex(decNum):
    hexStr = ""
    while decNum > 0:
        value = decNum % 16
        if value < 10:
            hexStr = str(value) + hexStr
        else:
            hexStr = chr(value - 10 + ord("A")) + hexStr
        decNum = decNum // 16
    return hexStr
