def convertedecimaltobase(numdec, base, symbols):
    convertednumber = ""
    while numdec > 0:
        d = numdec % base
        digit = symbols[d]
        convertednumber = digit + convertednumber
        numdec = int(numdec / base)
    return convertednumber


numdec = int(input("Number to be converted: "))
print("Conversion options: (1) to Octal; (2) to Binary; (3) to Hexadecimal.")
base = int(input('Choose the target base: '))
if base == 1:
    symbols = ('0', '1', '2', '3', '4', '5', '6', '7')
    result = convertedecimaltobase(numdec, 8, symbols)
    print(result)
elif base == 2:
    symbols = ('0', '1')
    result = convertedecimaltobase(numdec, 2, symbols)
    print(result)
elif base == 3:
    symbols = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    result = convertedecimaltobase(numdec, 16, symbols)
    print(result)
else:
    print('Invalid option!') 
