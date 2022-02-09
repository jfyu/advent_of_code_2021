import os

f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day8_inputs.txt'))
display = {}
for l in f.readlines():
    line = l.strip('\n').split('|')
    display[line[0].strip(' ')] = line[1].lstrip(' ')

counts = 0
for val in display.values():
    lengths = list(map(len, val.split(' ')))
    for l in lengths:
        if l in [2,4,3,7]:
            counts+=1
print(counts)

#part 2
#create the mapping
# from https://dev.to/qviper/advent-of-code-2021-python-solution-day-8-76p
# create all permutations of abcedfg
import itertools
pm = []
for p in itertools.permutations('abcedfg'):
    pm.append(p)

mapping = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

sol = 0
for key, val in display.items():
    for p in pm: #loop through all the permutations
        to = str.maketrans('abcedfg', ''.join(p))
        ts = [''.join(sorted(sig.translate(to))) for sig in key.split(' ')]
        top = [''.join(sorted(op.translate(to))) for op in val.split(' ')]

        if all(code in mapping for code in ts):
            sol += int(''.join(str(mapping[code]) for code in top))
print(sol)

## brute force would be to try to figure out the mapping out of the known digits
