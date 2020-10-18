def print_formatted(number):
    result=[]
    for i in range(1, 1+number):
        decimal = str(i)
        octal=str(oct(i)[2:])
        hex_=str(hex(i)[2:]).upper()
        bin_=str(bin(i)[2:])
        result.append([decimal, octal, hex_, bin_])
    width = len(result[-1][3])
    for i in result:
        print(*(y.rjust(width) for y in i))




if __name__ == '__main__':
    n = int(input())
    print_formatted(n)