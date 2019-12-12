import random


### opening the file 

f = open("data9Extra.txt","r")

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
### Raw data , time department, flowcost, and shifting cost
#print(myList)

departments = myList[0]
time_period = myList [1]
print (departments)
print (time_period)
print(len(myList))

### time period X = matrix X 
###  shifing cost = shiftCost[] 
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
			
print(shiftCost)
flowCost2.append(flowCost)
print("Hi:")
print (flowCost2)
print(len(flowCost2))
#print (flowCost2[0])
fc = 0
f=[]
for i in range(0,6):
	f = flowCost2[i]
	for j in range(0,6):
		fc+=f[j]



def AdjacentCost(f,sequence):
	adcost = 0
	for i in range (0,1):
		seq = sequence[i]		
		j = i*6
		k = j + 6
		fc = f[j:k]
		#print (fc)
		
		adcost += (fc [seq[0]-1][seq[2]-1] + fc[seq[2]-1][seq[0]-1])
		#adcost += fc [seq[0]-1][seq[3]-1] + fc[seq[3]-1][seq[0]-1] * 2
		#adcost += (fc [seq[0]-1][seq[4]-1] + fc[seq[4]-1][seq[0]-1]) * 1
		adcost += (fc [seq[0]-1][seq[5]-1] + fc[seq[5]-1][seq[0]-1])*2 

		#adcost += fc [seq[1]-1][seq[3]-1] + fc[seq[3]-1][seq[1]-1]
		#adcost += fc [seq[1]-1][seq[4]-1] + fc[seq[4]-1][seq[1]-1] * 2
		#adcost += fc [seq[1]-1][seq[5]-1] + fc[seq[5]-1][seq[1]-1] * 1

		#adcost += (fc [seq[2]-1][seq[4]-1] + fc[seq[4]-1][seq[2]-1])
		#adcost += fc [seq[2]-1][seq[5]-1] + fc[seq[5]-1][seq[2]-1] * 2
		adcost += (fc [seq[2]-1][seq[3]-1] + fc[seq[3]-1][seq[2]-1])*2

		adcost += (fc [seq[3]-1][seq[5]-1] + fc[seq[5]-1][seq[3]-1])
		#adcost += fc [seq[2]-1][seq[5]-1] + fc[seq[5]-1][seq[2]-1] * 2

		#adcost += fc [seq[0]-1][seq[5]-1] + fc[seq[5]-1][seq[0]-1] * 4
		#adcost += fc [seq[2]-1][seq[3]-1] + fc[seq[3]-1][seq[2]-1]
		#adcost += fc [seq[3]-1][seq[5]-1] + fc[seq[5]-1][seq[3]-1]

	return adcost
sequence = [[1,3,5,6,4,2], [1,4,2,5,3,6],  [1,5,3,2,4,6], [1,6,4,2,5,3], [3,2,6,4,1,5]]	
AC = AdjacentCost(flowCost2,sequence)
print('hi')

print(AC+fc)

def time_period_flowcost_matrix(time,depart,totalFC):
	t_f_1= []
	for k in range (depart*time, depart+time*depart):
	
		for l in range (0, depart):
			t_f_1.append(totalFC[k][l])
	return t_f_1

print("\nSeparate the flowcost for particular time period:")
tf0=time_period_flowcost_matrix(0,departments,flowCost2)
print(tf0)
print(time_period_flowcost_matrix(1,departments,flowCost2))
print(time_period_flowcost_matrix(2,departments,flowCost2))
print(time_period_flowcost_matrix(3,departments,flowCost2))
print(time_period_flowcost_matrix(4,departments,flowCost2))

print("\nSequence using time and number of departments:")

def SequenceGenerator(period, department):

    numbers = []
    for j in range (0,period):
    	num = []
    	for i in range(1,department + 1):
        	num.append(i)
    	random.shuffle(num)
    	numbers.append(num)
    return numbers
    
sg = SequenceGenerator(time_period,departments)

print (sg)

#def distance(single_sequence):
	

def CalculateSingleEnergy( flowcost,sequence):
	cost =0
	for c in flowcost:
		cost += c
	return cost	
	#for i in range (0,len(sequence)):
		#print(flowCost2[1][i])	

print(CalculateSingleEnergy (tf0, sg))



##############################################################################
# 																			 #
#                           data Clean for Objective Function                #
#																			 #
##############################################################################

# input Shifting cost , Sequence 






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
def RearrangementCost(A,Y,P,N): 
	RearrangementCost = 0
	for t in range (2,P):
		for i in range (1,N):
			for j in range (1,N):
				for l in range(1,N):
					RearrangementCost += A[t][i][j][l] * Y[t][i][j][l]
	return RearrangementCost

# f[t][i][k] = flowcost 
# X[t][i][j] = 0/1
# X[t][k][l]
# P = total time period
# N = number of departments  
# d[t][j][l] = distance 
def MHcost (f,d,X,P,N):
	MHcost = 0
	for t in range (1,P):
		for i in range (1,N):
			for j in range (1,N):
				for k in range (1,N):
					for l in range (1,N):
						MHcost += f[t][i][k] * d[t][j][l] * X[t][i][j] * X[t][k][l]
	return MHcost

##############################################################################
# 																			 #
#                           Ojective Function End                            #
#																			 #
##############################################################################