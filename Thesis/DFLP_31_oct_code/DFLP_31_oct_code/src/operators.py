import random
import sys

class Operators():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('6-10-data2.txt', 'a')

    ######################################################################
    # OnWall Ineffective Colision
    ######################################################################
    def on_wall(self, molecule): # new operator designed by me
        m = molecule[:]

        i = random.randint(0, len(molecule) - 1)
        j = random.randint(0, len(molecule) - 1)
        while i == j:
            j = random.randint(0, len(molecule)-1)
            print('i: {}  j: {}'.format(i+1, j+1))

        m[i], m[j] = m[j], m[i]


        print('m[j] = {}'.format(m[j]))
        # Endif
        # print(m)
        # m = Operators().repair(m)

        return m


    def O_OnWall (self,molecule):
        m = molecule
        i = random.randint(0, len(molecule)-1)
        j = random.randint(0, len(molecule)-1)
        m1 =[]
        for b in range(0,len(m)):
            m1.append(0)
        for a in range(0,len(m)):
            if a == i:
                m1[a] = m[i]
            elif a == j:
                m[a] = m[j]
            else:
                m[a] = m[a]

        # print(m)

        return m
    def OnWall(self,molecule) :
        m = molecule[:]
        i = random.randint(1,2 )
        print('m = {}, i = {}'.format(m,i))
        for itr in range(i):
            j = random.randint(0, len(molecule) - 1)
            a = Operators().on_wall(molecule[i])
            m[j] = a
            print('m = {}, a = {}'.format(m, a))
        return m

    ######################################################################
    # Decomposition
    ######################################################################
    def O_Decomposition (self,molecule):

        length = len(molecule)
        m1 = list(range(length))
        m2 = list(range(length))
        mid =int(length/2)


        # First half goes to the first half of the new molecule1
        for i in range(0,mid):
            m1[i] = molecule[i]
            #m1[i] = Operators().Repair(m1[i])
        #Endfor
        # Second half goes to the second half of the new molecule2
        for i in range(mid,length):
            m2[i] = molecule[i]
            #m2[i] = Operators().Repair(m2[i])
        #Endfor

        # Molecule1 second half randomly chosen
        for i in range(mid,length):
            for j in range(4000):
                for k in range(200):
                    pass
                #Endfor
            #Endfor
            m1[i] = random.randint(1, length-1)
        #Endfor

        # Molecule2 first half randomly chosen
        for i in range(0,mid):
            for j in range(4000):
                for k in range(200):
                    pass
                #Endfor
            #Endfor
            m2[i] = random.randint(1, length)
        #Endfor

        #test
        # print(m1)
        # print(m2)
        # Return 2 new molecule
        #deleted
        #m1 = Operators().Repair(m1)
        #m2 = Operators().Repair(m2)

        return m1,m2

    def Decomposition(self,molecule) :
        m1 = []
        m2 = []
        for i in range(0,len(molecule)):
            a,b = Operators().O_Decomposition(molecule[i])
            a = Operators().Repair(a)
            b = Operators().Repair(b)
            m1.append(a)
            m2.append(b)

        return m1,m2
    ######################################################################
    # Intermolecular Ineffective Colision
    ######################################################################

    def O_Intermolecular(self,molecule1, molecule2):
        length1 = len(molecule1)
        length2 = len(molecule2)
        m1 = list(range(length1))
        m2 = list(range(length2))

        #Random numbers x1, x2 generation
        x1 = random.randint(0, length1)
        for j in range(4000):
            for k in range(200):
                pass
            #Endf
        #Endf
        x2 = random.randint(0, length2)

        # Randormly choose form molecule1 or molecule2
        for i in range(0,length1):
            if (i<x1 or i>x2):  #if odd segments
                m1[i] = molecule1[i]
                #m1[i] = Operators().Repair(m1[i])
                m2[i] = molecule2[i]
                #m2[i] = Operators().Repair(m2[i])

            elif (i>=x1 and x2>=i): # if even segment
                m1[i] = molecule2[i]
                #m1[i] = Operators().Repair(m1[i])
                m2[i] = molecule1[i]
                #m2[i] = Operators().Repair(m2[i])

        #test
        # print(m1)
        # print(m2)
        # Return 2 new molecule


        m1 = Operators().Repair(m1)
        m2 = Operators().Repair(m2)

        return m1,m2
    def Intermolecular(self,molecule1,molecule2) :
        m1 = []
        m2 = []
        for i in range(0,len(molecule1)):
            a,b = Operators().O_Intermolecular(molecule1[i],molecule2[i])
            m1.append(a)

            m2.append(b)

        return m1,m2

    ######################################################################
    # Synthesis
    ######################################################################
    def O_Synthesis(self,molecule1, molecule2):

        length = len(molecule1)
        m = list(range(length))
        m = list(range(length))
        for i in range(0,length):
            r = random.uniform(0, 1)
            if (r<.5):
                m[i] = molecule1[i]
            else:
               m[i] = molecule2[i]

        #test
        # print(m)


        m = Operators().Repair(m)
        return m
    def Synthesis(self,molecule1,molecule2) :
        m = []
        for i in range(0,len(molecule1)):
            a = Operators().O_Synthesis(molecule1[i],molecule2[i])
            #a = Operators.Repair(a)
            m.append(a)
        return m
    ######################################################################
    # Repair operator
    ######################################################################
    def Repair(self,molecule):
        unique = []
        for n in molecule:
            if n not in unique:
                unique.append(n)
        if len(unique) != len(molecule):
            for x in range(1,len(molecule)+1):
                if x not in unique:
                    if x <= len(molecule):
                        unique.append(x)

        return unique
        #return molecule



######################################################################
#Module Test
######################################################################
'''
op = Operators()
mol = [1, 2, 3, 5, 8, 10, 5, 2, 5, 1]
mol2 = [1, 2, 4, 5, 8, 10, 0, 3, 5, 1]

sequence1 = [[2,4,6,1,3,5],[2,4,6,1,3,5],[2,6,4,1,5,3],[2,6,4,1,5,3],[2,1,4,6,5,3]]
sequence2 = [[1,3,5,6,4,2], [1,4,2,5,3,6],  [1,5,3,2,4,6], [1,6,4,2,5,3], [3,2,6,4,1,5]]
y =0
#op.OnWall(mol)
#x = op.OnWall(sequence1)


#x,y = op.Decomposition(sequence1)


#x,y = op.Intermolecular(sequence1,sequence2)
#x,y = op.U_Intermolecular(sequence1,sequence2)

x = op.Synthesis(sequence1,sequence2)
#x = op.Synthesis(sequence1,sequence2)

print(x)
print(y)

# op.OnWall(mol2)
# op.Decomposition(mol)
# op.Intermolecular(mol,mol2)
# op.Synthesis(mol,mol2)
'''

