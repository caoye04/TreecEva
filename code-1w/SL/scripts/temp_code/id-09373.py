def analyze_soil_quality(readings):
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return avg, variance

# Simulate agricultural plot data
temperature_logs = [22, 24, 19, 23, 25, 21, 20]
humidity_levels = [60, 65, 58, 70, 63, 67, 64]

soil_readings = {
    'plot_A': [4.5, 4.7, 4.6, 4.8, 4.4],
    'plot_B': [5.1, 5.0, 5.2, 4.9, 5.3],
    'plot_C': [3.8, 3.6, 3.9, 4.0, 3.7],
    'plot_D': [4.2, 4.3, 4.1, 4.4, 4.0]
}

# Irrelevant preprocessing: normalize humidity (not used later)
normalized_humidity = [round((h - min(humidity_levels)) / (max(humidity_levels) - min(humidity_levels)), 3) for h in humidity_levels]

# Extract relevant plots above temperature threshold
temp_threshold = 21
selected_plots = [temp for temp in temperature_logs if temp >= temp_threshold]

# Harvest yield simulation based on soil quality
base_yield_per_plot = {}
for name, readings in soil_readings.items():
    avg, _ = analyze_soil_quality(readings)
    base_yield_per_plot[name] = round(avg * 100)

# Misleading transformation: convert to percentages (unused)
yield_percentages = {k: round(v / max(base_yield_per_plot.values()) * 100, 1) for k, v in base_yield_per_plot.items()}

# Define efficiency function
def calculate_harvest_efficiency(plots, threshold):
    total_yield = 0
    adjustment_factor = 0.85
    
    # Simulate conditional nutrient boost
    nutrient_boost = {}
    for p in plots:
        if p in ['plot_A', 'plot_B']:
            nutrient_boost[p] = 1.1
        elif p == 'plot_D':
            nutrient_boost[p] = 1.05
        else:
            nutrient_boost[p] = 1.0
    
    # Apply boosts and compute adjusted yields
    adjusted_yields = []
    for name, base in base_yield_per_plot.items():
        boosted = int(base * nutrient_boost.get(name, 1.0))
        adjusted_yields.append(boosted)
    
    # Filter plots by index condition (based on external threshold)
    valid_indices = [i for i, t in enumerate(temperature_logs) if t > threshold]
    selected_yields = [adjusted_yields[i] for i in valid_indices if i < len(adjusted_yields)]
    
    # Final efficiency calculation
    if selected_yields:
        total_yield = sum(selected_yields) * adjustment_factor
    
    # Dead code: entropy calculation (not used)
    from math import log
    entropy = sum(-y/total_yield * log(y/total_yield) for y in selected_yields if y > 0) if total_yield > 0 else 0
    
    return int(total_yield)

# Main execution
plots = list(soil_readings.keys())
threshold = 20
final_yield = calculate_harvest_efficiency(plots, threshold)
print(f"Result: {final_yield}")