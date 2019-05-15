from stringDatabase import stringDatabase
from game import game
import random
wordList=stringDatabase()
gameObjects=[game()for i in range(0,99)]

print('** The great guessing game **')

gameCheck=True
gameCounter=0;
for i in range(0, 99) :
 if (gameCheck):
    gameCounter+=1
    gameObjects[i].word=wordList.list[random.randint(0,4029)]
    print(gameObjects[i].word)
    boolList=[0,0,0,0]
    check=True
    while check :
        counter=0;
        for m in range(0,4) :
            if(boolList[m]!=0) :
                counter+=1
        if(counter==4):
            gameObjects[i].status="Success"
            break
        print('Current Guess:',end="")
        for j in range(0,4) :
            if(boolList[j]==1) :
                print(gameObjects[i].word[j],end="")
            elif(boolList[j]==2) :
                print(gameObjects[i].word[j], end="")
            elif(boolList[j]==0) :
                print("_",end=" ")
        print()
        choice=input("g = guess, t = tell me, l for a letter, and q to quit")
        if(choice=="g") :
            guess=input()
            if(guess==gameObjects[i].word) :
                check=False
                gameObjects[i].status="Success"
            else:
                gameObjects[i].BadGuesses+=1
        elif(choice=="l") :
            guess = input("Enter a letter:")
            request_check=True
            for k in range(0,4):
                if(guess==gameObjects[i].word[k]) :
                    boolList[k]=2
                    request_check=False
                    gameObjects[i].MissedLetters-=gameObjects[i].MissedLetters
            if(request_check) :
                gameObjects[i].No_request+=1
        elif(choice=="t"):
            print(gameObjects[i].word)
            gameObjects[i].status="Gave up"
            check=False
        elif(choice=="q"):
            gameObjects[i].status = "Gave up"
            check=False
            gameCheck=False

for i in range(0,gameCounter):
    print(gameObjects[i].word ,end=" ")
    print(gameObjects[i].status, end=" ")
    print(gameObjects[i].BadGuesses, end=" ")
    print(gameObjects[i].MissedLetters, end=" ")
    print()
