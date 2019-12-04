'''

name = str(input("Insert Name:"))
surname = str(input("Insert surname:"))
age = int(input('Zadaj age:'))
text = 'Name:'+name+'\nsurname '+surname+'\nAge: '+str(age)

text_file = open("Output.txt", "w")
text_file.write(text)
text_file.close()

file = open("Output.txt", "r")
print(file.readline())

file = open("Output.txt", "a")
x = input('Birth Year:')
text = 'Birth year'+str(x)
file.write('\n'+x)
file.close()

file = open("Output.txt", "r")
for line in file:
    print(line)
file.close()
'''

import numpy as np
x = np.array([14, 21, 24, 24])
y = np.array([12, 6, 23, 29])
z = np.array([x, y])
print(z.size)
print(z.shape)

q = [22, 41, 14, 41, 39, 15]
print(max(q))

store = np.array([0, 9, 0, 1])
cost = np.array([82, 82, 73, 73])
np_cols = list((store, cost))
print(np_cols)

p = [0, 5, 15, 5, 10, 8]
print(sorted(p))