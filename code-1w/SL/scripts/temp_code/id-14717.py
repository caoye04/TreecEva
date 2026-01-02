import itertools

# Simulated sensor data processing pipeline for aerospace telemetry
def main():
    raw_readings = [0.88, 1.02, 0.95, 1.11, 0.76, 1.05, 0.83, 1.17]
    calibration_factor = 0.987
    offset_adjustment = 0.04

    # Irrelevant baseline metrics (distractor)
    baseline_avg = sum(raw_readings) / len(raw_readings)
    fluctuation_index = max(raw_readings) - min(raw_readings)
    reading_count = len(raw_readings)

    # Apply calibration (relevant)
    calibrated = [r * calibration_factor + offset_adjustment for r in raw_readings]

    # Generate synthetic timestamps (partly irrelevant)
    timestamps = [t for t in range(1000, 1000 + len(calibrated))]
    time_gaps = [b - a for a, b in zip(timestamps, timestamps[1:])]

    # Frame segmentation (relevant)
    frame_size = 4
    frames = [calibrated[i:i+frame_size] for i in range(0, len(calibrated), frame_size)]

    # Padding incomplete frames with dummy logic (mixed relevance)
    if len(frames[-1]) < frame_size:
        padding_value = calibrated[-1] * 0.9
        while len(frames[-1]) < frame_size:
            frames[-1].append(padding_value)

    # Decoy statistical analysis (irrelevant)
    variance_pool = []
    for f in frames:
        mean_f = sum(f) / len(f)
        var = sum((x - mean_f) ** 2 for x in f) / len(f)
        variance_pool.append(var)
    overall_variance = sum(variance_pool) / len(variance_pool)

    # Signal energy computation (misleading intermediate)
    signal_energy = sum(x**2 for x in calibrated)
    normalized_energy = signal_energy / len(calibrated)

    # Real processing begins: transform each frame using phase shift simulation
    processed_frames = []
    for idx, f in enumerate(frames):
        # Frequency modulation based on index (relevant)
        mod_factor = (idx + 1) * 0.1
        shifted = [v * (1 + mod_factor) if i % 2 == 0 else v * (1 - mod_factor) 
                   for i, v in enumerate(f)]
        
        # Apply windowing function (relevant)
        windowed = [shifted[i] * 0.5 * (1 - math.cos(2 * math.pi * i / (len(shifted) - 1))) 
                    for i in range(len(shifted))]
        
        # Compute frame power (used later)
        frame_power = sum(abs(x) for x in windowed)
        processed_frames.append((windowed, frame_power))

    # Dummy diagnostic chain (red herring)
    def legacy_diagnostic(powers):
        threshold = 3.0
        count_above = sum(1 for p in powers if p > threshold)
        return count_above * 1.5

    legacy_result = legacy_diagnostic([pwr for _, pwr in processed_frames])

    # Real analysis function (defined inside to obscure)
    def analyze_signal(frame_data_list):
        total_weight = 0.0
        cumulative_score = 0.0
        
        # Secondary decoy variables
        peak_magnitude = 0.0
        stability_ratio = 1.0
        entropy_proxy = 0.0
        
        for data, power in frame_data_list:
            # Extract alternating components
            even_part = [data[i] for i in range(0, len(data), 2)]
            odd_part = [data[i] for i in range(1, len(data), 2)]
            
            # Fake symmetry check (unused)
            symmetry_dev = abs(sum(even_part) - sum(odd_part))
            
            # Actual contribution: weighted accumulation
            weight = power ** 0.5
            total_weight += weight
            
            # Hidden logic: sum of cubes of first two elements
            cube_component = data[0]**3 + data[1]**3
            cumulative_score += weight * cube_component
            
            # Update fake metrics (distractors)
            if power > peak_magnitude:
                peak_magnitude = power
                stability_ratio = sum(data) / (max(data) - min(data) + 1e-8)
            entropy_proxy += math.log(power + 1)
        
        # Final result combines real and fake concepts, but only one matters
        final_value = cumulative_score / (total_weight + 1e-8)
        return final_value

    # Critical execution point
    final_diagnostic = analyze_signal(processed_frames)

    # More red herrings (dead code paths)
    def experimental_filter(signal):
        return [x for x in signal if x > 0.5]  # Never called
    
    debug_snapshot = {
        'frames': len(processed_frames),
        'energy': normalized_energy,
        'legacy': legacy_result
    }
    
    # Only this output matters
    print(f"Result: {final_diagnostic}")

# Unused helper (distractor)
def calculate_entropy(values):
    from collections import Counter
    counts = Counter(values)
    total = sum(counts.values())
    return -sum((cnt/total)*math.log2(cnt/total) for cnt in counts.values())

# Another decoy structure
task_registry = [
    ('process', True),
    ('validate', False),
    ('diagnose', True)
]

# Execute main logic
import math
main()