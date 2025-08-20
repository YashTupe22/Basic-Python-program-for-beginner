#Voting Age checker using Nested If Else Codes
print("Voting Age Checker")
age=int(input("Enter the age : "))
if age>=18:
    print("Your are eligible for voting")
    if age <=30:
        print("You are a young voter")  
        if age <=40:
            print("You are a middle-aged voter")
            if age <=60:
                print("You are a senior voter")
else:
    print("You are not eligible for voting") 
