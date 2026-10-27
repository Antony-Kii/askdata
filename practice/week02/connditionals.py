
# Week 2: Learning Python Conditionals and Input Validation

# Ask the user for study hours
user_input = input("How many hours did you study this week? ")

try:
    hours = int(user_input)

    if hours < 0:
        print("Error: Study hours cannot be negative.")

    elif hours >= 15:
        print("Excellent! You met your weekly study goal.")

    elif hours >= 10:
        print("Good progress! Try to reach 15 hours.")

    else:
        print("Keep going! Every hour counts.")

    if hours >= 0:
        print("You studied", hours, "hours this week.")

except ValueError:
    print("Error: Please enter a valid whole number.")
