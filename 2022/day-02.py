class rockPaperScissors:
	def __init__(self, opponentChoices:list, yourChoices:list) -> None:
		self.opponentChoices = opponentChoices # A: rock, B: paper, C: scissors
		self.yourChoices = yourChoices # X: rock, Y: paper, Z: scissors

	def getWinLossDraws(self):
		numericOpponent=[ord(choice)-65 for choice in self.opponentChoices]
		numericYou=[ord(choice)-88 for choice in self.yourChoices]
		winLossDraws = [(you-opponent)%3 for you, opponent in zip(numericOpponent, numericYou)] 
		return winLossDraws

	def getWinLossDrawScores(self):
		winLossDraws=self.getWinLossDraws()
		scores=[]
		for result in winLossDraws:
			if result == 0:
				scores.append(3)
			elif result == 2:
				scores.append(6)
			else:
				scores.append(0)
		return scores

	def getChoiceScores(self):
		scores=[]
		for choice in self.yourChoices:
			if choice == "X":
				scores.append(1)
			elif choice == "Y":
				scores.append(2)
			else:
				scores.append(3)
		return scores

	def getTotalScore(self):
		winLossDrawScores=self.getWinLossDrawScores()
		choiceScores=self.getChoiceScores()
		totalScore=sum(winLossDrawScores)+sum(choiceScores)
		return totalScore

def main():
	opponentChoices=[]
	yourChoices=[]
	with open("./2022/day-02-input.txt") as f:
		for line in f:
			opponent, you = line.split(' ')
			opponentChoices.append(opponent.strip())
			yourChoices.append(you.strip())
	rps=rockPaperScissors(opponentChoices, yourChoices)
	totalScore=rps.getTotalScore()
	print(totalScore)

if __name__ == "__main__":
	main()