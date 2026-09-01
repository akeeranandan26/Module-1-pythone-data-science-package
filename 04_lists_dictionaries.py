# Module 1 - Lists and Dictionaries

subjects = ["Python", "Data Science", "Digital Design", "Communication"]
print("Subjects:", subjects)

subjects.append("Signal Processing")
print("After adding a subject:", subjects)

student = {
    "name": "Akeera",
    "branch": "ECE",
    "semester": 3,
    "skills": ["Python", "C", "Digital Electronics"]
}

print("\nStudent details:")
for key, value in student.items():
    print(key, ":", value)
