import random

dataFile = "passwords.txt"


def getData() -> list:
    """Fetches the list of passwords from txt file and returns the list

    Returns:
            list: List of passwords
    """
    lib = []
    with open(dataFile, "r") as f:
        lib.extend(iter(f))
    print(f"# of Lines {len(lib)}")
    return lib


def displayScore() -> None:
    """Prints score of user and computer

    Returns:
            None
    """

    print(
        "\n\t\tSCORE:\n\tUSER-> "
        + str(scoreUser)
        + "\tIDIOTS-> "
        + str(scoreCom)
        + "\n\n"
    )
    return None


def getRandomWord() -> "tuple[int, str]":
    """Select random word from the list

    Returns:
            tuple[int, str]: Tuple of rank of the most common password with its password
    """
    rank = random.randint(0, 999)
    word = library[rank]
    return (rank + 1, word)


def getNextGuess() -> str:
    """Gets the next guess of the user

    Return:
            First word of the user input guess
    """

    try:
        val = list(input("Enter your next guess :\t>")) or getNextGuess()
        return val[0]
    except (KeyboardInterrupt, EOFError):
        exit()


"""
Hangman sprite 
	________
	|     |
	|     O
	|    /|\
	|     |
	|    / \
____|___
_ _ _ _ _ _ _ _ _
"""


def drawHangman(remaining: int) -> None:
    """Drawing the Hangman

    Args:
            remaining (int): Remaining guess of the user

    Returns:
            None
    """
    initialLimbs = 7
    limbsToDraw = initialLimbs - remaining
    print("     ________")
    print("     |     |")

    print("     |     O" if limbsToDraw > 0 else "     |")
    print(
        "     |    /|\\"
        if limbsToDraw > 3
        else "     |    /|"
        if limbsToDraw > 2
        else "     |     |"
        if limbsToDraw > 1
        else "     |"
    )
    print("     |     |" if limbsToDraw > 4 else "     |")
    print(
        "     |    / \\"
        if limbsToDraw > 6
        else "     |    /"
        if limbsToDraw > 5
        else "     |"
    )
    print(" ____|___")
    return None


def runGame() -> bool:
    """Core function of the game

    Returns:
            bool: Result of the game
    """
    (rank, word) = getRandomWord()
    word = list(word)

    guessed = word.copy()

    roundsLeft = 7
    for i in range(len(guessed) - 1):
        guessed[i] = "_"

    while roundsLeft >= 0:
        containedFlag = 0
        # print hangman
        drawHangman(roundsLeft)
        print(" ".join(guessed))
        # ensure game is not over
        if word == guessed:
            print(
                "Congratulations! You have guessed the #"
                + str(rank)
                + " most used password "
                + "".join(guessed)
            )
            return True
        val = getNextGuess()
        for i in range(len(guessed) - 1):
            if word[i] is val:
                guessed[i] = word[i]
                containedFlag += 1

        if containedFlag == 0:
            roundsLeft -= 1
        elif containedFlag >= 3:
            print(
                "Whoa.. "
                + str(containedFlag)
                + " "
                + str(val)
                + "'s found.. take an extra limb"
            )
            roundsLeft += 1

    print(
        "Embarrassing! You have could not guess the #"
        + str(rank)
        + " most used password "
        + "".join(word)
    )
    return False


# Main Loop
if __name__ == "__main__":
    library = getData()
    print("\n\t\tWelcome to Hangman!\n\t Now With the top 1,000 passwords!\n\n")
    scoreUser, scoreCom = 0, 0
    running = True
    while running:
        try:
            inp = str(input("Press 'y' to start new game or 'q' to quit...\n")).lower()
        except (KeyboardInterrupt, EOFError):
            exit()
        if inp != "y":
            running = False
        else:
            if runGame():
                scoreUser += 1
            else:
                scoreCom += 1
            displayScore()
