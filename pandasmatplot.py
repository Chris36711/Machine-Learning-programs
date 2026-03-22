import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Marks": [50, 60, 70, 80, 90],
    "Students": [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

print("Data Frame")
print(df)

print("Marks column")
print(df["Marks"])

plt.plot(df["Students"], df["Marks"])

plt.xlabel("Students")

plt.ylabel("Marks")

plt.title("Marks Graph")

plt.show()