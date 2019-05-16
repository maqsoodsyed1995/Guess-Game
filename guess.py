from stringDatabase import stringDatabase
from game import game
import random
wordList=stringDatabase()
gameObjects=[game()for i in range(0,99)]
mappings ={
"a" :8.17,
"b" :1.49,
"c" :2.78,
"d" :4.25,
"e" :12.70,
"f" :2.23,
"g" :2.02,
"h" :6.09,
"i" :6.97,
"j" :0.15,
"k" :0.77,
"l" :4.03,
"m" :2.41,
"n" :6.75,
"o" :7.51,
"p" :1.93,
"q" :0.10,
"r" :5.99,
"s" :6.33,
"t" :9.06,
"u" :2.76,
"v" :0.98,
"w" :2.36,
"x" :0.15,
"y":1.97,
"z" :0.07
}
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
                    gameObjects[i].missedSequence[k]=1
                    request_check=False
                    gameObjects[i].MissedLetters-=1
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


for i in range(0,gameCounter) :
 if(gameObjects[i].status=="Success"):
    for j in range(0,4) :
        if(gameObjects[i].missedSequence[j]==0):
            gameObjects[i].Score+=mappings[gameObjects[i].word[j]]
    if(gameObjects[i].No_request>0):
        gameObjects[i].Score /=gameObjects[i].No_request
    if(gameObjects[i].BadGuesses>0) :
        value=(gameObjects[i].Score/100)*(gameObjects[i].BadGuesses*10)
        gameObjects[i].Score-=value
 else:
     for j in range(0, 4):
         if (gameObjects[i].missedSequence[j] == 0):
            gameObjects[i].Score += mappings[gameObjects[i].word[j]]

     gameObjects[i].Score=-(gameObjects[i].Score );

     if (gameObjects[i].No_request > 0):
         gameObjects[i].Score *= gameObjects[i].No_request
     if (gameObjects[i].BadGuesses > 0):
         value = (gameObjects[i].Score / 100) * (gameObjects[i].BadGuesses * 10)
         gameObjects[i].Score -= value

print("Game",end="        ")
print("Word",end="        ")
print("Status", end="        ")
print("Bad Guesses", end="        ")
print("Missed Letters", end="        ")
print("Score")
print("____", end="        ")
print("____", end="        ")
print("______", end="        ")
print("___________", end="        ")
print("______________", end="        ")
print("_____")
for i in range(0,gameCounter):
    print(i+1,end="           ")
    print(gameObjects[i].word ,end="        ")
    print(gameObjects[i].status, end="       ")
    print(gameObjects[i].BadGuesses, end="                  ")
    print(gameObjects[i].MissedLetters, end="                     ")
    print(gameObjects[i].Score, end="        ")
    print()
