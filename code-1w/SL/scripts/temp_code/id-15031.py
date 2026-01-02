from collections import defaultdict

# Simulate sensor data aggregation and weighted scoring
raw_readings = [12, 15, 12, 18, 14, 15, 12, 13, 18, 14]
weights = {'base': 0.3, 'trend': 0.5, 'stability': 0.2}

def preprocess_data(readings):
    # Misleading normalization step (not used in final calculation)
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)) * 10, 2) for x in readings]
    
    # Actual processing: count frequency of each reading
    freq_map = defaultdict(int)
    for val in readings:
        freq_map[val] += 1
    
    # Extract modes (most frequent values)
    max_freq = max(freq_map.values())
    modes = sorted([k for k, v in freq_map.items() if v == max_freq])
    
    # Calculate trend as difference between last and first
    trend_component = readings[-1] - readings[0]
    
    # Return structured data
    return {
        'modes': modes,
        'trend': trend_component,
        'values': readings,
        'size': len(readings)
    }

def calculate_stability_metric(data_slice):
    # Dummy stability function with red herring logic
    if len(data_slice) < 2:
        return 0.0
    variance = sum((x - sum(data_slice)/len(data_slice))**2 for x in data_slice) / len(data_slice)
    return round(100 / (1 + variance), 2) if variance > 0 else 100.0

def calculate_final_score(data, w):
    # Key computation steps
    base_value = sum(data['values']) / len(data['values'])  # mean
    
    # Red herring: unused complex structure
    summary_stats = {}
    for i, val in enumerate(data['values']):
        summary_stats[f'entry_{i}'] = {
            'value': val,
            'deviation': round(val - base_value, 2),
            'weight_class': 'high' if val > base_value else 'low'
        }
    
    # Another distraction: nested loop building irrelevant matrix
    correlation_proxy = 0
    for i in range(min(3, len(data['values']))):
        for j in range(min(3, len(data['values']))):
            if i != j:
                correlation_proxy += abs(data['values'][i] - data['values'][j])
    
    # Real components for scoring
    trend_score = abs(data['trend']) * w['trend']
    stability_score = calculate_stability_metric(data['values'][:5]) * w['stability'] / 10  # scaled down
    
    # Final deterministic score
    final = base_value * w['base'] + trend_score + stability_score
    
    # Dead code path - never executed but looks important
    if False:
        backup = sum(data['modes']) * 0.1
        final = max(final, backup)
    
    return round(final, 4)

# Main execution flow
processed_data = preprocess_data(raw_readings)
initial_baseline = processed_data['values'][0] * 2  # unused distraction
offset_correction = sum([i for i in range(processed_data['size']) if i % 2 == 0]) / 10  # irrelevant

# Critical statement
final_score = calculate_final_score(processed_data, weights)

# Print result
print(f"Result: {final_score}")