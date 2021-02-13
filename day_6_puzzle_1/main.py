def format(input):
    formatted = []
    passport = ''
    for i in input:
        if i != '':
            passport += i
        else:
            formatted.append(passport)
            passport = ''
    return formatted

def count_answers(answers):
    answered_yes = []
    for i in answers:
        if i not in answered_yes:
            answered_yes.append(i)
    return len(answered_yes)

def main():
    total_yes = 0
    input = open('input.txt', 'r').read().splitlines()
    input.append('')
    input = format(input)
    for i in input:
        total_yes += count_answers(i)
    print(total_yes)

main()
