def main():
    file = open('input.txt', 'r')
    input = file.read().splitlines()
    file.close()

    for num1 in input:
        for num2 in input:
            num3 = 2020 - int(num1) - int(num2)
            if str(num3) in input and num3 != num2 != num1:
                print(int(num1)*int(num2)*num3)
                return

main()
