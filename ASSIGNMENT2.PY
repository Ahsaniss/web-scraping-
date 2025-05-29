import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean

# Given dataset
data = np.array([
    [5, 3, 0], [4, 2, 0], [2, 3, 0], [3, 4, 0], [4, 5, 0],
    [10, 5, 1], [11, 3, 1], [12, 6, 1], [13, 7, 1], [14, 5, 1]
])

# Split data into X, Y, and categories
X, Y, categories = data[:, 0], data[:, 1], data[:, 2]

# Plot initial points
plt.figure(figsize=(8, 6))
for x, y, category in data:
    plt.scatter(x, y, marker='o' if category == 0 else 'x', s=100)
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("KNN Classification")
plt.grid()
plt.legend()
plt.show()

# Get new point from user
new_x = float(input("Enter X coordinate: "))
new_y = float(input("Enter Y coordinate: "))
new_point = np.array([new_x, new_y])

# Step 1: Show new point on graph
plt.figure(figsize=(8, 6))
for x, y, category in data:
    plt.scatter(x, y, marker='o' if category == 0 else 'x', s=100)
plt.scatter(new_x, new_y, marker='s', color='blue', s=150, label="New Point")  # Temporary shape for new point
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("New Point Added")
plt.grid()
plt.legend()
plt.show()

input("\nPress Enter to classify the new point...")  # Wait for Enter key

# Step 2: Classify the point using KNN
k = 3
distances = [(euclidean(new_point, [x, y]), category, x, y) for x, y, category in data]
distances.sort(key=lambda x: x[0])
nearest_neighbors = distances[:k]  # Get 3 nearest neighbors

# Determine majority category
categories_of_neighbors = [category for _, category, _, _ in nearest_neighbors]
predicted_category = max(set(categories_of_neighbors), key=categories_of_neighbors.count)

# Step 3: Update shape based on classification
plt.figure(figsize=(8, 6))
for x, y, category in data:
    plt.scatter(x, y, marker='o' if category == 0 else 'x', s=100)
plt.scatter(new_x, new_y, marker='o' if predicted_category == 0 else 'x', color='red', s=150, label="Classified Point")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title(f"New Point Classified as Category {int(predicted_category)}")
plt.grid()
plt.legend()
plt.show()

input("\nPress Enter to show distances to the three closest points...")  # Wait for Enter key

# Step 4: Show distances to three nearest points
nearest_three = distances[:3]  # Only consider the 3 nearest neighbors

plt.figure(figsize=(8, 6))
for x, y, category in data:
    plt.scatter(x, y, marker='o' if category == 0 else 'x', s=100)
plt.scatter(new_x, new_y, marker='o' if predicted_category == 0 else 'x', color='red', s=150, label="Classified Point")

# Draw lines to the three nearest points
for i, (dist, category, nx, ny) in enumerate(nearest_three, 1):
    plt.plot([nx, new_x], [ny, new_y], 'g--', label=f"Distance {i}: {dist:.2f}")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Distances to Three Nearest Neighbors")
plt.grid()
plt.legend()
plt.show()

# Print distances
print("\nDistances from nearest three neighbors:")
for i, (dist, category, nx, ny) in enumerate(nearest_three, 1):
    print(f"{i}. Distance: {dist:.2f}, Category: {int(category)}, Nearest Point: ({nx}, {ny})")
