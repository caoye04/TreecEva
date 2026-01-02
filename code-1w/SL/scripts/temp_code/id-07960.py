def analyze_growth_patterns(data, threshold):
    above_threshold = [x for x in data if x > threshold]
    growth_rate = len(above_threshold) / len(data) if data else 0
    return growth_rate


def preprocess_field_readings(raw_readings):
    cleaned = [abs(x) for x in raw_readings if isinstance(x, (int, float))]
    normalized = [x / max(cleaned) for x in cleaned] if cleaned else []
    outliers = [x for x in normalized if x > 0.9]
    return normalized, outliers

def calculate_harvest_efficiency(fields, settings):
    total_yield = 0
    efficiency_factors = []
    
    for i, field in enumerate(fields):
        readings, params = field['readings'], field['params']
        
        # Preprocess sensor readings
        processed, anomalies = preprocess_field_readings(readings)
        
        # Irrelevant distraction: environmental noise adjustment (not used later)
        noise_level = sum(1 for x in readings if x < 0) / len(readings) if readings else 0
        adjusted_noise = noise_level * 0.7 + settings.get('baseline', 0.1)
        
        # Core logic: compute productivity index
        base_yield = sum(processed[:len(processed)//2])
        late_yield = sum(processed[len(processed)//2:])
        
        if late_yield > base_yield:
            improvement = (late_yield - base_yield) / base_yield
        else:
            improvement = 0
        
        # Use list comprehension to filter high-performing segments
        strong_segments = [seg for seg in processed if seg >= 0.6]
        segment_booster = len(strong_segments) * 0.1
        
        # Compute field-specific efficiency
        initial_estimate = base_yield + late_yield + improvement * 100
        final_estimate = initial_estimate * (1 + segment_booster)
        efficiency_factors.append(final_estimate)
        
        # Dead code path - never accessed in control flow
        if False:
            debug_log = f"Field {i}: {final_estimate}"
            print(debug_log)

    # Aggregate efficiency across fields
    aggregate_efficiency = sum(efficiency_factors) / len(efficiency_factors) if efficiency_factors else 0
    
    # Secondary distraction: simulate weather impact (not actually applied)
    weather_modifiers = [1.05, 0.98, 1.02, 1.1]
    avg_weather = sum(weather_modifiers) / len(weather_modifiers)
    projected = aggregate_efficiency * avg_weather  # Computed but unused
    
    # Final yield based on configuration scaling
    scale_factor = settings.get('scale', 1.5)
    final_yield = int(aggregate_efficiency * scale_factor)
    
    # Additional irrelevant computation
    peak_density = max(efficiency_factors) / min(efficiency_factors) if len(efficiency_factors) > 1 else 1
    stability_index = (1 / peak_density) * 100
    
    return final_yield

# Simulated agricultural field data
field_data = [
    {
        'readings': [85, -23, 91, 44, 102, 67, 110, -8],
        'params': {'soil': 'clay', 'moisture': 0.6}
    },
    {
        'readings': [77, 81, 90, 65, 100, 88, 93, 72],
        'params': {'soil': 'loam', 'moisture': 0.5}
    },
    {
        'readings': [60, 70, 68, 75, 80, 82, 78, 85],
        'params': {'soil': 'sand', 'moisture': 0.4}
    }
]

config = {
    'threshold': 70,
    'baseline': 0.15,
    'scale': 1.8
}

# Execute main calculation
final_yield = calculate_harvest_efficiency(field_data, config)
print(f"Result: {final_yield}")