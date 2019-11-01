def sockMerchant(n, ar):
    match = []
    count = 0
    for i in range(len(ar)):
        if str(ar[i]) not in match:
            match.append(str(ar[i]))
            match.append(1)
        else:
            for k in range(0, len(match)-1, 2):
                if str(ar[i]) == match[k]:
                    match[k+1] += 1
    # print(match)
    for j in range(1, len(match),2):
        count += match[j]//2
    return count


# sockMerchant(9, [10,20,20,10,10,10,30,50,10,20])
# print(sockMerchant(10,[1,1,3,1,2,1,3,3,3,3]))

arr = []
n = int(input())


a = input().split(' ')
arr = list(a)
print(sockMerchant(n, arr))