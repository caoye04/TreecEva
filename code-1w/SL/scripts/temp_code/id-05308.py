from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring with noise filtering
def preprocess_data(raw_data):
    processed = []
    noise_count = 0
    for val in raw_data:
        if abs(val - sum(processed) / len(processed)) > 10 if processed else False:
            noise_count += 1
            continue  # Filter outliers
        processed.append(val)
    return processed

# Identify recurring patterns in cleaned data
def detect_cycles(seq):
    freq = defaultdict(int)
    for i in range(len(seq) - 2):
        triplet = tuple(seq[i:i+3])
        freq[triplet] += 1
    cycle_score = sum(1 for v in freq.values() if v > 1)
    return cycle_score

# Main scoring logic with distractors
def calculate_final_score(data, weights):
    temp_buffer = [0] * len(data)
    running_sum = 0
    
    for i in range(len(data)):
        temp_buffer[i] = data[i] * (i + 1)  # Irrelevant accumulation
        running_sum += data[i]
    
    avg_val = running_sum / len(data) if data else 0
    
    # Distractor: unused transformation
    transformed = [x ** 0.5 if x > 0 else 0 for x in temp_buffer]
    
    base_score = 0
    weight_sum = 0
    
    for j, w in enumerate(weights):
        if j % 2 == 0:
            base_score += data[j % len(data)] * w * 0.9  # Apply weight with decay
        else:
            base_score += data[j % len(data)] * w * 1.1
        weight_sum += w
    
    normalized_score = base_score / weight_sum if weight_sum else 0
    
    # Secondary adjustment based on cycle detection
    cycle_indicator = detect_cycles(data)
    adjustment_factor = (cycle_indicator * 0.5) if cycle_indicator > 2 else 1.2
    
    # Final computation
    final_score = int((normalized_score * adjustment_factor) + avg_val) % 97
    
    # Dead code path (never executed due to logic above)
    if len(data) > 1000:
        fallback = sum(transformed) // 100
        final_score = fallback

    return final_score

# Simulated input data
raw_sensor_data = [12, 15, 12, 18, 12, 15, 21, 12, 15, 18]
weights_list = [0.8, 1.2, 0.9, 1.1, 0.7]

# Preprocess data
filtered_data = preprocess_data(raw_sensor_data)

# Compute final score
final_score = calculate_final_score(filtered_data, weights_list)

print(f"Result: {final_score}")