ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9

#print(ListOfNumbers)

'''
results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )
        
        
        
'''

# Multiples of 3 below 10
ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]
List = [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
print(len(List))
if __name__ =='__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
