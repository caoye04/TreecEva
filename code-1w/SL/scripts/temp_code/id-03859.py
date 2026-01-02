import math

def analyze_pattern(sequence):
    magnitude = sum([x ** 2 for x in sequence])
    normalized = [x / (magnitude ** 0.5) for x in sequence]
    return normalized

def detect_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    outliers = [x for x in data if abs(x - mean_val) > threshold * std_dev]
    return outliers  # Not used in final result, distraction

def transform_signal(raw_signal):
    shifted = [(x * 2 + 1) % 256 for x in raw_signal]
    filtered = [x for x in shifted if x > 10]  # Remove low values
    reversed_signal = filtered[::-1]
    return reversed_signal

def calculate_adjusted_score(data_chunk):
    base_total = sum(data_chunk)
    penalty = 0
    
    # Apply diminishing returns for high values
    for val in data_chunk:
        if val > 50:
            penalty += int(math.log(val, 2))
    
    adjustment_factor = len(data_chunk) / (1 + penalty)
    score = base_total * adjustment_factor
    return int(score)

# Simulated sensor readings
raw_readings = [12, 45, 67, 23, 89, 34, 76, 55, 18, 91, 43]

# Irrelevant preprocessing step (distraction)
decoy_analysis = [math.sin(x / 10) for x in raw_readings]

# Normalize signal pattern
pattern_normalized = analyze_pattern(raw_readings)
scaled_normalized = [int(x * 100) for x in pattern_normalized]

# Transform signal with bit manipulation twist
processed_signal = transform_signal(scaled_normalized)

# Introduce redundant grouping
high_band = [x for x in processed_signal if x > 50]
low_band = [x for x in processed_signal if x <= 50]
combined_bands = high_band + low_band  # Same as original order?

# Add misleading statistical check
even_count = len([x for x in combined_bands if x % 2 == 0])
avg_value = sum(combined_bands) / len(combined_bands)
median_approx = sorted(combined_bands)[len(combined_bands)//2]

# Main processing pipeline
filtered_data = [x for x in combined_bands if x % 3 != 0]  # Filter by divisibility
expanded_data = [x for pair in zip(filtered_data, [x+1 for x in filtered_data]) for x in pair]  # Interleave
truncated_data = expanded_data[:len(expanded_data)//2 * 2]  # Ensure even length
reshaped_data = [(truncated_data[i], truncated_data[i+1]) for i in range(0, len(truncated_data), 2)]
flattened_data = [x ^ 15 for x, y in reshaped_data for x in (x, y) if y > 20]  # XOR and filter

# Final scoring logic
temp_buffer = [x for x in flattened_data if x < 100]
processed_data = [max(x - 5, 10) for x in temp_buffer]

# Key execution point
final_score = calculate_adjusted_score(processed_data)

print(f"Result: {final_score}")