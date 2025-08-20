#Finding Leap year using If Else Codes
print("Leap Year finder")
year = int(input("Enter the Year: "))
print("Finding the given year =",year,"is leap year or not")
if(year%4==0):
    print(" ",year,"is a leap year")
else:
    print(" ",year, "is not a leap year")