# read data
import os

f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day5_inputs.txt'))
lines = []
for l in f.readlines():
    coords = l.strip('\n').split(' -> ')
    begin = [int(x) for x in coords[0].split(',')]
    end = [int(x) for x in coords[1].split(',')]
    lines.append([begin, end])

#part1
#only consider horizontal/vertical lines
part1_lines = []
for l in lines:
    x1 = l[0][0]
    y1 = l[0][1]
    x2 = l[1][0]
    y2 = l[1][1]
    if x1==x2 or y1==y2:
        part1_lines.append(l)

intersection = 0
import collections
grid = collections.defaultdict(int)
for l in part1_lines:
    x1 = l[0][0]
    y1 = l[0][1]
    x2 = l[1][0]
    y2 = l[1][1]

    if x1==x2:
        min_y = min(y1,y2)
        max_y = max(y1,y2)
        for y in range(min_y, max_y+1):
            grid[(x1,y)] += 1
            if grid[(x1,y)] == 2:
                intersection+=1
    elif y1==y2:
        max_x = max(x1,x2)
        min_x = min(x1,x2)
        for x in range(min_x, max_x+1):
            grid[(x,y1)] +=1
            if grid[(x,y1)] == 2:
                intersection += 1
print(intersection)

#part 2
intersection = 0
grid = collections.defaultdict(int)
for l in lines:
    x1 = l[0][0]
    y1 = l[0][1]
    x2 = l[1][0]
    y2 = l[1][1]

    if x1==x2:
        min_y = min(y1,y2)
        max_y = max(y1,y2)
        for y in range(min_y, max_y+1):
            grid[(x1,y)] += 1
            if grid[(x1,y)] == 2:
                intersection+=1
    elif y1==y2:
        max_x = max(x1,x2)
        min_x = min(x1,x2)
        for x in range(min_x, max_x+1):
            grid[(x,y1)] +=1
            if grid[(x,y1)] == 2:
                intersection += 1
    else: #diagonal lines
        #slope is always 1, but may be negative or positive
        x = x1
        y = y1
        for _ in range(abs(x2-x1)+1):
            grid[(x,y)] += 1
            if grid[(x, y)] == 2:
                intersection += 1
            x += 1 if x2>x1 else -1
            y += 1 if y2>y1 else -1
print(intersection)
