from collections import defaultdict, Counter

# Simulate system telemetry data
def collect_telemetry():
    raw_data = [12, 15, 22, 12, 17, 22, 25, 15, 12, 30]
    counts = Counter(raw_data)
    return counts

def analyze_patterns(seq):
    freq_map = defaultdict(int)
    for val in seq:
        freq_map[val] += 1
    # Irrelevant transformation
    temp_result = [k*v for k, v in freq_map.items() if k % 2 == 0]
    adjustment = sum(temp_result) // 3 if temp_result else 0
    return adjustment

def compute_baseline(data):
    # Distractor function with dead logic
    total = 0
    for x in data:
        if x > 20:
            total += x * 0.5
        elif x < 10:
            total -= x
    scaling = len(data) / 8
    return int(total / scaling) if scaling else 0

def extract_features(log_entries):
    # Real processing begins here
    stats = []
    for entry in log_entries:
        stats.append(entry * 2 if entry % 3 == 0 else entry + 1)
    # Slice middle portion (slicing operation)
    mid_section = stats[2:6]
    processed = [x - 5 for x in mid_section]
    return processed

def evaluate_performance(metrics, weights):
    score = 0
    # Weighted aggregation using zip
    for metric, weight in zip(metrics, weights):
        score += metric * weight
    # Apply non-linear adjustment
    if score > 50:
        score = score * 0.9 + 10
    else:
        score = score * 1.1
    # Final threshold clamp
    score = min(max(score, 0), 100)
    return int(score)

# Main execution flow
telemetry_counts = collect_telemetry()
data_list = list(telemetry_counts.keys())

# Irrelevant analysis branches
noise_floor = analyze_patterns(data_list)
baseline_offset = compute_baseline(data_list)

# Feature extraction - relevant path
features = extract_features(data_list)

# Mock configuration (distractor)
config = {
    'version': '2.1',
    'mode': 'diagnostic',
    'threshold': noise_floor + baseline_offset
}

# Critical variables
metrics = features[:3]  # Take first three features
weights = [0.4, 0.35, 0.25]  # Weight distribution

# Key statement
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")