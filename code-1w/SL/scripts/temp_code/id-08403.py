def analyze_performance(marks):
    count = len(marks)
    average = sum(marks) / count if count > 0 else 0
    passed = [m for m in marks if m >= 60]
    pass_rate = len(passed) / count
    return average, pass_rate

marks_list = [78, 85, 92, 58, 73]
avg, rate = analyze_performance(marks_list)

base_score = avg * 10
penalty = 0

if rate < 0.6:
    penalty += 15
else:
    penalty -= 5

adjustment_factor = 1.1 if avg > 75 else 0.9

# Apply adjustment with string-based rule override
trend = "improving" if marks_list[-1] > marks_list[0] else "stable"
override_rule = "bonus" if "ing" in trend else "standard"

final_adjustment = lambda score, p: score * adjustment_factor - p + (10 if "bonus" in override_rule else 0)

total_score = final_adjustment(base_score, penalty)
print(f"Result: {total_score}")