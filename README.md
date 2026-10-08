# Student Performance Analytics System

## Project Overview

The Student Performance Analytics System is a Python-based data analysis project. It reads student data from a CSV file and analyzes student marks and attendance using Python, NumPy and Pandas.

The system calculates total marks, average marks, grades, pass/fail status, subject-wise performance and identifies top-performing students.

## Objective

The main objectives of this project are:

- To read and organize student data using Pandas.
- To calculate total and average marks.
- To assign grades to students.
- To identify pass and fail students.
- To analyze subject-wise performance.
- To find the highest, lowest and overall class performance.
- To identify top-performing students.
- To practice Python functions, loops, conditions, NumPy and Pandas.

## Technologies Used

- Python
- NumPy
- Pandas
- CSV Dataset
- Visual Studio Code

## Dataset

The project uses a CSV dataset named `students.csv`.

The dataset contains 20 student records with the following fields:

- Student ID
- Name
- Department
- Python Marks
- Data Analysis Marks
- SQL Marks
- Attendance

## Project Features

### 1. Data Loading

The student dataset is loaded using Pandas `read_csv()`.

### 2. Total Marks

The system calculates the total marks obtained by each student in Python, Data Analysis and SQL.

### 3. Average Marks

The average marks of each student are calculated using NumPy.

### 4. Grade Calculation

Grades are assigned according to the student's average marks.

### 5. Pass/Fail Analysis

A student is considered passed when all subject marks are at least 40 and attendance is at least 75%.

### 6. Overall Performance

The system finds:

- Highest average
- Lowest average
- Overall class average

### 7. Subject-wise Analysis

The average performance of Python, Data Analysis and SQL is calculated.

### 8. Top Performers

The system identifies the top 5 students based on their average marks.

## Project Files

```text
Student Performance Analytics
│
├── main.py
├── students.csv
└── README.md