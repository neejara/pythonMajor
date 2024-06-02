import matplotlib.pyplot as plt

# Extract the student ids and Computer Science marks from the given list
student_ids = [student["student id"] for student in student]
cs_marks = [student["Computer Science"] for student in student]

# Create a line chart with student ids on the x-axis and Computer Science marks on the y-axis
plt.plot(student_ids, cs_marks)
plt.xlabel("Student ID")
plt.ylabel("Computer Science Mark")
plt.title("Line Chart of Student IDs and Computer Science Marks")
plt.show()
