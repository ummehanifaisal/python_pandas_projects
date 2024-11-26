import pandas as pd

# Employee salary data
data = {
    "Employee Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Department": ["HR", "Engineering", "Sales", "Marketing", "Finance"],
    "Salary": [50000, 70000, 60000, 80000, 75000]
}

df = pd.DataFrame(data)

# Calculate the average salary
average_salary = df["Salary"].mean()
print(f"Average Salary: ${average_salary}")

# Employee with the highest salary
highest_salary_employee = df.loc[df["Salary"].idxmax()]
print(f"Highest Salary Employee: {highest_salary_employee['Employee Name']} with ${highest_salary_employee['Salary']}")
