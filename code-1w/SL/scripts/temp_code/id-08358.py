import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_signal, noise_level, duration):
    samples = []
    for t in range(duration):
        noise = (t % 7) * noise_level / 10
        signal = base_signal * math.sin(t / 2) + noise
        samples.append(signal)
    return samples

# Irrelevant auxiliary function - dead code path
def deprecated_filter(data):
    filtered = [x for x in data if x > 0]
    scaling = sum(filtered) / len(filtered) if filtered else 0
    return [x * scaling for x in filtered]

# Signal transformation with red herring operations
def transform_signal(raw_samples, mode='standard'):
    shifted = [x + 2.5 for x in raw_samples]
    squared = [x**2 for x in shifted]
    normalized = [x / max(squared) for x in squared]
    
    # Distractor: complex but unused transformation branch
    if mode == 'enhanced':
        processed = []
        for val in normalized:
            temp = val * 1.5 if val > 0.5 else val * 0.8
n            temp = max(0.1, min(temp, 0.9))
            processed.append(round(temp, 3))
        return processed
    
    # Actual used transformation (simpler)
    compressed = [round(math.sqrt(x), 4) for x in normalized]
    return compressed

# Diagnostic pattern analyzer - core logic
def analyze_pattern(data, limit):
    count = 0
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Count rising edges above threshold
    for i in range(len(trend)):
        if i > 0 and trend[i] == 1 and trend[i-1] == -1:
            if data[i+1] > limit:  # Note: index offset intentional
                count += 1
    
    # Misleading intermediate calculation (unused)
    avg_trend = sum(trend) / len(trend) if trend else 0
    volatility = len([x for x in trend if x != 0]) / len(trend) if trend else 0
    
    # Final diagnostic score based on actual pattern
    score = 0
    sequence = 0
    for val in data:
        if val > limit:
            sequence += 1
            if sequence == 3:
                score += 2
        else:
            sequence = 0
    
    # Additional irrelevant stats
    peak = max(data) if data else 0
    percentile_90 = sorted(data)[int(0.9 * len(data))] if data else 0
    
    return score * 17 + int(peak * 10)

# Unused helper - decoy function
def compute_entropy(values):
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

# Main execution flow
if __name__ == '__main__':
    # Generate initial signal
    raw_data = collect_samples(base_signal=3.7, noise_level=1.4, duration=23)
    
    # Apply transformation
    transformed_data = transform_signal(raw_data, mode='standard')
    
    # Setup parameters
    threshold = 0.65
    safety_margin = 0.15  # unused parameter
    calibration_offset = sum(raw_data[:5]) / 5 if len(raw_data) >= 5 else 0
    
    # Dead code block - misleading control flow
    if len(transformed_data) > 50:
        refined = [x for x in transformed_data if x > 0.2]
        adjusted_refined = [x * 0.95 for x in refined]
    else:
        dummy_mark = [x * 0 for x in transformed_data]
        # This block does nothing consequential
        for idx in range(len(dummy_mark)):
            dummy_mark[idx] += calibration_offset * 0.01
    
    # Core computation - target intervention point
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Red herring: secondary analysis with no impact
    if final_diagnostic > 20:
        stability_index = 1
        for i in range(1, len(transformed_data)):
            if abs(transformed_data[i] - transformed_data[i-1]) < 0.05:
                stability_index += 0.2
    else:
        stability_index = -1 * final_diagnostic / 2
    
    # Output the required result
    print(f"Result: {final_diagnostic}")