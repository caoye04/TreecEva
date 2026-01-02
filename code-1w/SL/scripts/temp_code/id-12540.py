def analyze_sequence(data):
    """Irrelevant helper function for distraction."""
    return [x ** 2 for x in data if x % 3 == 0]


def preprocess_inputs(raw):
    """Another decoy function that is never called."""
    cleaned = raw.strip().lower().replace(' ', '_')
    parts = cleaned.split(',')
    return [p for p in parts if len(p) > 2]

# Unused constants (distractors)
MAX_THRESHOLD = 98765
DEFAULT_PADDING = [0] * 10
TEMPORAL_FACTOR = 3.14159

# Simulated sensor metrics with mixed types (some relevant, some not)
sensor_logs = [
    {'id': 'S1', 'readings': [12, 15, 22, 8], 'active': True},
    {'id': 'S2', 'readings': [9, 11, 10], 'active': False},
    {'id': 'S3', 'readings': [18, 24, 20, 25, 19], 'active': True}
]

# Baseline calibration values (partially relevant)
baseline = {
    'offset': 10,
    'gain': 1.5,
    'noise_floor': 7,
    'history': [14, 16, 15, 13]
}

# Raw string input (unused but looks important)
raw_config = "mode: debug, buffer: 512, retries: 3"

# Main metric computation chain
metrics = {}

# Step 1: Aggregate active sensor readings
all_values = []
for log in sensor_logs:
    if log['active']:
        all_values.extend(log['readings'])

# Step 2: Compute primary statistics (used later)
mean_val = sum(all_values) / len(all_values)
variance = sum((x - mean_val) ** 2 for x in all_values) / len(all_values)
std_dev = variance ** 0.5

# Step 3: Apply transformation using modular arithmetic and bit shifts
transformed = []
for i, v in enumerate(all_values):
    shifted = (v << 1) & 63  # Bitwise shift and mask
    adjusted = (shifted + i) % 23
    transformed.append(adjusted)

# Step 4: Count frequency groups (list comprehension with filtering)
frequency_bins = {k: len([t for t in transformed if t % 5 == k]) for k in range(5)}

dominant_group = max(frequency_bins, key=lambda x: frequency_bins[x])

# Step 5: Generate checksum from stringified pattern (string method usage)
pattern_str = ''.join(str(frequency_bins[i]) for i in sorted(frequency_bins))
checksum = sum(ord(c) - ord('0') for c in pattern_str) ^ 255  # XOR with mask

# Step 6: Compute correlation between two derived sequences (set operations)
unique_t = set(transformed)
unique_a = set(all_values)
symmetric_diff_score = len(unique_t ^ unique_a)
common_elements = len(unique_t & unique_a)

# Step 7: Normalize and weight components into performance vector
weights = [0.3, 0.2, 0.25, 0.15, 0.1]
components = [
    mean_val / baseline['offset'],
    std_dev,
    dominant_group * 2.5,
    checksum / 10.0,
    common_elements
]

performance_vector = [w * c for w, c in zip(weights, components)]

# Step 8: Final evaluation function
def evaluate_performance(perf_metrics, base):
    score = sum(perf_metrics)
    
    # Red herring conditional (never affects result due to prior logic)
    if len(base['history']) < 5:
        penalty = 10
    else:
        penalty = 0  # Neutral effect
    
    # Additional irrelevant transformation
    temp_result = [x * TEMPORAL_FACTOR for x in perf_metrics[:3]]
    
    # Critical adjustment using modular arithmetic
    adjustment = (len(perf_metrics) * 100) % 89
    
    # Final score computation (this is the actual answer point)
    final_score = score + adjustment - penalty
    
    return final_score

# Execute main logic
evaluated = [x for x in all_values if x > mean_val]  # unused list comp
dropped = set(all_values) - set(evaluated)  # unused set op

final_score = evaluate_performance(performance_vector, baseline)

# Output result
print(f"Result: {final_score}")