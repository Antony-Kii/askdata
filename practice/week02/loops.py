# Week 2: Learning Python Loops

# Part 1: Using a while loop

while True:
    user_input = input("How many hours did you study this week? ")

    try:
        hours = int(user_input)

        if hours < 0:
            print("Error: Hours cannot be negative.")
            continue

        break

    except ValueError:
        print("Error: Please enter a valid whole number.")


# Check study progress
if hours >= 15:
    print("Excellent! You met your weekly goal.")
elif hours >= 10:
    print("Good progress! Keep going.")
else:
    print("Every hour counts. Keep learning!")

print("You studied", hours, "hours this week.")


# Part 2: Using a for loop

print("Your study schedule:")

for day in range(1, 6):
    print("Study day", day)
