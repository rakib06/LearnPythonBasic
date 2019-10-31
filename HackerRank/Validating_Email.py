import email.utils

n = int(input())
my_list = []

for i in range(n):
    email_format = input()
    my_list.append(email.utils.parseaddr(email_format))
    try:
        u1, d1, e1 = False, False, False
        all = my_list[i][1].split('@')
        username = all[0]
        if (username.isalnum() or username.find('.') or username.find('_') or username.find('-')) and (str(list(username)[0])).isalpha():
            u1 = True
        domain_extension = all[1].split('.')
        domain = domain_extension[0]
        if domain.isalpha():
            d1 = True

        extension = domain_extension[1]
        others = domain_extension[2:]
        if 1 <= len(extension) <= 3 and extension.isalpha():
            e1 = True
        if u1 and d1 and e1 and others == []:
            print(email.utils.formataddr((my_list[i])))
        # print(u1,d1,e1)
        # print(username, ' ', domain, ' ', extension, ' ', others)

    except:
        pass
'''    
for i in range(len(my_list)):
    for item in my_list[0]:
        print(type(item))
'''



