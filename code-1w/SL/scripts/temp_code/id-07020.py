def analyze_trends(data, threshold):
    trend_count = 0
    temp_result = []
    for i, value in enumerate(data):
        if value > threshold:
            trend_count += 1
            temp_result.append(value * 0.9)
        else:
            temp_result.append(value * 1.1)
    return trend_count

# Irrelevant helper function (decoy)
def normalize_dataset(arr):
    total = sum(arr)
    return [x / total for x in arr] if total != 0 else arr

# Unused transformation chain
def transform_signal(signal):
    transformed = []
    for idx, val in enumerate(signal):
        if idx % 2 == 0:
            transformed.append(val ** 0.5)
        else:
            transformed.append(val ** 2)
    return transformed

# Simulate sensor readings (distractor data)
sensor_logs = [120, 140, 160, 130, 150]
baseline = [100, 105, 110, 115, 120]

# Fake correlation matrix (red herring)
corr_matrix = [[1.0, 0.3], [0.3, 1.0]]

# Core logic disguised among distractions
def compute_weighted_index(values, weights):
    weighted_sum = 0
    weight_total = 0
    for v, w in zip(values, weights):
        weighted_sum += v * w
        weight_total += w
    return weighted_sum / weight_total if weight_total != 0 else 0

# Misleading intermediate calculation
dummy_aggregate = 0
for item in sensor_logs:
    dummy_aggregate += item // 10

def evaluate_performance(metrics, reference):
    # Real computation buried in noise
    offset = len(metrics) - len(reference)
    adjusted_metrics = [m - ref for m, ref in zip(metrics, reference)]
    
    # Key distraction: irrelevant filtering
    filtered_vals = []
    for val in adjusted_metrics:
        if abs(val) > 5:
            filtered_vals.append(val * 1.2)
        else:
            filtered_vals.append(val * 0.8)
    
    # Secondary red herring: unused recursive function
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)

# More decoys
status_flags = [True, False, True]
flag_summary = any(status_flags) and not all(status_flags)

# Actual key logic hidden here
def evaluate_performance(metrics, baseline):
    raw_diffs = [m - b for m, b in zip(metrics, baseline)]
    positive_impact = sum(1 for d in raw_diffs if d > 0)
    total_deviation = sum(abs(d) for d in raw_diffs)
    
    # Complex conditional masking
    adjustment_factor = 0
    for i, diff in enumerate(raw_diffs):
        if i % 2 == 0 and diff > 0:
            adjustment_factor += 2
        elif i % 2 == 1 and diff < 0:
            adjustment_factor -= 1
    
    # Real result computed here — obscured by prior noise
    base_score = sum(raw_diffs)
    bonus = positive_impact * 3
    penalty = total_deviation // 4
    final_score = base_score + bonus - penalty + adjustment_factor
    
    # Dead code branch (never reached due to return)
    if final_score < 0:
        final_score *= -1
    
    return final_score

# Execution point of interest
metrics = [130, 108, 115, 112, 125]
final_score = evaluate_performance(metrics, baseline)
print(f"Target result: {final_score}")