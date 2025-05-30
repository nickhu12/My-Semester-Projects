#Nick Hu
#10/11/2024
#Period 5
#Conditional Statements

#Init


#Functions
#This function checks whether you are eligible to vote
#18 years of age and above
#US citizen
def vote_check():
    #Collect our input
    age = int(input("Please enter your age: "))
    citizen = input("Are you an U.S. Citizen(Yes, No)")
    #Process the data w/ conditionals
    if age > 18 and citizen == "yes" : #Condtionals statement. When the computer sees this line it will evaluate it TRUE or FALSE
        print("You are eligible to vote")
    else:
        print("You are NOT eligibile to to vote")

def max_num(a,b,c):
    #No input needed
    #Figure out which is the largest using conditionals statements
    if a > b and a > c:
        print("A is the largest number, the value of a is: " + str(a))
    if b > a and b > c:
        print("B is the largest number, the value of a is: " + str(b))
    if c > a and c > b:
        print("C is the largest number, the value of a is: " + str(c))

def grades(score):
    #No input needed/score is our input
    #Conditionals go here
    if score >= 90:
        print("Your grade is an A")
    elif score >= 80:
        print("Your grade is a B")
    elif score >= 70:
        print("Your grade is a C")
    elif score >= 60:
        print("Your grade is a D")
    elif score <= 59:
        print("Your grade is a F")

#main
grades(60)
