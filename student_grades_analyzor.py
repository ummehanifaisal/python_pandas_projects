import pandas as pd

# Create a dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Math": [85, 78, 92, 88],
    "Science": [90, 85, 95, 89],
    "English": [88, 72, 80, 85],
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Analysis
df["Average"] = df[["Math", "Science", "English"]].mean(axis=1)
print("Student Grades:\n", df)

print("\nHighest Scores:")
print(df[["Math", "Science", "English"]].max())

print("\nLowest Scores:")
print(df[["Math", "Science", "English"]].min())
