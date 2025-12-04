import itertools

def process_noise_levels(readings):
    # This simulates noise filtering but actually doesn't affect our result
    processed = []
    for r in readings:
        # Apply complex but irrelevant transformations
        noise_factor = (r % 7) * 0.15
        adjusted = r + noise_factor if r > 20 else r - noise_factor
        processed.append(round(adjusted, 2))
    return processed

def calculate_signal_metrics(data):
    # Calculate various metrics that seem important
    metrics = {
        'peak': max(data) if data else 0,
        'minimum': min(data) if data else 0,
        'fluctuation': max(data) - min(data) if data else 0,
        'avg_high': sum([x for x in data if x > 15]) / len([x for x in data if x > 15]) if any(x > 15 for x in data) else 0
    }
    # This looks important but the result isn't used in final calculation
    harmonics = [x * 1.5 for x in data if x % 2 == 0]
    metrics['harmonic_avg'] = sum(harmonics) / len(harmonics) if harmonics else 0
    return metrics

def extract_signal_pattern(values):
    # This function appears to extract important patterns but result isn't critical
    pattern_sum = 0
    for i, v in enumerate(values):
        if i % 3 == 0 and v > 10:
            pattern_sum += v * 0.1
        elif i % 2 == 0:
            pattern_sum -= v * 0.05
    return pattern_sum

def calculate_final_strength(readings):
    # The key calculation happens here
    if not readings:
        return 0
        
    # Get every third reading (this is what actually matters)
    key_readings = readings[::3]
    
    # Apply a slice operation to get a subset (this is important)
    critical_segment = key_readings[1:4]
    
    # This appears important but is a distraction
    all_permutations = list(itertools.permutations(critical_segment))
    permutation_products = [p[0] * p[-1] for p in all_permutations]
    
    # Calculate frequency bands (distraction)
    bands = {'low': [], 'mid': [], 'high': []}
    for r in readings:
        if r < 10:
            bands['low'].append(r)
        elif r < 20:
            bands['mid'].append(r)
        else:
            bands['high'].append(r)
    
    # The actual calculation that matters
    base_value = sum(critical_segment)
    multiplier = len([r for r in key_readings if r > 12])
    
    # More distraction calculations
    signal_variance = sum((r - sum(readings)/len(readings))**2 for r in readings) / len(readings)
    normalized_readings = [r / max(readings) for r in readings]
    
    # Final calculation - only base_value and multiplier matter
    return base_value * multiplier

# Main signal processing pipeline
sensor_readings = [15, 7, 22, 9, 14, 18, 5, 11, 23, 16]

# Process the raw readings (distraction)
processed_readings = process_noise_levels(sensor_readings)

# Calculate metrics that seem important (distraction)
metrics = calculate_signal_metrics(sensor_readings)

# This looks important but isn't used for final answer
signal_pattern = extract_signal_pattern(sensor_readings)
pattern_strength = signal_pattern * metrics['peak'] / metrics['minimum'] if metrics['minimum'] != 0 else 0

# Apply filters that look important but are distractions
filtered_readings = [r for r in sensor_readings if 5 <= r <= 25]

# This looks like it would change filtered_readings but it creates a new list
strong_signals = [r for r in filtered_readings if r >= metrics['peak'] * 0.7]

# The critical line that determines our answer
signal_strength = calculate_final_strength(filtered_readings)

# More calculations to distract
average_strength = sum(filtered_readings) / len(filtered_readings)
strength_ratio = signal_strength / average_strength if average_strength != 0 else 0

# Misleading final calculation
final_output = (signal_strength + pattern_strength) / 2 if pattern_strength != 0 else signal_strength

print(f"Result: {signal_strength}")