# Week 2: Learning Input Validation and Functions

# Function 1: Get valid study hours
def get_valid_hours():

    while True:
        user_input = input("How many hours did you study this week? ")

        # Check for empty input
        if user_input.strip() == "":
            print("Error: Input cannot be empty.")
            continue

        try:
            hours = int(user_input)

            # Check for negative numbers
            if hours < 0:
                print("Error: Hours cannot be negative.")
                continue

            return hours

        except ValueError:
            print("Error: Please enter a valid whole number.")


# Function 2: Evaluate study progress
def evaluate_progress(hours):

    if hours >= 15:
        return "Excellent! You met your weekly goal."

    elif hours >= 10:
        return "Good progress! Try to reach 15 hours."

    else:
        return "Keep going! Every hour counts."


# Main program
study_hours = get_valid_hours()

message = evaluate_progress(study_hours)

print(message)
print("You studied", study_hours, "hours this week.")
