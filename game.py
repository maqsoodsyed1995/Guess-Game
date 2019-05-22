class game:
    """
    Class game has the Variables for the Game,
    Word stores the Word,
    Status stores the Status of the Word,
    BadGuesses Stores the bad Guesses done,
    Score stores the final score,
    No_request stores the number of times the user request a letter.
    """
    word=""
    status=""
    BadGuesses=0
    MissedLetters=4
    Score=0.0
    No_request=0
    missedSequence=[0,0,0,0]