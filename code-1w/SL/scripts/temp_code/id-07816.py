def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    count_consonants = sum(1 for c in sequence if c.isalpha() and c.lower() not in 'aeiou')
    return count_vowels * 2 - count_consonants

baseline = 42
offset_factor = -5
adjustment = 17

activity_log = 'MonitoringSystemLogEntry_2024'

# Auxiliary metric (distractor)
char_count = len(activity_log)
digit_count = sum(1 for c in activity_log if c.isdigit())

# Misleading intermediate calculation
weight = digit_count * 1000 if char_count > 20 else offset_factor

# Conditional expression used (required python feature)
scaling = 1.5 if 'Sys' in activity_log else 0.8

# Secondary helper with partial relevance
def evaluate_stability(metric):
    if metric < 0:
        return metric ** 2
    return metric + 10

# Core logic embedded with distractors
raw_performance = analyze_pattern(activity_log)
stability_metric = evaluate_stability(raw_performance)

# Simulated calibration (some steps are distractions)
calibration_offset = weight * 0.1  # Depends on weight, which uses dead logic
adjusted_baseline = baseline + adjustment - offset_factor

# Multiple assignments (relevant concept)
interim, flag = adjusted_baseline * 2, False

# Conditional expression again for intervention
correction = 5 if stability_metric > 15 else -3

# Final computation chain
aggregate = interim + stability_metric * scaling + correction

# Key statement
final_score = calculate_performance(baseline, activity_log) if 'Entry' in activity_log else -1

# Redefinition of function to ensure determinism (was missing)
def calculate_performance(base, log):
    temp = base + len(log) // 2
    if temp % 2 == 0:
        temp = temp // 2
    return temp + analyze_pattern(log)

# Print result as required
print(f"Result: {final_score}")