def analyze_signal(data, threshold=0.5):
    filtered = [x for x in data if abs(x) > threshold]
    return [abs(x) ** 0.5 for x in filtered]


def normalize_readings(readings):
    max_val = max(readings)
    return [r / max_val for r in readings]


def transform_coordinates(coords):
    # Irrelevant transformation (decoy function)
    return [(c[0] * 2 + 1, c[1] * 3 - 1) for c in coords]


def simulate_buffer_overflow():
    # Dead-end simulation with no impact
    buffer = [0] * 256
    for i in range(len(buffer)):
        buffer[i] = (i * 17) % 251
    return sum(buffer) // 100  # Misleading scalar


def decode_frequency_pattern(signal):
    # Complex but ultimately unused decoding logic
    base = sum(signal) / len(signal)
    deviations = [abs(s - base) for s in signal]
    adjusted = [d * (1 + (i % 3)) for i, d in enumerate(deviations)]
    return [a for a in adjusted if a > 1.0]


def calculate_thermal_output(fluctuations):
    # Core calculation chain
    raw_energy = sum([f ** 2 for f in fluctuations])
    entropy_factor = len([f for f in fluctuations if f < 0])
    correction_shift = 1 + (entropy_factor / len(fluctuations))
    
    # Apply decay envelope
    envelope = [raw_energy * (0.95 ** i) for i in range(5)]
    effective_energy = sum(envelope) / 5
    
    # Secondary modulation via bit manipulation
    modulated = int(effective_energy) ^ 0xFF  # XOR with 255
    modulated = modulated & 0xFFFF  # Clamp to 16-bit
    
    # Tertiary adjustment using slicing and string conversion (red herring layer)
    bin_str = bin(modulated)[2:]
    truncated_bin = bin_str[-8:]  # Take last 8 bits
    parsed_value = int(truncated_bin, 2)
    
    # Final scaling using average of normalized fluctuations
    normalized = [abs(f) / (sum(abs(x) for x in fluctuations)) for f in fluctuations]
    avg_norm = sum(normalized) / len(normalized)
    thermal_capacity = parsed_value * (avg_norm * 100)
    
    return thermal_capacity

# Main execution flow
if __name__ == '__main__':
    # Sensor input data (real signal)
    energy_fluctuations = [-0.3, 0.7, -1.2, 0.9, -0.8, 1.1, -0.4]
    
    # Irrelevant setup - distractors
    coordinates = [(1, 2), (3, 4), (5, 6)]
    transformed_coords = transform_coordinates(coordinates)
    
    # Noise analysis (dead path)
    noise_profile = [0.1, 0.05, 0.2, 0.15, 0.1]
    analyzed_noise = analyze_signal(noise_profile, threshold=0.12)
    
    # Normalization of unrelated sensor array
    sensor_readings = [100, 230, 180, 95, 210]
    normalized_readings = normalize_readings(sensor_readings)
    
    # Unused frequency analysis
    frequencies = [440.0, 880.0, 660.0, 220.0]
    pattern_analysis = decode_frequency_pattern(frequencies)
    
    # Buffer simulation result (misleading intermediate)
    overflow_metric = simulate_buffer_overflow()
    
    # Key computation
    thermal_capacity = calculate_thermal_output(energy_fluctuations)
    
    # Output target result
    print(f"Result: {thermal_capacity}")