def analyze_growth_patterns(data):
    baseline = sum(data.get('temperatures', [])) / len(data.get('temperatures', [1]))
    threshold = data.get('threshold', 25)
    exceeded_days = 0
    for temp in data.get('temperatures', []):
        if temp > threshold:
            exceeded_days += 1
    return exceeded_days


def calculate_moisture_retention(soil_type, readings):
    retention_map = {'clay': 0.8, 'loam': 0.6, 'sand': 0.3}
    base_retention = retention_map.get(soil_type, 0.5)
    daily_loss = 0.05
    total_retained = 0
    for reading in readings:
        total_retained += reading * base_retention
        total_retained -= daily_loss
    return round(total_retained, 4) if total_retained > 0 else 0

# Simulate agricultural yield prediction with mixed reasoning
temperature_log = [22, 24, 27, 29, 26, 23, 21]
humidity_readings = [0.65, 0.71, 0.68, 0.73, 0.69, 0.72, 0.70]

region_data = {
    'temperatures': temperature_log,
    'humidity': humidity_readings,
    'soil': 'loam',
    'threshold': 25,
    'irrigation_events': 3
}

# Irrelevant intermediate calculations (distractors)
avg_temp = sum(temperature_log) / len(temperature_log)
drought_risk = analyze_growth_patterns(region_data)
moisture_level = calculate_moisture_retention(region_data['soil'], humidity_readings)

# Key state tracking with conditional logic
effective_days = 0
for i, temp in enumerate(region_data['temperatures']):
    if temp >= 22 and humidity_readings[i] > 0.68:
        effective_days += 1

# Destructuring assignment (relevant concept)
base_yield_per_day, adjustment_factor = 12.5, 0.9

# Set operations to identify peak conditions
peak_temps = set(t for t in region_data['temperatures'] if t > 25)
high_humidity = set(h for h in humidity_readings if h > 0.69)
co_occurrence_index = len(peak_temps) * len(high_humidity)  # semi-relevant metric

# Conditional expression influencing final result
bonus_applied = True if len(peak_temps) > 2 and moisture_level > 0.4 else False
growth_multiplier = 1.25 if bonus_applied else 1.0

# Final aggregation using dictionary lookup and arithmetic chain
growth_potential = effective_days * base_yield_per_day
maintenance_loss = region_data.get('irrigation_events') * 1.8
adjusted_potential = growth_potential - maintenance_loss

# Core answer computation
final_yield = calculate_harvest_efficiency(region_data)

# Helper function defined after usage (syntax valid in Python due to execution order)
def calculate_harvest_efficiency(area):
    raw_efficiency = adjusted_potential * growth_multiplier
    efficiency_cap = 150.0
    return min(raw_efficiency, efficiency_cap)

print(f"Result: {final_yield}")