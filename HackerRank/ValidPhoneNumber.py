n = int(input())


for i in range(n):
    nn = input()
    try:
        xx = int(nn)
        if len(nn) == 10 and (nn[0]=='7' or nn[0]=='8' or nn[0]=='9'):
            print('YES')
        else:
            print('NO')
    except:
        print('NO')
