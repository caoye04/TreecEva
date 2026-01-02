def analyze_soil_composition(elements):
    # Irrelevant analysis with dead-end logic
    trace_levels = {k: v * 1.7 for k, v in elements.items() if v < 5}
    heavy_metals = sum(v for v in elements.values() if v > 10)
    return len(trace_levels) + (heavy_metals // 2)


def normalize_readings(readings):
    # Distractor function - never called
    normalized = [round((x - min(readings)) / (max(readings) - min(readings)), 3) for x in readings]
    return normalized

# Simulated sensor data from agricultural plots
sensors = [
    {'id': 'S1', 'moisture': 42, 'ph': 6.5, 'temp': 24},
    {'id': 'S2', 'moisture': 38, 'ph': 5.9, 'temp': 26},
    {'id': 'S3', 'moisture': 45, 'ph': 6.8, 'temp': 23},
    {'id': 'S4', 'moisture': 35, 'ph': 6.1, 'temp': 27}
]

plots = [
    {'plot_id': 'P1', 'size': 120, 'crop': 'wheat', 'yield_last': 98},
    {'plot_id': 'P2', 'size': 150, 'crop': 'corn',  'yield_last': 110},
    {'plot_id': 'P3', 'size': 130, 'crop': 'wheat', 'yield_last': 105},
    {'plot_id': 'P4', 'size': 100, 'crop': 'barley','yield_last': 88}
]

# Misleading intermediate calculations
baseline_moisture = sum(s['moisture'] for s in sensors) / len(sensors)
marginal_ph_count = len([s for s in sensors if 6.0 <= s['ph'] <= 6.5])

temp_buckets = {}
for s in sensors:
    bucket = s['temp'] // 5
    temp_buckets[bucket] = temp_buckets.get(bucket, 0) + 1

# Hidden state tracking (distractor)
calibration_log = []
for i, s in enumerate(sensors):
    delta = abs(s['moisture'] - baseline_moisture)
    calibration_log.append(f"C{i+1}:{round(delta,1)}")

# Bitwise red herring
sensor_flags = 0
for s in sensors:
    if s['moisture'] > 40:
        sensor_flags |= (1 << (s['id'][-1]))
sensor_flags ^= 0b1111  # Obfuscation

# Real computation buried in noise
def calculate_harvest_efficiency(plot_list, sensor_list):
    efficiency_mod = 0.0
    
    # Use of zip and enumerate together (required features)
    for idx, (p, s) in enumerate(zip(plot_list, sensor_list)):
        base_eff = p['yield_last'] / p['size']
        moisture_boost = 1.0
        
        # Relevant conditional branch
        if s['moisture'] > 40:
            moisture_boost += 0.1
        elif s['moisture'] < 37:
            moisture_boost -= 0.05
            
        ph_optimal = 1.0 if 6.0 <= s['ph'] <= 6.8 else 0.9
        
        # Temperature penalty using bit check as red herring
        temp_shift = (s['temp'] >> 1) & 3  # distractor usage
        temp_penalty = 1.0
        if s['temp'] > 25:
            temp_penalty = 0.95
            
        # Actual contribution
        step_yield = base_eff * moisture_boost * ph_optimal * temp_penalty
        efficiency_mod += step_yield
        
        # Dead code path (never used)
        if idx == 99:
            fallback = step_yield * 0.8
            break
            
    # Final aggregation
    total_eff = int(efficiency_mod * 100)
    
    # Irrelevant string transformation
    code_name = "H" + "".join([chr(65 + (total_eff % 10))])
    
    return total_eff

# Unused helper that looks important
def predict_pest_risk(sensor_data):
    risk_score = 0
    for s in sensor_data:
        if s['temp'] > 25 and s['moisture'] > 40:
            risk_score += 2
    return risk_score

# Key execution point
final_yield = calculate_harvest_efficiency(plots, sensors)

# Print result as required
print(f"Result: {final_yield}")