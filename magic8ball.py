#Nick Hu


#Init
import random
import time
magic8ball_list = ["Yes","It is certain","Certainly","Without a doubt","Yes definitely","Reply hazy, try again","No","Better not tell you now","Cannot predict now","Concentrate and ask again","Maybe","Don’t count on it","Outlook not so good","My sources say no","Very doubtful"]

#Functions
def magic8():
    global magic8ball_list
    while True:
        print("Welcome to Magic 8 Ball!")
        print("Please ask Magic 8 Ball your question.")
        x = input("Please ask Magic 8 Ball your question.")
        y = x.endswith("?")
        if y == True:
            print("Shake..")
            time.sleep(2)
            print("Shake..")
            time.sleep(2)
            print(random.choice(magic8ball_list))
        else:
            print("ERROR: Not a question!")
            break

#Main
magic8()
