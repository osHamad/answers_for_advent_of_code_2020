def main():
    file = open('input.txt', 'r')
    input = file.read().splitlines()
    file.close()

    for num1 in input:
        num2 = 2020 - int(num1)
        if str(num2) in input and num2 != num1:
            print(num2*int(num1))
            return

main()
