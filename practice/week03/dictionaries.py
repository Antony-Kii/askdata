
# Week 3: Learning Python Dictionaries

# Create a dictionary
student = {
    "name": "Antony",
    "career_goal": "AI Engineer",
    "weekly_hours": 15,
    "learning_python": True
}

# Display the entire dictionary
print("Student information:", student)

# Access values using keys
print("Name:", student["name"])
print("Career goal:", student["career_goal"])
print("Weekly study hours:", student["weekly_hours"])

# Add a new key-value pair
student["current_week"] = 3

# Update an existing value
student["weekly_hours"] = 20

# Display updated dictionary
print("Updated student information:", student)

# Count the number of key-value pairs
print("Number of fields:", len(student))

# Loop through the dictionary
print("\nStudent details:")

for key, value in student.items():
    print(key, ":", value)

# Safely retrieve a value
print("\nProgramming language:", student.get("language", "Not specified"))
