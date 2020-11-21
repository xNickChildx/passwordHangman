import random

dataFile = "passwords.txt"
def getData():
 	lib = []
 	f = open(dataFile, "r")
 	for line in f:
 		lib.append(line)
 	f.close()
 	print("# of Lines " + str(len(lib)))
 	return lib

def displayScore():
	print("\n\t\tSCORE:\n\tUSER-> " + str(scoreUser) + "\tIDIOTS-> " + str(scoreCom) + "\n\n")	

def getRandomWord():
	rank = random.randint(0, 999) 
	word = library[rank]
	#bc you know there isn't a #0 most used password
	rank += 1
	return (rank, word)
def getNextGuess():
	val = list(input("Enter your next guess :\t>"))
	if len(val) == 0:
		val = getNextGuess()
	return val[0]

def drawHangman(remaining):
	initialLimbs = 7
	limbsToDraw = initialLimbs - remaining
	print("     ________")
	print("     |     |")
	
	print("     |     O" if limbsToDraw > 0 else "     |")
	print("     |    /|\\" if limbsToDraw > 3 else "     |    /|" if limbsToDraw > 2 else "     |     |" if limbsToDraw > 1 else "     |")
	print("     |     |" if limbsToDraw > 4 else "     |")
	print("     |    / \\" if limbsToDraw > 6 else "     |    /" if limbsToDraw > 5 else "     |")
	print(" ____|___")
	

def runGame():
	(rank, word) = getRandomWord()
	word = list(word)

	guessed = word.copy()

	roundsLeft = 7
	for i in range(0,len(guessed)-1):
		guessed[i] = '_'

	while roundsLeft >= 0 :
		containedFlag = 0
		#print hangman
		drawHangman(roundsLeft)
		print(' '.join(guessed))
		#ensure game is not over
		if word == guessed:
			print("Congraulatons! You have guessed the #" + str(rank) + " most used password " + ''.join(guessed));
			return True
		val = getNextGuess()
		for i in range(0, len(guessed) -1):
			if word[i] is val:
				guessed[i] = word[i]
				containedFlag += 1

		if containedFlag == 0 :
			roundsLeft -= 1
		elif containedFlag >= 3:
			print("Woah.. "+ str(containedFlag) + " " + str(val)+ "'s found.. take an extra limb")
			roundsLeft += 1
	
	print("Embaressing! You have could not guess the #" + str(rank) + " most used password " + ''.join(word));
	return False


library = getData()
print("\n\t\tWelcome to Hangman!\n\t Now With the top 1,000 passwords!\n\n")
scoreUser = 0
scoreCom = 0
inp = "yeet"
while inp[0] == 'y':
	inp = input("Press 'y' to start new game or 'q' to quit...\n")
	if inp[0] == 'y':
		if runGame():
			scoreUser += 1;
		else:
			scoreCom += 1;
	displayScore()


