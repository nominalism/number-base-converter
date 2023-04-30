def convertedecimalparabase(numdec, base, simbolos):
    numeroconvertido = ""
    while numdec > 0:
        d = numdec % base
        digit = simbolos[d]
        numeroconvertido = digit + numeroconvertido
        numdec = int(numdec / base)
    return numeroconvertido



numdec = int(input(" Número a ser convertido: "))
print("Opções de conversão: (1) para Octal; (2) para Binário; (3) para Hexadecimal.")
base = int(input(' Escolha a base de destino: '))
if base == 1:
    simbolos = ('0', '1', '2', '3', '4', '5', '6', '7')
    result = convertedecimalparabase(numdec, 8, simbolos)
    print(result)
elif base == 2:
    simbolos = ('0', '1')
    result = convertedecimalparabase(numdec, 2, simbolos)
    print(result)
elif base == 3:
    simbolos = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
    result = convertedecimalparabase(numdec, 16, simbolos)
    print(result)
else:
    print(' Opção inválida! ')
