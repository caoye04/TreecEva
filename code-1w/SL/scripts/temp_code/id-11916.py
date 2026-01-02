import math

def process_metrics(stream):
    raw_values = [x for x in stream if x > 0]
    temp_buffer = [math.log(v) for v in raw_values if v > 1]
    
    # Irrelevant tracking (distractor)
    peak_magnitude = max(raw_values, default=0)
    normalization_factor = math.sqrt(sum(v**2 for v in raw_values)) or 1
    scaled_data = [v / normalization_factor for v in raw_values]

    # Semi-relevant transformation
    adjusted_values = []
    for i, val in enumerate(raw_values):
        if i % 2 == 0:
            adjusted_values.append(val * 0.9)
        else:
            adjusted_values.append(val * 1.1)

    # Core logic begins here
    cumulative_weight = 0.0
    efficiency_score = 0
    
    for idx, (orig, adj) in enumerate(zip(raw_values, adjusted_values)):
        delta = abs(adj - orig)
        contribution = delta * (idx + 1)
        cumulative_weight += contribution
        
        if idx > 0 and idx % 3 == 0:
            efficiency_score += int(cumulative_weight)
            cumulative_weight = 0  # Reset for next phase

    # Final update outside loop
    efficiency_score += int(cumulative_weight)
    
    # Dead code path (distractor)
    if len(temp_buffer) > 100:
        efficiency_score *= 2

    final_output = efficiency_score
    return final_output

# Simulated data input
data_stream = [5, -2, 8, 0, 12, 15, -7, 4, 6, 9, 3]
result = process_metrics(data_stream)
print(f"Result: {result}")