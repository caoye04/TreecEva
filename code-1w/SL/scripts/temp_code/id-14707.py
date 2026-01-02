import math

def preprocess_signal(raw_signal):
    filtered = [x for x in raw_signal if x > -50 and x < 50]
    normalized = [(val + 50) / 100 for val in filtered]
    inverted = [1 - v for v in normalized][:len(normalized)//2]
    return inverted

# Irrelevant helper (dead function)
def compute_entropy(data):
    entropy = 0.0
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq[:n]

# Distractor data
tone_mapping = {'A': 440, 'B': 494, 'C': 523, 'D': 587, 'E': 659}
scale_factors = [math.sin(i * 0.1) for i in range(10)]
offset_tracker = {i: i * 0.5 for i in range(5)}

# Core transformation chain
def transform_readings(readings):
    shifted = [r * 1.5 + 2.0 for r in readings]
    squared_if_positive = [v**2 if v > 0 else v for v in shifted]
    sliced_window = squared_if_positive[::2][-8:]
    return [round(x, 2) for x in sliced_window]

# Recursive pattern analyzer (key logic)
def analyze_pattern(seq):
    if len(seq) <= 1:
        return seq[0] if seq else 0.0
    
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]
    
    # Heavily distractor-laden computation
    avg_left = sum(left) / len(left) if left else 0
    max_right = max(right) if right else 0
    deviance_score = abs(avg_left - max_right) * len(seq)
    
    # Real recursive work
    reduced_right = [x * 0.9 for x in right if x > avg_left]
    return analyze_pattern(left) + analyze_pattern(reduced_right)

# Simulate sensor array input
base_readings = generate_sequence(12)
sensor_noise = [(-1)**i * math.log(i + 2) for i in range(12)]
corrupted_input = [br + sn for i, (br, sn) in enumerate(zip(base_readings, sensor_noise))]

# Processing pipeline with distractions
filtered_diagnostic = preprocess_signal(corrupted_input)
dummy_histogram = [0]*10
for val in corrupted_input:
    bucket = int((val + 10) // 5)
    if 0 <= bucket < 10:
        dummy_histogram[bucket] += 1

transformed_data = transform_readings(filtered_diagnostic)

# Unused intermediate (distractor)
aggregated_profile = []
for i in range(len(transformed_data) - 1):
    diff = transformed_data[i+1] - transformed_data[i]
    category = 'up' if diff > 0.1 else 'down' if diff < -0.1 else 'stable'
    aggregated_profile.append(category)

# Key execution point
final_diagnostic = analyze_pattern(transformed_data)
print(f"Result: {final_diagnostic}")