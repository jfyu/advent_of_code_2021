#import data
import os
f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day10_inputs.txt'))
inputs = []
for l in f.readlines():
    inputs.append(l.strip('\n'))

mapping = {'(':')', '[':']', '{':'}', '<':'>'}

illegal_char = []
correct_char = []
for l in inputs:
    stack = []
    cur_line = []
    for i in range(len(l)):
        char = list(l)[i]
        if  char in mapping.keys():
            stack.append(char)
        else:
            last_bracket = stack.pop()
            if char == mapping[last_bracket]:
                pass
            else:
                illegal_char.append(char)
                correct_char.append(mapping[last_bracket])
                break
print(illegal_char)

pts_lookup = {')':3, ']':57, '}':1197, '>':25137}

print(sum([pts_lookup[x] for x in illegal_char]))

#part 2
lines_kept = []
need_to_complete=[]
for l in inputs:
    stack = []
    cur_line = []
    corrupt_flag = False
    for i in range(len(l)):
        char = list(l)[i]
        if  char in mapping.keys():
            stack.append(char)
            cur_line.append(char)
        else:
            last_bracket = stack.pop()
            if char == mapping[last_bracket]:
                cur_line.append(char)
            else:
                corrupt_flag = True
                break
    if corrupt_flag is False:
        if len(stack)>0:
            need_to_complete.append(''.join(stack))
        lines_kept.append(''.join(cur_line))

pts_complete_mapping = {')':1, ']':2,'}':3, '>':4}

complete_add = []
total_score = []
for l in need_to_complete:
    completion_line = []
    score = 0
    for i in range(len(l)-1,-1, -1):
        char = list(l)[i]
        completion_line.append(mapping[char])
        score = 5*score
        score += pts_complete_mapping[mapping[char]]
    complete_add.append(''.join(completion_line))
    total_score.append(score)
print(complete_add)
print(total_score)
total_score.sort()
print(total_score[len(total_score)//2])

