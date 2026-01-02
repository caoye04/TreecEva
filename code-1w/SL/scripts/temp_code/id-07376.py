def analyze_conditions(temp_seq, press_seq):
    # Irrelevant transformation (distractor)
    normalized = [round((t - 20) * 1.8 + 32, 2) for t in temp_seq]  # to Fahrenheit

    temp_pressure_map = {}
    for i, (t, p) in enumerate(zip(temp_seq, press_seq)):
        adjusted_p = p * (1 + (t - 25) / 100)
        temp_pressure_map[t] = adjusted_p

    return temp_pressure_map


def calculate_stability_index(data_dict):
    values = list(data_dict.values())
    avg = sum(values) / len(values)
    variance = sum((x - avg) ** 2 for x in values) / len(values)
    stability = 100 / (1 + variance) if variance != 0 else 100
    
    # Dead computation: not used later (distractor)
    outlier_count = sum(1 for v in values if abs(v - avg) > 2 * variance**0.5)
    
    return stability


def calculate_optimal_yield(temps, press_adj):
    # Main relevant logic
    readings = []
    for t, p in zip(temps, press_adj):
        if t < 0 or p < 0.5:
            continue  # early filter
        efficiency = t * p / (t + 50)
        readings.append(efficiency)
    
    if not readings:
        return 0
    
    # Key result calculation
    base_yield = sum(readings) * 0.75
    
    # Distractor: complex but unused structure
    status_flags = {i: ('high' if r > 10 else 'low') for i, r in enumerate(readings)}
    flag_set = set(status_flags.values())
    
    # Secondary adjustment based on average temperature
    avg_temp = sum(temps) / len(temps)
    modifier = 1 + (avg_temp - 25) / 100
    final_yield = base_yield * modifier
    
    # Additional irrelevant tracking (distractor)
    log_entries = []
    for idx, val in enumerate(readings):
        log_entries.append(f"Step {idx}: {val:.3f}")
    
    return round(final_yield, 4)

# Input data
temperature_data = [30, 35, 40, 25, 20, 50]
pressure_adj = [0.8, 0.85, 0.9, 0.75, 0.7, 0.95]

# Auxiliary call with side distraction
mapping = analyze_conditions(temperature_data, pressure_adj)
stability_score = calculate_stability_index(mapping)

# Critical execution point
final_yield = calculate_optimal_yield(temperature_data, pressure_adj)

print(f"Result: {final_yield}")