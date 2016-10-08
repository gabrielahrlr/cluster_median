"""
Created by Gabriela and Maira on December 2014

Input:
- numer of data points

Output:
- InputDataAMPL.txt, For AMPL
- DataPoints.txt, shows the data points

Pre-conditions:
Numpy and matplot.lib packages must be installed

"""

input2 = input("number of data points: m = ")
m = int(input2)

import numpy as np

datSet = 100 * np.random.random_sample((m, 2))

import os

path = os.path.dirname(os.path.realpath(__file__))
f = open(path + '/InputDataAMPL.txt', 'w')
f1 = open(path + '/DataPoints.txt', 'w')
f2 = open(path + '/InputMatrix.txt', 'w')

X = np.zeros((m, m), float)
for i in range(m):
    f1.write(str(datSet[i][0]) + ' ' + str(datSet[i][1]) + '\n')
    for j in range(m):
        dist = np.linalg.norm(datSet[i] - datSet[j])
        X[i][j] = dist
        f.write(str(j + 1) + ' ' + str(i + 1) + '   ' + str(dist) + '\n')
        f2.write(str(dist) + '      ')
    f2.write('\n')

f.close()
f1.close()
f2.close()


import matplotlib.pyplot as plt

plt.scatter(datSet[:, 0], datSet[:, 1])
aux = 1
for dat in datSet:
    plt.annotate(aux, ((dat[0]+1.2), (dat[1]-2)))
    aux += 1
plt.show()

