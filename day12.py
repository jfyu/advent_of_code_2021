import os

def read_data(dataset):
    if dataset not in ('test', 'inputs'):
        raise ValueError('Must be test or inputs')
    f = open(os.path.expanduser(f"~/projects/advent_of_code/inputs/day12_{dataset}.txt"))
    lines = [l.strip('\n') for l in f.readlines()]
    return lines

data = read_data('inputs')

#https://www.reddit.com/r/adventofcode/comments/rehj2r/2021_day_12_solutions/ho8zlrj/?utm_source=share&utm_medium=web2x&context=3
from collections import defaultdict
paths = defaultdict(list)

for conn in data:
    for a,b in [conn.split('-')]:
        paths[a].append(b)
        paths[b].append(a)

#use dfs
def dfs(cave, visited, one_off):
    if (cave == 'end'):
        return 1
    if (cave.islower()):
        visited.add(cave)
    total = sum([dfs(i, visited, one_off) for i in paths[cave] if not i in visited])
    total += sum([dfs(i, visited, i) for i in paths[cave] if i in visited and i != 'start']) if one_off == ' ' else 0
    if (cave != one_off):
        visited.discard(cave)
    return total

print(dfs('start', set(), ''))
print(dfs('start', set(), ' '))

# def explicit_dfs(paths):
    # #this is showing 4 because it doesn't understand how to take into consideration that 
    # #A can be visited multiple times
    # visited = set()
    # counter = 0
    # stack = []
    # stack.append('start')
    # while stack:
        # cave = stack.pop()
        # if cave.islower() and cave != 'end':
            # visited.add(cave)
        # for next_cave in paths[cave]:
            # if next_cave != 'end' and next_cave not in visited:
                # print(f"{cave}-{next_cave}")
                # stack.append(next_cave)
                # print(stack)
            # if next_cave == 'end':
                # print(f"{cave}-{next_cave}")
                # counter += 1
               # # print(stack)
    # print(visited)
    # return counter


