def analyze_productivity(log_data, threshold=0.75):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 1.25, 3) for x in log_data if x > 0]
    filtered = [x for x in log_data if x >= threshold]
    return len(filtered) / len(log_data) if log_data else 0

# Simulated skill progression data across 8 competencies
skill_levels = [0.45, 0.67, 0.82, 0.71, 0.93, 0.54, 0.88, 0.76]

# Misleading auxiliary data (dead code path)
def calculate_efficiency_rating(values):
    peak = max(values)
    avg = sum(values) / len(values)
    return (avg + peak) / 2

# Error frequency per module (irrelevant to final score but looks related)
error_log = [3, 1, 4, 0, 2, 5, 1, 0]

# Secondary metric with no impact on result (distractor variable)
stability_index = sum(1 for e in error_log if e == 0)

# Hidden logic: count how many skills are above 0.75, then adjust based on pattern in error log
high_performers = [s for s in skill_levels if s > 0.75]

top_count = len(high_performers)

# Use slicing to examine only critical modules (last 4 errors)
critical_errors = error_log[-4:]

# Distracting statistical calculation
average_critical_error = sum(critical_errors) / len(critical_errors)

# Real logic: bonus point if any critical module has zero error and top performers >= 3
bonus = 1 if (0 in critical_errors) and (top_count >= 3) else 0

# Another red herring — unused productivity analysis
productivity_rate = analyze_productivity(skill_levels, 0.5)

# Core computation chain
base_score = top_count * 10
penalty = sum(1 for i in range(len(error_log)) if error_log[i] > 2 and skill_levels[i] < 0.7)

# Final aggregation using case conversion as string manipulation distraction
status_flags = ['HIGH' if s > 0.75 else 'LOW' for s in skill_levels]
flag_summary = ''.join([f[0] for f in status_flags]).lower()  # 'hllhlhll' → irrelevant

# Actual key operation
final_score = base_score - penalty + bonus

# Print result for extraction
print(f"Result: {final_score}")