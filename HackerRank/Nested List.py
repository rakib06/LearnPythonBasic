if __name__ == '__main__':
    list = []
    # score_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())

        list.append([score, name])

    list.sort()
    # print(list[0][0])
    sp = list[0][0]
    for item in list:
        if item[0] != sp:
            sp = item[0]
            break
    pnames = []
    for j in list:
        if j[0] == sp:
            pnames.append(j[1])
            #print('if works',j[1])
    pnames.sort()
    for item in pnames:
        print(item)

