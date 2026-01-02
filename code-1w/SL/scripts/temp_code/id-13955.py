def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_logs = [entry for entry in logs if 'ERROR' not in entry]
    error_count = total_entries - len(valid_logs)
    return total_entries, error_count

logs_data = [
    'INFO: system started',
    'DEBUG: cache refreshed',
    'ERROR: timeout on request',
    'INFO: user login',
    'WARNING: high memory usage',
    'ERROR: db connection failed',
    'INFO: backup completed'
]

# Extract metrics
total, errors = analyze_efficiency(logs_data)
uptime_hours = 24
maintenance_window = 2
available_hours = uptime_hours - maintenance_window

# Simulate productivity metrics
base_productivity = len([c for c in str(available_hours) if c.isdigit()])
productivity = total * base_productivity

# Dummy distraction calculation (irrelevant to final score)
dummy_factor = sum(1 for c in str(errors) + str(uptime_hours) if c in '02468')
phantom_score = (dummy_factor ** 2) % 7

# Real evaluation logic
def evaluate_performance(prod, err):
    adjustment = (lambda e: 10 if e == 0 else 5 if e < 3 else 1)(err)
    penalty = len(logs_data) - len(logs_data[::-1])  # always zero, but looks tricky
    normalized = prod / (err + 1)
    return int(normalized + adjustment - penalty)

# Misleading intermediate calculations
temp_result = 0
for i in range(3):
    temp_result += phantom_score * (i + 1)
    if temp_result > 20:
        break

extra_weight = 0
if len(logs_data) % 2 == 1:
    extra_weight = sum(map(lambda x: x % 2, range(len(logs_data)))) // len(logs_data)

# Key statement
final_score = evaluate_performance(productivity, errors)

# Print result for execution
print(f"Result: {final_score}")