from collections import defaultdict

# Simulate sensor array readings over time with noise filtering
def analyze_sensor_efficiency(readings):
    raw_data = [r for r in readings if r > 0]
    filtered = [x for x in raw_data if x < 1000]
    
    # Misleading intermediate transformation (not used in final result)
    normalized = [round((x - min(filtered)) / (max(filtered) - min(filtered)) * 100) for x in filtered]
    
    # Group efficiency by magnitude bands (distractor computation)
    bands = defaultdict(int)
    for val in filtered:
        band_key = val // 50
        bands[band_key] += 1
    
    # Compute rolling three-point efficiency (semi-relevant but not final)
    temp_efficiency = []
    for i in range(2, len(filtered)):
        window_avg = (filtered[i-2] + filtered[i-1] + filtered[i]) / 3
        efficiency_score = (window_avg / (i + 1)) * 1.5
        temp_efficiency.append(efficiency_score)
    
    # Core logic: actual efficiency derived from even-indexed high-magnitude signals
    significant_indices = [i for i in range(len(filtered)) if filtered[i] > 75 and i % 2 == 0]
    base_values = [filtered[i] for i in significant_indices]
    
    # Apply decay factor over positional index (relevant)
    efficiencies = []
    for idx, val in enumerate(base_values):
        decayed = val * (0.9 ** idx)
        if decayed > 40:  # threshold filter
            efficiencies.append(decayed)
    
    # Add dummy filler values to obscure intent
    filler = [12.5, 8.3, 6.1]
    extended = efficiencies + filler
    
    # Key statement: extract peak from true efficiency chain
    peak_efficiency = max(efficiencies)
    
    # Print final target result
    print(f"Result: {peak_efficiency}")
    return peak_efficiency

# Input data: synthetic sensor stream
sensor_readings = [85, -5, 102, 203, 801, 45, 96, 700, 305, 880, 150, 77]
analyze_sensor_efficiency(sensor_readings)