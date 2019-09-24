import numpy as np
import random
import re


strs = input("Please input w0,w1,w2,m,n: ")
#strs = strs.split(",", strs.count(','))
strs = re.findall(r"\d+\.?\d*",strs)

for i in range(len(strs)):   #split the input data
    strs[i] = int(strs[i])

w0 = strs[0]
w1 = strs[1]
w2 = strs[2]
m = strs[3]
n = strs[4]

positive = []  # generate a blank list to store '+'
negative = []  # generate a blank list to store '-'

while len(negative) < n:  # when the number of "negative" values reach n, terminate the loop
     temp1 = round(random.uniform(-100, 100), 1)  # generate a random value to represent input x1
     temp2 = round(random.uniform(-100, 100), 1)  # generate a random value to represent input x2

     if np.sign(temp1 * w1 + temp2 * w2 + w0) == -1:
            temp = [temp1, temp2]
            temp.append('-')
            negative.append(temp)  # generate a "negative" list that contains x1, x2 and its sign

while len(positive) < m:  # when the number of "positive" values reach m, terminate the loop
    temp1 = round(random.uniform(-100, 100), 1)
    temp2 = round(random.uniform(-100, 100), 1)
    if np.sign(temp1 * w1 + temp2 * w2 + w0) == 1:
            temp = [temp1, temp2]
            temp.append('+')
            positive.append(temp)  # generate a "positive" list that contains x1, x2 and its sign
lists = positive + negative
print(lists)

output = open('train.txt', 'w', encoding='gbk')  # generate a txt file to store all the data points
for row in lists:
    rowtxt = '{},{},{}'.format(row[0], row[1], row[2])
    output.write(rowtxt)
    output.write('\n')
output.close()




