# the code is a bit messy
def format(input):
    formated = []
    passport = ''
    for i in input:
        if i != '':
            passport += f'{i} '
        else:
            formated.append(passport.strip())
            passport = ''
    return formated

def make_dict(input):
    Dict = dict((x.strip(), y.strip())
        for x, y in (element.split(':')
        for element in input.split(' ')))

    return Dict

def verify(passport):
    needed_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    for i in needed_keys:
        if i not in passport:
            return 0
    a = 1920 <= int(passport['byr']) <= 2002
    b = 2010 <= int(passport['iyr']) <= 2020
    c = 2020 <= int(passport['eyr']) <= 2030
    d = None
    e = None
    f = None
    height = ''
    sign = ''
    for i in passport['hgt']:
        if i.isdigit():
            height+=i
        elif i.isalpha():
            sign+=i

    if sign == 'cm':
        d = 150 <= int(height) <= 193
    elif sign == 'in':
        d = 59 <= int(height) <= 76

    for i in passport['hcl']:
        if not i.isdigit():
            if i in '#abcdef':
                e = True
            else:
                e = False
                break
        elif i.isdigit():
            if int(i) in range(10):
                e = True
            else:
                e = False
                break

    if passport['ecl'] in 'amb blu brn gry grn hzl oth':
        f = True
    else:
        f = False

    try:
        g = len(passport['pid']) == 9
    except ValueError:
        g = False

    if a and b and c and d and e and f and g and len(passport['hcl'])==7:
        return 1
    else:
        return 0

def main():
    input = open('input.txt', 'r')
    input = format(input.read().splitlines())
    valid_passports = 0
    for passport in input:
        valid_passports += verify(make_dict(passport))
    print(valid_passports)
main()
