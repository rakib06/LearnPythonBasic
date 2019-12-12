import random
import os

# Generates given number of molecules
def GenerateMolecule(period, department):
    molecule = []
    for j in range(0,period):
        num = []
        for i in range(1,department + 1):
            num.append(i)
        random.shuffle(num)
        molecule.append(num)
    return molecule

# end GenerateMolecule function



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


def MHcost (f):
    cost = 0
    fx = 0

    for i in range(0,len(f)):
        for j in range(len(f[i])):
            cost+= f[i][j]
    return cost


def AdjacentCost6(f,sequence):
    adcost = 0
    x = len(sequence)
    for i in range (0,x):
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


def AdjacentCost15(f, sequence):
    adcost = 0
    x = len(sequence)
    for i in range(0, x):
        seq = sequence[i]
        j = i * 15
        k = j + 15
        fc = f[j:k]
        # print('fc = ',fc)
        adcost += (fc[seq[0] - 1][seq[2] - 1] + fc[seq[2] - 1][seq[0] - 1])
        adcost += (fc[seq[0] - 1][seq[3] - 1] + fc[seq[3] - 1][seq[0] - 1])*2
        adcost += (fc[seq[0] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[0] - 1])*3
        adcost += (fc[seq[0] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[0] - 1])
        adcost += (fc[seq[0] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[0] - 1])*2
        adcost += (fc[seq[0] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[0] - 1])*3
        adcost += (fc[seq[0] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[0] - 1])*4
        adcost += (fc[seq[0] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[0] - 1])
        adcost += (fc[seq[0] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[0] - 1])*2
        adcost += (fc[seq[0] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[0] - 1])*3
        adcost += (fc[seq[0] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[0] - 1]) * 4
        adcost += (fc[seq[0] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[0] - 1]) * 5

        adcost += (fc[seq[1] - 1][seq[3] - 1] + fc[seq[3] - 1][seq[1] - 1])
        adcost += (fc[seq[1] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[1] - 1])
        adcost += (fc[seq[1] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[1] - 1])
        adcost += (fc[seq[1] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[1] - 1])
        adcost += (fc[seq[1] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[1] - 1]) * 4

        adcost += (fc[seq[2] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[2] - 1])
        adcost += (fc[seq[2] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[2] - 1])*2
        adcost += (fc[seq[2] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[2] - 1])
        adcost += (fc[seq[2] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[2] - 1])
        adcost += (fc[seq[2] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[2] - 1])*2
        adcost += (fc[seq[2] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[2] - 1])*3
        adcost += (fc[seq[2] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[2] - 1])*2
        adcost += (fc[seq[2] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[2] - 1])*1
        adcost += (fc[seq[2] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[2] - 1])*2
        adcost += (fc[seq[2] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[2] - 1])*3

        adcost += (fc[seq[3] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[3] - 1])*3
        adcost += (fc[seq[3] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[3] - 1])*2
        adcost += (fc[seq[3] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[3] - 1])
        adcost += (fc[seq[3] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[3] - 1])
        adcost += (fc[seq[3] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[3] - 1]) * 4
        adcost += (fc[seq[3] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[3] - 1]) * 2
        adcost += (fc[seq[3] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[3] - 1])
        adcost += (fc[seq[3] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[3] - 1])

        adcost += (fc[seq[4] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[4] - 1]) * 4
        adcost += (fc[seq[4] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[4] - 1]) * 2
        adcost += (fc[seq[4] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[4] - 1])
        adcost += (fc[seq[4] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[4] - 1]) * 5
        adcost += (fc[seq[4] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[4] - 1]) * 4
        adcost += (fc[seq[4] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[13] - 1] + fc[seq[14] - 1][seq[4] - 1]) * 2
        adcost += (fc[seq[4] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[4] - 1]) * 1

        adcost += (fc[seq[5] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[5] - 1]) * 1
        adcost += (fc[seq[5] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[5] - 1]) * 2
        adcost += (fc[seq[5] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[5] - 1]) * 3
        adcost += (fc[seq[5] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[5] - 1]) * 1
        adcost += (fc[seq[5] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[5] - 1]) * 2
        adcost += (fc[seq[5] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[5] - 1]) * 3
        adcost += (fc[seq[5] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[5] - 1]) * 4

        adcost += (fc[seq[6] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[6] - 1]) * 1
        adcost += (fc[seq[6] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[6] - 1]) * 2
        adcost += (fc[seq[6] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[6] - 1]) * 1
        adcost += (fc[seq[6] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[6] - 1]) * 1
        adcost += (fc[seq[6] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[6] - 1]) * 2
        adcost += (fc[seq[6] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[6] - 1]) * 3

        adcost += (fc[seq[7] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[7] - 1]) * 2
        adcost += (fc[seq[7] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[7] - 1]) * 2

        adcost += (fc[seq[8] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[8] - 1]) * 3
        adcost += (fc[seq[8] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[8] - 1]) * 1
        adcost += (fc[seq[8] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[8] - 1]) * 1

        adcost += (fc[seq[9] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[9] - 1]) * 4
        adcost += (fc[seq[9] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[9] - 1]) * 3
        adcost += (fc[seq[9] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[9] - 1]) * 2
        adcost += (fc[seq[9] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[9] - 1]) * 1

        adcost += (fc[seq[10] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[10] - 1]) * 1
        adcost += (fc[seq[10] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[10] - 1]) * 2
        adcost += (fc[seq[10] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[10] - 1]) * 3

        adcost += (fc[seq[11] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[11] - 1]) * 1
        adcost += (fc[seq[11] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[11] - 1]) * 2

        adcost += (fc[seq[12] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[12] - 1]) * 1

    return adcost


def AdjacentCost30(f,sequence):
    adcost = 0
    x = len(sequence)
    for i in range(0, x):
        seq = sequence[i]
        j = i * 30
        k = j + 30
        fc = f[j:k]
        # print (fc)
        adcost += (fc[seq[0] - 1][seq[2] - 1] + fc[seq[2] - 1][seq[0] - 1])
        adcost += (fc[seq[0] - 1][seq[3] - 1] + fc[seq[3] - 1][seq[0] - 1])*2
        adcost += (fc[seq[0] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[0] - 1])*3
        adcost += (fc[seq[0] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[0] - 1]) * 4
        adcost += (fc[seq[0] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[0] - 1])*1
        adcost += (fc[seq[0] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[0] - 1])*2
        adcost += (fc[seq[0] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[0] - 1])*3
        adcost += (fc[seq[0] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[0] - 1])*4
        adcost += (fc[seq[0] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[0] - 1]) * 5
        adcost += (fc[seq[0] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[0] - 1]) * 1
        adcost += (fc[seq[0] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[0] - 1]) * 2
        adcost += (fc[seq[0] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[0] - 1]) * 3
        adcost += (fc[seq[0] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[0] - 1]) * 4
        adcost += (fc[seq[0] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[0] - 1]) * 5
        adcost += (fc[seq[0] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[0] - 1]) * 6
        adcost += (fc[seq[0] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[0] - 1]) * 2
        adcost += (fc[seq[0] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[0] - 1]) * 3
        adcost += (fc[seq[0] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[0] - 1]) * 4
        adcost += (fc[seq[0] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[0] - 1]) * 5
        adcost += (fc[seq[0] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[0] - 1]) * 6
        adcost += (fc[seq[0] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[0] - 1]) * 7
        adcost += (fc[seq[0] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[0] - 1]) * 3
        adcost += (fc[seq[0] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[0] - 1]) * 4
        adcost += (fc[seq[0] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[0] - 1]) * 5
        adcost += (fc[seq[0] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[0] - 1]) * 6
        adcost += (fc[seq[0] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[0] - 1]) * 7
        adcost += (fc[seq[0] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[0] - 1]) * 8

        # I'm done here 3:55 date : 10/30/2019
        adcost += (fc[seq[1] - 1][seq[3] - 1] + fc[seq[3] - 1][seq[1] - 1]) * 1
        adcost += (fc[seq[1] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[1] - 1]) * 1
        adcost += (fc[seq[1] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[1] - 1]) * 1
        adcost += (fc[seq[1] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[1] - 1]) * 4
        adcost += (fc[seq[1] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[1] - 1]) * 1
        adcost += (fc[seq[1] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[1] - 1]) * 4
        adcost += (fc[seq[1] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[1] - 1]) * 5
        adcost += (fc[seq[1] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[1] - 1]) * 2
        adcost += (fc[seq[1] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[1] - 1]) * 4
        adcost += (fc[seq[1] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[1] - 1]) * 5
        adcost += (fc[seq[1] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[1] - 1]) * 6
        adcost += (fc[seq[1] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[1] - 1]) * 4
        adcost += (fc[seq[1] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[1] - 1]) * 3
        adcost += (fc[seq[1] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[1] - 1]) * 4
        adcost += (fc[seq[1] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[1] - 1]) * 5
        adcost += (fc[seq[1] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[1] - 1]) * 6
        adcost += (fc[seq[1] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[1] - 1]) * 7

        # from 2
        adcost += (fc[seq[2] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[2] - 1]) * 1
        adcost += (fc[seq[2] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[2] - 1]) * 2
        adcost += (fc[seq[2] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[2] - 1]) * 2
        adcost += (fc[seq[2] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[2] - 1]) * 1
        adcost += (fc[seq[2] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[2] - 1]) * 0
        adcost += (fc[seq[2] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[2] - 1]) * 1
        adcost += (fc[seq[2] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[2] - 1]) * 2
        adcost += (fc[seq[2] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[2] - 1]) * 3
        adcost += (fc[seq[2] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[2] - 1]) * 3
        adcost += (fc[seq[2] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[2] - 1]) * 2
        adcost += (fc[seq[2] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[2] - 1]) * 1
        adcost += (fc[seq[2] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[2] - 1]) * 2
        adcost += (fc[seq[2] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[2] - 1]) * 3
        adcost += (fc[seq[2] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[2] - 1]) * 4
        adcost += (fc[seq[2] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[2] - 1]) * 4
        adcost += (fc[seq[2] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[2] - 1]) * 3
        adcost += (fc[seq[2] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[2] - 1]) * 2
        adcost += (fc[seq[2] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[2] - 1]) * 3
        adcost += (fc[seq[2] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[2] - 1]) * 4
        adcost += (fc[seq[2] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[2] - 1]) * 5
        adcost += (fc[seq[2] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[2] - 1]) * 5
        adcost += (fc[seq[2] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[2] - 1]) * 4
        adcost += (fc[seq[2] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[2] - 1]) * 3
        adcost += (fc[seq[2] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[2] - 1]) * 4
        adcost += (fc[seq[2] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[2] - 1]) * 5
        adcost += (fc[seq[2] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[2] - 1]) * 6

        # from 3
        adcost += (fc[seq[3] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[3] - 1]) * 1
        adcost += (fc[seq[3] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[3] - 1]) * 2
        adcost += (fc[seq[3] - 1][seq[8] - 1] + fc[seq[3] - 1][seq[8] - 1]) * 1
        adcost += (fc[seq[3] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[3] - 1]) * 0
        adcost += (fc[seq[3] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[3] - 1]) * 1
        adcost += (fc[seq[3] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[3] - 1]) * 2
        adcost += (fc[seq[3] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[3] - 1]) * 4
        adcost += (fc[seq[3] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[3] - 1]) * 2
        adcost += (fc[seq[3] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[3] - 1]) * 1
        adcost += (fc[seq[3] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[3] - 1]) * 2
        adcost += (fc[seq[3] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[3] - 1]) * 5
        adcost += (fc[seq[3] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[3] - 1]) * 4
        adcost += (fc[seq[3] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[3] - 1]) * 2
        adcost += (fc[seq[3] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[3] - 1]) * 4
        adcost += (fc[seq[3] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[3] - 1]) * 6
        adcost += (fc[seq[3] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[3] - 1]) * 5
        adcost += (fc[seq[3] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[3] - 1]) * 4
        adcost += (fc[seq[3] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[3] - 1]) * 3
        adcost += (fc[seq[3] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[3] - 1]) * 4
        adcost += (fc[seq[3] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[3] - 1]) * 5

        # from 4
        adcost += (fc[seq[4] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[4] - 1]) * 4
        adcost += (fc[seq[4] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[4] - 1]) * 2
        adcost += (fc[seq[4] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[4] - 1]) * 1
        adcost += (fc[seq[4] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[4] - 1]) * 0
        adcost += (fc[seq[4] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[4] - 1]) * 1
        adcost += (fc[seq[4] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[4] - 1]) * 5
        adcost += (fc[seq[4] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[4] - 1]) * 4
        adcost += (fc[seq[4] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[4] - 1]) * 2
        adcost += (fc[seq[4] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[4] - 1]) * 1
        adcost += (fc[seq[4] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[4] - 1]) * 2
        adcost += (fc[seq[4] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[4] - 1]) * 6
        adcost += (fc[seq[4] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[4] - 1]) * 5
        adcost += (fc[seq[4] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[4] - 1]) * 4
        adcost += (fc[seq[4] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[4] - 1]) * 2
        adcost += (fc[seq[4] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[4] - 1]) * 7
        adcost += (fc[seq[4] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[4] - 1]) * 6
        adcost += (fc[seq[4] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[4] - 1]) * 5
        adcost += (fc[seq[4] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[4] - 1]) * 4
        adcost += (fc[seq[4] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[4] - 1]) * 3
        adcost += (fc[seq[4] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[4] - 1]) * 4

        # from 5
        adcost += (fc[seq[5] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[5] - 1]) * 5
        adcost += (fc[seq[5] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[5] - 1]) * 4
        adcost += (fc[seq[5] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[5] - 1]) * 3
        adcost += (fc[seq[5] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[5] - 1]) * 2
        adcost += (fc[seq[5] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[5] - 1]) * 1
        adcost += (fc[seq[5] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[5] - 1]) * 0
        adcost += (fc[seq[5] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[5] - 1]) * 6
        adcost += (fc[seq[5] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[5] - 1]) * 5
        adcost += (fc[seq[5] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[5] - 1]) * 4
        adcost += (fc[seq[5] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[5] - 1]) * 3
        adcost += (fc[seq[5] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[5] - 1]) * 2
        adcost += (fc[seq[5] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[5] - 1]) * 1
        adcost += (fc[seq[5] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[5] - 1]) * 7
        adcost += (fc[seq[5] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[5] - 1]) * 6
        adcost += (fc[seq[5] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[5] - 1]) * 5
        adcost += (fc[seq[5] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[5] - 1]) * 4
        adcost += (fc[seq[5] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[5] - 1]) * 3
        adcost += (fc[seq[5] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[5] - 1]) * 2
        adcost += (fc[seq[5] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[5] - 1]) * 8
        adcost += (fc[seq[5] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[5] - 1]) * 7
        adcost += (fc[seq[5] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[5] - 1]) * 6
        adcost += (fc[seq[5] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[5] - 1]) * 5
        adcost += (fc[seq[5] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[5] - 1]) * 4
        adcost += (fc[seq[5] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[5] - 1]) * 3

        # from 6
        adcost += (fc[seq[6] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[6] - 1]) * 1
        adcost += (fc[seq[6] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[6] - 1]) * 2
        adcost += (fc[seq[6] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[6] - 1]) * 3
        adcost += (fc[seq[6] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[6] - 1]) * 4
        adcost += (fc[seq[6] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[6] - 1]) * 0
        adcost += (fc[seq[6] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[6] - 1]) * 1
        adcost += (fc[seq[6] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[6] - 1]) * 2
        adcost += (fc[seq[6] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[6] - 1]) * 3
        adcost += (fc[seq[6] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[6] - 1]) * 4
        adcost += (fc[seq[6] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[6] - 1]) * 5
        adcost += (fc[seq[6] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[6] - 1]) * 1
        adcost += (fc[seq[6] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[6] - 1]) * 2
        adcost += (fc[seq[6] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[6] - 1]) * 3
        adcost += (fc[seq[6] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[6] - 1]) * 4
        adcost += (fc[seq[6] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[6] - 1]) * 5
        adcost += (fc[seq[6] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[6] - 1]) * 6
        adcost += (fc[seq[6] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[6] - 1]) * 2
        adcost += (fc[seq[6] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[6] - 1]) * 3
        adcost += (fc[seq[6] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[6] - 1]) * 4
        adcost += (fc[seq[6] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[6] - 1]) * 5
        adcost += (fc[seq[6] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[6] - 1]) * 6
        adcost += (fc[seq[6] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[6] - 1]) * 7

        # From 7
        adcost += (fc[seq[7] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[7] - 1]) * 2
        adcost += (fc[seq[7] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[7] - 1]) * 3
        adcost += (fc[seq[7] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[7] - 1]) * 0
        adcost += (fc[seq[7] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[7] - 1]) * 2
        adcost += (fc[seq[7] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[7] - 1]) * 3
        adcost += (fc[seq[7] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[7] - 1]) * 4
        adcost += (fc[seq[7] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[7] - 1]) * 2
        adcost += (fc[seq[7] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[7] - 1]) * 1
        adcost += (fc[seq[7] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[7] - 1]) * 2
        adcost += (fc[seq[7] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[7] - 1]) * 3
        adcost += (fc[seq[7] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[7] - 1]) * 4
        adcost += (fc[seq[7] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[7] - 1]) * 5
        adcost += (fc[seq[7] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[7] - 1]) * 3
        adcost += (fc[seq[7] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[7] - 1]) * 2
        adcost += (fc[seq[7] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[7] - 1]) * 3
        adcost += (fc[seq[7] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[7] - 1]) * 4
        adcost += (fc[seq[7] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[7] - 1]) * 5
        adcost += (fc[seq[7] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[7] - 1]) * 6

        # from 8
        adcost += (fc[seq[8] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[8] - 1]) * 1
        adcost += (fc[seq[8] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[8] - 1]) * 1
        adcost += (fc[seq[8] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[8] - 1]) * 0
        adcost += (fc[seq[8] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[8] - 1]) * 1
        adcost += (fc[seq[8] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[8] - 1]) * 3
        adcost += (fc[seq[8] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[8] - 1]) * 3
        adcost += (fc[seq[8] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[8] - 1]) * 1
        adcost += (fc[seq[8] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[8] - 1]) * 3
        adcost += (fc[seq[8] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[8] - 1]) * 4
        adcost += (fc[seq[8] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[8] - 1]) * 4
        adcost += (fc[seq[8] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[8] - 1]) * 3
        adcost += (fc[seq[8] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[8] - 1]) * 2
        adcost += (fc[seq[8] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[8] - 1]) * 3
        adcost += (fc[seq[8] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[8] - 1]) * 4
        adcost += (fc[seq[8] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[8] - 1]) * 5

        # From 9
        adcost += (fc[seq[9] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[9] - 1]) * 1
        adcost += (fc[seq[9] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[9] - 1]) * 3
        adcost += (fc[seq[9] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[9] - 1]) * 2
        adcost += (fc[seq[9] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[9] - 1]) * 1
        adcost += (fc[seq[9] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[9] - 1]) * 0
        adcost += (fc[seq[9] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[9] - 1]) * 1
        adcost += (fc[seq[9] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[9] - 1]) * 2
        adcost += (fc[seq[9] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[9] - 1]) * 4
        adcost += (fc[seq[9] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[9] - 1]) * 3
        adcost += (fc[seq[9] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[9] - 1]) * 2
        adcost += (fc[seq[9] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[9] - 1]) * 1
        adcost += (fc[seq[9] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[9] - 1]) * 2
        adcost += (fc[seq[9] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[9] - 1]) * 3
        adcost += (fc[seq[9] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[9] - 1]) * 5
        adcost += (fc[seq[9] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[9] - 1]) * 4
        adcost += (fc[seq[9] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[9] - 1]) * 3
        adcost += (fc[seq[9] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[9] - 1]) * 2
        adcost += (fc[seq[9] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[9] - 1]) * 3
        adcost += (fc[seq[9] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[9] - 1]) * 4

        # From 10
        adcost += (fc[seq[10] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[10] - 1]) * 4
        adcost += (fc[seq[10] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[10] - 1]) * 3
        adcost += (fc[seq[10] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[10] - 1]) * 2
        adcost += (fc[seq[10] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[10] - 1]) * 1
        adcost += (fc[seq[10] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[10] - 1]) * 0
        adcost += (fc[seq[10] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[10] - 1]) * 1
        adcost += (fc[seq[10] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[10] - 1]) * 5
        adcost += (fc[seq[10] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[10] - 1]) * 4
        adcost += (fc[seq[10] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[10] - 1]) * 3
        adcost += (fc[seq[10] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[10] - 1]) * 2
        adcost += (fc[seq[10] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[10] - 1]) * 1
        adcost += (fc[seq[10] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[10] - 1]) * 2
        adcost += (fc[seq[10] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[10] - 1]) * 6
        adcost += (fc[seq[10] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[10] - 1]) * 5
        adcost += (fc[seq[10] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[10] - 1]) * 4
        adcost += (fc[seq[10] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[10] - 1]) * 3
        adcost += (fc[seq[10] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[10] - 1]) * 2
        adcost += (fc[seq[10] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[10] - 1]) * 3

        # From 11
        adcost += (fc[seq[11] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[11] - 1]) * 5
        adcost += (fc[seq[11] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[11] - 1]) * 4
        adcost += (fc[seq[11] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[11] - 1]) * 3
        adcost += (fc[seq[11] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[11] - 1]) * 2
        adcost += (fc[seq[11] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[11] - 1]) * 1
        adcost += (fc[seq[11] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[11] - 1]) * 0
        adcost += (fc[seq[11] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[11] - 1]) * 6
        adcost += (fc[seq[11] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[11] - 1]) * 5
        adcost += (fc[seq[11] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[11] - 1]) * 4
        adcost += (fc[seq[11] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[11] - 1]) * 3
        adcost += (fc[seq[11] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[11] - 1]) * 2
        adcost += (fc[seq[11] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[11] - 1]) * 1
        adcost += (fc[seq[11] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[11] - 1]) * 7
        adcost += (fc[seq[11] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[11] - 1]) * 6
        adcost += (fc[seq[11] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[11] - 1]) * 5
        adcost += (fc[seq[11] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[11] - 1]) * 4
        adcost += (fc[seq[11] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[11] - 1]) * 3
        adcost += (fc[seq[11] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[11] - 1]) * 2

        # From 12
        adcost += (fc[seq[12] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[12] - 1]) * 1
        adcost += (fc[seq[12] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[12] - 1]) * 2
        adcost += (fc[seq[12] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[12] - 1]) * 3
        adcost += (fc[seq[12] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[12] - 1]) * 4
        adcost += (fc[seq[12] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[12] - 1]) * 0
        adcost += (fc[seq[12] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[12] - 1]) * 1
        adcost += (fc[seq[12] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[12] - 1]) * 2
        adcost += (fc[seq[12] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[12] - 1]) * 3
        adcost += (fc[seq[12] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[12] - 1]) * 4
        adcost += (fc[seq[12] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[12] - 1]) * 5
        adcost += (fc[seq[12] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[12] - 1]) * 1
        adcost += (fc[seq[12] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[12] - 1]) * 2
        adcost += (fc[seq[12] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[12] - 1]) * 3
        adcost += (fc[seq[12] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[12] - 1]) * 4
        adcost += (fc[seq[12] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[12] - 1]) * 5
        adcost += (fc[seq[12] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[12] - 1]) * 6

        # From 13
        adcost += (fc[seq[13] - 1][seq[15] - 1] + fc[seq[15] - 1][seq[13] - 1]) * 1
        adcost += (fc[seq[13] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[13] - 1]) * 2
        adcost += (fc[seq[13] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[13] - 1]) * 3
        adcost += (fc[seq[13] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[13] - 1]) * 1
        adcost += (fc[seq[13] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[13] - 1]) * 0
        adcost += (fc[seq[13] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[13] - 1]) * 1
        adcost += (fc[seq[13] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[13] - 1]) * 2
        adcost += (fc[seq[13] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[13] - 1]) * 3
        adcost += (fc[seq[13] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[13] - 1]) * 4
        adcost += (fc[seq[13] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[13] - 1]) * 2
        adcost += (fc[seq[13] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[13] - 1]) * 1
        adcost += (fc[seq[13] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[13] - 1]) * 2
        adcost += (fc[seq[13] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[13] - 1]) * 3
        adcost += (fc[seq[13] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[13] - 1]) * 4
        adcost += (fc[seq[13] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[13] - 1]) * 5

        # From 14
        adcost += (fc[seq[14] - 1][seq[16] - 1] + fc[seq[16] - 1][seq[14] - 1]) * 1
        adcost += (fc[seq[14] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[14] - 1]) * 2
        adcost += (fc[seq[14] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[14] - 1]) * 2
        adcost += (fc[seq[14] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[14] - 1]) * 1
        adcost += (fc[seq[14] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[14] - 1]) * 0
        adcost += (fc[seq[14] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[14] - 1]) * 1
        adcost += (fc[seq[14] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[14] - 1]) * 2
        adcost += (fc[seq[14] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[14] - 1]) * 3
        adcost += (fc[seq[14] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[14] - 1]) * 3
        adcost += (fc[seq[14] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[14] - 1]) * 2
        adcost += (fc[seq[14] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[14] - 1]) * 1
        adcost += (fc[seq[14] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[14] - 1]) * 2
        adcost += (fc[seq[14] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[14] - 1]) * 3
        adcost += (fc[seq[14] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[14] - 1]) * 4

        # from 15
        adcost += (fc[seq[15] - 1][seq[17] - 1] + fc[seq[17] - 1][seq[15] - 1]) * 1
        adcost += (fc[seq[15] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[15] - 1]) * 3
        adcost += (fc[seq[15] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[15] - 1]) * 2
        adcost += (fc[seq[15] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[15] - 1]) * 1
        adcost += (fc[seq[15] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[15] - 1]) * 0
        adcost += (fc[seq[15] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[15] - 1]) * 1
        adcost += (fc[seq[15] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[15] - 1]) * 2
        adcost += (fc[seq[15] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[15] - 1]) * 4
        adcost += (fc[seq[15] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[15] - 1]) * 3
        adcost += (fc[seq[15] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[15] - 1]) * 2
        adcost += (fc[seq[15] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[15] - 1]) * 1
        adcost += (fc[seq[15] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[15] - 1]) * 2
        adcost += (fc[seq[15] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[15] - 1]) * 3

        # From 16
        adcost += (fc[seq[16] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[16] - 1]) * 4
        adcost += (fc[seq[16] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[16] - 1]) * 3
        adcost += (fc[seq[16] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[16] - 1]) * 2
        adcost += (fc[seq[16] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[16] - 1]) * 1
        adcost += (fc[seq[16] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[16] - 1]) * 0
        adcost += (fc[seq[16] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[16] - 1]) * 1
        adcost += (fc[seq[16] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[16] - 1]) * 5
        adcost += (fc[seq[16] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[16] - 1]) * 4
        adcost += (fc[seq[16] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[16] - 1]) * 3
        adcost += (fc[seq[16] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[16] - 1]) * 2
        adcost += (fc[seq[16] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[16] - 1]) * 1
        adcost += (fc[seq[16] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[16] - 1]) * 2

        # From 17
        adcost += (fc[seq[17] - 1][seq[18] - 1] + fc[seq[18] - 1][seq[17] - 1]) * 5
        adcost += (fc[seq[17] - 1][seq[19] - 1] + fc[seq[19] - 1][seq[17] - 1]) * 4
        adcost += (fc[seq[17] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[17] - 1]) * 3
        adcost += (fc[seq[17] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[17] - 1]) * 2
        adcost += (fc[seq[17] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[17] - 1]) * 1
        adcost += (fc[seq[17] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[17] - 1]) * 0
        adcost += (fc[seq[17] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[17] - 1]) * 6
        adcost += (fc[seq[17] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[17] - 1]) * 5
        adcost += (fc[seq[17] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[17] - 1]) * 4
        adcost += (fc[seq[17] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[17] - 1]) * 3
        adcost += (fc[seq[17] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[17] - 1]) * 2
        adcost += (fc[seq[17] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[17] - 1]) * 1

        # from 18
        adcost += (fc[seq[18] - 1][seq[20] - 1] + fc[seq[20] - 1][seq[18] - 1]) * 1
        adcost += (fc[seq[18] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[18] - 1]) * 2
        adcost += (fc[seq[18] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[18] - 1]) * 3
        adcost += (fc[seq[18] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[18] - 1]) * 4
        adcost += (fc[seq[18] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[18] - 1]) * 0
        adcost += (fc[seq[18] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[18] - 1]) * 1
        adcost += (fc[seq[18] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[18] - 1]) * 2
        adcost += (fc[seq[18] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[18] - 1]) * 3
        adcost += (fc[seq[18] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[18] - 1]) * 4
        adcost += (fc[seq[18] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[18] - 1]) * 5

        # From 19
        adcost += (fc[seq[19] - 1][seq[21] - 1] + fc[seq[21] - 1][seq[19] - 1]) * 1
        adcost += (fc[seq[19] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[19] - 1]) * 2
        adcost += (fc[seq[19] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[19] - 1]) * 3
        adcost += (fc[seq[19] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[19] - 1]) * 1
        adcost += (fc[seq[19] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[19] - 1]) * 0
        adcost += (fc[seq[19] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[19] - 1]) * 1
        adcost += (fc[seq[19] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[19] - 1]) * 2
        adcost += (fc[seq[19] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[19] - 1]) * 3
        adcost += (fc[seq[19] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[19] - 1]) * 4

        # From 20
        adcost += (fc[seq[20] - 1][seq[22] - 1] + fc[seq[22] - 1][seq[20] - 1]) * 1
        adcost += (fc[seq[20] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[20] - 1]) * 2
        adcost += (fc[seq[20] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[20] - 1]) * 2
        adcost += (fc[seq[20] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[20] - 1]) * 1
        adcost += (fc[seq[20] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[20] - 1]) * 0
        adcost += (fc[seq[20] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[20] - 1]) * 1
        adcost += (fc[seq[20] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[20] - 1]) * 2
        adcost += (fc[seq[20] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[20] - 1]) * 3

        # From 21
        adcost += (fc[seq[21] - 1][seq[23] - 1] + fc[seq[23] - 1][seq[21] - 1]) * 1
        adcost += (fc[seq[21] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[21] - 1]) * 3
        adcost += (fc[seq[21] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[21] - 1]) * 2
        adcost += (fc[seq[21] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[21] - 1]) * 1
        adcost += (fc[seq[21] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[21] - 1]) * 0
        adcost += (fc[seq[21] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[21] - 1]) * 1
        adcost += (fc[seq[21] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[21] - 1]) * 2

        # From 22
        adcost += (fc[seq[22] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[22] - 1]) * 4
        adcost += (fc[seq[22] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[22] - 1]) * 3
        adcost += (fc[seq[22] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[22] - 1]) * 2
        adcost += (fc[seq[22] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[22] - 1]) * 1
        adcost += (fc[seq[22] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[22] - 1]) * 0
        adcost += (fc[seq[22] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[22] - 1]) * 1

        # From 23
        adcost += (fc[seq[23] - 1][seq[24] - 1] + fc[seq[24] - 1][seq[23] - 1]) * 5
        adcost += (fc[seq[23] - 1][seq[25] - 1] + fc[seq[25] - 1][seq[23] - 1]) * 4
        adcost += (fc[seq[23] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[23] - 1]) * 3
        adcost += (fc[seq[23] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[23] - 1]) * 2
        adcost += (fc[seq[23] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[23] - 1]) * 1
        adcost += (fc[seq[23] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[23] - 1]) * 0

        # From 24
        adcost += (fc[seq[24] - 1][seq[26] - 1] + fc[seq[26] - 1][seq[24] - 1]) * 1
        adcost += (fc[seq[24] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[24] - 1]) * 2
        adcost += (fc[seq[24] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[24] - 1]) * 3
        adcost += (fc[seq[24] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[24] - 1]) * 4

        # From 25
        adcost += (fc[seq[25] - 1][seq[27] - 1] + fc[seq[27] - 1][seq[25] - 1]) * 1
        adcost += (fc[seq[25] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[25] - 1]) * 2
        adcost += (fc[seq[25] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[25] - 1]) * 3

        # from 26
        adcost += (fc[seq[26] - 1][seq[28] - 1] + fc[seq[28] - 1][seq[26] - 1]) * 1
        adcost += (fc[seq[26] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[26] - 1]) * 2

        # From 27
        adcost += (fc[seq[27] - 1][seq[29] - 1] + fc[seq[29] - 1][seq[27] - 1]) * 1

    return adcost


def CalculateEnergy(sequence,shiftCost,flowcost,N):
        MC = MHcost(flowcost)
        SC = 0
        AC = 0
        if N == 6:
            AC = AdjacentCost6(flowcost,sequence)
        elif N == 15:
            AC = AdjacentCost15(flowcost, sequence)
        elif N == 30:
            AC = AdjacentCost30(flowcost, sequence)
        else:
            AC = 0

        SC = TotalShiftCost(sequence,shiftCost,N)

        return MC + SC + AC 


# end CalculateEnergy function

# Generates an array of given size and return them with shuffling
def SequenceGenerator(period, department):

    numbers = []
    for j in range (0,period):
        num = []
        for i in range(1,department + 1):
            num.append(i)
        random.shuffle(num)
        numbers.append(num)
    return numbers
    
# end function

def PrintableMolecule(molecule):
    moleculeStr = ""
    for i in molecule:
        moleculeStr+=i
    # endfor
    
    return moleculeStr

# end function
