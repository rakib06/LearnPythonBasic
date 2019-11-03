n,m = map(int,input().split())
arr = input().split(' ')
A = set(input().split(' '))
B = set(input().split(' '))
happiness=0

for i in arr:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)

# to avoid time limit we avoid set and map