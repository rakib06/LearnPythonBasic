'''
for i in range(30):
    for j in range(i+2,30):
        print('adcost += (fc[seq[{}] - 1][seq[{}] - 1] + fc[seq[{}] - 1][seq[{}] - 1]) * 1'.format(i,j,j,i))
'''

mylist = [27, 29, 28, 3, 11, 19, 23, 9, 14, 2, 24, 17, 25, 22, 30, 16, 7, 13, 6, 1, 15, 4, 26, 8, 5, 10, 12, 18, 20, 21]
mylist.sort()
print(mylist)
