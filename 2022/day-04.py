class ElfPair:
	allPairs=[]
	def __init__(self, taskString) -> None:
		self.taskString = taskString
		self.firstTaskString, self.secondTaskString = taskString.split(',')
		self.firstTaskIDs = self.getTaskIDList(self.firstTaskString)
		self.secondTaskIDs = self.getTaskIDList(self.secondTaskString)
		self.allPairs.append(self)

	def getTaskIDList(self, taskSring):
		start, stop =taskSring.split('-')
		start=int(start)
		stop=int(stop)
		taskIDs=[taskNumber for taskNumber in range(start, stop+1)]
		return taskIDs

	def checkIfSuperset(self):
		list1=self.firstTaskIDs
		list2=self.secondTaskIDs
		check1=all(element in list1 for element in list2)
		check2=all(element in list2 for element in list1)
		return check1 or check2

	def checkIfOverlap(self):
		list1=self.firstTaskIDs
		list2=self.secondTaskIDs
		check=any(element in list1 for element in list2)
		return check

	@classmethod
	def getSumOfSupersets(cls):
		supersetExistenceChecks=[]
		for pair in cls.allPairs:
			checkValue=pair.checkIfSuperset()
			supersetExistenceChecks.append(checkValue)
		return sum(supersetExistenceChecks)

	@classmethod
	def getSumOfOverlaps(cls):
		overlapExistenceChecks=[]
		for pair in cls.allPairs:
			checkValue=pair.checkIfOverlap()
			overlapExistenceChecks.append(checkValue)
		return sum(overlapExistenceChecks)

def main():
	with open("./2022/day-04-input.txt") as f:
		for line in f:
			ElfPair(line.strip())
	superSets=ElfPair.getSumOfSupersets()
	overlaps=ElfPair.getSumOfOverlaps()
	print(f'There are {superSets} Elf pairs with one set of tasks being the superset of the other')
	print(f'There are {overlaps} Elf pairs with overlapping tasks')

if __name__ == "__main__":
	main()