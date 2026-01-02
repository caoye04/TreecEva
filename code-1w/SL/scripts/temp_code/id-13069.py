import math

# Simulate sensor data calibration and scoring in an environmental monitoring system
def collect_sensor_readings():
    raw_readings = [23.4, 19.8, 20.1, 25.3, 18.7, 21.0, 22.5]
    offsets = [0.2, -0.1, 0.05, -0.3, 0.15, -0.05, 0.1]
    calibrated = [raw_readings[i] + offsets[i] for i in range(len(raw_readings))]
    return calibrated

# Filter out readings below threshold using lambda
valid_range_filter = lambda x: 19.0 <= x <= 24.0

# Apply correction factors based on environmental conditions
def apply_correction(readings):
    corrected = []
    base_factor = 1.02
    for idx, val in enumerate(readings):
        if idx % 2 == 0:
            adjusted = val * base_factor
        else:
            adjusted = val * (base_factor - 0.01)
        corrected.append(round(adjusted, 2))
    
    # Distractor: Unused transformation
    squared_values = [x**2 for x in readings]
    mean_square = sum(squared_values) / len(squared_values)
    rms = math.sqrt(mean_square)
    
    return corrected

# Calculate quality score with weighted components
def compute_quality_component(values):
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    
    # Irrelevant computation (distractor)
    peak_to_peak = max(values) - min(values)
    normalized_pp = peak_to_peak / (avg + 1e-5)
    
    stability_score = 100 - (std_dev * 10)
    return round(stability_score, 2)

# Scoring logic with bitwise influence from system state
def calculate_final_score(data):
    base_score = compute_quality_component(data)
    
    # Simulated system health flags (bitwise encoded)
    system_flags = 0b1101  # e.g., diagnostics: 4 bits representing different statuses
    noise_flag = (system_flags & 0b0100) >> 2  # Extract third bit
    
    # Modify score based on flag (only one affects logic)
    adjustment = 0
    if system_flags & 0b1000:  # First bit set?
        adjustment += 5
    if system_flags & 0b0010:
        adjustment -= 2
    
    # Red herring: unused flag combination
    diagnostic_check = (system_flags & 0b1010) == 0b1010
    status_summary = bin(system_flags ^ 0b1111)  # Complement for logging
    
    final_score = base_score + adjustment
    
    # Additional irrelevant state tracking
    history_log = [{'entry': 'calibration', 'value': base_score},
                   {'entry': 'adjustment_applied', 'value': adjustment}]
    
    return round(final_score, 2)

# Main execution flow
def main():
    readings = collect_sensor_readings()
    filtered_readings = [r for r in readings if valid_range_filter(r)]
    processed_data = apply_correction(filtered_readings)
    
    # Distractor: unused alternative processing path
    alt_processed = [x for x in readings if x > 20.0]
    alt_avg = sum(alt_processed) / len(alt_processed) if alt_processed else 0
    
    final_score = calculate_final_score(processed_data)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()