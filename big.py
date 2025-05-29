

# Sample input values
assignment_score = 85
exam_score = 90
project_score = 80
bonus_percent = 5

# Big expression version
score = assignment_score
score___ = (score * 0.4) + (exam_score * 0.5)
project_score___ = (project_score * 0.1)
percent_ = (1 + bonus_percent / 100)
final_score = (score___ + project_score___) * percent_

# Output
print("=== Final Score (Big Expression) ===")
print("Final Score:", round(final_score, 2))
