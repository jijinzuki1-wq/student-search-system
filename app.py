
import streamlit as st
import pandas as pd

# Load the dataset
df = pd.read_csv("students_cleaned.csv")

# Page title
st.title("Student Search System")

# Total number of students
st.write("Total students:", len(df))

# Student ID input
student_id = st.text_input("Enter Student ID")

if student_id:

    # Search for the student
    result = df[df["student_id"].astype(str) == student_id]

    if not result.empty:
        st.success("Student found!")

        # Get the first matching student
        student = result.iloc[0]

        st.subheader("Student Information")

        # Create a table
        student_data = {
            "Information": [
                "Student ID",
                "Full Name",
                "Gender",
                "Region",
                "Course",
                "Age",
                "Math Score",
                "Programming Score",
                "Networking Score",
                "Attendance",
                "Registration Date",
                "Phone"
            ],

            "Value": [
                student["student_id"],
                student["full_name"],
                student["gender"],
                student["region"],
                student["course"],
                int(student["age"]),
                student["score_math"],
                student["score_programming"],
                student["score_networking"],
                str(student["attendance_percent"]) + "%",
                student["registration_date"],
                student["phone"]
            ]
        }

        # Display the table
        student_table = pd.DataFrame(student_data)

        st.table(student_table)

    else:
        st.error("Student not found!")
