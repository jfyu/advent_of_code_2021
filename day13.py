#Get data
import os

def read_data(dataset):
    if dataset not in ('test', 'inputs'):
        raise ValueError('Must be test or inputs')
    f = open(os.path.expanduser(f"~/projects/advent_of_code/inputs/day13_{dataset}.txt"))
    instructions = []
    x = []
    y = []
    for l in f.readlines():
        l = l.strip('\n')
        if len(l) ==0:
            continue
        if 'fold' in l:
            axis = list(l.split(' ')[-1].split('=')) #this is like 'fold along x=a'
            instructions.append((axis[0], int(axis[-1])))
        else:
            coords = l.split(',')
            x.append(int(coords[0]))
            y.append(int(coords[1]))
    return x,y, instructions

x,y, instructions= read_data('inputs')

def construct_matrix(x,y):
    #in this constuct, x is column, y is row
    n = max(y)+1
    m = max(x)+1

    matrix = []
    for i in range(n):
        matrix.append([0]*m) #initialize
    for j in range(len(y)):
        matrix[y[j]][x[j]] = 1
    return matrix

def reflect_axis(grid, axis, constant):
    if axis == 'x':
        for x in range(len(grid[0])):
            if x > constant:
                for y in range(len(grid)):
                    x_trans = x-2*(x-constant)
                    grid[y][x_trans] = max(grid[y][x], grid[y][x_trans])
    #now drop the columns that are greater than constant
        grid = [row[:constant] for row in grid]
    if axis =='y':
        for y in range(len(grid)):
            if y > constant:
                for x in range(len(grid[0])):
                    y_trans = y-2*(y-constant)
                    grid[y_trans][x] = max(grid[y][x], grid[y_trans][x])
    #drop the rows that are greater than constant
        grid = [row for i, row in enumerate(grid) if i < constant]
    return grid

def print_mat(matrix):
    for row in matrix:
        row_text = ''.join(['#' if x==1 else ' ' for x in row])
        print(row_text)
#checking
#matrix = construct_matrix(list(range(6)), list(range(6)))
# grid = reflect_axis(matrix, 'x', 3)
# print(grid)
# matrix = construct_matrix(list(range(6)), list(range(6)))
# grid = reflect_axis(matrix, 'y', 3)

# matrix = construct_matrix(x,y)
# axis, constant = instructions[0]
# grid = reflect_axis(matrix, axis, constant)
# print(sum([sum(row) for row in grid]))

matrix = construct_matrix(x,y)
for i in range(len(instructions)):
    axis, constant = instructions[i]
    matrix = reflect_axis(matrix, axis, constant)

print(sum([sum(row) for row in matrix]))
print_mat(matrix)

