#Finding month using 1-12.py
months = ["Null = no-0", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]  # List of months in a year
month = int(input("Enter a number between 1 and 12: "))  # Taking user input for month number   
if month < 1 or month > 12:  # Checking if the input is valid
    print("Invalid input! Please enter a number between 1 and 12.")  # Displaying error message for invalid input
else:
    print("The month is:", months[month])   
# This script finds the month of the year based on user input from 1 to 12.
# It uses a list to store the months and checks if the input is valid before displaying the
import datetime
print("The current month is:", datetime.datetime.now().strftime("%B"))  # Displaying the current month using datetime module