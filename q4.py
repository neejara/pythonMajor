# Initialize the list of students
student = [{"student id": 1, "M ath": 50, "Computer Science": 60, "Science": 73},
           {"student id": 2, "M ath": 40, "Computer Science": 50, "Science": 55},
           {"student id": 3, "M ath": 90, "Computer Science": 70, "Science": 95},
           {"student id": 4, "M ath": 80, "Computer Science": 62, "Science": 72},
           {"student id": 5, "M ath": 80, "Computer Science": 90, "Science": 45},
           {"student id": 6, "M ath": 84, "Computer Science": 90, "Science": 50},
           {"student id": 7, "M ath": 90, "Computer Science": 95, "Science": 55},
           {"student id": 8, "M ath": 89, "Computer Science": 93, "Science": 53},
           {"student id": 9, "M ath": 88, "Computer Science": 92, "Science": 58},
           {"student id": 10, "M ath": 90, "Computer Science": 95, "Science": 55},
           {"student id": 11, "M ath": 70, "Computer Science": 65, "Science": 39},
           {"student id": 12, "M ath": 65, "Computer Science": 60, "Science": 35},
           {"student id": 13, "M ath": 60, "Computer Science": 55, "Science": 30},
           {"student id": 14, "M ath": 55, "Computer Science": 57, "Science": 25},
           {"student id": 15, "M ath": 49, "Computer Science": 54, "Science": 22},
           {"student id": 16, "M ath": 10, "Computer Science": 30, "Science": 11},
           {"student id": 17, "M ath": 50, "Computer Science": 40, "Science": 16},
           {"student id": 18, "M ath": 90, "Computer Science": 45, "Science": 80},
           {"student id": 19, "M ath": 70, "Computer Science": 50, "Science": 39},
           {"student id": 20, "M ath": 70, "Computer Science": 80, "Science": 75}]

# Extract the Computer Science marks from the list of students
computer_science_marks = [student["Computer Science"] for student in student]

# Calculate the mean of the Computer Science marks
mean = sum(computer_science_marks) / len(computer_science_marks)

# Calculate the median of the Computer Science marks
sorted_computer_science_marks = sorted(computer_science_marks)
n = len(sorted_computer_science_marks)
if n % 2 == 0:
    median = (sorted_computer_science_marks[n // 2] + sorted_computer_science_marks[n // 2 - 1]) / 2
else:
    median = sorted_computer_science_marks[n // 2]

# Calculate the mode of the Computer Science marks
from collections import Counter
mode = Counter(computer_science_marks).most_common(1)[0][0]

# Print the mean, median, and mode of the Computer Science marks
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
