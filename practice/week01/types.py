# Week 1: Learning Python Data Types

# Type 1: String (str) - stores text
name = "Antony"
career_goal = "AI Engineer"

# Type 2: Integer (int) - stores whole numbers
age = 10
hours_per_week = 15

# Type 3: Float (float) - stores decimal numbers
monthly_hours = 65.0
course_progress = 25.5

# Type 4: Boolean (bool) - stores True or False
is_learning_python = True
has_finished_training = False

# Display the values and their data types
print("My name:", name, "| Type:", type(name))
print("My age:", age, "| Type:", type(age))
print("Career goal:", career_goal, "| Type:", type(career_goal))
print("Weekly study hours:", hours_per_week, "| Type:", type(hours_per_week))
print("Monthly study hours:", monthly_hours, "| Type:", type(monthly_hours))
print("Course progress:", course_progress, "| Type:", type(course_progress))
print("Learning Python:", is_learning_python,
      "| Type:", type(is_learning_python))
print("Finished training:", has_finished_training,
      "| Type:", type(has_finished_training))

# Practice converting between data types
hours_as_text = str(hours_per_week)
age_as_decimal = float(age)

print("Hours converted to text:", hours_as_text, type(hours_as_text))
print("Age converted to decimal:", age_as_decimal, type(age_as_decimal))
