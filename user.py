print("hello")

day = input("what day is it today")

if input.upper() == FRIDAY:
    print("yes")
else:
    print("false")

lala = input("from 1 to 10, how would you rate your pain: ")

# this line let the user rate their pain so we can do the solution
if lala == "10":
    lala = 10
    print("I will call ambulance for you")
# we call ambulance 

verify = input("we need to verify your identity. What is your last name?: ")

if verify.upper() == "CHARLES":
    print("we will send it immediately, thank you for your patience")


while lala >= 5:
    print("please eat some pills")
    lala = lala - 1 
