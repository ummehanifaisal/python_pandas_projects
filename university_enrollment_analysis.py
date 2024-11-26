import pandas as pd

# University enrollment data
data = {
    "Department": ["Computer Science", "Electrical Engineering", "Mechanical Engineering", "Civil Engineering"],
    "Enrolled Students": [120, 90, 75, 100]
}

df = pd.DataFrame(data)

# Calculate total enrolled students
total_enrollment = df["Enrolled Students"].sum()
print(f"Total Number of Enrolled Students: {total_enrollment}")

# Department with the highest enrollment
highest_enrollment = df.loc[df["Enrolled Students"].idxmax()]
print(f"Department with the Highest Enrollment: {highest_enrollment['Department']} with {highest_enrollment['Enrolled Students']} students")
