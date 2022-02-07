#part one
import os

f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day4_input.txt'))
called_nums = [int(x) for x in list(f.readline().strip('\n').split(','))]

boards=[]
for l in f.readlines():
    if l == '\n':
        boards.append([])
    else:
        boards[-1].append([int(x) for x in list(l.strip('\n').split(' ')) if x!= ''])
from collections import Counter

marked_ind = [{'row':[], 'col':[], 'num':[]} for x in range(len(boards))]
winning_flag = False
for num in called_nums:
    for ind in range(len(boards)):
        board = boards[ind]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == num:
                    marked_ind[ind]['row'].append(i)
                    marked_ind[ind]['col'].append(j)
                    marked_ind[ind]['num'] = num
                    row_cnt = Counter(marked_ind[ind]['row'])
                    col_cnt = Counter(marked_ind[ind]['col'])
                    if 5 in row_cnt.values() or 5 in col_cnt.values():
                        print(f"winner! board {ind+1} wins on {num} called")
                        winning_board = board
                        winning_mark = marked_ind[ind]
                        winning_number = num
                        winning_flag = True
                if winning_flag:
                    break
            if winning_flag:
                break
        if winning_flag:
            break
    if winning_flag:
        break
#calculate the score
score = 0
for i in range(len(winning_board)):
    for j in range(len(winning_board[0])):
        if (i,j) not in zip(winning_mark['row'], winning_mark['col']):
            score+= winning_board[i][j]

print(score*winning_number)

#part 2
marked_ind = [{'row':[], 'col':[], 'num':[]} for x in range(len(boards))]
boards_with_wins = []
winning_flag = False
for num in called_nums:
    for ind in range(len(boards)):
        board = boards[ind]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == num:
                    marked_ind[ind]['row'].append(i)
                    marked_ind[ind]['col'].append(j)
                    marked_ind[ind]['num'] = num
                    row_cnt = Counter(marked_ind[ind]['row'])
                    col_cnt = Counter(marked_ind[ind]['col'])
                    if 5 in row_cnt.values() or 5 in col_cnt.values():
                        if ind not in boards_with_wins:
                            if len(boards_with_wins)<len(boards)-1: #new board
                                boards_with_wins.append(ind)
                            else:
                                print(f"last winner! board {ind+1} wins on {num} called")
                                winning_board = board
                                winning_mark = marked_ind[ind]
                                winning_number = num
                                winning_flag = True
                                break
                if winning_flag:
                    break
            if winning_flag:
                break
        if winning_flag:
            break
    if winning_flag:
        break
#calculate the score
score = 0
for i in range(len(winning_board)):
    for j in range(len(winning_board[0])):
        if (i,j) not in zip(winning_mark['row'], winning_mark['col']):
            score+= winning_board[i][j]

print(score*winning_number)


