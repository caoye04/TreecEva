def analyze_growth_cycle(data, threshold=0.75):
    """Irrelevant analysis function (dead code path)"""
    return sum(1 for x in data if x > threshold)


def normalize_readings(readings):
    """Normalizes sensor readings using min-max scaling"""
    if not readings:
        return []
    min_val, max_val = min(readings), max(readings)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.5] * len(readings)
    return [(x - min_val) / range_val for x in readings]


def detect_anomalies(logs):
    """Detects anomalous patterns in log strings - uses string methods"""
    anomalies = 0
    for log in logs:
        if log.strip().lower().startswith("err") or 'fail' in log.lower():
            anomalies += 1
    return anomalies


def compute_root_zone(depths, moisture_levels):
    """Calculates effective root zone based on depth and moisture"""
    weighted_sum = sum(d * m for d, m in zip(depths, moisture_levels))
    total_moisture = sum(moisture_levels)
    if total_moisture == 0:
        return 0.0
    avg_depth = weighted_sum / total_moisture
    return round(avg_depth, 4)


def calculate_harvest_efficiency(fields, settings):
    base_efficiency = settings['base']
    bonus_factor = settings.get('bonus', 1.0)
    stress_penalty = settings.get('penalty', 0.9)
    
    total_yield = 0
    efficiency_mod = 1.0
    
    # Simulate field processing with nested logic
    for i, field in enumerate(fields):
        region_code = field['region']
        crop_type = field['crop']
        size_acres = field['size']
        soil_ph = field['soil_ph']
        
        # Irrelevant intermediate calculations (distractors)
        ph_trend = abs(soil_ph - 6.5)  # ideal pH baseline
        adjustment_score = 1 - (ph_trend * 0.05) if ph_trend < 5 else 0.2
        
        # Real logic: yield depends on crop-specific factors
        if crop_type == 'wheat':
            base_yield_per_acre = 45
            climate_boost = 1.1 if 'sun' in region_code else 1.0
        elif crop_type == 'corn':
            base_yield_per_acre = 160
            climate_boost = 1.2 if 'midwest' in region_code else 0.9
        elif crop_type == 'soy':
            base_yield_per_acre = 48
            climate_boost = 1.15 if 'midwest' in region_code else 0.85
        else:
            base_yield_per_acre = 30
            climate_boost = 1.0
        
        # Moisture impact via root zone calculation
        depths = field['root_depths']
        moistures = field['moisture_levels']
        avg_root_depth = compute_root_zone(depths, moistures)
        moisture_efficiency = 0.7 + (avg_root_depth * 0.1)  # assume max 1.0
        moisture_efficiency = min(moisture_efficiency, 1.0)
        
        # Pest detection from string logs
        pest_logs = field['pest_logs']
        pest_count = detect_anomalies(pest_logs)
        pest_penalty = 0.95 ** pest_count  # exponential decay
        
        # Final per-field yield
        field_yield = (
            base_yield_per_acre * 
            climate_boost * 
            moisture_efficiency * 
            pest_penalty * 
            size_acres
        )
        
        # Accumulate only if above minimum threshold
        if field_yield >= 50:
            total_yield += field_yield
        
        # Update efficiency mod using conditional expression
        efficiency_mod = (efficiency_mod * 1.02) if pest_count == 0 else (efficiency_mod * 0.98)
    
    # Apply configuration-based adjustments
    if bonus_factor > 1.0 and total_yield > 1000:
        total_yield *= bonus_factor
    
    if efficiency_mod < stress_penalty:
        total_yield *= stress_penalty
    
    final_efficiency = total_yield * base_efficiency * efficiency_mod
    return int(round(final_efficiency))

# Main execution block
if __name__ == '__main__':
    # Sensor data inputs
    sensor_readings = [0.4, 0.6, 0.8, 0.5, 0.9, 0.3]
    normalized_sensors = normalize_readings(sensor_readings)  # unused distractor
    
    # Configuration setup
    config = {
        'base': 0.87,
        'bonus': 1.08,
        'penalty': 0.93
    }
    
    # Field dataset with mixed crops and conditions
    field_data = [
        {
            'region': 'midwest-summer',
            'crop': 'corn',
            'size': 120,
            'soil_ph': 6.2,
            'root_depths': [18, 24, 30, 36],
            'moisture_levels': [0.3, 0.5, 0.7, 0.4],
            'pest_logs': ['ok', 'ok', 'warning: aphids detected', 'ok']
        },
        {
            'region': 'plains-sun',
            'crop': 'wheat',
            'size': 200,
            'soil_ph': 7.0,
            'root_depths': [12, 15, 18],
            'moisture_levels': [0.4, 0.6, 0.5],
            'pest_logs': ['ok', 'ok', 'ok']
        },
        {
            'region': 'southeast-rain',
            'crop': 'soy',
            'size': 150,
            'soil_ph': 5.8,
            'root_depths': [14, 20, 25],
            'moisture_levels': [0.6, 0.8, 0.6],
            'pest_logs': ['error: scout failed', 'ok', 'fail: trap full']
        },
        {
            'region': 'desert-arid',
            'crop': 'barley',
            'size': 80,
            'soil_ph': 8.0,
            'root_depths': [10, 12],
            'moisture_levels': [0.1, 0.05],
            'pest_logs': ['ok']
        }
    ]
    
    # Trigger irrelevant growth cycle analysis (red herring)
    flat_moisture = [level for field in field_data for level in field['moisture_levels']]
    growth_cycles_completed = analyze_growth_cycle(flat_moisture, threshold=0.5)
    
    # Critical execution point
    final_yield = calculate_harvest_efficiency(field_data, config)
    
    # Output result
    print(f"Target result: {final_yield}")