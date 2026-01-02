def calculate_final_score(values, deductions):
    normalized = [v ** 0.5 for v in values]
    adjusted = []
    for i, val in enumerate(normalized):
        if i % 2 == 0:
            adjusted.append(val - deductions[i // 2])
        else:
            adjusted.append(val)
    return round(sum(adjusted), 3)

# Irrelevant auxiliary data (minimal distraction)
timestamps = [162345, 162346, 162348]
status_flags = [True, False, True]

# Main computation input
scores = [81, 64, 49, 36]
penalties = [2, 3]

result = calculate_final_score(scores, penalties)
print(f"Target result: {result}")