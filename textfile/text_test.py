#  write and create a file if it does not exist in library
contents = []
f = open("guru99.txt", "r")
if f.mode == 'r':
    contents = f.read()
    # print(contents)

fl = f.readlines()
my_list = []
for x in f.readlines():
    print(x)
print(my_list)


file = open("guru99.txt", "a+")

for i in range(10):
    file.write("This is line3 %d\r\n" % (i+1))

file.close()

