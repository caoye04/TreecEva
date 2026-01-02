from collections import defaultdict

# Simulated sensor data analysis with noise filtering and performance scoring
def analyze_readings(raw_data, filter_threshold):
    filtered_data = []
    noise_count = 0
    cumulative_shift = 0

    for val in raw_data:
        shifted_val = (val ^ 255) & 127  # Bit-flip and mask to simulate correction
        if shifted_val > filter_threshold:
            filtered_data.append(shifted_val)
        else:
            noise_count += 1

    # Irrelevant statistics (distractor)
    avg_noise = noise_count / len(raw_data) if raw_data else 0
    temp_offset = sum(filtered_data) % 10 if filtered_data else 0

    return filtered_data, noise_count

def compute_entropy(values):
    if not values:
        return 0.0
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
    entropy = 0.0
    total = len(values)
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Simplified pseudo-entropy
    return round(entropy, 4)

def evaluate_performance(log, thresh):
    readings = [r['value'] for r in log if r['active']]
    
    # Dummy transformation chain (semi-relevant)
    processed, dropped = analyze_readings(readings, thresh)
    
    # Secondary filtering based on parity (adds complexity)
    even_stream = [v for v in processed if v % 2 == 0]
    odd_stream = [v for v in processed if v % 2 == 1]
    
    # Compute derived metrics (only one used later)
    even_sum = sum(even_stream)
    odd_product = 1
    for x in odd_stream:
        odd_product *= (x % 9) + 1  # Avoid zero explosion
    
    # Red herring computation
    compression_ratio = len(processed) / len(readings) if readings else 0
    
    # Core logic: score based on weighted components
    base_score = len(processed) * 3
    entropy_bonus = int(compute_entropy(processed) * 100)
    balance_penalty = abs(len(even_stream) - len(odd_stream)) * 2
    
    # Final interference: unused intermediate
    debug_snapshot = {
        'even_sum': even_sum,
        'odd_product': odd_product,
        'compression': compression_ratio
    }
    
    final_score = base_score + entropy_bonus - balance_penalty
    return final_score

# Setup input data
data_log = [
    {'value': 67, 'active': True},
    {'value': 130, 'active': False},  # Inactive, should be skipped
    {'value': 45, 'active': True},
    {'value': 200, 'active': True},
    {'value': 73, 'active': True},
    {'value': 180, 'active': True},
    {'value': 30, 'active': True},
    {'value': 95, 'active': True}
]
threshold = 60

# Execute main logic
final_score = evaluate_performance(data_log, threshold)
print(f"Result: {final_score}")