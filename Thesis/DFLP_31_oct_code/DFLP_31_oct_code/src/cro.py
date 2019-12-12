import random
from operators import Operators
from molecule import Molecule
import population
import sys
import time
class CRO():
	# sys.stdin = open('input.txt', 'r')
	# sys.stdout = open('6-10-data2.txt', 'a')


	# Variables
	structureFound = ""
	sensitivity = 0
	specificity = 0
	f_measure = 0
	true_basepair = 0
	false_negative_basepair = 0
	false_positive_basepair = 0

	# CRO parameters
	popSize = 0
	KELossRate = 0
	MoleColl = 0
	InitialKE = 0
	buffer = 0
	alpha = 0
	beta = 0
	sequence = []
	mole = None


	######################################################################
	# CRO Init
	######################################################################
	# def Init(self,popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole):
	# 	self.popSize = popSize
	# 	self.KELossRate = KELossRate
	# 	self.MoleColl = MoleColl
	# 	self.InitialKE = InitialKE
	# 	self.alpha = alpha
	# 	self.beta = beta
	# 	self.self.buffer = self.buffer
	# 	self.sequence = sequence
	# 	self.mole = mole
	# # end function

	######################################################################
	# OnWall Ineffective Colision handler
	######################################################################
	def OnwallIneffectiveCollision(self,mole,oldMol, index,shiftcost,flowcost,N):
		operator = Operators()
		newMol = operator.OnWall(oldMol)
		PEnew = CRO().CalculatePE(newMol,shiftcost,flowcost,N)
		KEnew = 0.0
		#mole.numHit[index] = mole.numHit[index] + 1
		t = mole.PE[index] + mole.KE1[index]
		if (t>=PEnew):
			a = (random.uniform(0,1) * (1-self.KELossRate))+self.KELossRate
			#KEnew = (mole.PE[index] - PEnew + mole.KE[index])*a
			'''
			#mole.KE1[index] = KEnew
			if(mole.PE[index]<mole.minPE[index]):
				mole.minStruct.append(mole)
				#mole.minPE[index] = mole.PE[index]
				#mole.minHit[index] = mole.numHit[index]
			#endif
			'''
		mole.moleculeTable.append(newMol)
		mole.KE1.append(KEnew)
		#print(mole.moleculeTable)
		mole.PE.append(PEnew)
		mole.KE1.append(KEnew)
		#endif
	#end function

	######################################################################
	# Decomposition handler
	######################################################################
	def Decomposition(self,mole,oldMol,index,shiftcost,flowcost,N):
		operator = Operators()
		newMol1, newMol2 = operator.Decomposition(oldMol)
		#print('DEcom ',newMol1,'\n',newMol2)
		pe1 = CRO().CalculatePE(newMol1,shiftcost,flowcost,N)
		pe2 = CRO().CalculatePE(newMol2,shiftcost,flowcost,N)
		mole.moleculeTable.append(newMol1)
		mole.moleculeTable.append(newMol2)
		#print(mole.moleculeTable)
		mole.PE.append(pe1)
		mole.PE.append(pe2)

		e_dec = 0
		gamma1 = 0
		gamma2 = 0
		gamma3 = 0
		gamma1 = random.uniform(0,1)
		gamma2 = random.uniform(0,1)

		if ((mole.PE[index] + mole.KE1[index]) >= (pe1+pe2)):
			e_dec = (mole.PE[index] + mole.KE1[index]) - (pe1 + pe2)
		else:
			e_dec = (mole.PE[index] + mole.KE1[index]) + gamma1 * gamma2 * self.buffer - (pe1 + pe2)
		# endif
		mole.KE1.append(e_dec * gamma3)

		if (e_dec>=0):
			self.buffer = self.buffer * (1 -( gamma1*gamma2))
			gamma3 = random.uniform(0,1)

			#mole.moleculeTable[index] = newMol1
			#mole.PE[index] = pe1
			mole.KE1[index] = e_dec * gamma3
			#mole.numHit[index] = 0
			#mole.minHit[index] = 0
			#mole.minStruct[index] = newMol1
			#mole.minPE[index] = pe1

			#mole.moleculeTable.append(newMol1)
			#mole.PE.append(pe1)
			#mole.KE1.append(e_dec * gamma3)
			mole.numHit.append(0)
			mole.minHit.append(0)
			mole.minStruct.append(newMol1)
			mole.minPE.append(pe1)

		#else:
			#mole.numHit[index] = mole.numHit[index] + 1
		# endif
	# end function

	######################################################################
	# IntermolecularIneffectiveCollision handler
	######################################################################
	def IntermolecularIneffectiveCollision(self,mole,oldMol1,oldMol2,index1,index2,shiftcost,flowcost,N):
		operator = Operators()
		newMol1, newMol2 = operator.Intermolecular(oldMol1, oldMol2)
		pe1 = CRO().CalculatePE(newMol1,shiftcost,flowcost,N)
		pe2 = CRO().CalculatePE(newMol2,shiftcost,flowcost,N)
		
		e_inter = 0
		gamma4 = random.uniform(0,1)
		#print ('Intermoleculer newMoll', newMol1)

		mole.moleculeTable.append(newMol1)
		mole.moleculeTable.append(newMol2)
		mole.PE.append(pe1)
		mole.PE.append(pe2)
		#print('PE Check',mole.PE)
		#print ('Intermoleculer Table', mole.moleculeTable)
		#mole.numHit[index1] = mole.numHit[index1] + 1
		#mole.numHit[index2] = mole.numHit[index2] + 1
		e_inter = (mole.PE[index1] + mole.PE[index2] + mole.KE1[index1] + mole.KE1[index2]) - (pe1 + pe2)
		mole.KE1.append(e_inter * gamma4)
		mole.KE1.append(e_inter * (1-gamma4))
		if (e_inter>=0):
			#mole.moleculeTable[index1] = newMol1
			#mole.moleculeTable[index2] = newMol2

			#mole.moleculeTable.append(newMol1)
			#mole.moleculeTable.append(newMol2)



			#mole.PE[index1] = pe1
			#mole.PE[index2] = pe2

			#mole.KE1[index1] = e_inter * gamma4
			#mole.KE1[index2] = e_inter * (1 - gamma4)
			'''
			if (mole.PE[index1]<mole.minPE[random.randint(0,len(mole.PE)-1)]):
				mole.minStruct[index1] = mole.moleculeTable[index1]
				mole.minPE[index1] = mole.PE1[index1]
				mole.minHit[index1] = mole.numHit[index1]
			# endif
			
			if (mole.PE[index2]<mole.minPE[index2]):
				mole.minStruct[random.randint(0,len(mole.moleculeTable)-1)] = mole.moleculeTable[index2]
'''
			# endif
		# endif
	# end function

	def Synthesis (self,mole,oldMol1,oldMol2,index1,index2,shiftcost,flowcost,N):
		operator = Operators()
		newMol = operator.Synthesis(oldMol1, oldMol2)
		#print('EI j ',newMol)
		pe_new = CRO().CalculatePE(newMol,shiftcost,flowcost,N)

		mole.moleculeTable.append(newMol)
		mole.PE.append(pe_new)
		mole.KE1.append(pe_new)
		if((mole.PE[index1]+mole.PE[index2] + mole.KE1[index1]+mole.KE1[index2])>=pe_new):
			
			ke_new = (mole.PE[index1] + mole.PE[index2] + mole.KE1[index1] + mole.KE1[index2]) - pe_new

			mole.KE1.append(ke_new)
			#del mole.moleculeTable[index1]
			#del mole.PE[index1]

			#del mole.KE1[index1]
			#del mole.numHit[index1]
			#del mole.minHit[index1]
			#del mole.minStruct[index1]
			#del mole.minPE[index1]

			if(index2>=index1):
				# position of index2 is decreased by 1
				index2 = index2 -1




			#mole.moleculeTable.append(newMol)
			#mole.PE.append(pe_new)

			mole.KE1.append(ke_new)
			mole.numHit.append(0)
			mole.minHit.append(0)

			mole.minStruct.append(newMol)
			mole.minPE.append(pe_new)
		else:
			mole.numHit[index1] = mole.numHit[index1] + 1
			mole.numHit[index1] = mole.numHit[index1] + 1
		# endif
	# end function

	######################################################################
	# Main CRO handler
	######################################################################
	def CRO(self,popSize, KELossRate, MoleColl, InitialKE, alpha, beta, buffer, sequence, mole,iteration,fileName,shiftcost,flowcost,N):
		b = 0
		i = 0
		w = None
		oldMol1 = []
		oldMol2 = []
		index, index1, index2 = 0,1,2
		minEnrg = 100000
		sl=0

		for j in range(len(mole.PE)):
			if (mole.PE[j] < minEnrg):
				minEnrg = mole.PE[j]
				sl = j+1
			#endif
		#endfor

		# Save Initials
		# energyBefore = open(path+"output/initial_population_"+fileName,"a")
		# energyBefore.write("Minimum energy: "+str(minEnrg))
		# energyBefore.write(" at position: "+str(sl))
		# energyBefore.write("\n======================================================\n")

		# Oprators hit counter
		on = 0
		dec = 0
		inef = 0
		syn = 0

		# Main iteration starts
		for i in range(iteration):

			b = random.uniform(0,1)
			# Decomposition or OnwallIneffectiveCollision
			if (b>MoleColl):
				index = random.randint(0, len(mole.PE)-1)
				if ((mole.NumHit[random.randint(0,2)]-mole.MinHit[random.randint(0,2)])>alpha):
					dec+=1
					CRO().Decomposition(mole,mole.moleculeTable[index], index,shiftcost,flowcost,N)
				#endif
				else:

					if random.randint(0,1)==1 :
						dec+=1
						CRO().Decomposition(mole,mole.moleculeTable[index], index,shiftcost,flowcost,N)
					else:

						on+=1
						CRO().OnwallIneffectiveCollision(mole,mole.moleculeTable[index], index,shiftcost,flowcost,N)
				#end else
			#endif

			# Synthesis or IntermolecularIneffectiveCollision
			else:
				index1 = random.randint(0,len(mole.moleculeTable)-1)
				index2 = random.randint(0,len(mole.moleculeTable)-1)
				if ((mole.KE1[index1]+mole.KE1[index2])<beta):
					syn+=1
					CRO().Synthesis(mole,mole.moleculeTable[index1], mole.moleculeTable[index2], index1, index2,shiftcost,flowcost,N)
				#endif
				else:

					if random.randint(0,1)==1 :
						syn+=1
						CRO().Synthesis(mole,mole.moleculeTable[index1], mole.moleculeTable[index2], index1, index2,shiftcost,flowcost,N)
					else:
						inef+=1
						CRO().IntermolecularIneffectiveCollision(mole, mole.moleculeTable[index1], mole.moleculeTable[index2], index1, index2,shiftcost,flowcost,N)
				#endelse
			#end else
		# Endfor iteration
		
		# Finding minimum energy
		minEnrg = 100000

		minEnrgIndex = None


		for j in range(len(mole.PE)):
			if (mole.PE[j]<minEnrg):
				minEnrg = mole.PE[j]
				minEnrgIndex = j
			#endif
		#endfor

		hits = "Onwall= "+str(on) +"\tDec = "+str(dec)+"\tSyn = "+str(syn)+"\tIntermolecular = "+str(inef)+"\n"
		print(hits)
		#print('Last',len(mole.moleculeTable))
		#print('Tata',len(mole.PE))
		print('### ----------- ' + str(N)  + ' ------------  ###')
		finalSequence,finalCost = CRO().FindMinimumStructure(mole.PE,mole.moleculeTable)
		print('Final Sequence:')
		print(finalSequence)
		print('Final Cost: \n{}'.format(finalCost))



		start_time = time.time()
		# print("--- %s seconds ---" % (time.time() - start_time))
		# Save information
		#energyAfter = open(path+"output/final_population_"+fileName,"a")




	#end CRO function



	# Calculate Cost/Energy

	def AdjacentCost6(self,f,sequence):
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

	def AdjacentCost15(self, f, sequence):
		adcost = 0
		x = len(sequence)
		for i in range(0, x):
			seq = sequence[i]
			j = i * 15
			k = j + 15
			fc = f[j:k]
			# print (fc)
			adcost += (fc[seq[0] - 1][seq[2] - 1] + fc[seq[2] - 1][seq[0] - 1])
			adcost += (fc[seq[0] - 1][seq[3] - 1] + fc[seq[3] - 1][seq[0] - 1]) * 2
			adcost += (fc[seq[0] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[0] - 1]) * 3
			adcost += (fc[seq[0] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[0] - 1])
			adcost += (fc[seq[0] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[0] - 1]) * 2
			adcost += (fc[seq[0] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[0] - 1]) * 3
			adcost += (fc[seq[0] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[0] - 1]) * 4
			adcost += (fc[seq[0] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[0] - 1])
			adcost += (fc[seq[0] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[0] - 1]) * 2
			adcost += (fc[seq[0] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[0] - 1]) * 3
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
			adcost += (fc[seq[2] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[2] - 1]) * 2
			adcost += (fc[seq[2] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[2] - 1])
			adcost += (fc[seq[2] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[2] - 1])
			adcost += (fc[seq[2] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[2] - 1]) * 2
			adcost += (fc[seq[2] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[2] - 1]) * 3
			adcost += (fc[seq[2] - 1][seq[11] - 1] + fc[seq[11] - 1][seq[2] - 1]) * 2
			adcost += (fc[seq[2] - 1][seq[12] - 1] + fc[seq[12] - 1][seq[2] - 1]) * 1
			adcost += (fc[seq[2] - 1][seq[13] - 1] + fc[seq[13] - 1][seq[2] - 1]) * 2
			adcost += (fc[seq[2] - 1][seq[14] - 1] + fc[seq[14] - 1][seq[2] - 1]) * 3

			adcost += (fc[seq[3] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[3] - 1]) * 3
			adcost += (fc[seq[3] - 1][seq[6] - 1] + fc[seq[6] - 1][seq[3] - 1]) * 2
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

	def AdjacentCost30(self, f, sequence):
		adcost = 0
		x = len(sequence)
		for i in range(0, x):
			seq = sequence[i]
			j = i * 30
			k = j + 30
			fc = f[j:k]
			# print (fc)
			adcost += (fc[seq[0] - 1][seq[2] - 1] + fc[seq[2] - 1][seq[0] - 1])
			adcost += (fc[seq[0] - 1][seq[3] - 1] + fc[seq[3] - 1][seq[0] - 1]) * 2
			adcost += (fc[seq[0] - 1][seq[4] - 1] + fc[seq[4] - 1][seq[0] - 1]) * 3
			adcost += (fc[seq[0] - 1][seq[5] - 1] + fc[seq[5] - 1][seq[0] - 1]) * 4
			adcost += (fc[seq[0] - 1][seq[7] - 1] + fc[seq[7] - 1][seq[0] - 1]) * 1
			adcost += (fc[seq[0] - 1][seq[8] - 1] + fc[seq[8] - 1][seq[0] - 1]) * 2
			adcost += (fc[seq[0] - 1][seq[9] - 1] + fc[seq[9] - 1][seq[0] - 1]) * 3
			adcost += (fc[seq[0] - 1][seq[10] - 1] + fc[seq[10] - 1][seq[0] - 1]) * 4
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
	def TotalShiftCost(self,sequence,shiftCost,N):
		sc  = 0
		T = len(sequence)
		for t in range (1,T):
			X1 = sequence[t-1]
			X2 = sequence[t]
			for j in range (0,N):
				if (X1.index(j+1) != X2.index(j+1) ):
					sc += shiftCost[j]
		return sc

	def MHcost (self,f):
		cost = 0
		for i in range(0,len(f)):
			for j in range(len(f[i])):
				cost+= f[i][j]
		return cost

	def CalculatePE(self,sequence,shiftCost,flowCost,N):
		MC = CRO().MHcost(flowCost)
		# print('N = ',N)
		if N == 6:
			AC = CRO().AdjacentCost6(flowCost,sequence)
		elif N == 15:
			AC = CRO().AdjacentCost15(flowCost,sequence)
		elif N == 30:
			AC = CRO().AdjacentCost30(flowCost,sequence)
		else:
			print('Waring : Adjacent Cost Not Found')
			AC = 0

		SC = CRO().TotalShiftCost(sequence,shiftCost,N)
		return MC+SC+AC

	#End

	def FindMinimumStructure(self,b,c):
		finalCost = min(b)
		finalSequence = c[b.index(min(b))]
		return finalSequence, finalCost

# End class
