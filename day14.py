import os

def read_data(dataset):
    if dataset not in ('test', 'inputs'):
        raise ValueError('Must be test or inputs')
    f = open(os.path.expanduser(f"~/projects/advent_of_code/inputs/day14_{dataset}.txt"))
    init = f.readline().strip('\n')
    rules = {}
    for l in f.readlines():
        l = l.strip('\n')
        if len(l):
            rule = l.split(' -> ')
            rules[rule[0]] = rule[1]
    return init, rules

polymer, rules = read_data('inputs')

def advance(init, rules):
    window = 1
    new_polymer = []
    for i in range(len(init)-1):
        curr_pair = init[i:i+2]
        if curr_pair in rules.keys():
            add_on = rules[curr_pair]
        else:
            add_on = ''
        if i < len(init)-2:
            mutation = curr_pair[0]+add_on
        else:
            mutation = curr_pair[0]+add_on+curr_pair[1]
        new_polymer.append(''.join(mutation))
    return ''.join(new_polymer)

#part 1
for step in range(10):
    polymer = advance(polymer, rules)

from collections import Counter
counter = Counter(polymer)
counter_list = list(sorted(counter.items(), key=lambda x: x[1], reverse=True))

most_frequent_letter, most_frequent_freq = counter_list[0]
least_frequent_letter, least_frequent_freq = counter_list[-1]

print(most_frequent_freq - least_frequent_freq)

#part 2
#need to optimise
#looks like we should update counter, not the string
#from https://www.reddit.com/r/adventofcode/comments/rfzq6f/2021_day_14_solutions/hoib78w/?utm_source=share&utm_medium=web2x&context=3
import os
from collections import Counter

def read_data(dataset):
    if dataset not in ('test', 'inputs'):
        raise ValueError('Must be test or inputs')
    with open(os.path.expanduser(f"~/projects/advent_of_code/inputs/day14_{dataset}.txt")) as f:
        template, rules = f.read().split('\n\n')
        chars = Counter(template) #for each char
        template = Counter(a+b for a, b in zip(template, template[1:]))#for pairs
        rules = {x.split(' -> ')[0]: x.split(' -> ')[1] for x in rules.split('\n') if len(list(x))}
    return template, rules, chars

template, rules, chars = read_data('inputs')

def advance_steps(template, rules, chars, steps):
    for _ in range(steps):
        new_template = Counter()
        for (a,b), value in template.items():
            insert = rules[a+b]
            new_template[a+insert] += value
            new_template[insert+b] += value
            chars[insert] += value
        template = new_template #now looking for the new template
    return max(chars.values()) - min(chars.values())

print(advance_steps(template, rules, chars, 40))



