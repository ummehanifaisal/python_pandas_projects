import pandas as pd

# Expense Data
data = {
    "Category": ["Rent", "Groceries", "Utilities", "Entertainment", "Miscellaneous"],
    "January": [1000, 200, 150, 100, 50],
    "February": [1000, 220, 160, 80, 70],
    "March": [1000, 210, 155, 90, 60],
}

df = pd.DataFrame(data)

# Analysis
df["Total"] = df[["January", "February", "March"]].sum(axis=1)
print("Expense Tracker:\n", df)

print("\nTotal Expense Across Months:", df["Total"].sum())
print("Category-wise Total Expenses:")
print(df[["Category", "Total"]])
