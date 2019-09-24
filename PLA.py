import numpy as np
import random
import matplotlib.pyplot as plt

f = open("train.txt","r")
str = f.readlines()     #put all the data points in txt file into variable "str"
f.close()

x1 = []   #generate a blank list to restore x1 seperated from sequence 'x1,x2,'sign''
x2 = []   #generate a blank list to restore x2 seperated from sequence 'x1,x2,'sign''
labels = []  #generate a blank list to restore the sign of data point seperated from sequence 'x1,x2,'sign''
sign = []

w0 = 1
w1 = 1
w2 = 1
#W = np.array([w0,w1,w2])
#generate w0, w1, w2 as weights and bias of the input data

w0_original = w0
w1_original = w1
w2_original = w2
#w_original = np.array([w0_original,w1_original,w2_original])

for item in str:
    item_split = item.split(',',3)
    x1.append(float(item_split[0]))
    x2.append(float(item_split[1]))
    labels.append(item_split[2].strip('\n'))
#split the data points into x1, x2 and the sign of data point
#X = np.array([x1,x2])

for label in labels:
    if label == '+':
        sign.append(1)
    else:
        sign.append(-1)
#genrate a list storing the output of data points


i = 0
while i < len(sign):
    if sign[i] != np.sign(w0 + w1 * x1[i] + w2 * x2[i]):
        w1 = w1 + sign[i] * x1[i]
        w2 = w2 + sign[i] * x2[i]
        w0 = w0 + sign[i]
        i = 0
    else:
        i += 1

                # update the weights and bias by the PLA algorithm

print(w0)
print(w1)
print(w2)

k1 = -1 * (w1/w2)
b1 = -1 * (w0/w2)

k2 = -1 * (w1_original/w2_original)
b2 = -1 * (w0_original/w2_original)

k3 = -1 * (1/2)
b3 = -1 * (1/2)

x = np.arange(-100,100,0.01)
y1 = k1 * x + b1
y2 = k2 * x + b2
y3 = k3 * x + b3
plt.plot(x,y1,label='trained line',color='black')   #plot the line represented by trained <w0,w1,w2>.
plt.plot(x,y3,label='actual line',color='green')    #plot the line represented by actual <w0,w1,w2>.
plt.legend(loc=0,ncol=2)
for j in range(len(labels)):
    if labels[j] == '+':
        plt.scatter(x1[j], x2[j],c='b')
    else:
        plt.scatter(x1[j],x2[j],c='r',marker='x')
        #plot the data points
plt.title('Perceptron Learning Algorithm')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()