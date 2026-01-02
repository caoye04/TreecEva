def analyze_efficiency(levels):
    efficiency_scores = {}
    temp_accum = 0
    for idx, level in enumerate(levels):
        if level > 50:
            score = (level * 0.8) + 10
        else:
            score = level * 0.5
        efficiency_scores[idx] = round(score, 2)
        temp_accum += score  
    return efficiency_scores


def adjust_workload(data, threshold=45):
    adjusted = []
    dummy_sum = 0
    for val in data:
        dummy_sum += val * 0.1  
        if val < threshold:
            adjusted.append(val + 5)
        else:
            adjusted.append(val - 3)
    return adjusted


def simulate_phases(inputs):
    phase_results = []
    shift_log = []
    for i, val in enumerate(inputs):
        shifted = val * (i + 1)
        shift_log.append(shifted)
        if i % 2 == 0:
            phase_results.append(shifted * 0.9)
        else:
            phase_results.append(shifted * 1.1)
    total_phase = sum(phase_results)
    avg_shift = sum(shift_log) / len(shift_log)
    return phase_results, total_phase, avg_shift


def harvest_results(outputs):
    base_total = sum(outputs)
    bonus = 0
    for out in outputs:
        if out > 200:
            bonus += 15
    final_yield = base_total + bonus
    return final_yield

# Main execution
production_levels = [34, 67, 55, 41, 78, 60]
efficiency_map = analyze_efficiency(production_levels)
workload_data = [x * 2 for x in production_levels]
adjusted_load = adjust_workload(workload_data)
phases_input = [efficiency_map[i] * 2.5 for i in range(len(efficiency_map))]
phase_output, total_outputs, average_shift = simulate_phases(phases_input)
final_yield = harvest_results(total_outputs)
print(f"Target result: {final_yield}")