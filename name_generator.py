#Nick Hu
#10/16/2024

def generator():
    ans = (input("Which type of weather do you like more, cold or hot?"))
    if ans == "cold":
        ans = (input("Which type of cold season do you like more, fall or winter?"))
        if ans == "fall":
            ans = (input("Which animal do you like more, hogs or deers?"))
            if ans == "hogs":
                print("You are a Hedgehog")
            elif ans == "deers":
                print("You are a Key Deer")
        elif ans == "winter":
            ans = (input("Which winter location do you like more, Polar or Arctic?"))
            if ans == "polar":
                print("You are a Polar Bear")
            elif ans == "arctic":
                print("You are a Arctic Wolf")
    else:
        ans = (input("Which type of hot season do you like more, spring or summer?"))
        if ans == "spring":
            ans = (input("Which animal do you like more, ducks or birds?"))
            if ans == "ducks":
                print("You are a Domestic Duck")
            elif ans == "Bird":
                print("You are a Humming Bird")
        elif ans == "summer":
            ans = (input("Which aquatic animal do you like more, sharks or dolphin?"))
            if ans == "sharks":
                print("You are a Whale Shark")
            elif ans == "dolphin":
                print("You are a Striped Dolphin")


generator()
