def main(n, option):
    if option == 1:
        octal_number = ""
        while n > 0:
            d = n % 8
            digit = str(d)
            octal_number = digit + octal_number
            n = int(float(n) / 8)
        if len(octal_number) == 0:
            octal_number = "0"
        print(octal_number)
        
    elif option == 2:
        binary_number = ""
        while n > 0:
            d = n % 2
            digit = str(d)
            binary_number = digit + binary_number
            n = int(float(n) / 2)
        if len(binary_number) == 0:
            binary_number = "0"
        print(binary_number)
        
    elif option == 3:
        hexadecimal_number = ""
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
            hexadecimal_number = digit + hexadecimal_number
            n = int(float(n) / 16)
        if len(hexadecimal_number) == 0:
            hexadecimal_number = "0"
        print(hexadecimal_number)
    else:
        print("Invalid option!")

n = int(input("Number to convert: "))
print("Conversion options: (1) to Octal; (2) to Binary; (3) to Hexadecimal.")
option = int(input())
main(n, option)
