from collections import defaultdict, Counter

# Simulate sensor data processing with noise filtering and performance scoring
def analyze_sensor_readings(raw_data, threshold=50):
    filtered_data = []
    noise_count = 0
    cumulative_shift = 0

    for val in raw_data:
        if isinstance(val, str):
            cleaned = val.strip().lower()
            if 'err' in cleaned:
                noise_count += 1
                continue
            digits = ''.join(filter(str.isdigit, cleaned))
            if digits:
                val = int(digits)
            else:
                noise_count += 1
                continue

        if val < 10 or val > 99:
            noise_count += 1
            shifted_val = (val % 90) + 10
            cumulative_shift += abs(val - shifted_val)
        else:
            filtered_data.append(val)

    # Misleading intermediate calculation
    average_noise_impact = cumulative_shift / (noise_count + 1) * 1.5 if noise_count > 0 else 0
    
    return filtered_data, average_noise_impact, noise_count

def normalize_readings(data_list):
    if not data_list:
        return [0]
    min_val, max_val = min(data_list), max(data_list)
    range_val = max_val - min_val or 1
    normalized = [(x - min_val) / range_val for x in data_list]
    return normalized

def calculate_stability_metric(norm_vals):
    variance_proxy = sum((norm_vals[i] - norm_vals[i-1])**2 for i in range(1, len(norm_vals)))
    stability = 1 / (1 + variance_proxy)
    return stability

def calculate_performance(base, readings):
    # Core logic embedded within distractions
    processed, impact, noise = analyze_sensor_readings(readings)
    
    # Distractor: complex but unused structure
    stats_summary = defaultdict(lambda: {'count': 0, 'flagged': False})
    for v in readings:
        key = str(v)[0] if isinstance(v, (int, str)) and str(v).isdigit() else 'X'
        stats_summary[key]['count'] += 1
    
    # Another distractor: character frequency analysis on numbers
    digit_counter = Counter(''.join(str(x) for x in readings if str(x).isdigit()))
    dominant_digit = int(digit_counter.most_common(1)[0][0])

    normalized = normalize_readings(processed)
    stability = calculate_stability_metric(normalized)
    
    # Real computation path
    base_modifier = base * 0.8 if len(processed) < 5 else base * 1.1
    adjustment_factor = stability * (0.9 + (dominant_digit % 3) * 0.1)
    
    # Final score depends only on specific chain
    preliminary = sum(normalized) * base_modifier
    final_score = int(preliminary * adjustment_factor + 5)  # Final deterministic integer
    
    # Dead code - never used
    if noise > 10:
        final_score -= 20
    elif impact > 100:
        final_score += 10
        
    return final_score

# Input data with mixed types and embedded noise
dataset = [55, ' 78 ', 'err_sensor', 44, 67, '92x', 'abc', 33, 81, 55, '77']
baseline = 15

# Key execution point
final_score = calculate_performance(baseline, dataset)
print(f"Result: {final_score}")