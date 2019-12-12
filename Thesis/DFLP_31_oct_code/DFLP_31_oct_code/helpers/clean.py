import random
#import numpy as np 

### opening the file 

def dataClean(f):#file
	myList = []

	for line in f:
		line.split(" ")
		value2 = ""
		for value in line:
			if value != " " and value != "\t":
				value2 += value		
			else:
				if value2 != "":
					value2 = int(value2)
					myList.append(value2)
				value2 = ""
	return myList
 
def shiftCost(myList,departments):

	shiftCost = []

	flowCost = []
	flowCost2 =[]
	dep = 1;
	time =1;
	for i in range(3,len(myList)):
		if i >= len(myList) - departments :
			shiftCost.append(myList[i])
		else:

			if (len(flowCost) >= 6):
			#print (len(flowCost)   % departments )
				flowCost2.append(flowCost)
				flowCost =[]
				flowCost.append(myList[i])
			else:
				flowCost.append(myList[i])
	return shiftCost


def allflowCost(myList,departments):

	shiftCost = []

	flowCost = []
	flowCost2 =[]
	dep = 1;
	time =1;
	for i in range(3,len(myList)):
		if i >= len(myList) - departments :
			shiftCost.append(myList[i])
		else:

			if (len(flowCost) >= 6):
			#print (len(flowCost)   % departments )
				flowCost2.append(flowCost)
				flowCost =[]
				flowCost.append(myList[i])
			else:
				flowCost.append(myList[i])
	flowCost2.append(flowCost)
	return flowCost2

def timeBaseflowcost(time,depart,totalFC):
	t_f_1= []
	for k in range (depart*time, depart+time*depart):
	
		for l in range (0, depart):
			t_f_1.append(totalFC[k][l])
	return t_f_1

def SequenceGenerator(period, department):
	numbers = []
	testSequence  = []
	for j in range(0,period):
		num = []
		for i in range(1,department + 1):
			num.append(i)
		random.shuffle(num)
		numbers.append(num)
	for i in range (0,period):
		for j in range(0,department):
			testSequence.append(numbers[i][j])
	return numbers,testSequence
    

	#for i in range (0,len(sequence)):
		#print(flowCost2[1][i])	






##############################################################################
# 																			 #
#                           data Clean for Objective Function                #
#																			 #
##############################################################################

# input  
# Y[t][i][j][l] = 0/1
# A[t][i][j][l] = shifting cost 
# P = total time period
# N = number of departments
# f[t][i][k] = flowcost 
# X[t][i][j] = 0/1
# X[t][k][l]
# P = total time period
# N = number of departments  
# d[t][j][l] = distance 

f = open("data1.txt","r")
myList = dataClean(f)
N = myList[0]  # N = number of departments  
P = myList [1] # P = total time period
shiftCost = shiftCost(myList,N)
flowCost = allflowCost(myList,N)
#print (len(flowCost))
#print(shiftCost)
#print(flowCost)
sequence,testSequence  = SequenceGenerator(P,N)
#test rosenbalt
#sg = [1,3,5,6,4,2] # 12822 # 12827  # +5
#sg = [1,4,2,5,3,6] # 14853 # 14387 # -499
#sg = [1,5,3,2,4,6] # 13172  # 13351 # + 179
#sg = [1,6,4,2,5,3] # 13,032  # 13031 # -1
#sg = [3,2,6,4,1,5] # 12,819 # 12,891 # 24 to 30

sequence = [[1,3,5,6,4,2], [1,4,2,5,3,6],  [1,5,3,2,4,6], [1,6,4,2,5,3], [3,2,6,4,1,5]]
#sequence = [[2,4,6,1,3,5],[2,4,6,1,3,5],[2,6,4,1,5,3],[2,6,4,1,5,3],[2,1,4,6,5,3]]
#sequence = [[6,4,2,1,3,5],[6,4,2,1,3,5],[6,4,2,3,5,1],[3,5,2,4,6,1],[3,2,6,4,1,5]]

#sequence = [[1,4,2,5,3,6], [1,3,5,6,4,2],   [1,5,3,2,4,6], [1,6,4,2,5,3], [3,2,6,4,1,5]]

#sequence = [[1,3,5,6,4,2],[1,4,2,5,3,6],[1,5,3,2,4,6],[1,6,4,2,5,3],[3,2,6,4,1,5]] 
#sequence = [[1, 4, 2, 6, 3, 5], [5, 4, 1, 2, 3, 6], [5, 3, 1, 4, 6, 2], [3, 1, 4, 2, 5, 6], [6, 3, 5, 2, 1, 4]]
print(sequence)

print(testSequence)
#print (len(sequence))
#print(shiftCost)
#print(len(shiftCost))


##############################################################################
# 																			 #
#                    End of data Clean for Objective Function                #
#																			 #
##############################################################################




##############################################################################
# 																			 #
#                           Ojective Function                                #
#																			 #
##############################################################################

# Y[t][i][j][l] = 0/1
# A[t][i][j][l] = shifting cost 
# P = total time period
# N = number of departments
# shifting cost pura ok 

def TotalShiftCost(sequence,shiftCost,N):
	sc  = 0
	T = len(sequence)
	for t in range (1,T):
		X1 = sequence[t-1]	
		X2 = sequence[t]	
		for j in range (0,N):
			if (X1.index(j+1) != X2.index(j+1) ):				
				sc += shiftCost[j] 
	return sc

# totally ok :)
# f[t][i][k] = flowcost 
# X[t][i][j] = 0/1
# X[t][k][l]
# P = total time period
# N = number of departments  
# d[t][j][l] = distance 


def MHcost (f):
	cost = 0
	fx = 0

	for i in range(0,len(f)):
		for j in range(len(f[i])):
			cost+= f[i][j]
	return cost
# test for adjacent cost 
'''
fc = flowCost[0:6]
print("fc")
print(fc)
seq = sequence[1]
print(fc[0][2])
x = fc [seq[0]-1][seq[2]-1] + fc[seq[2]-1][seq[0]-1]
print(x)

#end test
'''
#AdjacentCost



def AdjacentCost6(f,sequence):
	adcost = 0
	for i in range (0,5):
		seq = sequence[i]		
		j = i*6
		k = j + 6
		fc = f[j:k]
		#print (fc)
		adcost += (fc [seq[0]-1][seq[2]-1] + fc[seq[2]-1][seq[0]-1]) 
		adcost += (fc [seq[0]-1][seq[4]-1] + fc[seq[4]-1][seq[0]-1])
		adcost += (fc [seq[0]-1][seq[5]-1] + fc[seq[5]-1][seq[0]-1])*2
		adcost += fc [seq[1]-1][seq[3]-1] + fc[seq[3]-1][seq[1]-1] 
		adcost += fc [seq[1]-1][seq[5]-1] + fc[seq[5]-1][seq[1]-1] 
		adcost += (fc [seq[2]-1][seq[3]-1] + fc[seq[3]-1][seq[2]-1])*2
		adcost += (fc [seq[2]-1][seq[4]-1] + fc[seq[4]-1][seq[2]-1])
		adcost += (fc [seq[3]-1][seq[5]-1] + fc[seq[5]-1][seq[3]-1])
		
	return adcost
def CalculatePE(sequence,shiftCost,flowcost,N):
		MC = MHcost(flowcost)
		if (N == 6):
			AC = AdjacentCost6(flowcost,sequence)
		SC = TotalShiftCost(sequence,shiftCost,N)

		return MC + SC + AC 


TSC = TotalShiftCost(sequence,shiftCost,len(shiftCost))
print (TSC)
print(len(sequence[1]))

MC = MHcost(flowCost)
AC = AdjacentCost6(flowCost,sequence)
print("TSC")
print(TSC)

print("MC")
print(MC)

print("AC")
print(AC)

print("MC+AC")
print(MC+AC)

print("TSC+MC+AC")
print(TSC+MC+AC)


totalCost = CalculatePE(sequence,shiftCost,flowCost,N)
print(totalCost)
#MC = MHcost(flowCost,sequence,P)
#print(MC)
##############################################################################
# 																			 #
#                           Ojective Function End                            #
#																			 #
##############################################################################




### Raw data , time department, flowcost, and shifting cost
#print(myList)
'''
f = open("data9Extra.txt","r")

myList = dataClean(f)

departments = myList[0]
time_period = myList [1]
print("Number of departments: ")
print (departments)
print("Time period: ")
print (time_period)
#print(len(myList))

### time period X = matrix X 
###  shifing cost = shiftCost[]
print("Shifting Cost: ")
shiftCost = shiftCost(myList)	

print(shiftCost)
flowCost2 = allflowCost(myList)
#print (flowCost2)
#print (flowCost2[0])
print("\nSeparate the flowcost for particular time period:")

tf0 = timeBaseflowcost(0,departments,flowCost2)
tf1 = timeBaseflowcost(1,departments,flowCost2)
tf2 = timeBaseflowcost(2,departments,flowCost2)
tf3 = timeBaseflowcost(3,departments,flowCost2)
tf4 = timeBaseflowcost(4,departments,flowCost2)
print(tf0)


print("\nSequence using time and number of departments:")

sg = SequenceGenerator(time_period,departments)

print (sg)

#test rosenbalt
#sg = [1,3,5,6,4,2] # 12822 # 12827  # +5
#sg = [1,4,2,5,3,6] # 14853 # 14387 # -499
#sg = [1,5,3,2,4,6] # 13172  # 13351 # + 179
#sg = [1,6,4,2,5,3] # 13,032  # 13031 # -1
#sg = [3,2,6,4,1,5] # 12,819 # 12,891 # 24 to 30

#print(ce)
#print(tf0)
flowcost_t_1 = []
for i in range (0,6):
	flowcost_t_1.append(flowCost2[i])

print(flowcost_t_1)

ce = CalculateSingleEnergy6 (flowcost_t_1, sg[0],tf4,shiftCost)


print(ce)
print(tf1)


'''
