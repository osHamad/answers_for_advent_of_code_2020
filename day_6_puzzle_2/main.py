def format(input):
    formatted = []
    group = []
    for response in input:
        if response != '':
            group.append(response)
        else:
            formatted.append(group)
            group = []
    return formatted

def find_common(group):
    common = group[0]
    for response in group:
        common = list(set(common).intersection(response))
    return len(common)

def main():
    total = 0
    input = open('input.txt', 'r').read().splitlines()
    input.append('')
    input = format(input)
    for group in input:
        total += find_common(group)
    print(total)

main()
