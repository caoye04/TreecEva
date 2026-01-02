from collections import defaultdict, Counter
import math

# Simulated system metrics from a distributed computing environment
task_logs = [
    'TASK_START id:1001 duration:230 status:SUCCESS priority:HIGH',
    'TASK_FAIL id:1002 duration:450 status:FAILURE priority:MEDIUM reason:TIMEOUT',
    'TASK_START id:1003 duration:180 status:SUCCESS priority:LOW',
    'TASK_START id:1004 duration:600 status:FAILURE priority:HIGH reason:OOM',
    'TASK_START id:1005 duration:310 status:SUCCESS priority:MEDIUM'
]

# Irrelevant auxiliary mapping (distractor)
priority_map = {'LOW': 1, 'MEDIUM': 2, 'HIGH': 3}
status_codes = {'SUCCESS': 0, 'FAILURE': 1}

# Parse logs into structured data
def parse_logs(logs):
    parsed = []
    for log in logs:
        parts = log.split(' ')
        data = {}
        for part in parts:
            if ':' in part:
                k, v = part.split(':', 1)
                data[k] = v
        parsed.append(data)
    return parsed

# Extract durations and statuses
decoded_tasks = parse_logs(task_logs)
durations = [int(t['duration']) for t in decoded_tasks]
statuses = [t['status'] for t in decoded_tasks]

# Dead code path - never called (red herring)
def legacy_calculate(x):
    return sum(i ** 2 for i in range(x) if i % 3 == 0)

# Misleading intermediate metric (decoy)
avg_duration = sum(durations) / len(durations) if durations else 0
total_failure_count = sum(1 for s in statuses if s == 'FAILURE')

# Bit manipulation distraction - unused result
obfuscated_mask = 0
for d in durations:
    obfuscated_mask ^= (d << 2) | (d >> 3)

# Another distractor: frequency analysis of digits in task IDs (irrelevant)
task_id_digits = ''.join([t.get('id', '') for t in decoded_tasks])
digit_freq = Counter(task_id_digits)

# Conditional expression decoy
penalty_factor = 1.5 if any(d > 500 for d in durations) else 1.0

# Data transformation with list comprehension and filtering
efficiency_ratings = [
    round((300 - abs(d - 300)) * 0.1, 2) for d in durations if d > 0
]

# Unused nested structure (complexity without purpose)
resource_profile = {
    'cpu': { 'peak': max(durations) * 0.7, 'floor': min(durations) * 0.3 },
    'memory': {
        'allocated': [d * 2 for d in durations],
        'freed': [d * 1.8 for d in durations if d < 500]
    }
}

# Core evaluation logic buried among noise
def analyze_stability(ratings):
    if not ratings:
        return 0.0
    mean_rating = sum(ratings) / len(ratings)
    variance = sum((r - mean_rating) ** 2 for r in ratings) / len(ratings)
    return round(math.sqrt(variance), 4)

# Secondary processing with default dictionary (partially relevant)
metrics = defaultdict(float)
metrics['stability'] = analyze_stability(efficiency_ratings)
metrics['completion_rate'] = (len(statuses) - total_failure_count) / len(statuses)
metrics['avg_efficiency'] = sum(efficiency_ratings) / len(efficiency_ratings)

# Baseline thresholds for performance comparison
baseline = {
    'stability': 8.5,
    'completion_rate': 0.75,
    'avg_efficiency': 15.0
}

# Decoy function using string methods - never used
def format_report(data):
    lines = []
    for k, v in data.items():
        line = f'{k.upper()} -> {str(v).ljust(10)} [OK]'
        lines.append(line.replace('->', '=>'))
    return '\n'.join(lines)

# Real computation hidden in complex conditional logic
def evaluate_performance(met, base):
    score = 100.0
    # Apply adjustments based on deviation from baseline
    for key in base.keys():
        if key == 'stability':
            # Invert stability impact: lower deviation is better
            deviation = abs(met[key] - base[key])
            score -= deviation * 2
        elif key == 'completion_rate':
            bonus = (met[key] - base[key]) * 40
            score += bonus
        elif key == 'avg_efficiency':
            efficiency_delta = met[key] - base[key]
            if efficiency_delta >= 0:
                score += 10
            else:
                score -= abs(efficiency_delta) * 1.5
    
    # Hidden adjustment: add XOR of first three duration values modulo 10
    hidden_boost = (durations[0] ^ durations[1] ^ durations[2]) % 10
    score += hidden_boost
    
    # Final nonlinear transformation (obscured)
    if score > 0:
        score = math.log(score * 2) * 10
    
    return round(score, 4)

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Output the target result
print(f"Target result: {final_score}")