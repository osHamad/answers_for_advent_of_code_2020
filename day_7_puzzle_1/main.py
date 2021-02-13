def get_colors(dict, curr_node_key):
    if curr_node_key not in dict:
        return {curr_node_key}
    else:
        set_colors = {curr_node_key}
        parent_list = dict[curr_node_key]
        for parent in parent_list:
            curr_colors = get_colors(dict, parent)
            set_colors.update(curr_colors)
        return set_colors

def main():
    bags = {}
    with open('input.txt','r') as file:
        file = file.read().splitlines()

    for input in file:
        input=input.split()
        bag = input[0]+input[1]
        [input.remove(input[0]) for l in range(2)]
        contain = []
        name = ''
        for i in input:
            if i not in 'bags,bag,bag.bags.contain':
                if i.isalpha():
                    name += i
                elif i.isdigit():
                    contain.append(name)
                    name = ''
        contain.append(name)
        for parent in contain:
            try:
                bags[parent].append(bag)
            except KeyError:
                bags.update({parent:[bag]})

    print(len(get_colors(bags, 'shinygold'))-1)

main()
