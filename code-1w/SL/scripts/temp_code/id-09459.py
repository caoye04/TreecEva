from collections import defaultdict, Counter
import math

# Simulated health monitoring system with noise and irrelevant transformations
def analyze_vital(vital):
    if vital < 60:
        return 'low'
    elif vital > 100:
        return 'high'
    else:
        return 'normal'

def compute_rri(interval, factor=1.05):
    # Irrelevant computation: Respiratory rate index (not used in final logic)
    return round(math.log(interval + 1) * factor, 3)

def deprecated_normalizer(data_list):
    # Dead code path: never called
    return [x / sum(data_list) for x in data_list]

def filter_outliers(seq, limit=3):
    count = Counter(seq)
    return [k for k, v in count.items() if v >= limit]

# Misleading auxiliary variables
temp_log = []
diagnostic_codes = {"A": 10, "B": 25, "C": 17}
baseline_adjustment = 0.89
scaling_factor = 12.7

# Core dataset: heart rate intervals over 24h in minutes
raw_intervals = [72, 68, 75, 60, 80, 73, 73, 73, 68, 68, 75, 75, 80, 80, 80, 80]

# Process step 1: categorize each interval
interval_labels = [analyze_vital(x) for x in raw_intervals]

# Distractor: complex but unused transformation using slicing and set ops
reversed_slice = raw_intervals[::-1]
mid_segment = reversed_slice[4:12]
unique_mid = set(mid_segment)
sorted_unique = sorted(unique_mid.union({max(raw_intervals)}))

# Another red herring: bit manipulation on diagnostic codes
encoded_diagnostics = 0
for code in diagnostic_codes:
    encoded_diagnostics ^= ord(code) << (diagnostic_codes[code] % 8)

# Simulate artifact filtering (unused)
artifact_mask = [x in range(65, 78) for x in raw_intervals]
filtered_artifacts = [raw_intervals[i] for i in range(len(raw_intervals)) if artifact_mask[i]]

# Real processing begins here — hidden among distractions
window_size = 4
critical_peaks = 0
for i in range(len(raw_intervals) - window_size + 1):
    window = raw_intervals[i:i+window_size]
    if all(w > 70 for w in window):
        critical_peaks += 1

# Secondary metric: frequency of normal readings
label_freq = Counter(interval_labels)
normal_count = label_freq['normal']

# Tertiary: detect sustained patterns via set operations
sustained_windows = []
for i in range(0, len(interval_labels) - 2, 3):
    triad = interval_labels[i:i+3]
    if len(set(triad)) == 1:
        sustained_windows.append(triad[0])

# Now begin actual score calculation chain
base_metric = normal_count * 13
peak_bonus = critical_peaks * 22

# Hidden dependency: use of collections.defaultdict for aggregation
diagnosis_grid = defaultdict(int)
for label in interval_labels:
    diagnosis_grid[label] += 1

# This next block looks important but only one value matters
aggregate_risk = 0
for k, v in diagnosis_grid.items():
    if k == 'low':
        aggregate_risk += v * 3
    elif k == 'high':
        aggregate_risk += v * 5

adjustment_score = diagnosis_grid['normal']  # Used later

# Decoy function that computes something plausible but unused
def calculate_stability_index(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    stability = sum(1 for d in diffs if d < 5)
    return round(stability / len(diffs), 4) if diffs else 0.0

stability_index = calculate_stability_index(raw_intervals)  # Computed but not used

# Real path resumes: determine threshold from sustained analysis
threshold = len(sustained_windows) if sustained_windows else 5

# Health data structure that combines multiple concepts
health_data = {
    'readings': raw_intervals,
    'labels': interval_labels,
    'metrics': {
        'base': base_metric,
        'bonus': peak_bonus,
        'risk': aggregate_risk,
        'stable_windows': len(sustained_windows)
    },
    'summary': diagnosis_grid
}

# Final processing function with distraction inside
def process_metrics(data, thresh):
    m = data['metrics']
    total = m['base'] + m['bonus']
    
    # Several misleading branches
    if m['risk'] > 10:
        total -= 15
    if len(data['readings']) % 4 == 0:
        total += 7
    if data['summary']['high'] > data['summary']['low']:
        total += 3
    
    # Critical check: uses adjustment_score from earlier defaultdict
    # But obscured by decoy variables
    fallback = data['summary'].get('missing', 0)
    adjustment = adjustment_score  # Captured from outer scope
    
    # Final computation
    result = total + (adjustment * 2) - (thresh * 4)
    
    # Dead branch: never executes due to fixed data
    if fallback > 100:
        result = result * 0.5  # Never reached
        
    return int(result)

# Execute main logic
critical_threshold = threshold  # Copy to obscure usage
final_score = process_metrics(health_data, threshold)

# Output result as required
print(f"Result: {final_score}")