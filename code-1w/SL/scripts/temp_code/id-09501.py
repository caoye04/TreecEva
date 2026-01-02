def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_logs = [entry for entry in logs if 'ERROR' not in entry]
    error_count = total_entries - len(valid_logs)
    clean_data = ''.join(valid_logs).upper()
    keyword_hits = clean_data.count('SUCCESS') + clean_data.count('COMPLETE')
    return keyword_hits, error_count

logs_input = [
    'task_123 started',
    'task_124 COMPLETE',
    'task_125 ERROR: timeout',
    'task_126 SUCCESS',
    'task_127 ERROR: io',
    'task_128 COMPLETE'
]

hits, err = analyze_efficiency(logs_input)
productivity = hits * 10
error_penalty = max(0, 100 - err * 15)

# Distractor block: string analysis with no impact
log_text = ' | '.join(logs_input)
distinct_chars = set(log_text)
redundant_metric = len(distinct_chars) % 7
auxiliary_flag = 'ERROR' in log_text and len(distinct_chars) > 10

# Distractor: unused helper function
def compute_entropy(s):
    from math import log2
    freq = {c: s.count(c) for c in set(s)}
    entropy = sum(-(f/len(s)) * log2(f/len(s)) for f in freq.values())
    return round(entropy, 3)

entropy_value = compute_entropy('abcde')  # Dead-end computation

# Real logic resumes
baseline = 50
if productivity >= 30:
    baseline += 20
else:
    baseline -= 5

# Another distractor: complex but irrelevant set operation
unique_tasks = {entry.split()[0] for entry in logs_input}
task_prefixes = {task.split('_')[0] for task in unique_tasks}
overlap_check = len(unique_tasks & task_prefixes)

# Main scoring logic
stability_factor = 1 if err <= 2 else 0.5
efficiency_ratio = (productivity * stability_factor) / (err + 1)

# Final evaluation
interim_result = efficiency_ratio + error_penalty

# Key assignment point
final_score = evaluate_performance(productivity, errors)

# Redefine function to avoid undefined error
def evaluate_performance(prod, errs):
    base = 2 * prod
    deduction = 5 * errs
    if prod >= 25:
        bonus = 15
    else:
        bonus = 0
    # Additional noise: string manipulation that does nothing
    status_str = "High" if prod > 20 else "Low"
    padded = status_str.center(10)
    trimmed = padded.strip()
    return base - deduction + bonus + 10  # Constant offset included

# Recompute final_score after function definition
final_score = evaluate_performance(productivity, err)
print(f"Result: {final_score}")