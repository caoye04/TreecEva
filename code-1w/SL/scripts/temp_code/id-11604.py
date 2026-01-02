def analyze_signal_data(raw_samples, threshold=0.75):
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = [x for x in normalized if x > threshold]
    
    # Irrelevant transformation - distractor
    inverted = [1 - x for x in normalized]
    temp_sum = sum(inverted)  # Dead computation

    segments = [normalized[i:i+3] for i in range(0, len(normalized), 3)]
    processed_segments = []
    
    for seg in segments:
        if len(seg) == 3:
            mid_val = seg[1]
            smoothed = (seg[0] + seg[2]) / 2
            if abs(mid_val - smoothed) < 0.2:
                processed_segments.append(smoothed * 10)
            else:
                # This block modifies a variable not used later
                dummy_entry = mid_val * 0.5
                processed_segments.append(dummy_entry * 2)
        else:
            processed_segments.extend([x * 0.1 for x in seg])

    # Redundant dictionary construction - distractor
    stats = {
        'count': len(raw_samples),
        'high_count': len([x for x in normalized if x > 0.9]),
        'average': sum(normalized) / len(normalized)
    }
    outlier_ratio = stats['high_count'] / stats['count']  # Not used

    baseline = 0.5
    adjustment = len(filtered) * 0.05
    efficiency_factor = baseline + adjustment

    # Key computational step
    filtration_yield = sum(processed_segments) * efficiency_factor

    # Additional unused variables - interference
    max_segment = max(processed_segments) if processed_segments else 0
    decay_rate = 0.98
    predicted_next = max_segment * decay_rate

    print(f"Result: {filtration_yield}")
    return filtration_yield

# Input data
input_data = [3.4, 6.1, 2.2, 7.8, 5.5, 1.0, 8.9, 4.3, 6.7, 2.5]
analyze_signal_data(input_data)