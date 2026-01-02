import math

def analyze_pattern(sequence):
    magnitude = sum([x ** 2 for x in sequence])
    norm = math.sqrt(magnitude) if magnitude > 0 else 1
    normalized = [round(x / norm, 4) for x in sequence]
    return normalized

def compute_entropy(values):
    total = 0
    for v in values:
        if v > 0:
            total -= v * math.log(v)
    return round(total, 4)

def process_metrics(data_str):
    raw_values = [float(x) for x in data_str.split(',')]
    filtered = [x for x in raw_values if 0 <= x <= 100]
    
    # Distractor: irrelevant transformation
    temp_buffer = ''.join([chr(int(x) % 97 + 33) for x in filtered if int(x) % 2 == 0])
    shadow_copy = [x * 1.5 for x in filtered]  # Not used later
    
    avg_val = sum(filtered) / len(filtered) if filtered else 0
    deviation = [abs(x - avg_val) for x in filtered]
    consistency = 100 - (sum(deviation) / len(deviation) if deviation else 0)
    
    # Conditional expression and slicing
    category_label = 'high' if consistency > 75 else 'low'
    sample_segment = filtered[:len(filtered)//2] if category_label == 'high' else filtered[len(filtered)//2:]
    
    # Use of string method
    tag = f"METRIC_{category_label.upper()}".replace('_', '-')
    
    # Key computation chain
    processed_norm = analyze_pattern(sample_segment)
    entropy = compute_entropy(processed_norm)
    weight_factor = 0.8 if len(filtered) > 5 else 1.2
    base_efficiency = (consistency * 0.6) + (entropy * 15)  # Scale entropy contribution
    
    # Final score with conditional adjustment
    adjustment = 10 if 'HIGH' in tag and avg_val > 50 else 0
    efficiency_score = base_efficiency * weight_factor + adjustment
    
    # Dead code path (distractor)
    if False:
        efficiency_score *= 0.9
        buffer_flush = [0] * len(shadow_copy)

    final_output = efficiency_score
    return final_output

# Simulated input
raw_data = "85.0,90.2,76.5,88.9,92.1,79.8,87.4,83.0"
efficiency_score = process_metrics(raw_data)
print(f"Target result: {efficiency_score}")