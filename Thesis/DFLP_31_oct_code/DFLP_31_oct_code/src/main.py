import os
import population
from molecule import Molecule
from cro import CRO
import random
import time
from initial_sequence_generator import Sequence
import sys
start_time = time.time()
print("--- %s seconds ---" % (time.time() - start_time))

class Main:
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('6-10-data2.txt', 'a')

    def dataClean(self, f):#file

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

    def shiftCost(self, myList, departments):

        shiftCost = []
        flowCost = []
        flowCost2 = []

        for i in range(3,len(myList)):
            if i >= len(myList) - departments :
                shiftCost.append(myList[i])
            else:
                if len(flowCost) >= 6:
                    # print (len(flowCost)   % departments )
                    flowCost2.append(flowCost)
                    flowCost =[]
                    flowCost.append(myList[i])
                else:
                    flowCost.append(myList[i])
        return shiftCost

    def allflowCost(self, myList,departments):

        shiftCost = []

        flowCost = []
        flowCost2 =[]
        for i in range(3,len(myList)):
            if i >= len(myList) - departments :
                shiftCost.append(myList[i])
            else:

                if len(flowCost) >= departments:
                    # print (len(flowCost)   % departments )
                    flowCost2.append(flowCost)
                    flowCost =[]
                    flowCost.append(myList[i])
                else:
                    flowCost.append(myList[i])
        flowCost2.append(flowCost)
        return flowCost2

    def timeBaseflowcost(self, time,depart,totalFC):
        t_f_1= []
        for k in range(depart*time, depart+time*depart):

            for l in range (0, depart):
                t_f_1.append(totalFC[k][l])
        return t_f_1

    def SequenceGenerator(self,period, department):
        numbers = []

        for j in range(0,period):
            num = []
            for i in range(1,department + 1):
                num.append(i)
            random.shuffle(num)
            numbers.append(num)

        return numbers

    def run(self):
        # path = "../data/sa/"
        path = '../data/input/dlp 6-5/'
        filename = 'data8.txt'
        f = open(path + filename, "r")
        iteration = 80
        myList = Main().dataClean(f)
        department = myList[0]  # N = number of departments
        period = myList [1] # P = total time period
        # print(myList)
        shiftCost = Main().shiftCost(myList,department)
        flowCost = Main().allflowCost(myList,department)
        print(flowCost)
        print(shiftCost)
        P, N = period,department
        # print(department)
        # print(period)
        print(period)
        sequence_object = Sequence()
        sequence = sequence_object.sequence_generator_smart( department,period,filename)
        # sequence = [[1,3,5,6,4,2], [1,4,2,5,3,6],  [1,5,3,2,4,6], [1,6,4,2,5,3], [3,2,6,4,1,5]]
        # sequence = [[6, 2, 25, 29, 22, 9, 17, 4, 11, 10, 18, 7, 5, 12, 21, 3, 28, 19, 20, 24, 27, 1, 8, 13, 14, 15,
        # 16, 23, 26, 30], [27, 23, 10, 16, 14, 28, 24, 2, 4, 17, 22, 6, 12, 7, 30, 1, 8, 3, 29, 18, 21, 13, 5, 9, 11, 15, 19, 20, 25, 26], [27, 23, 18, 16, 14, 28, 24, 2, 4, 17, 22, 6, 12, 7, 30, 1, 8, 3, 29, 10, 21, 13, 5, 9, 11, 15, 19, 20, 25, 26], [11, 20, 1, 15, 4, 9, 5, 12, 30, 14, 21, 28, 6, 24, 22, 17, 29, 25, 23, 27, 10, 2, 3, 7, 8, 13, 16, 18, 19, 26], [27, 3, 24, 20, 14, 5, 9, 28, 2, 16, 17, 10, 4, 7, 6, 25, 15, 18, 29, 22, 21, 1, 8, 11, 12, 13, 19, 23, 26, 30], [14, 16, 13, 26, 17, 6, 29, 25, 12, 7, 20, 30, 8, 1, 5, 11, 21, 28, 2, 24, 23, 3, 4, 9, 10, 15, 18, 19, 22, 27], [27, 23, 10, 16, 14, 28, 24, 2, 4, 17, 3, 6, 12, 7, 30, 18, 13, 22, 11, 1, 8, 5, 9, 15, 19, 20, 21, 25, 26, 29], [10, 21, 6, 23, 7, 9, 2, 5, 28, 20, 30, 18, 25, 4, 14, 17, 3, 16, 15, 29, 19, 1, 13, 8, 11, 12, 22, 24, 26, 27], [27, 23, 4, 16, 14, 28, 24, 2, 10, 17, 22, 6, 12, 7, 30, 21, 5, 29, 25, 1, 3, 8, 9, 11, 13, 15, 18, 19, 20, 26], [23, 21, 22, 10, 12, 28, 19, 14, 24, 6, 29, 2, 13, 20, 11, 16, 8, 7, 17, 27, 15, 4, 1, 3, 5, 9, 18, 25, 26, 30]]
        # sequence1,testSequence1 = Main().SequenceGenerator(P,N)
        # sequence2,testSequence2 = Main().SequenceGenerator(P,N)
        # print(sequence)

        # Parameters
        popSize = 30
        KELossRate= 0.45
        MoleColl= 0.35
        InitialKE= 0
        # non negative number tolerance of system accepting worst solution
        alpha = 5
        beta = 6
        buffer = 0

        # ----------------------------------------------------------------------------------------------
        # Population generation
        # ----------------------------------------------------------------------------------------------
        # sequence = testSequence

        sequence = Main.SequenceGenerator(self, period, department)
        mole = Molecule()
        mole.Mol(sequence,period,department,shiftCost,flowCost)

        # Save initial information
        minEnergy = 999999
        index = 0
        minIndex = 0
        # initPop = [[6, 4, 1, 2, 5, 3], [1, 6, 4, 2, 5, 3], [1, 5, 4, 2, 3, 6], [2, 5, 3, 1, 4, 6], [2, 3, 1, 5, 4, 6]]
        initPop = Main.SequenceGenerator(period,period,department)
        initPop = sequence
        # end for
        # initPop.write("\n")
        # ----------------------------------------------------------------------------------------------
        # Optimize with CRO
        # ----------------------------------------------------------------------------------------------
        c = CRO()
        # C.Init(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole)

        c.CRO(popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration,initPop,shiftCost,flowCost,N)



    # end function
# end class
# for i in range(10):


x = Main()
x.run()
