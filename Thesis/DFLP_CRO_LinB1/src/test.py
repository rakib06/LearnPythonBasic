#!/usr/bin/python3

# read the lines from the file
fh = open('../dataset/dlp6_5/data1.txt')
for line in fh.readlines():
    print(line, end='')


def FizzBuzz(num):
    t = ''
    for i in range(1, num + 1):
        s = str(i)
        if i % 3 == 0 and i % 5 != 0: s = 'Fizz'
        if i % 5 == 0 and i % 3 != 0: s = 'Buzz'
        if i % 5 == 0 and i % 3 == 0: s = 'FizzBuzz'
        if num == i:
            t += s
        else:
            t += s+' '
        # code goes here
    return t


# keep this function call here
print(FizzBuzz(15))


def LRUCache(strArr):
    ls = []
    for item in strArr:
        if len(ls) == 5 and item not in ls:
            ls.remove(ls[0])
        if item not in ls:
            ls.append(item)
        if item in ls:
            ls.remove(item)
            ls.append(item)
    ls_str = ''
    n = len(ls)
    for i in range (0,n):
        if i < n-1:
            ls_str+=ls[i]+'-'
        else:
            ls_str+= ls[i]

    return ls_str

# keep this function call here
print (LRUCache( ["B", "A", "C", "D", "E", "Z", "Q", "G"]))

