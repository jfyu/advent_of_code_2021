# read data
import os
f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day7_test.txt'))
pos = list(map(int, f.readline().strip('\n').split(',')))


#part 1 
min_fuel = float('inf')
min_pos = 0

for i in range(0, max(pos)):
    total_fuel = sum([abs(x-i) for x in pos])
    if total_fuel < min_fuel:
        min_fuel = total_fuel
        min_pos = i

print(min_fuel)
print(min_pos)

#part 2
import os
f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day7_inputs.txt'))
pos = list(map(int, f.readline().strip('\n').split(',')))


min_fuel = float('inf')
min_pos = 0

for i in range(0, max(pos)):
    total_fuel = 0
    for x in pos:
        dist = x-i
        total_fuel += (abs(x-i))*(abs(x-i)+1)/2
    if total_fuel < min_fuel:
        min_fuel = total_fuel
        min_pos = i

print(min_fuel)
print(min_pos)

