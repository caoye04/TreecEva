def analyze_trend(values):
    if len(values) < 2:
        return 0
    trend = sum(1 for i in range(1, len(values)) if values[i] > values[i-1])
    volatility = sum(abs(values[i] - values[i-1]) for i in range(1, len(values)))
    irrelevant_trend_factor = (trend * 1.5 + volatility * 0.1) / len(values) if values else 0
    return trend

# Simulated sensor readings over time
temperature_readings = [22, 24, 25, 23, 26, 28, 27, 29]
humidity_readings = [45, 47, 50, 52, 51, 49, 48, 50]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1013, 1012, 1011]

# Unused and misleading data paths
def compute_stability(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    stability_score = 1 / (1 + variance) if variance > 0 else 1
    fake_correction = stability_score * 0.87 + 2.1
    return stability_score

stability = compute_stability(pressure_readings)
stagnation_point = None
for i, val in enumerate(humidity_readings):
    if val == 50 and stagnation_point is None:
        stagnation_point = i

# Data transformation pipeline
deviation_map = {}
for idx in range(len(temperature_readings)):
    diff = temperature_readings[idx] - humidity_readings[idx]
    deviation_map[f'temp_humid_gap_{idx}'] = diff

# Red herring: complex but unused transformation
global_offset = 0.0
for key, value in deviation_map.items():
    if value > 0:
        global_offset += value * 0.05
    else:
        global_offset -= abs(value) * 0.03

# Real processing begins here — subtle due to distractions above
def process_metrics(logs):
    total_energy = 0
    peak_load = 0
    for reading in logs:
        adjusted = (reading ** 2) // 10
        if adjusted > peak_load:
            peak_load = adjusted
        total_energy += adjusted
    efficiency_ratio = total_energy / (peak_load + 1)
    return total_energy, efficiency_ratio

energy_usage, efficiency = process_metrics(temperature_readings)

# Conditional data restructuring
metric_data = {
    'energy': energy_usage,
    'efficiency': round(efficiency, 3),
    'size': len(temperature_readings),
    'trend_strength': analyze_trend(temperature_readings)
}

base_threshold = 85

# Core logic hidden among decoys
def evaluate_performance(metrics, threshold):
    score = 0
    
    # Weighted contribution from multiple factors
    if metrics['energy'] > threshold * 2:
        score += 25
    if metrics['efficiency'] > 0.7:
        score += 20
    if metrics['size'] >= 8:
        score += 15
    
    # Nested condition with tuple unpacking distraction
    growth_phase, decline_phase = 0, 0
    for i in range(1, len(temperature_readings)):
        if temperature_readings[i] > temperature_readings[i-1]:
            growth_phase += 1
        else:
            decline_phase += 1
    
    balance_ratio = growth_phase / (decline_phase + 1)
    
    # Decoy assignment below — looks important but unused
    hypothetical_balance_score = (growth_phase * 2 + decline_phase) / 3.5
    
    if balance_ratio >= 1.0:
        score += 10
    
    # Dictionary-based bonus lookup
    bonus_table = {0: 5, 1: 8, 2: 12, 3: 15}
    extra_bonus_key = min(metrics['trend_strength'], 3)
    if extra_bonus_key in bonus_table:
        score += bonus_table[extra_bonus_key]
    
    # Final adjustment using integer division and rounding
    final_penalty = metrics['energy'] // 100
    score = max(score - final_penalty, 0)
    
    return score

# Critical statement
final_score = evaluate_performance(metric_data, base_threshold)

# Output result as required
print(f"Target result: {final_score}")