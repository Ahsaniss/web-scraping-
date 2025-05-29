import numpy as np
import os
import subprocess
from sklearn.neighbors import KNeighborsClassifier

# ✅ Step 1: Define the dataset (X, Y, Category)
data = np.array([
    [5, 3, 0], [4, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0],
    [10, 5, 1], [11, 3, 1], [12, 6, 1], [13, 7, 1], [14, 5, 1]
])

# ✅ Step 2: Create and save the dataset to 'data.txt'
data_file = "data.txt"
with open(data_file, "w") as f:
    for row in data:
        f.write(f"{row[0]} {row[1]} {row[2]}\n")

print(f"✅ Data file '{data_file}' created.")

# ✅ Step 3: Function to get valid numeric input from user
def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")

# ✅ Step 4: Ask User for a New Point
X_new = get_float_input("Enter X coordinate of new point: ")
Y_new = get_float_input("Enter Y coordinate of new point: ")
new_point = np.array([[X_new, Y_new]])

# ✅ Step 5: Train KNN Classifier (K=3)
X_train = data[:, :2]  # Features (X, Y)
y_train = data[:, 2]   # Categories (0 or 1)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predict category for new point
predicted_category = int(knn.predict(new_point)[0])
print(f"Predicted Category: {predicted_category}")

# ✅ Step 6: Append New Point to 'data.txt'
with open(data_file, "a") as f:
    f.write(f"{X_new} {Y_new} {predicted_category}\n")

print(f"✅ New point added to '{data_file}'.")

# ✅ Step 7: Create Gnuplot Script (plot.gnu)
gnuplot_script = f"""
set title "KNN Classification"
set xlabel "X"
set ylabel "Y"
set grid
set key outside
plot "{data_file}" using 1:2:3 with points pt 7 lc variable title "Existing Points", \
     "{data_file}" every ::-1 using 1:2:3 with points pt 9 lc variable title "New Point"
pause -1
"""

# Save Gnuplot script
plot_file = "plot.gnu"
with open(plot_file, "w") as f:
    f.write(gnuplot_script)

print(f"✅ Gnuplot script '{plot_file}' created.")

# ✅ Step 8: Run Gnuplot
try:
    subprocess.run(["gnuplot", plot_file], check=True)
    print("✅ Gnuplot executed successfully.")
except FileNotFoundError:
    print("❌ Error: Gnuplot is not installed or not found in system PATH.")
except subprocess.CalledProcessError:
    print("❌ Error: Gnuplot encountered an issue while running.")
