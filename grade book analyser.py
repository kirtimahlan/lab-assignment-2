print("=== GradeBook Analyzer ===")

# Step 1: Take number of students
n = int(input("Enter number of students: "))

# Step 2: Create empty lists
names = []
marks = []

# Step 3: Get input from user
for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    mark = float(input(f"Enter marks for {name}: "))
    names.append(name)
    marks.append(mark)

# Step 4: Calculate statistics
total = sum(marks)
average = total / n
highest = max(marks)
lowest = min(marks)

# Step 5: Function to assign grades
def get_grade(m):
    if m >= 90:
        return "A"
    elif m >= 75:
        return "B"
    elif m >= 60:
        return "C"
    elif m >= 45:
        return "D"
    else:
        return "F"

# Step 6: Display results
print("\n===== GRADEBOOK SUMMARY =====")
print("Total Students:", n)
print("Average Marks:", round(average, 2))
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

print("\nStudent Grades:")
for i in range(n):
    grade = get_grade(marks[i])
    print(names[i], ":", marks[i], "-> Grade:", grade)
