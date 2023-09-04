def dectobinary(dec):
    if dec == 0:
        return "0"
    binary = ""
    while dec > 0:
        remainder = dec % 2
        binary = str(remainder) + binary
        dec //= 2
    return binary


def binaryton(bin_str, conversion_type):
    if conversion_type == 'int':
        decimal = 0
        binary_len = len(bin_str)
        for i, digit in enumerate(bin_str):
            if digit == '1':
                decimal += 2 ** (binary_len - i - 1)
        return decimal
    elif conversion_type == 'oct':
        decimal = binaryton(bin_str, 'int')
        return oct(decimal)[2:]
    elif conversion_type == 'hex':
        decimal = binaryton(bin_str, 'int')
        return hex(decimal)[2:]


def dectooctal(dec):
    if dec == 0:
        return "0"
    octal = ""
    while dec > 0:
        remainder = dec % 8
        octal = str(remainder) + octal
        dec //= 8
    return octal


def dectohex(dec):
    if dec == 0:
        return "0"
    hexadecimal = ""
    while dec > 0:
        remainder = dec % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        dec //= 16
    return hexadecimal


def main():
    decimal_number = int(input("Please enter a decimal number: "))
    print("Binary representation: ", dectobinary(decimal_number))

    binary_str = input("Please enter a binary number: ")
    conversion_type = input("Conversion type (int, oct, hex): ")
    print(f"Converted value: ", binaryton(binary_str, conversion_type))

    print(f"Octal representation: ", dectooctal(decimal_number))
    print(f"Hexadecimal representation: ", dectohex(decimal_number))


if __name__ == "__main__":
    main()
