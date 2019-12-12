import population
import sys

class Molecule():
    # sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('6-10-data2.txt', 'a')

    w = [] # Molecule strcuture
    PE = []  #
    KE = []
    KE1 = []
    NumHit = []
    numHit = []
    minStruct = []
    minPE = []
    minHit = []
    MinHit = [0]
    sequence = []
    #basePairs = {}       # Unique stemlist; size = molSize; Sorted by energy in ascending order
    # Molecule table contains permuated stem info and it is the population
    moleculeTable = [] # Stem list of slide; size = popSize
    moleculeEnergy= [] # Stem list molecule energy; size = popSize
    infoEnergy= None     # i,j stored for energy evaluation
    stemTable = []       # Stem information; size = stemNo; base of the molecule generation
    infoTable = []       # Stem information; size = stemNo; base of the molecule generation
    stemPool= {}         # Dictionary of unused stems during molecule generation; size = popSize (baseSize - molSize)
    molecules= None      # Vienna RNA notation; no use in the program except showing structure
    moleculeShort = []   # Shortened molecule list of dictionary indexed with original length; size = popSize
    scElements = []      # A list of stems (may be shortened) take participate in secondary structure
    pkElements = []      # A list of stems (pseudoknotted) take participate in making pseudoknot
    elements = []        # scElements + pkElements = uniqueElements
    def Mol(self,sequence,period,department,shiftCost,flowCost):

        self.sequence = sequence
        self.PE1 = []
        # Copying the varible to keep original one

        self.sequence1 = population.GenerateMolecule(period, department)
        self.sequence2 = population.GenerateMolecule(period, department)

        self.KE1.append(population.TotalShiftCost(sequence,shiftCost,department))
        self.KE1.append(population.TotalShiftCost(self.sequence1,shiftCost,department))
        self.KE1.append(population.TotalShiftCost(self.sequence2,shiftCost,department))

        #population.PrintInfo(molecule,stemPool,infoEnergy,moleculeEnergy)
        self.PE11 =  population.CalculateEnergy(self.sequence1,shiftCost,flowCost,department)
        self.PE0 =  population.CalculateEnergy(self.sequence,shiftCost,flowCost,department)
        self.PE2 =  population.CalculateEnergy(self.sequence2,shiftCost,flowCost,department)

        self.period = period
        self.department = department
        #print(self.sequence)
        #print(self.sequence2)
        #print(self.sequence1)
        self.moleculeTable = []
        self.moleculeTable.append(self.sequence)
        self.moleculeTable.append(self.sequence2)
        self.moleculeTable.append(self.sequence1)

        self.moleculeEnergy.append(self.PE0)
        self.moleculeEnergy.append(self.PE2)
        self.moleculeEnergy.append(self.PE11)
        print(self.moleculeEnergy)

        initialKE = population.TotalShiftCost(sequence,shiftCost,department)

        for i in range(len(self.moleculeTable)):
            self.PE.append(self.moleculeEnergy[i])
            self.PE1.append(self.moleculeEnergy[i])
            self.KE.append(initialKE)
            self.KE1.append(initialKE)
            self.NumHit.append(0)
            self.numHit.append(0)
            self.minStruct.append(self.sequence)
            self.minPE.append(self.moleculeEnergy[i])
            self.minHit.append(0)
            self.MinHit.append(0)
            print(self.moleculeTable[i])

        #endfor

    #end
#endclass

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# IMPORTANT
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Need to uniquify: moleculeTables
