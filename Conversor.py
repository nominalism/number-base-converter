from re import A


def convertToOctal(n):
    octalNumber = ""
    while n > 0:
        d = n % 8
        digit = str(d)
        octalNumber = digit + octalNumber
        n = int(float(n) / 8)
    if len(octalNumber) == 0:
        octalNumber = "0"
    
    return octalNumber

def convertToBinary(n):
    binaryNumber = ""
    while n > 0:
        d = n % 2
        digit = str(d)
        binaryNumber = digit + binaryNumber
        n = int(float(n) / 2)
    if len(binaryNumber) == 0:
        binaryNumber = "0"
    
    return binaryNumber

def hexadecimal(n):
    hexNumber = ""
    while n > 0:
        d = n % 16
        digit = str(d)

        if d >= 10:
            if d == 10:
                digit = 'A'
            if d == 11:
                digit = 'B'
            if d == 12:
                digit = 'C'
            if d == 13:
                digit = 'D'
            if d == 14:
                digit = 'E'
            if d == 15:
                digit = 'F' 
        hexNumber = digit + hexNumber
        n = int(float(n) / 16)
    if len(hexNumber) == 0:
        hexNumber = "0"
    
    return hexNumber
    


n = int(input("Number to be converted: "))
print("Conversion options: (1) to Octal; (2) to Binary; (3) to Hexadecimal.")
option = int(input())
if option == 1:
    result = convertToOctal(n)
    print(result)
else:
    if option == 2:
        result = convertToBinary(n)
        print(result)
    else:
        if option == 3:
            result = hexadecimal(n)
            print(result)
        else:
            print("Invalid option!")
