class Rucksack:
	rucksacks=[]
	def __init__(self, contentString) -> None:
		self.contentString = contentString
		self.firstHalf = contentString[:len(contentString)//2]
		self.secondHalf = contentString[len(contentString)//2:]
		self.commonCharacter = self.getCommonCharacter()
		self.rucksacks.append(self)

	def getCommonCharacter(self):
		return str(set(self.firstHalf).intersection(self.secondHalf))[2]

	def getPriorityScore(self):
		if self.commonCharacter.islower():
			return ord(self.commonCharacter)-96
		else:
			return ord(self.commonCharacter)-38

	@classmethod
	def getSumOfPriorities(cls):
		priorityScores=[]
		for rucksack in cls.rucksacks:
			score=rucksack.getPriorityScore()
			priorityScores.append(score)
		return sum(priorityScores)

def main():
	with open("./2022/day-03-input.txt") as f:
		for line in f:
			Rucksack(line.strip())
	print(Rucksack.getSumOfPriorities())

if __name__ == "__main__":
	main()