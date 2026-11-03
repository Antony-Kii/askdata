# Week 3: Learning Python Lists

# Create a list of programming skills
skills = ["Python", "SQL", "GitHub", "AI"]

# Display the full list
print("My skills:", skills)

# Access individual items
print("First skill:", skills[0])
print("Second skill:", skills[1])

# Add a new skill
skills.append("Machine Learning")

# Display the updated list
print("Updated skills:", skills)

# Count items in the list
print("Number of skills:", len(skills))

# Use a loop to display each skill
for skill in skills:
    print("I am learning:", skill)
