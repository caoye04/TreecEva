import math

def analyze_signal(samples):
    filtered = [x for x in samples if abs(x) > 0.5]
    squared = [x * x for x in filtered]
    return sum(squared) / len(squared) if squared else 0.0

def detect_spikes(values, threshold=3.0):
    moving_avg = sum(values[:len(values)//2]) / (len(values)//2 or 1)
    spikes = [v for v in values if v > moving_avg * threshold]
    normalization_factor = max(spikes) if spikes else 1.0
    return [s / normalization_factor for s in spikes]

def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def transform_sequence(seq):
    rev = seq[::-1]
    shifted = [rev[i] ^ rev[(i+1)%len(rev)] for i in range(len(rev))] if rev else []
    return [s + 2 for s in shifted]

def aggregate_metrics(trends, importance_weights):
    base_score = 0
    for i, trend in enumerate(trends):
        if i % 2 == 0:
            base_score += trend * importance_weights.get('even', 1.2)
        else:
            base_score += trend ** 1.1 * importance_weights.get('odd', 0.8)
    adjustment = math.sin(len(trends)) * 0.5
    final_score = base_score + adjustment
    return int(round(final_score))

def main():
    # Real input data
    sensor_readings = [0.3, 1.2, -0.9, 2.1, 3.3, -1.4, 0.8, 2.7]
    
    # Irrelevant preprocessing chain 1
    processed_a = analyze_signal(sensor_readings)
    temp_result_x = processed_a * 1.7
    
    # Irrelevant preprocessing chain 2
    spike_list = detect_spikes(sensor_readings)
    normalized_spikes = [sp * 0.9 for sp in spike_list]
    temp_result_y = sum(normalized_spikes)
    
    # Irrelevant transformation
    binary_rep = [int(abs(x) > 1) for x in sensor_readings]
    flipped_bits = [1 - b for b in binary_rep]
    entropy_value = compute_entropy(flipped_bits)
    
    # Another decoy path: bit manipulation on index positions
    indices = list(range(len(sensor_readings)))
    xor_fold = 0
    for idx in indices:
        xor_fold ^= (idx + 1) << 1
    masked = xor_fold & 0xFF
    dummy_metric = math.log(masked + 1) if masked else 0
    
    # Distractor: unused function call with side effect that does nothing
    transformed_seq = transform_sequence(indices)
    secondary_adjust = sum(transformed_seq) / (len(transformed_seq) or 1)
    
    # Core relevant data generation
    trend_data = [
        sensor_readings[1] + sensor_readings[2],
        sensor_readings[3] - sensor_readings[0],
        abs(sensor_readings[5]),
        sensor_readings[7] * 0.5,
        sum(sensor_readings[2:5])
    ]
    
    # Weight configuration (some keys are red herrings)
    weights = {
        'even': 1.5,
        'odd': 0.7,
        'baseline': 100,  # unused
        'offset': dummy_metric,  # irrelevant
        'scale': secondary_adjust  # not used in calculation
    }
    
    # Key computation
    intermediate_offset = math.cos(math.pi / 4) * 2
    adjusted_trends = [t + intermediate_offset for t in trend_data]
    
    # Final diagnostic depends only on aggregate_metrics
    final_diagnostic = aggregate_metrics(adjusted_trends, weights)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main()