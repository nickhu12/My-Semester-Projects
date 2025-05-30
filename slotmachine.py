#Nick Hu
#1/29/25

#1. Introduction
#2. ASK player to spin or quit
#3. Randomly pull 3 items/images from out list
#Advice: Remember each of these pulls(VARIABLES)
#4. Display the three images
#5. Determine the outcome(IF, ELIF, Else)



#Functions
slotmachine = ['♥', '♣', '7']
import random
import time
credit = 100
#Initialize
def machine():
    print("Welcome to the slot machine!")
    while True:
        global slot1
        global slot2
        global slot3
        global credit
        print("Do you want to spin?")
        ans = input("1.Spin, 2.Money, 3.End") #gives you choices
        ans = int(ans)
        if ans == 1:
            slot1 = random.choice(slotmachine)
            slot2 = random.choice(slotmachine)
            slot3 = random.choice(slotmachine)
            print("How much money do you want to spin?")
            ans1 = input("Amount to spin:")
            credit1 = int(ans1)
        if credit >= credit1:
            print("Spinning..")
            time.sleep(2)
            print("Spinning..")
            time.sleep(2)
            credit = credit-credit1
        else: #Not enough credits will print the outputs of these
            print("You dont have enough.")
            break
        if credit <= 0:
                print(slot1)
                print(slot2)
                print(slot3)
                print("You have no more credit to spin. Your broke!")
                break
        if slot1 == '7'and slot2 == '7' and slot3 == '7': #Big jackpot prize
            credit = credit*100
            print("You got a JACKPOT!  $"+ str(credit))
        elif slot1 == '♥' and slot2 == '♥' and slot3 == '♥': #Normal win prize
            credit = credit*10
            print("You WIN!  $"+ str(credit))
        elif slot1 == '♣' and slot2 == '♣' and slot3 == '♣':
            credit = credit*10
            print("You WIN!  $"+ str(credit))
        elif slot1 == slot2 or slot2 == slot3 or slot3 == slot1: #Double credit since you rolled 2 of the same outcomes
            credit = credit*2
            print("You got a double.  $"+ str(credit))
        else:
            print(slot1)
            print(slot2)
            print(slot3)
            print("You lost")
        print(slot1)
        print(slot2)
        print(slot3)
        if ans == 2:
            print("$"+str(credit))
        if ans == 3: #This is the exit/ stop playing
            print("Boohoo, See you next time brokie!")
            break
#Main
machine()
