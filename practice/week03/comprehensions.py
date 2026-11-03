
# Week 3: Learning Python Comprehensions

# Part 1: List comprehension
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print("Original numbers:", numbers)
print("Squared numbers:", squares)

# Part 2: Filtering with a condition
study_hours = [5, 12, 18, 8, 20, 15]

high_study_hours = [
    hours for hours in study_hours if hours >= 15
]

print("\nAll study hours:", study_hours)
print("Hours meeting the goal:", high_study_hours)

# Part 3: Dictionary comprehension
skills = ["Python", "SQL", "GitHub"]

skill_lengths = {
    skill: len(skill) for skill in skills
}

print("\nSkill name lengths:", skill_lengths)

# Part 4: Set comprehension
genres = ["Rock", "Jazz", "Rock", "Metal", "Jazz"]

unique_genres = {genre for genre in genres}

print("Unique genres:", sorted(unique_genres))
