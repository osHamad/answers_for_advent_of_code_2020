def create_dict(input, index=0, first_iter=True):
    bag = input[0]+input[1]
    contain = {}
    input.remove(input[0])
    input.remove(input[0])
    name = ''
    fullname = []
    num = ''
    for i in input:
        if i not in 'bags,bag,bag.bags.contain':
            if i.isalpha():
                name += i

            elif i.isdigit():
                if first_iter:
                    num = i
                    first_iter = False
                else:
                    contain[f'contain{index}'] = [num,name]
                    fullname.append(name)
                    name = ''
                    num = ''

                    num = i


                    index+=1

        contain[f'contain{index}'] = [num,name]

    return bag, contain


def find_container(condition, bags, counter):
    for i in bags:
        for j in bags[i]:
            if bags[i][j][1] == condition:
                return find_container(i, bags, counter+1)



def main():
    bags = {}
    with open('input.txt','r') as input:
        input = input.read().splitlines()
    for i in input:
        bag = create_dict(i.split())
        bags[bag[0]] = bag[1]

    print(find_container('shinygold', bags, 0))


main()



'''dictionary = {'poshteal': {'contain0': ['2', 'fadedcoral'], 'contain1': ['3', 'stripedcrimson'], 'contain2': ['1', 'fadedred']},
    'mirroredchartreuse': {'contain0': ['3', 'clearbeige'], 'contain1': ['3', 'shinysilver'], 'contain2': ['3', 'brightgreen']}}

for bag in dictionary:
    for contain in dictionary[bag]:
        print(dictionary[bag][contain][0])'''
