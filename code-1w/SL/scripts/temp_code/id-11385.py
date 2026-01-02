from itertools import cycle

# Simulate sensor readings over time with noise and calibration offsets
def simulate_sensor_data(baseline, duration):
    return [baseline + (i % 7) - 3 for i in range(duration)]

def analyze_phase_shift(data_stream):
    shift_sum = 0
    for i, val in enumerate(data_stream):
        if i % 3 == 0:
            shift_sum += val % 4
        elif i % 5 == 0:
            shift_sum -= val % 2  # Minor correction, not critical
    return shift_sum

def compute_harmonic_load(profile):
    total = 0
    for x in profile:
        total += (x ** 2) >> 2  # Simulated power computation
    return total

def main():
    base_level = 18
    time_steps = 12
    
    # Generate raw sensor data
    raw_readings = simulate_sensor_data(base_level, time_steps)
    
    # Apply initial filtering (relevant)
    filtered_readings = [x for x in raw_readings if x > 12]
    
    # Compute intermediate metrics (some used, some not)
    avg_reading = sum(filtered_readings) / len(filtered_readings)
    reading_variance = sum((x - avg_reading) ** 2 for x in filtered_readings) / len(filtered_readings)
    
    # Distractor: Unused statistical moment
    skew_proxy = sum((x - avg_reading) ** 3 for x in filtered_readings) / len(filtered_readings)
    
    # Analyze phase behavior (used later)
    phase_offset = analyze_phase_shift(raw_readings)
    
    # Simulate load harmonics from filtered data
    harmonic_energy = compute_harmonic_load(filtered_readings)
    
    # Mapping of cycle patterns (semi-relevant, only length used)
    pattern_cycle = list(zip(cycle([1, 0]), filtered_readings))
    pattern_influence = len(pattern_cycle) * 0.5
    
    # Core output calculation (relevant)
    core_output = harmonic_energy / 10.0
    adjustment_factor = abs(phase_offset) * 0.3
    adjusted_core_output = core_output - adjustment_factor
    
    # Secondary correction based on pattern influence (distractor, not used in final)
    dummy_correction = pattern_influence * 0.7
    
    # Phase correction derived from original offset
    phase_correction = phase_offset // 2
    
    # Key statement: Final integration of flux
    final_flux = adjusted_core_output + phase_correction
    
    # Irrelevant string transformation (dead code path)
    status_flag = ''.join(chr(97 + (x % 26)) for x in raw_readings[:5])
    normalized_flag = status_flag.upper().swapcase()
    
    # Output target result
    print(f"Result: {final_flux}")

if __name__ == "__main__":
    main()