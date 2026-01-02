from collections import defaultdict, Counter

# Simulate agricultural yield analysis across microplots
def analyze_microplot_stability(plot_data):
    stability_log = defaultdict(float)
    for plot, readings in plot_data.items():
        valid_readings = [r for r in readings if r > 0.5]
        if len(valid_readings) >= 3:
            stability_log[plot] = sum(valid_readings) / len(valid_readings)
        else:
            stability_log[plot] = 0.0
    return stability_log


def calculate_growth_potential(baseline, modifiers):
    potential = baseline
    for mod in modifiers:
        if mod['active']:
            potential *= (1 + mod['factor'])
    return round(potential, 4)

# Initial dataset: sensor readings from 5 microplots over 7 days
sensor_readings = {
    'plot_A': [0.8, 0.9, 0.4, 0.85, 0.92],
    'plot_B': [0.6, 0.55, 0.62, 0.3, 0.7],
    'plot_C': [0.95, 0.98, 0.93, 0.89, 0.91],
    'plot_D': [0.2, 0.35, 0.4, 0.5],
    'plot_E': [0.77, 0.81, 0.74, 0.83, 0.79]
}

# Step 1: Analyze stability of each microplot
stability_scores = analyze_microplot_stability(sensor_readings)

# Irrelevant intermediate computation (distractor) - simulates calibration drift adjustment
baseline_drift = 1.05
adjusted_drift_scores = {k: v * baseline_drift for k, v in stability_scores.items()}
calibration_offset = sum(adjusted_drift_scores.values()) * 0.01  # Minor offset, not used later

# Growth cycle parameters
modifiers = [
    {'active': True,  'factor': 0.15, 'type': 'fertilizer'},
    {'active': False, 'factor': 0.3,  'type': 'irrigation'},  # Inactive
    {'active': True,  'factor': 0.05, 'type': 'light'}
]

# Simulate multiple growth cycles with varying baselines
growth_cycles = []
for base in [0.8, 0.9, 1.0, 1.1]:
    net_potential = calculate_growth_potential(base, modifiers)
    growth_cycles.append({'base': base, 'potential': net_potential})

# Area-specific metrics
area_metrics = {
    'total_plots': len(sensor_readings),
    'stable_count': len([s for s in stability_scores.values() if s > 0.7]),
    'avg_stability': sum(stability_scores.values()) / len(stability_scores)
}

# Key irrelevant block: simulate redundant environmental correlation check
env_correlation = defaultdict(list)
for cycle in growth_cycles:
    for i in range(3):
        env_correlation[f'cycle_{i}'].append(cycle['potential'] * 0.1)
flat_corr = [item for sublist in env_correlation.values() for item in sublist]
total_corr = sum(flat_corr)  # Dead-end computation

# Core logic: harvest efficiency calculation based on area and cycle data
def calculate_harvest_efficiency(area, cycles):
    base_efficiency = area['avg_stability'] * area['stable_count']
    cumulative_boost = 0
    for c in cycles:
        if c['base'] >= 1.0:
            cumulative_boost += c['potential']
    # Final formula: base efficiency modulated by high-base cycle boosts
    efficiency = base_efficiency * (1 + cumulative_boost)
    return round(efficiency, 4)

# Critical execution point
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Print result
print(f"Result: {final_yield}")