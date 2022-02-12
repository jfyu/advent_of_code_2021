# read data
import os
from collections import deque

def read_data(dataset):
    if dataset not in ('test', 'inputs'):
        raise ValueError('Must be test or inputs')
    f = open(os.path.expanduser(f"~/projects/advent_of_code/inputs/day11_{dataset}.txt"))
    grid = []
    for l in f.readlines():
        grid.append(list(map(int, list(l.strip('\n')))))
    return grid

def directions(i,j, m, n):
    nbrs = []
    for x, y in ((i+1, j), (i-1, j), (i,j+1), (i, j-1), (i-1,j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1)):
        if 0<=x<m and 0<=y<n:
            nbrs.append((x,y))
    return nbrs

def advance(grid):
    m = len(grid) #row 
    n = len(grid[0]) #columns
    flashed = []
    neighbours = []
    flashes = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]==9:
                grid[i][j] = 0
                flashes +=1
                flashed.append((i,j))
                neighbours.extend(directions(i,j, m, n))
            else:
                grid[i][j]+=1
    while neighbours:
        i,j = neighbours.pop(0)
        if (i,j) not in flashed:
            if grid[i][j] == 9:
                grid[i][j] = 0
                flashes+=1
                flashed.append((i,j))
                neighbours.extend(directions(i,j,m,n))
            else:
                grid[i][j] += 1
    return int(flashes)
grid = read_data('inputs')
flashes = 0
for step in range(100):
    flashes+=advance(grid)
print(flashes)

#part 2
grid = read_data('inputs')
flashes = 0
step = 0
while flashes < len(grid)*len(grid[0]):
    flashes=advance(grid)
    step+=1
print(step)
