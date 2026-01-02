from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_health(data):
    return sum(x * 0.3 for x in data if x > 50)

# Misleading metric calculation (red herring)
temp_weights = [0.1, 0.2, 0.3, 0.4]
raw_metrics = [85, 90, 78, 92]
weighted_avg = sum(temp_weights[i] * raw_metrics[i] for i in range(len(temp_weights)))

# Unused but plausible-looking normalization function
def normalize_scores(scores):
    max_val = max(scores)
    return [s / max_val for s in scores]

# Distractor: complex but unused data structure
diagnostic_log = defaultdict(lambda: 'unknown')
diagnostic_log.update({
    'sensor_a': 'active',
    'sensor_b': 'idle',
    'calibration': 'passed',
    'firmware': 'v2.1.5'
})

# Fake performance trace (dead code path)
trace_enabled = False
if trace_enabled:
    execution_trace = []
    for i in range(5):
        execution_trace.append(f'Step {i}: OK')

# Actual core logic buried in noise
def calculate_efficiency(records):
    count = 0
    total = 0
    for r in records:
        if r >= 80:
            count += 1
            total += r
    return total / count if count else 0

def detect_outliers(values, threshold=10):
    # Unused outlier detection
    avg = sum(values) / len(values)
    return [v for v in values if abs(v - avg) > threshold]

# Key function with relevant logic obscured by context
def evaluate_performance(met, base):
    # Real computation begins here
    efficiency = calculate_efficiency(met)
    
    # Distraction: irrelevant transformation
    transformed = [math.log(x + 1) for x in met if x % 2 == 0]
    dummy_shift = sum(transformed) * 0.01
    
    # Another decoy operation
    freq_count = Counter(met)
    mode_value = freq_count.most_common(1)[0][1]
    
    # Critical path: comparison against baseline
    if efficiency > base:
        bonus = 15
    else:
        bonus = -10
    
    # Multiple steps of reasoning
    adjustment = len(met) if efficiency > 85 else 5
    penalty = 0
    for m in met:
        if m < 70:
            penalty += 5
    
    # Composite score calculation (true answer source)
    base_score = efficiency * 1.2
    final = base_score + bonus + adjustment - penalty - dummy_shift
    
    # Dead code: looks important but never reached
    if final < 0:
        final = 0
    
    return int(round(final))

# Auxiliary string processing (distractor)
def format_report(name):
    name = name.strip().upper()
    return name.replace(' ', '_') + '_REPORT'

report_name = format_report(' Q3 Performance ')

# Noise: fake data used nowhere
historical_data = [
    [76, 88, 81],
    [91, 73, 85],
    [80, 82, 89]
]

# Relevant data buried among distractions
metrics = [88, 92, 76, 95, 83, 91, 87]
baseline = 85

# Key assignment statement — this is where the answer forms
final_score = evaluate_performance(metrics, baseline)

# Output required result
print(f"Result: {final_score}")