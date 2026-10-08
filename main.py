import pandas as pd
import numpy as np


# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to calculate pass/fail
def check_result(row):
    subjects = ["Python", "Data_Analysis", "SQL"]

    for subject in subjects:
        if row[subject] < 40:
            return "Fail"

    if row["Attendance"] < 75:
        return "Fail"

    return "Pass"


# 1. Read the dataset
df = pd.read_csv("students.csv")

print("\n===== STUDENT PERFORMANCE ANALYTICS SYSTEM =====")

# 2. Display basic information
print("\n--- Student Dataset ---")
print(df)

print("\nTotal number of students:", len(df))

print("\n--- Dataset Information ---")
print(df.info())

# 3. Calculate Total Marks
subjects = ["Python", "Data_Analysis", "SQL"]

df["Total"] = df[subjects].sum(axis=1)

# 4. Calculate Average using NumPy
df["Average"] = np.round(df["Total"] / len(subjects), 2)

# 5. Assign Grade
df["Grade"] = df["Average"].apply(calculate_grade)

# 6. Pass / Fail
df["Result"] = df.apply(check_result, axis=1)

# 7. Display processed data
print("\n--- Processed Student Performance ---")
print(
    df[
        [
            "Student_ID",
            "Name",
            "Total",
            "Average",
            "Grade",
            "Attendance",
            "Result",
        ]
    ]
)

# 8. Highest and Lowest Performance
highest_average = df["Average"].max()
lowest_average = df["Average"].min()
class_average = np.mean(df["Average"])

print("\n--- Overall Performance ---")
print("Highest Average:", highest_average)
print("Lowest Average:", lowest_average)
print("Overall Class Average:", round(class_average, 2))

# 9. Find Top Performer
top_student = df.loc[df["Average"].idxmax()]

print("\n--- Top Performer ---")
print("Name:", top_student["Name"])
print("Average:", top_student["Average"])
print("Grade:", top_student["Grade"])

# 10. Pass / Fail Statistics
pass_count = (df["Result"] == "Pass").sum()
fail_count = (df["Result"] == "Fail").sum()

print("\n--- Pass / Fail Statistics ---")
print("Students Passed:", pass_count)
print("Students Failed:", fail_count)

# 11. Subject-wise Performance
print("\n--- Subject-wise Average ---")

subject_averages = df[subjects].mean()

for subject in subjects:
    print(subject, "Average:", round(subject_averages[subject], 2))

# 12. Best Subject
best_subject = subject_averages.idxmax()

print("\nBest Performing Subject:", best_subject)

# 13. Top 5 Students
print("\n--- Top 5 Students ---")

top_5 = df.sort_values(by="Average", ascending=False).head(5)

print(
    top_5[
        [
            "Student_ID",
            "Name",
            "Average",
            "Grade",
            "Result",
        ]
    ]
)

print("\n===== ANALYSIS COMPLETED SUCCESSFULLY =====")