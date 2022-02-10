#read data
import os
from collections import deque
f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day9_inputs.txt'))
grid = [] #this will be a list of lists
for l in f.readlines():
    grid.append(list(map(int, list(l.strip('\n')))))

#part1
m = len(grid)
n = len(grid[0])
risk = []
low_pts = []
for k in range(m):
    for l in range(n):
        val = grid[k][l]
        risk.append(val+1) #assume low
        low_pts.append((k,l))
        neighbours = []
        for x,y in ((k+1, l), (k-1,l), (k, l+1), (k, l-1)):
            if 0<=x<=m-1 and 0<=y<=n-1 and grid[x][y]+1: #do a plus 1 because 0 is considered false
                if grid[x][y] <= val:
                    risk.pop()
                    low_pts.pop()
                    break
print(sum(risk))

#part 2
basins = []
stack = []
seen = set()
for pts in low_pts:
    k,l = pts
    seen.add((k,l))
    stack.append((k,l))
    size = 1
    while stack:
        k,l = stack.pop() #we know we can start at the low points
        seen.add((k,l))
        for x,y in ((k+1, l), (k-1,l), (k, l+1), (k, l-1)):
            if 0<=x<=m-1 and 0<=y<=n-1 and grid[x][y]+1: #do a plus 1 because 0 is considered false
                if grid[x][y] != 9 and (x,y) not in seen:
                    stack.append((x,y))
                    seen.add((x,y))
                    size += 1
    basins.append(size)
basins.sort(reverse=True)
product_size = 1
for x in range(3):
    product_size = product_size*basins[x]
print(product_size)

