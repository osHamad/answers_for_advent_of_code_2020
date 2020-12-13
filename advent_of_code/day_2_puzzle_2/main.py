def format(input):
    num1 = ''
    num2 = ''
    letter = ''
    password = []
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
            password.append(i)


    return int(num1)-1, int(num2)-1, letter, password


def check(index1, index2, condition, password):
    if password[index1] == condition or password[index2] == condition:
        if password[index1] != password[index2]:
            return 1
        else:
            return 0
    else:
        return 0


def main():
    input = open('input.txt', 'r')
    input = input.read().splitlines()
    good_passwords = 0
    for i in input:
        index1, index2, condition, password = format(i)
        good_passwords += check(index1, index2, condition, password)

    print(good_passwords)
main()
