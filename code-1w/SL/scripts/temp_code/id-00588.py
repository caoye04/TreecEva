from itertools import cycle

# Simulate sensor data processing with noise filtering and metric extraction
def process_sensor_stream(raw_data, threshold):
    filtered = [x for x in raw_data if abs(x) > threshold]
    smoothed = [sum(filtered[i:i+3]) / len(filtered[i:i+3]) for i in range(len(filtered))]
    
    # Distractor: normalization not used in final path
    normalized = [x / (max(smoothed) + 1e-9) for x in smoothed] if smoothed else [0]
    
    peak_count = sum(1 for i in range(1, len(smoothed)-1) if smoothed[i] > smoothed[i-1] and smoothed[i] > smoothed[i+1])
    average = sum(smoothed) / len(smoothed) if smoothed else 0
    
    return average, peak_count, normalized

# Analyze temporal coherence using sliding window correlation
def compute_coherence(sequence):
    if len(sequence) < 4:
        return 0.0
    
    pairs = [(sequence[i], sequence[i+1]) for i in range(len(sequence)-1)]
    diffs = [abs(a - b) for a, b in pairs]
    
    # Irrelevant transformation
    squared_diffs = [d**2 for d in diffs]
    
    # Actual signal: trend stability
    stable_transitions = sum(1 for d in diffs if d < 1.5)
    return stable_transitions / len(diffs) if diffs else 0

# Core evaluation logic
def calculate_rating(convergence, metrics):
    base = metrics[0] * 0.6
    peaks = metrics[1] * 1.2
    adjustment = convergence * 100
    
    # Red herring calculation
    fake_dependency = (base ** 2 + peaks) % 7 if adjustment > 0 else 0
    
    rating = base + peaks + adjustment
    return int(rating)

# Main execution
if __name__ == '__main__':
    raw_input_stream = [0.1, -0.3, 2.4, 1.8, -5.2, 3.1, 2.9, 0.2, -1.1, 4.4, 3.3, 0.5]
    
    # Unused but plausible preprocessing
    shifted_data = [x + 0.5 for x in raw_input_stream]
    cyclic_pattern = cycle([1, -1, 0])
    perturbed = [x + next(cyclic_pattern) for x, _ in zip(shifted_data, range(len(shifted_data)))]
    
    # Key processing steps
    avg_val, peak_num, _ = process_sensor_stream(raw_input_stream, threshold=0.5)
    coherence = compute_coherence([raw_input_stream[i] * 2 for i in range(0, len(raw_input_stream), 2)])
    
    # Construct metrics tuple (average, peak_count)
    metrics_summary = (avg_val, peak_num)
    
    # Dummy state tracking (no effect)
    status_flags = {"active": True, "valid": False, "cached": None}
    if status_flags["active"]:
        status_flags["valid"] = len(raw_input_stream) > 5

    convergence = round(coherence, 2)
    
    # Critical statement
    final_score = calculate_rating(convergence, metrics_summary)
    
    print(f"Result: {final_score}")