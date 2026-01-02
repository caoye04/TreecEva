def analyze_readings(readings):
    cumulative = 0
    trend_flags = []
    for i, val in enumerate(readings):
        if i > 0 and readings[i] > readings[i-1]:
            trend_flags.append(1)
        else:
            trend_flags.append(0)
        cumulative += val ** 0.5
    return cumulative, trend_flags

# Irrelevant helper (decoy function)
def compute_score(items):
    total = 0
    for item in items:
        total += item * 2
    return total  # Unused in main logic

# Unused transformation
def normalize(data):
    max_val = max(data)
    return [x / max_val for x in data]

# Distractor variables
temp_log = [23.5, 24.1, 22.9, 25.0, 26.3]
diagnostic_codes = ['A1', 'B2', 'C3', 'D4']

# Main data
health_data = [88, 92, 76, 81, 96, 79, 85]
thresholds = {'low': 80, 'high': 90}

# Dead code path
if len(health_data) < 5:
    health_data = [x * 1.1 for x in health_data]
elif len(health_data) > 10:
    health_data = health_data[:10]
else:
    pass  # No-op, misleading structural complexity

# Auxiliary processing with red herring
shifted_data = [x - 75 for x in health_data]
index_map = {i: val for i, val in enumerate(shifted_data)}

# Real but obscured core logic
baseline_adjusted = [x - thresholds['low'] for x in health_data]
positive_deviation = [abs(x) if x < 0 else 0 for x in baseline_adjusted]

def evaluate_stability(seq):
    stable_count = 0
    for a, b in zip(seq, seq[1:]):
        if abs(a - b) <= 5:
            stable_count += 1
    return stable_count

# Misleading intermediate calculation
drift_analysis = sum([i * 0.1 for i in range(len(health_data))])

# Key function containing answer path
def process_metrics(data, config):
    # Step 1: Analyze raw trends
    raw_sum = sum(data)
    
    # Step 2: Count values within threshold bounds
    within_range = 0
    for val in data:
        if config['low'] <= val <= config['high']:
            within_range += 1
    
    # Step 3: Use enumerate to track qualifying indices
    qualified_indices = []
    for idx, val in enumerate(data):
        if val >= config['low']:
            qualified_indices.append(idx)
    
    # Step 4: Compute stability metric using zip
    stability_metric = evaluate_stability(data)
    
    # Step 5: Apply weighted combination
    weight_a = 3.1
    weight_b = 2.7
    partial_result = (raw_sum * 0.1) + (within_range * weight_a)
    
    # Step 6: Add stability contribution
    partial_result += stability_metric * weight_b
    
    # Step 7: Adjust based on qualified indices count
    index_influence = len(qualified_indices) * 1.5
    
    # Step 8: Final diagnostic score
    final_score = partial_result + index_influence - sum(positive_deviation)
    
    # Distractor: unused detailed breakdown
    details = {
        'raw': raw_sum,
        'qualified': qualified_indices,
        'deviations': positive_deviation,
        'stability': stability_metric
    }
    
    return int(final_score)  # Deterministic integer result

# Execute core logic
cumulative_metric, _ = analyze_readings(health_data)
final_diagnostic = process_metrics(health_data, thresholds)

# Print required output
print(f"Target result: {final_diagnostic}")