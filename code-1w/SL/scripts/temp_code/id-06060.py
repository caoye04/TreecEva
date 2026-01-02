import math

# Simulated sensor data from a distributed environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 48, 50, 44, 52, 49, 47, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant calibration offset (distractor)
CALIBRATION_OFFSET_X = 0.987
CALIBRATION_OFFSET_Y = -1.023
BASELINE_DRIFT = sum([abs(CALIBRATION_OFFSET_X), abs(CALIBRATION_OFFSET_Y)])

# Misleading health indicators (dead computations)
raw_stability_index = sum([(t - 24) ** 2 for t in temperature_readings]) / len(temperature_readings)
stale_normalization_factor = max(humidity_readings) - min(humidity_readings)

# Real signal preprocessing
filtered_temps = list(filter(lambda x: 23 <= x <= 25, temperature_readings))
normalized_humidity = [(h - min(humidity_readings)) / stale_normalization_factor for h in humidity_readings]

# Composite feature engineering
thermal_variance = sum([(t - sum(temperature_readings)/len(temperature_readings))**2 for t in temperature_readings]) / len(temperature_readings)
pressure_trend = sum(pressure_readings[i+1] - pressure_readings[i] for i in range(len(pressure_readings)-1))

# Auxiliary diagnostic maps (some relevant, some not)
diagnostic_map = {
    'temp_stability': raw_stability_index,
    'humidity_range': stale_normalization_factor,
    'thermal_noise': thermal_variance,
    'barometric_drift': pressure_trend,
    'sample_count': len(temperature_readings)
}

# Decoy function that looks important but isn't used in final path
def deprecated_diagnostic(data):
    return sum(d ** 2 for d in data) % 100

# Core processing function with nested logic
def analyze_fluctuations(readings):
    if len(readings) < 5:
        return 0
    
    windowed_diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    significant_changes = list(filter(lambda x: x > 0.5, windowed_diffs))
    
    if len(significant_changes) == 0:
        return 10
        
    avg_jump = sum(significant_changes) / len(significant_changes)
    return round(avg_jump * 100)

# Secondary transformation chain
entropy_proxy = -sum(p * math.log(p + 1e-9) for p in normalized_humidity)
entropy_proxy = entropy_proxy if entropy_proxy > 0 else 0.5

# Create synthetic index using list comprehension and dictionary mapping
synthetic_indices = [
    diagnostic_map['thermal_noise'] * 2 if i % 2 == 0 else diagnostic_map['barometric_drift'] + i
    for i in range(4)
]

# Dummy state tracker (irrelevant)
current_state_flags = {"active": True, "calibrated": False, "synced": len(temperature_readings) % 2 == 0}
state_score = sum([1 for k,v in current_state_flags.items() if v])

# Health signature generation (key computation path)
def generate_signature(temp, hum, press):
    a = sum(temp) / len(temp)
    b = max(hum) - min(hum)
    c = abs(press[-1] - press[0])
    
    # Complex interaction
    s1 = (a * 1.5) + (b * 2.0)
    s2 = c * 10 + (thermal_variance * 0.1)
    
    # Nested conditional with red herring branch
    if s1 > 100 or s2 < 0:
        return s1 - s2  # Dead branch (never reached)
    else:
        return (s1 + s2) * 0.75

health_signature = generate_signature(filtered_temps, humidity_readings, pressure_readings)

# Unused alternate method (distractor)
compute_risk_score = lambda x, y: (x * 0.6) + (y * 0.4)
risk_baseline = compute_risk_score(diagnostic_map['temp_stability'], diagnostic_map['humidity_range'])

# Final processing with multiple abstraction layers
def process_metrics(sig):
    # Level 1: noise injection and filtering
    candidates = [sig + i*0.5 for i in range(-3, 4)]
    refined = [c for c in candidates if c > 0]
    
    # Level 2: transformation via dictionary aggregation
    stats = {
        'mean': sum(refined)/len(refined),
        'peak': max(refined),
        'range': max(refined) - min(refined)
    }
    
    # Level 3: recursive refinement (simple recursion)
    def converge_value(x, depth=0):
        if depth >= 3:
            return x
        updated = x * 0.9 + stats['mean'] * 0.1
        return converge_value(updated, depth + 1)
    
    intermediate = converge_value(stats['peak'])
    
    # Level 4: final adjustment with irrelevant context
    device_weights = {'sensor_a': 0.7, 'sensor_b': 0.3}
    weighted_adjustment = intermediate * device_weights['sensor_a']
    
    # ACTUAL final result
    result = int(round(weighted_adjustment * 1.25))
    
    # DEAD CODE PATHS BELOW
    if intermediate < 0:
        fallback = math.sqrt(abs(intermediate))
        return int(fallback)
    elif result % 7 == 0:
        alternative = result // 7
        return alternative  # Never taken due to value
    
    return result

final_diagnostic = process_metrics(health_signature)
print(f"Target result: {final_diagnostic}")