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

def directions(i,j):
    return ((i+1, j), (i-1, j), (i,j+1), (i, j-1), (i-1,j-1), (i-1, j+1), (i+1, j-1), (i+1, j+1))

def increase_energy(grid):
    m = len(grid) #row 
    n = len(grid[0]) #columns
    stack = []
    seen = set()
    for i in range(m):
        for j in range(n):
            grid[i][j] += 1
            if grid[i][j] >9:
                stack.append((i,j))
                seen.add((i,j))
    return stack,seen

def reset_energy(grid):
    m = len(grid) #row 
    n = len(grid[0]) #columns
    flashes = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]>9:
                grid[i][j] = 0
                flashes += 1
    return flashes

def dfs(grid, stack, seen):
    m = len(grid) #row 
    n = len(grid[0]) #columns
    while stack:
        i,j = stack.pop() #LIFO
        seen.add((i,j))
        for k,l in directions(i,j):
            if 0<=k<m and 0<=l<n and (k,l) not in seen:
                grid[k][l]+=1
                if grid[k][l]>9:
                    grid[k][l] = 10 #reset to 10
                    stack.append((k,l))

def advance(grid):
    # first we increase the energy
    stack,seen = increase_energy(grid)
    #DFS
    dfs(grid, stack, seen)
    flashes = reset_energy(grid)
    return flashes

grid = read_data('test')
