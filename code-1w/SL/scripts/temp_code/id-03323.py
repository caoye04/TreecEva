def measure_stability(levels):
    normalize = lambda x: (x - min(levels)) / (max(levels) - min(levels)) if max(levels) != min(levels) else 0
    normalized = [normalize(level) for level in levels]
    avg_normalized = sum(normalized) / len(normalized)
    
    # Irrelevant diagnostic metric (distractor)
    peak_count = sum(1 for i in range(1, len(levels)-1) if levels[i-1] < levels[i] > levels[i+1])
    
    adjustment_factor = 0.85 if avg_normalized > 0.5 else 1.15
    energy_threshold = avg_normalized * adjustment_factor * 100
    
    return energy_threshold

# Sensor data simulation
time_intervals = [t for t in range(0, 10)]
base_signal = [t * 2 + 1 for t in time_intervals]
noise_component = [(t % 3) for t in time_intervals]
energy_levels = [base_signal[i] + noise_component[i] for i in range(len(time_intervals))]

# Secondary irrelevant calculation (minimal interference)
cumulative_energy = sum(energy_levels[:len(energy_levels)//2])

diagnostic_mode = True
final_diagnostic = measure_stability(energy_levels)
energy_threshold = final_diagnostic
print(f"Result: {energy_threshold}")