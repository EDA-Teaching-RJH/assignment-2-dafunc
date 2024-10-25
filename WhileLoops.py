### Part Two -- your code goes here. 
import random
guesser= random.randint(1,100)
answer= int(input("what number am i thinking of? "))

if answer == guesser:
    print("good job!")

while (answer != guesser) :
    print ("the answer is " +str (guesser))

    print ("try again!")

    answer= int(input("what number am i thinking of?"))