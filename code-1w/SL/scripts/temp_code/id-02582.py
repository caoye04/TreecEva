def analyze_soil_ph(readings):
    avg_ph = sum(readings) / len(readings)
    normalized = [(r - avg_ph) ** 2 for r in readings]
    return sum(normalized)

soil_samples = [6.2, 6.4, 6.8, 7.1, 6.9, 6.5]
distraction_value = (sum(soil_samples) * 0.15) + 4.2
ph_variance_score = analyze_soil_ph(soil_samples)

area_metrics = {
    'plots': [(120, 80), (95, 70), (110, 85)],
    'units': 'sq_meters',
    'conversion_factor': 0.0001
}

growth_cycles = [
    {'temp': 24, 'humidity': 60, 'days': 90},
    {'temp': 26, 'humidity': 65, 'days': 88},
    {'temp': 23, 'humidity': 58, 'days': 92}
]

# Irrelevant string processing to increase cognitive load
temp_labels = [f"Cycle-{i+1}" for i in range(len(growth_cycles))]
labeled_data = {k: v for k, v in zip(temp_labels, growth_cycles)}
processed_tags = [label.lower().replace('-', '_') for label in temp_labels if 'Cycle' in label]

# Misleading computation with bitwise operations
bitwise_trace = 0
for i, tag in enumerate(processed_tags):
    bitwise_trace ^= len(tag) << 1

baseline_yield = 0.78
efficiency_log = []

for i, plot in enumerate(area_metrics['plots']):
    width, height = plot
    area_sqm = width * height
    area_hectares = area_sqm * area_metrics['conversion_factor']
    
    cycle = growth_cycles[i]
    base_productivity = (cycle['temp'] * 1.5) + (cycle['humidity'] * 0.8)
    duration_factor = cycle['days'] / 90.0
    
    # Distractor calculation not used in final result
    phantom_score = (width & int(cycle['humidity'])) | (height ^ int(cycle['temp']))
    
    adjusted_yield = base_productivity * duration_factor * baseline_yield
    efficiency_log.append(adjusted_yield)

# Another red herring: string-based filtering
status_flags = ['OK' if y > 40 else 'LOW' for y in efficiency_log]
valid_count = status_flags.count('OK')

# Final efficiency uses only the average and ph score modifier
average_efficiency = sum(efficiency_log) / len(efficiency_log)
ph_modifier = 1 + (0.05 if 6.0 <= ph_variance_score < 0.2 else -0.05)

# Key statement
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

def calculate_harvest_efficiency(parcel, cycles):
    total_area = sum(w * h for w, h in parcel['plots'])
    efficiency_per_cycle = []
    for c in cycles:
        score = (c['temp'] * 1.2) + (c['humidity'] * 0.7) + (c['days'] * 0.1)
        efficiency_per_cycle.append(score)
    avg_score = sum(efficiency_per_cycle) / len(efficiency_per_cycle)
    return (total_area * avg_score * 0.001)

print(f"Result: {final_yield}")