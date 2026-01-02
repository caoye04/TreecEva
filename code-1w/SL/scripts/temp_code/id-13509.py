def analyze_phase_stability(temp_seq, threshold=0.15):
    stability_log = []
    for i, (t1, t2) in enumerate(zip(temp_seq, temp_seq[1:])):
        diff = abs(t2 - t1)
        stable = diff < threshold
        stability_log.append(stable)
    return stability_log


def adjust_calibration(points):
    calibrated = []
    for i, point in enumerate(points):
        adjusted = point * (0.98 + i * 0.001)
        calibrated.append(adjusted)
    return sorted(calibrated)


def calculate_optimal_yield(efficiency_list, temp_variation):
    cumulative_factor = 1.0
    peak_influence = 0.0
    
    # Misleading loop - appears important but only minor effect
    for i, val in enumerate(temp_variation):
        if i % 2 == 0:
            peak_influence += val ** 0.5
        else:
            peak_influence -= val * 0.1

    # Real computation starts here
    base_yield = sum(efficiency_list) / len(efficiency_list)
    
    adjustment_tracker = []
    for i, eff in enumerate(efficiency_list):
        if i == 0:
            adjustment = eff * 1.1
        elif i == len(efficiency_list) - 1:
            adjustment = eff * 0.9
        else:
            adjustment = eff * (1.0 + 0.05 * (-1)**i)
        adjustment_tracker.append(adjustment)
    
    adjusted_sum = sum(adjustment_tracker)
    
    # Secondary red herring: complex-looking but weakly connected
    temp_score = 0
    for a, b in zip(adjustment_tracker, adjustment_tracker[1:]):
        temp_score += abs(a - b) * 0.01
    
    # Final yield calculation — depends only on base_yield and peak_influence
    final_component = base_yield * 100 + (peak_influence * 10)
    return int(final_component)

# Main execution
process_efficiency = [0.88, 0.92, 0.76, 0.85, 0.91]
temperature_fluctuations = [0.02, 0.08, 0.11, 0.04, 0.10]

# Distractor function calls
stability_results = analyze_phase_stability(temperature_fluctuations, threshold=0.15)
calibration_points = [1024, 2048, 512, 4096]
adjusted_calibration = adjust_calibration(calibration_points)

# Key statement
final_yield = calculate_optimal_yield(process_efficiency, temperature_fluctuations)

Result: {final_yield}