def my_set_problem1():
    n = int(input())
    country = []
    for i in range(n):
        country.append(input())
    country = set(country)
    print(len(country))


def my_set_problem_2():
    n = int(input())
    s = set(map(int, input().split()))
    nc = int(input())
    cmd = []
    for i in range(nc):
        cmd.append(input())
    print(cmd)
    for item in cmd:
        if item.strip(' ') == 'pop':
            s.pop()
            print('after pop s = ', s)
        elif item.__contains__('discard'):
            i = item.split(' ')
            s.discard(int(i[1]))
            print('after  ', item, 's = ', s)
        elif item.__contains__('remove'):
            i = item.split(' ')
            s.remove(int(i[1]))
            print('after  ', item, 's = ', s)
    print(sum(s))
my_set_problem_2()
