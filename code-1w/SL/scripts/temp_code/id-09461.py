def analyze_signal(data, window_size=5):
    smoothed = []
    for i in range(len(data) - window_size + 1):
        segment = data[i:i + window_size]
        avg = sum(segment) / window_size
        smoothed.append(avg)
    
    # Distractor: transform data in a way that isn't used later
    inverted = [1.0 / (x + 1e-5) for x in data]
    temp_sum = sum(inverted[:10]) if len(inverted) > 10 else sum(inverted)

    return smoothed


def calculate_efficiency(signal, limit):
    count_above = 0
    total = 0
    for val in signal:
        if val > limit:
            count_above += 1
        total += val

    # Semi-relevant computation: normalization factor not directly used
    norm_factor = max(signal) if signal else 1
    normalized_total = total / (norm_factor + 1e-8)

    efficiency = (count_above / len(signal)) * 100 if signal else 0
    return efficiency

# Main execution
raw_readings = [
    12.5, 14.2, 11.8, 13.7, 9.9, 10.1, 15.3, 16.2, 14.0, 13.8,
    12.9, 11.7, 10.5, 13.3, 14.6, 15.1, 13.9, 12.4, 11.3, 10.8
]

# Unnecessary preprocessing step (distractor)
denoised = [x for x in raw_readings if 10 <= x <= 16]
offset_correction = sum(x - 12 for x in denoised)
adjusted_readings = [x + 0.1 for x in raw_readings]  # Not used

# Signal processing pipeline
filtered_output = analyze_signal(raw_readings, window_size=4)

# Additional irrelevant transformation
sorted_segments = sorted(filtered_output[::2])  # Every other element sorted
auxiliary_stat = sum(sorted_segments) / len(sorted_segments)

threshold = 12.75
# Key statement
efficiency_score = calculate_efficiency(filtered_output, threshold)

# Final output
print(f"Result: {efficiency_score}")