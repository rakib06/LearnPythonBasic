
def takeCost(elem):
    return elem[3]
my_list = [[8,'2',2,'8'],[8,1,5,'1'],[8,1,1,'3']]
my_list.sort(key=takeCost)
print(my_list)