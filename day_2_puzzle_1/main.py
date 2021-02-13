def format(input):
    num1 = ''
    num2 = ''
    letter = ''
    password = ''
    move_num = False
    is_password = False
    for i in input:
        if i.isdigit() and not move_num:
            num1 += i
        elif i.isdigit() and move_num:
            num2 += i
        elif i == '-':
            move_num = True
        elif i.isalpha() and not is_password:
            letter += i
        elif i == ':':
            is_password = True
        elif i.isalpha() and is_password:
            password += i


    return int(num1), int(num2), letter, password


def check(min, max, condition, password):
    occurance = 0
    for i in password:
        if i == condition:
            occurance +=1

    if min <= occurance <= max:
        return 1
    else:
        return 0


def main():
    input = open('input.txt', 'r')
    input = input.read().splitlines()
    good_passwords = 0
    for i in input:
        min, max, condition, password = format(i)
        good_passwords += check(min, max, condition, password)

    print(good_passwords)

main()
