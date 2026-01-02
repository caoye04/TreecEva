student_ids = set(range(101, 116))
exam_results = {101: 88, 102: 75, 103: 95, 104: 60, 105: 72, 106: 90, 107: 85, 108: 68, 109: 93, 110: 70, 111: 80, 112: 87, 113: 74, 114: 91, 115: 65}

# Determine passing records (students with score >= 80)
passing_records = {sid for sid, score in exam_results.items() if score >= 80}

# High priority cases are students with odd IDs
high_priority = {sid for sid in student_ids if sid % 2 == 1}

# Calculate final score as intersection of passing and high-priority students
final_score = len(passing_records & high_priority)

print(f"Result: {final_score}")