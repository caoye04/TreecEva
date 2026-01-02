from itertools import combinations

def analyze_sensor_data(data_stream):
    # Irrelevant preprocessing: normalize values (not actually used in final result)
    normalized = [round((x - min(data_stream)) / (max(data_stream) - min(data_stream)) * 100) for x in data_stream]
    threshold = sum(normalized) / len(normalized) + 10

    # Real computation: extract peaks above dynamic threshold
    peaks = [val for i, val in enumerate(data_stream) if val > 75 and (i == 0 or data_stream[i-1] < val)]

    # Distractor: unused frequency analysis
    freq_count = {}
    for p in peaks:
        freq_count[p] = freq_count.get(p, 0) + 1
    
    return set(peaks)

# Simulated sensor readings from agricultural field
readings = [68, 76, 82, 79, 85, 88, 83, 90, 91, 87, 77, 74, 80]

def calculate_efficiency_indices(peaks):
    # Generate all 2-element combinations of peaks (unused distractor)
    comb_pairs = list(combinations(peaks, 2))
    total_energy = 0
    
    # Relevant calculation: sum of squared differences between consecutive peaks
    sorted_peaks = sorted(peaks)
    for i in range(1, len(sorted_peaks)):
        total_energy += (sorted_peaks[i] - sorted_peaks[i-1]) ** 2
    
    # Distractor: irrelevant averaging over pairs
    avg_pair_sum = sum(a + b for a, b in comb_pairs) / len(comb_pairs) if comb_pairs else 0
    
    # Efficiency derived from energy dispersion
    efficiency_score = int(total_energy // 10)
    return efficiency_score

# Unused helper that simulates alternative processing path
def predict_growth_trend(data):
    trend = 0
    for i, val in enumerate(data):
        trend += val * (0.9 ** i)  # exponential decay weighting
    return round(trend / len(data))

# Harvest function combines sensor data and efficiency

def harvest_results(raw_readings, rates):
    # Extract meaningful indices
    valid_peaks = analyze_sensor_data(raw_readings)
    base_efficiency = calculate_efficiency_indices(valid_peaks)
    
    # Secondary adjustment using rate map (some entries are red herrings)
    adjustment_map = {
        'A': 1.2, 'B': 0.8, 'C': 1.5, 'D': 0.5  # C and D are not used
    }
    
    # Only 'A' and 'B' contribute
    adjusted = base_efficiency * adjustment_map['A']
    if base_efficiency > 50:
        adjusted *= adjustment_map['B']
    
    # Final yield computed from adjusted efficiency
    final_yield = int(adjusted + len(valid_peaks) * 5)
    
    # Print intermediate diagnostics (irrelevant to result)
    diagnostics = {"count": len(valid_peaks), "energy": base_efficiency}
    
    return final_yield

# Efficiency rates placeholder (used in function signature but not directly)
efficiency_rates = {'sensor_A': 0.92, 'sensor_B': 0.88}

# Main execution flow
collected_data = readings
final_yield = harvest_results(collected_data, efficiency_rates)
print(f"Result: {final_yield}")