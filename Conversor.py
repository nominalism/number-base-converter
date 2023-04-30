from re import A


def converteParaOctal(n):
    numeroOctal = ""
    while n > 0:
        d = n % 8
        digit = str(d)
        numeroOctal = digit + numeroOctal
        n = int(float(n) / 8)
    if len(numeroOctal) == 0:
        numeroOctal = "0"
    
    return numeroOctal

def converteparabinario(n):
    numerobin = ""
    while n > 0:
        d = n % 2
        digit = str(d)
        numerobin = digit + numerobin
        n = int(float(n) / 2)
    if len(numerobin) == 0:
        numerobin = "0"
    
    return numerobin

def hexadecimal(n):
    numeroexa = ""
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
        numeroexa = digit + numeroexa
        n = int(float(n) / 16)
    if len(numeroexa) == 0:
        numeroexa = "0"
    
    return numeroexa
    


n = int(input(" Número a ser convertido: "))
print("Opções de conversão: (1) para Octal; (2) para Binário; (3) para Hexadecimal.")
opcao = int(input())
if opcao == 1:
    result = converteParaOctal(n)
    print(result)
else:
    if opcao == 2:
        result = converteparabinario(n)
        print(result)
    else:
        if opcao == 3:
            result = hexadecimal(n)
            print(result)
        else:
             print("Opção inválida!")
