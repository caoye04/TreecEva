import math

# Simulated sensor data processing pipeline with diagnostic analysis
def collect_readings():
    raw_samples = [127, 255, 193, 64, 222, 142, 88, 201, 73, 158]
    scaling_factor = 0.75
    adjusted = [int(x * scaling_factor) for x in raw_samples]
    return adjusted

# Irrelevant transformation: color space analogy (distractor)
def rgb_to_grayscale(pixels):
    return [int(0.299 * p + 0.587 * p + 0.114 * p) for p in pixels]  # No effect on logic

# Data filtering based on dynamic thresholds
def filter_outliers(data, low_bound=70, high_bound=200):
    return [x for x in data if low_bound <= x <= high_bound]

# Secondary irrelevant function: network packet simulation (dead path)
def simulate_packet_size(n):
    base = 64
    increment = (n * 17) % 93
    return base + increment

# Core analysis function with set operations and arithmetic accumulation
def analyze_readings(readings, exception_set):
    cumulative_score = 0
    temp_flags = set()
    
    for val in readings:
        if val in exception_set:
            temp_flags.add(val)
            continue
        
        # Bit manipulation chain
        shifted = (val >> 2) & 0b1111
        inverted = ((~val) & 0xFF) ^ 0b101010
        
        # Arithmetic transformations
        log_component = math.log(val + 1) if val > 0 else 0
        squared_norm = (val ** 2) / 1000.0
        
        # Accumulation with rounding and integer division
        step1 = int(squared_norm // 1) + int(log_component)
        step2 = step1 * (shifted % 4 + 1)
        
        # Conditional branching with red herring
        if step2 > 50:
            adjustment = simulate_packet_size(step2)  # Dead-end call
            step2 = 50  # Hard cap
        
        cumulative_score += step2

        # Fake entropy calculation (unused)
        entropy = 0
        for bit in range(8):
            if (val >> bit) & 1:
                entropy -= 0.5 * math.log(0.5)

    # Set-based correction factor
    missing_refs = {100, 120, 140, 160}.difference(exception_set)
    correction = len(missing_refs) * 3
    
    # Final computation
    final_score = cumulative_score - correction
    
    # Key diagnostic output
    final_diagnostic = abs(final_score - 88) * -1  # Inversion to negative scale
    
    # Unused telemetry (distraction)
    telemetry_snapshot = {
        'peak': max(readings, default=0),
        'samples': len(readings),
        'anomalies': len(temp_flags)
    }
    
    return final_diagnostic

# Orchestration sequence
if __name__ == '__main__':
    # Initial data collection
    all_readings = collect_readings()  # [95, 191, 144, 48, 166, 106, 66, 150, 54, 118]
    
    # Apply filter (removes values <70 or >200)
    filtered_data = filter_outliers(all_readings)  # [95, 191, 144, 166, 106, 66, 150, 118]
    
    # Irrelevant grayscale conversion (no side effects)
    _ = rgb_to_grayscale(all_readings)
    
    # Define exception set using set operations
    critical_values = {191, 144}
    calibration_points = {106, 118, 130}
    threshold_set = critical_values.union(calibration_points).intersection(range(50, 200))
    
    # Execute main analysis
    final_diagnostic = analyze_readings(filtered_data, threshold_set)
    
    # Output result
    print(f"Result: {final_diagnostic}")