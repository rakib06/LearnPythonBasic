# input: ['ahffaksfajeeubsne','jefaa']

def minwindowSubstring(mainstr):
    mystr = mainstr[0]
    substr = mainstr[1]
    l1 = len(mystr)
    l2 = len(substr)

    have_str = []
    found_1 = False
    found = False
    for i in range(l1-l2):
        cn = 0
        my_s = mystr[i:l2+i]
        test = 1
        j = 0
        while(j < l2):
            j = j + 1
            print(substr[j-1])
            print(my_s)
            if substr[j-1] in my_s:
                found_1 = True
                print(my_s)
            if j ==l2 and found_1:
                found = True
            else:
                cn += 1
                j = j-1
                print('hi : ', mystr[i+l2+cn-1])
                my_s = my_s + mystr[i + l2 + cn-1]
        if not found:
            for item in have_str:
                if len(my_s) < len(item) or len(have_str) == 0:
                    have_str.append(my_s)


    print(have_str)
    have_str.sort(key=len)
    print(have_str)
str = 'python'
s = 'yo'
for i in range(len(str)):
    c = 0
    for j in range(len(s)):
        if s[j]in str[i:len(s)+c]:
            continue
        else:
            j = j-1
            c = c+1





# string = input('String: ')
# substring = input('Substring: ')
string = 'ahffaksfajeeubsne'
substring = 'jefaa'
minwindowSubstring([string, substring])