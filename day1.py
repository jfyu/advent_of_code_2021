#get input
input = []
f = open('inputs/day1_input.txt')
for line in f.readlines():
    input.append(int(line.strip('\n')))

#part one
count = 0
for i in range(1,len(input)):
    if input[i]>input[i-1]:
        count+=1
print(count)

#part 2
sum_count = 0

previous_sum = sum(input[0:3])
for j in range(1, len(input)):
    if j>len(input)-3:
        break
    else:
        curr_sum = sum(input[j:j+3])
    if  curr_sum > previous_sum:
            sum_count+=1
    previous_sum = curr_sum
print(sum_count)




