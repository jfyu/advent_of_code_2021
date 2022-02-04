#read input
f = open('inputs/day2_input.txt')
lines = f.readlines()

#part 1
plan = []
for l in lines:
   plan.append(l.strip('\n').split(' ')) 

depth = 0
horizontal = 0

for step in plan:
    if step[0] == 'forward':
        horizontal+=int(step[1])
    elif step[0] == 'down':
        depth += int(step[1])
    elif step[0] == 'up':
        depth -= int(step[1])
print('Part 1')
print(horizontal)
print(depth)
print(horizontal*depth)

#part 2
depth = 0
horizontal = 0
aim = 0
for step in plan:
    if step[0] == 'forward':
        X = int(step[1])
        horizontal += X
        depth += aim*X
    elif step[0] == 'down':
        X = int(step[1])
        aim+=X
    elif step[0] == 'up':
        X = int(step[1])
        aim -= X
    print(f"step is {step}, depth is {depth}, horizontal is {horizontal}, aim is {aim}")

print('Part 2')
print(horizontal)
print(depth)
print(aim)
print(horizontal*depth)

