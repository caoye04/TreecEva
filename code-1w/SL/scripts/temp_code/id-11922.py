from itertools import combinations

def analyze_sensor_readings(readings):
    filtered = [r for r in readings if r > 25]
    paired = list(combinations(filtered, 2))
    avg_gap = sum(abs(a - b) for a, b in paired) / len(paired) if paired else 0
    
    # Distractor: irrelevant statistical computation
    variance_proxy = sum((r - 30) ** 2 for r in readings) / len(readings)
    _ = [variance_proxy * i for i in range(3)]  # Dead computation

    return avg_gap

def preprocess_batch(raw_samples):
    normalized = [x * 0.95 for x in raw_samples]
    offset_correction = 1.05
    corrected = [n + offset_correction for n in normalized]
    truncated = [int(val) for val in corrected]  # Some precision loss
    
    # Semi-relevant transformation
    scaled = [t * 1.1 for t in truncated]
    
    # Early filtering based on threshold
    if sum(scaled) < 100:
        return [0]
    
    return scaled

def calculate_optimal_yield(data_sequence):
    base_yield = 0
    peak_contributions = []

    for i, value in enumerate(data_sequence):
        if value > 30:
            base_yield += value * 0.1
            peak_contributions.append(value * 0.05)
        elif value > 20:
            base_yield += value * 0.05

    # Additional logic with conditional expression
    bonus = 10 if len(peak_contributions) > 2 else 5
    
    # Use of slicing to consider recent peaks only
    relevant_peaks = peak_contributions[-3:]
    extra_yield = sum(relevant_peaks) * 0.2
    
    total = base_yield + extra_yield + bonus
    
    # Red herring: complex but unused calculation
    shadow_factor = max(data_sequence) / min(data_sequence) if data_sequence else 1
    adjustment_chain = [shadow_factor / (i + 1) for i in range(5)]
    _ = sum(adjustment_chain)  # Computation has no effect

    return total

# Main execution flow
sensor_data = [22, 26, 31, 45, 28, 33, 19]
drift_compensated = [x - 2 for x in sensor_data]
processed_data = preprocess_batch(drift_compensated)

# Key analysis step
gap_metric = analyze_sensor_readings(processed_data)

# Critical statement
final_yield = calculate_optimal_yield(processed_data)

print(f"Result: {final_yield}")