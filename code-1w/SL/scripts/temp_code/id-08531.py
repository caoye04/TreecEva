from collections import defaultdict
import math

# Simulate user feedback analysis with signal processing
raw_inputs = [0.85, 0.91, 0.76, 0.88, 0.93, 0.79, 0.84]
decay_factor = 0.93
smoothing_window = 3

# Irrelevant preprocessing: normalize inputs (not used in final logic)
normalized_inputs = [round((x - min(raw_inputs)) / (max(raw_inputs) - min(raw_inputs)), 4) for x in raw_inputs]

# Weighted moving average with decay (only partially relevant)
smoothed_signal = []
for i in range(len(raw_inputs)):
    window_start = max(0, i - smoothing_window + 1)
    weighted_sum = 0.0
    weight_sum = 0.0
    for j in range(window_start, i + 1):
        weight = decay_factor ** (i - j)
        weighted_sum += raw_inputs[j] * weight
        weight_sum += weight
    smoothed_signal.append(weighted_sum / weight_sum)

# Feedback categorization (semi-relevant)
categories = defaultdict(int)
for val in raw_inputs:
    if val >= 0.9:
        categories['excellent'] += 1
    elif val >= 0.8:
        categories['good'] += 1
    else:
        categories['fair'] += 1

# Misleading transformation: frequency analysis (unused)
frequency_map = {x: raw_inputs.count(x) for x in set(round(v, 2) for v in raw_inputs)}

# Core logic disguised among distractions
base_rating = 75
adjustment_factor = 1.25
penalty_rate = 0.08

# Simulated historical benchmark (distractor)
historical_avg = sum(smoothed_signal) / len(smoothed_signal)
variance_estimate = sum((x - historical_avg) ** 2 for x in smoothed_signal) / len(smoothed_signal)

# Actual performance aggregation begins here
def compute_consistency_score(values):
    diffs = [abs(values[i] - values[i-1]) for i in range(1, len(values))]
    return 10.0 - (sum(diffs) / len(diffs) * 10)  # Inverted difference score

consistency = compute_consistency_score(raw_inputs)

# Use lambda to filter significant feedback only
significant_threshold = lambda x: x >= 0.8
filtered_count = len(list(filter(significant_threshold, raw_inputs)))

# Build summary with redundant and relevant fields
feedback_summary = {
    'total_entries': len(raw_inputs),
    'high_performers': categories['excellent'],
    'consistency_metric': consistency,
    'filtered_volume': filtered_count,
    'baseline': base_rating,
    'temp_adjust': adjustment_factor  # Unused in final calculation
}

# Dead code path - never executed
if False:
    temp_result = math.log(sum(frequency_map.values()))
    feedback_summary['legacy_flag'] = int(temp_result)

# Key statement with actual answer computation
def aggregate_performance(summary, base):
    count_bonus = summary['filtered_volume'] * 3
    consistency_weight = summary['consistency_metric'] * 0.7
    excellence_multiplier = 1 + (summary['high_performers'] * 0.05)
    
    # Final score calculation
    raw_score = base + count_bonus + consistency_weight
    adjusted_score = raw_score * excellence_multiplier
    
    # Apply artificial cap
    capped_score = min(adjusted_score, 100)
    
    # Red herring: unused bitwise adjustment
    mask = 0b1111
    masked_correction = (int(capped_score) ^ 5) & mask  # Computed but not used
    
    return round(capped_score, 2)

# Execution point of interest
final_score = aggregate_performance(feedback_summary, base_rating)

# Print result as required
print(f"Result: {final_score}")