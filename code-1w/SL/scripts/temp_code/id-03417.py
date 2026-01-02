def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = sum(1 for entry in logs if 'ERROR' not in entry)
    error_rate = (total_entries - valid_count) / total_entries if total_entries > 0 else 0
    return error_rate

logs_data = [
    'INFO: system start',
    'DEBUG: module loaded',
    'ERROR: timeout exceeded',
    'INFO: retry attempt 1',
    'WARNING: low memory',
    'INFO: recovery successful'
]

# Irrelevant transformation (distractor)
transformed = list(map(lambda x: x.upper().replace(' ', '_'), logs_data))
processed_count = len([x for x in transformed if 'INFO' in x])

# Simulate productivity metrics
base_productivity = 85
hours_worked = 7.5
breaks_taken = 2

# Real metric calculation (semi-relevant)
adjusted_productivity = base_productivity * (1 - (breaks_taken * 0.05))
clock_hours = 8
utilization = adjusted_productivity / 100 / clock_hours * hours_worked

# Core logic inputs
productivity = int(adjusted_productivity + utilization * 10)
error_logs = sum(1 for log in logs_data if 'ERROR' in log)
warning_logs = sum(1 for log in logs_data if 'WARNING' in log)

# Secondary distraction: character frequency analysis (mostly irrelevant)
all_chars = ''.join(logs_data)
char_freq = {c: all_chars.count(c) for c in set(all_chars)}
special_char_count = sum(1 for c in all_chars if c in '!@#$%')

# Another red herring: hypothetical risk score
risk_factor = 1.2 if warning_logs > 0 else 1.0
hypothetical_risk = special_char_count * 100 / (len(all_chars) or 1) * risk_factor if len(all_chars) > 0 else 0

# Actual error weighting (used later)
errors = error_logs * 10 + warning_logs * 3

# Conditional expression and lambda usage (required Python features)
evaluate_performance = lambda prod, err: prod - err if err > 5 else prod + 5

# Key statement
final_score = evaluate_performance(productivity, errors)

# Print result as required
print(f"Target result: {final_score}")