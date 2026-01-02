def analyze_feedback(reports):
    critical_issues = set()
    for report in reports:
        if 'error' in report.lower():
            critical_issues.add(report.strip().split()[0])
    return critical_issues

reports_list = [
    'ERROR: disk failure',
    'Warning: high latency',
    'INFO: system stable',
    'ERROR: memory leak',
    'DEBUG: trace enabled'
]

# Misleading intermediate analysis with unused result
temp_analysis = [r for r in reports_list if 'warning' in r.lower() or 'error' in r.lower()]
alert_count = len(temp_analysis)

feedback_set = analyze_feedback(reports_list)

# Distractor: irrelevant computation on string lengths
total_chars = sum(len(r) for r in reports_list)
useless_avg = total_chars / len(reports_list) if reports_list else 0

baseline = 100
penalty_fn = lambda x: 10 if x > 2 else 5

# Complex conditional expression with nested logic
evaluation_metric = (75 if len(feedback_set) == 0 else 
                    60 if len(feedback_set) <= 2 else 
                    40)

benchmark = {
    'threshold': 50,
    'grace_period': True,
    'multiplier': 1.2
}

# Core logic hidden among distractors
def evaluate_performance(issues, config):
    base = baseline - (len(issues) * 15)
    adjustment = penalty_fn(len(issues)) if 'grace_period' in config and config['grace_period'] else 0
    raw_score = base + adjustment
    
    # Final adjustment using conditional expression
    final = raw_score if raw_score >= config['threshold'] else config['threshold']
    return int(final * config['multiplier'])

# Key statement
final_score = evaluate_performance(feedback_set, benchmark)

print(f"Result: {final_score}")