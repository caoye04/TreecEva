import itertools

def analyze_productivity(logs):
    total_entries = len(logs)
    valid_entries = [entry for entry in logs if 'error' not in entry]
    error_entries = [entry for entry in logs if 'error' in entry]
    
    # Irrelevant transformation (distractor)
    reversed_logs = [log[::-1] for log in logs]
    palindrome_count = sum(1 for log in reversed_logs if log == log[::-1])

    productivity = len(valid_entries)
    errors = len(error_entries)
    return productivity, errors

def calculate_efficiency(raw_data, baseline=100):
    processed = 0
    skipped = 0
    
    for item in raw_data:
        if item < 0:
            skipped += 1
            continue
        processed += 1
    
    # Distractor: complex but unused calculation
    cumulative = list(itertools.accumulate(raw_data))
    normalized = [c / (baseline + 1) for c in cumulative if c > 0]
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0

    efficiency = (processed / len(raw_data)) * 100 if raw_data else 0
    return efficiency

def evaluate_performance(p, e, eff):
    base = p * 10
    penalty = e * 5
    bonus = eff * 0.75
    
    if eff < 50:
        bonus *= 0.5
    
    score = base - penalty + bonus
    
    # Early return red herring (not taken)
    if p == 0:
        return 0
        unused_value = 999  # dead code
    
    return int(score)

# Main execution
system_logs = [
    'task_complete_1', 'task_error_critical', 'task_complete_2',
    'task_complete_3', 'task_error_minor', 'task_complete_4',
    'task_complete_5'
]

raw_metrics = [10, -5, 20, 15, 0, 25, -10]

productivity, errors = analyze_productivity(system_logs)
efficiency = calculate_efficiency(raw_metrics)

# Key statement
final_score = evaluate_performance(productivity, errors, efficiency)

print(f"Result: {final_score}")