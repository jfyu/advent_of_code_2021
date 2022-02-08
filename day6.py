#read data
import os

f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day6_inputs.txt'))
fish = list(map(int, f.readline().strip('\n').split(',')))

total_days = 80
for day in range(total_days):
    new_fish = 0
    for i in range(len(fish)):
        if fish[i]==0:
            fish[i]=6
            new_fish+=1
        else:
            fish[i]-=1
    for j in range(new_fish):
        fish.append(8)

print(len(fish))

#part 2
f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day6_inputs.txt'))
fish = list(map(int, f.readline().strip('\n').split(',')))
#bruteforce as above will timeout
# use age group instead, use counter
from collections import Counter, defaultdict
lifes = dict(Counter(fish))

total_days = 256 
for days in range(1, total_days+1):
    lifes = {l:(0 if lifes.get(l+1) is None else lifes.get(l+1)) for l in range(-1, 8)} #basically update the lifes at each clock for the ones that were at l+1 last time
    lifes[8] = lifes[-1] #add new life 
    lifes[6] += lifes[-1] #reset
    lifes[-1] = 0
print(sum(lifes.values()))

