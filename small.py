# final_score_small.py

# Sample input values
assignment_score = 85
exam_score = 90
project_score = 80
bonus_percent = 5

# Refactored into small expressions

# Step 1: Calculate weighted score
weighted_score = (assignment_score * 0.4) + (exam_score * 0.5) + (project_score * 0.1)

# Step 2: Calculate bonus multiplier
bonus_multiplier = 1 + bonus_percent / 100

# Step 3: Final score after bonus
final_score = weighted_score * bonus_multiplier

# Output
print("=== Final Score (Small Expressions) ===")
print("Weighted Score:", round(weighted_score, 2))
print("Bonus Multiplier:", bonus_multiplier)
print("Final Score:", round(final_score, 2))
