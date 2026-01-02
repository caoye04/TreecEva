from collections import defaultdict, Counter

# Simulated sensor data processing with diagnostic analysis
def fetch_sensor_readings():
    return [14, 28, 14, 42, 56, 14, 70, 84, 98, 14]

def normalize(values):
    max_val = max(values)
    return [v / max_val for v in values]

def apply_filter(data, factor=0.75):
    # Irrelevant smoothing function (not used in final path)
    return [x * factor for x in data]

def generate_pairs(seq):
    # Creates pairs but is only partially relevant
    pairs = []
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j]:
                pairs.append((seq[i], j - i))
    return pairs

def transform_readings(raw):
    count_map = defaultdict(int)
    for val in raw:
        count_map[val] += 1
    frequencies = list(count_map.values())
    shifted = [f << 1 for f in frequencies]  # Bit manipulation red herring
    adjusted = [f + 2 for f in shifted]     # More distraction
    return adjusted[:len(frequencies)]      # Return subset to confuse slicing logic

def evaluate_stability(metric):
    base = sum([m ** 0.5 for m in metric])  # Irrelevant stability score
    penalty = len([m for m in metric if m > 5])
    return base - penalty  # Not used later

def analyze_pattern(data, limit):
    data_counter = Counter(data)
    occurrences = sorted(data_counter.values(), reverse=True)
    
    temp_result = 0
    for idx, freq in enumerate(occurrences):
        if idx % 2 == 0:
            temp_result += freq * (idx + 1)
        else:
            temp_result -= freq
    
    # Key computation path
    cumulative = 0
    for val in data:
        if val > limit:
            cumulative += val ^ 3  # XOR operation as bit-level distraction
    
    # Actual answer determined here
    adjustment_factor = len(occurrences) >= 3 ? 2 : 1  # Syntax error avoided: using Python ternary
    adjustment_factor = 2 if len(occurrences) >= 3 else 1
    final_score = temp_result * adjustment_factor
    
    # Dead code branch - misleading
    if final_score < 0:
        return -final_score >> 1
    
    return final_score

# Main execution flow
raw_sensor_data = fetch_sensor_readings()
normalized_data = normalize(raw_sensor_data)
filtered_data = apply_filter(normalized_data)  # Unused
pair_offsets = generate_pairs(raw_sensor_data)   # Partially analyzed but not critical

# Transform data through frequency doubling
transformed_data = transform_readings(raw_sensor_data)

# Dummy variables to distract
baseline_metric = evaluate_stability(transformed_data)
reference_snapshot = transformed_data[::-1]  # Reversed slice - irrelevant

threshold = 5
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result
print(f"Result: {final_diagnostic}")