from itertools import compress

def analyze_performance(log_entries):
    valid_entries = [entry for entry in log_entries if 'ERROR' not in entry]
    return len(valid_entries) > 5

def calculate_final_score(points, deductions):
    base_score = sum(points)
    penalty_total = sum(d for d in deductions if d > 0)
    adjustment = len([p for p in points if p >= 10]) * 1.5
    return base_score - penalty_total + adjustment

# Simulation data from system logs
log_data = [
    'INFO: startup',
    'DEBUG: routine check',
    'ERROR: disk full',
    'INFO: user login',
    'INFO: file saved',
    'WARNING: low memory',
    'INFO: backup complete',
    'INFO: shutdown'
]

# Extract numeric activity points from log keywords
raw_points = []
for entry in log_data:
    if 'INFO' in entry:
        raw_points.append(8)
    elif 'DEBUG' in entry:
        raw_points.append(5)
    elif 'WARNING' in entry:
        raw_points.append(3)

penalties = [2, 0, 5, 1]  # Deductible penalties

# Determine performance status (not directly used in score)
performance_ok = analyze_performance(log_data)

# Key computation
final_score = calculate_final_score(raw_points, penalties)
print(f"Result: {final_score}")