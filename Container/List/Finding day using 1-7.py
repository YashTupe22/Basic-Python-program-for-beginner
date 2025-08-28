#Finding Day using 1-7.py
week=["Null = no-0","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # List of days in a week
day=int(input("Enter a number between 1 and 7: "))  # Taking user input for day number
if day < 1 or day > 7:  # Checking if the input is valid
    print("Invalid input! Please enter a number between 1 and 7.")  # Displaying error message for invalid input
else:
    print("The day is:", week[day]) # Displaying the corresponding day from the list    
# This script finds the day of the week based on user input from 1 to 7.
# It uses a list to store the days and checks if the input is valid before displaying the