# Module 1 - File Handling

filename = "student_notes.txt"

# Write to a file
with open(filename, "w") as file:
    file.write("Python & Data Science Fundamentals\n")
    file.write("Practiced variables, loops, functions, lists and dictionaries.\n")

# Read from the file
with open(filename, "r") as file:
    content = file.read()

print(content)

# Append more information
with open(filename, "a") as file:
    file.write("Also practiced basic file handling.\n")

print("File created and updated successfully.")
