def format(input):
    formated = []
    passport = ''
    for i in input:
        if i != '':
            passport += i
        else:
            formated.append(passport)
            passport = ''
    return formated

def main():
    input = open('input.txt', 'r')
    input = input.read().splitlines()
    input = format(input)
    valid_passports = len(input)
    conditions = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for passport in input:
        passport = passport
        for condition in conditions:
            if condition not in passport:
                valid_passports -= 1
                break

    print(valid_passports)

main()
