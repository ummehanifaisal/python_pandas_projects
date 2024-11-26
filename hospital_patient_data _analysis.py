import pandas as pd

# Patient data
data = {
    "Patient ID": [1, 2, 3, 4, 5],
    "Age": [30, 45, 60, 23, 50],
    "Disease": ["Flu", "Diabetes", "Cancer", "Cold", "Hypertension"],
    "Treatment Outcome": ["Recovered", "Chronic", "Recovered", "Recovered", "Chronic"]
}

df = pd.DataFrame(data)

# Count of each treatment outcome
outcome_counts = df["Treatment Outcome"].value_counts()
print("Treatment Outcome Counts:")
print(outcome_counts)

# Average age of patients with chronic conditions
average_age_chronic = df[df["Treatment Outcome"] == "Chronic"]["Age"].mean()
print(f"Average Age of Chronic Patients: {average_age_chronic}")
