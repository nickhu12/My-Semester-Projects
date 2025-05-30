#Nick Hu
#1/16/2025
#Semester 1 Final



#Init
import random
day = 0
Health = 100
gold = 0

#Function
def story():
    global day
    global Health
    global gold
    print("Hello there Warrior, You have been chosen to save this village from invading forces")
    print("To accomplish this, you must find a legendary sword.")
    while True:
        day = day + 1
        print("Select an activity for the day " + str(day)+ ". Make sure you are healed before fighting!")
        print("""
        1. Rest
        2. Fight
        3. Check Inventory
        4. Quit(Too hard)""")
        option = int(input("1,4:"))

        if option == 1:
            print("You took a rest, You have healed 30hp.")
            Health = Health + 30
            if Health > 100:
                Health = 100
            print("You currently have " +str(Health) + " health.")

        if option == 2:
            option1 = (random.randint(1,3))
            if option1 == 1:
                print("You have encountered some enemies. They hurt you but you killed them and you looted them.")
                damage = (random.randint(1,20))
                Health = Health - damage
                print("You currently have "+str(Health)+" health.")
                rangold = (random.randint(1,30))
                gold = gold + rangold
                if Health <= 0:
                    print("You have no more hp to fight. You lost")

            if option1 == 2:
                print("You have encountered a boss. *note. Does a lot of damage")
                damage = (random.randint(20,30))
                Health = Health - damage
                print("You currently have "+str(Health)+" health.")
                rangold = (random.randint(30,100))
                gold = gold + rangold
                if Health <= 0:
                    print("You have no more hp to fight. You lost")

            if option1 == 3:
                print("You have been hit by a rock")
                damage = (random.randint(10,15))
                Health = Health - damage
                print("You currently have " + str(Health) + " health.")


        if option == 3:
            print("You have spent the day counting your stuff. You currently have " + str(Health)+" health and "+ str(gold) + " gold.")

        if option == 4:
            print("You have left the village in disappointment towards you..")
            break

        if day == 25 and option == 2:
            print("You have found the Legendary Sword")
            print("Congrats young warrior. You made it")
            break
        elif day == 20 and option == 1:
            print("You took a rest but went for a walk and accidentally found a sword. You uncover it and find the Legendary Sword.")
            print("Congrats young warrior. You made it")
            break
        elif day == 25 and option == 1:
            print("You took a rest but went for a walk and accidentally found a sword. You uncover it and find the Legendary Sword.")
            print("Congrats young warrior. You made it")
            break
        elif day == 20 and option == 2:
            print("You have found the Legendary Sword")
            print("Congrats young warrior. You made it")
            break
        elif day <= 30 and option == 3:
            print("You have found the Legendary Sword")
            print("Congrats young warrior. You made it")


#Main
story()
