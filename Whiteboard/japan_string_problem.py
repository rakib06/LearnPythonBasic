# input: ['ahffaksfajeeubsne','jefaa']

def minwindowSubstring(mainstr):
    mystr = mainstr[0]
    substr = mainstr[1]
    l1 = len(mystr)
    l2 = len(substr)

    have_str = []
    found = False
    for i in range(l1-l2):
        cn = 0
        my_s = mystr[i:l2+i]
        test = 1
        for j in range(l2):
            print(substr[j])
            print(my_s)
            if substr[j] in my_s:
                found = True
                print(my_s)
            elif not found:
                cn += 1
                j = j-1
                print('hi : ',mystr[i+l2+cn])
                my_s = my_s + mystr[i + l2 + cn]
        if not found :
            for item in have_str:
                if len(my_s) < len(item) or len(have_str) == 0:
                    have_str.append(my_s)


    print(have_str)
    have_str.sort(key=len)
    print(have_str)


# string = input('String: ')
# substring = input('Substring: ')
string = 'ahffaksfajeeubsne'
substring = 'jefaa'
minwindowSubstring([string, substring])