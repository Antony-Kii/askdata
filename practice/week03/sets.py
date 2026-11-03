# Week 3: Learning Python Sets

# Create a list with duplicate values
skills_list = ["Python", "SQL", "GitHub", "Python", "AI", "SQL"]

print("Original list:", skills_list)

# Convert the list into a set to remove duplicates
skills_set = set(skills_list)

print("Unique skills:", sorted(skills_set))

# Count the unique values
print("Number of unique skills:", len(skills_set))

# Add a new skill
skills_set.add("Machine Learning")

print("Updated skills:", sorted(skills_set))

# Check whether a skill exists
if "Python" in skills_set:
    print("Python is in my skill set.")

# Compare two sets
my_skills = {"Python", "SQL", "GitHub"}
required_skills = {"Python", "SQL", "Docker", "Azure"}

# Find skills common to both sets
common_skills = my_skills.intersection(required_skills)

# Find skills I still need to learn
missing_skills = required_skills.difference(my_skills)

# Combine all unique skills
all_skills = my_skills.union(required_skills)

print("\nCommon skills:", sorted(common_skills))
print("Skills to learn:", sorted(missing_skills))
print("All skills:", sorted(all_skills))

# Loop through the missing skills
print("\nMy future learning goals:")

for skill in sorted(missing_skills):
    print("I need to learn:", skill)
