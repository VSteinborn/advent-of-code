
class Elf:
	listOfElvs=[]
	def __init__(self, caloriesList : list) -> None:
		self.calories = caloriesList
		self.listOfElvs.append(self)

	def sum(self):
		return sum(self.calories)

	@classmethod
	def findMaxCalorieElf(cls):
		sums = [elf.sum() for elf in Elf.listOfElvs]
		maxCalories = max(sums)
		maxCalorieElfIndex=sums.index(maxCalories)
		return f"Elf number {maxCalorieElfIndex+1} is carrying the most calories ({maxCalories} calories)."


def main():
	currentCalorieList=[]
	with open("./2022/day-01-input.txt") as f:
		for line in f:
			try:
				currentCalorieList.append(int(line))
			except ValueError:
				if line=='\n':
					Elf(currentCalorieList)
					currentCalorieList=[]
				else:
					print('Something unexpected happened!')
	print(Elf.findMaxCalorieElf())

if "__main__" == __name__:
	main()