# Module 1 - Basic Data Science Example
# Install pandas if required: pip install pandas

import pandas as pd

data = {
    "Student": ["A", "B", "C", "D", "E"],
    "Python": [85, 72, 90, 65, 78],
    "Data_Science": [80, 75, 88, 70, 82]
}

df = pd.DataFrame(data)

df["Average"] = (df["Python"] + df["Data_Science"]) / 2

print("Dataset:")
print(df)

print("\nAverage Python mark:", df["Python"].mean())
print("Highest average:", df["Average"].max())
print("\nStudents with average >= 80:")
print(df[df["Average"] >= 80])
