def analyze_crop_performance(data):
    total_rainfall = sum([entry['rain'] for entry in data])
    temperature_spikes = [t for t in data if t['temp'] > 35]
    spike_count = len(temperature_spikes)
    base_threshold = 200

    # Irrelevant tracking (distractor)
    wind_speed_avg = sum([w['wind'] for w in data]) / len(data)
    humidity_log = {idx: record['humidity'] for idx, record in enumerate(data)}

    adjusted_rainfall = total_rainfall - (spike_count * 10)

    # Destructuring assignment (relevant)
    first_cycle, *remaining_cycles = data

    # Character counting in metadata keys (semi-relevant)
    key_chars = sum(len(k) for k in first_cycle.keys())

    efficiency_mod = 1.0
    if key_chars > 20:
        efficiency_mod *= 0.95

    # Simulate growth accumulation over cycles
    cumulative_growth = 0
    for cycle in remaining_cycles:
        if cycle['sunlight'] >= 6:
            cumulative_growth += cycle['growth'] * efficiency_mod

    return cumulative_growth


def calculate_harvest_efficiency(metrics, cycles):
    base_area = metrics['hectares']
    soil_quality = metrics['soil_score']
    pest_factor = metrics.get('pests', 1.0)

    # Unrelated computation (dead code path - distractor)
    if soil_quality < 50:
        fallback_strategy = "irrigate"
        buffer_zone = base_area * 0.1

    # Real calculation starts
    yield_per_hectare = 0
    for i in range(len(cycles)):
        cycle_yield = cycles[i]['yield']
        adjustment = 1.0
        if cycles[i]['drought']:
            adjustment *= 0.8
        if cycles[i]['fertilizer']:
            adjustment *= 1.15
        yield_per_hectare += cycle_yield * adjustment

    total_yield = base_area * (yield_per_hectare / len(cycles))

    # Apply soil and pest factors
    final_adjustment = (soil_quality / 100) * pest_factor
    total_yield *= final_adjustment

    return int(total_yield)

# Main execution
area_metrics = {
    'hectares': 45,
    'soil_score': 82,
    'pests': 0.93,
    'region_code': 'AGRI-NW'
}

growth_cycles = [
    {'cycle': 1, 'yield': 1200, 'drought': False, 'fertilizer': True},
    {'cycle': 2, 'yield': 1350, 'drought': True, 'fertilizer': True},
    {'cycle': 3, 'yield': 1400, 'drought': False, 'fertilizer': False},
    {'cycle': 4, 'yield': 1300, 'drought': False, 'fertilizer': True}
]

temp_data = [
    {'temp': 28, 'rain': 40, 'wind': 12, 'humidity': 60, 'sunlight': 7},
    {'temp': 36, 'rain': 30, 'wind': 15, 'humidity': 55, 'sunlight': 8},
    {'temp': 32, 'rain': 50, 'wind': 10, 'humidity': 65, 'sunlight': 6}
]

# Call helper (uses string methods and dict ops - semi-relevant)
diagnostic_key = ''.join(sorted(area_metrics.keys()))
key_length = len(diagnostic_key)
modifier_flag = 'region' in area_metrics['region_code'].lower()

baseline_growth = analyze_crop_performance(temp_data)

# Key statement
final_yield = calculate_harvest_efficiency(area_metrics, growth_cycles)

# Print result
print(f"Result: {final_yield}")