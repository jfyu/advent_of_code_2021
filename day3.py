#part 1
import os

f = open(os.path.expanduser('~/projects/advent_of_code/inputs/day3_inputs.txt'))
inputs = []
for l in f.readlines():
    inputs.append(list(l.strip('\n')))

#now input is a matrix
from collections import Counter, OrderedDict

gamma_l = []
epsilon_l = []
for i in range(len(inputs[0])):
    col = [x[i] for x in inputs]
    cnts = list(sorted(Counter(col).items(), key=lambda item:item[1], reverse=True))
    gamma_l.append(cnts[0][0])
    epsilon_l.append(cnts[1][0])

gamma = int(''.join(gamma_l),2)
epsilon = int(''.join(epsilon_l),2)
power = gamma*epsilon
print(f"gamma = {gamma}, epsilon = {epsilon}, power = {power}")

#part 2

#o2
candidates_o2 = inputs.copy()
i = 0
while len(candidates_o2) > 1:
    col = [x[i] for x in candidates_o2]
    cnts = list(sorted(Counter(col).items(), key=lambda item:(item[1], item[0]), reverse=True))
    keep_o2=cnts[0][0]
    #now remove the candidates
    keep_candidates = []
    for j in range(len(candidates_o2)):
        if candidates_o2[j][i] == keep_o2:
            keep_candidates.append(j)
    candidates_o2 = [candidates_o2[ind] for ind in keep_candidates]
    i+=1
o2_rating = int(''.join(candidates_o2[0]),2)
print(f"o2 generator rating is {o2_rating}")

candidates_co2 = inputs.copy()
i = 0
while len(candidates_co2) > 1:
    col = [x[i] for x in candidates_co2]
    cnts = list(sorted(Counter(col).items(), key=lambda item:(item[1], item[0])))
    keep_co2=cnts[0][0]
    #now remove the candidates
    keep_candidates = []
    for j in range(len(candidates_co2)):
        if candidates_co2[j][i] == keep_co2:
            keep_candidates.append(j)
    candidates_co2 = [candidates_co2[ind] for ind in keep_candidates]
    i+=1
co2_rating = int(''.join(candidates_co2[0]),2)
print(f"co2 generator rating is {co2_rating}")

print(f"life support rating is {o2_rating*co2_rating}")


