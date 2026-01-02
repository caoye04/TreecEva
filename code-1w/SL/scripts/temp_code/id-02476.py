import itertools

def sensor_diagnostic(data_stream):
    # Irrelevant diagnostic function – dead code path
    anomalies = []
    for val in data_stream:
        if val < 0:
            anomalies.append(val)
    return anomalies

def analyze_phase_shift(frequencies):
    # Misleading signal processing function – never called
    shifted = []
    for f in frequencies:
        shifted.append((f * 1.5) % 360)
    return shifted

def filter_outliers(values, threshold=2.5):
    mean_val = sum(values) / len(values)
    deviances = [(v - mean_val) ** 2 for v in values]
    variance = sum(deviances) / len(deviances)
    std_dev = variance ** 0.5
    filtered = [v for v in values if abs(v - mean_val) <= threshold * std_dev]
    return filtered  # Used but not part of main logic

def compute_harvest(env_data, sensors):
    # Core logic buried under distractions
    base_yield = 0
    modifier = 1.0
    
    # Distractor: irrelevant sensor metadata
    sensor_names = ['solar', 'moisture', 'thermal', 'pressure']
    sensor_map = {k: v for k, v in zip(sensor_names, sensors)}
    active_sensors = [s for s in sensors if s > 0.3]
    
    # Real logic begins
    temp_seq = env_data.get('temperatures', [])
    humidity_seq = env_data.get('humidity_levels', [])
    
    if len(temp_seq) == 0 or len(humidity_seq) == 0:
        return -1
    
    # Conditional expression red herring
    growth_factor = 1.2 if sum(temp_seq) > 150 else 0.8
    
    # Use of enumerate and zip (required)
    stress_index = 0
    for i, (t, h) in enumerate(zip(temp_seq, humidity_seq)):
        if i % 3 == 0:
            stress_index += (t - 20) * (h / 100)
        elif i % 5 == 0:
            stress_index -= (t - 25) * 0.1  # Minor correction
    
    # Bit manipulation decoy
    encoded_flag = (len(temp_seq) << 2) ^ (len(humidity_seq) >> 1)
    encoded_flag &= 0xFF
    
    # Conditional branches with nested logic
    if stress_index < 5:
        base_yield = 85
    elif stress_index < 10:
        base_yield = 70
    else:
        base_yield = 45
    
    # Multiple assignments distraction
    a, b, c = 10, 20, 30
    dummy_sum = a + b + c  # irrelevant
    
    # Real modifier computation
    valid_sensors = [s for s in sensors if 0.2 <= s <= 0.9]
    if len(valid_sensors) >= 3:
        modifier += 0.15
    
    efficiency_log = []
    for idx, sensor in enumerate(sensors):
        efficiency_log.append((idx, sensor ** 2))  # logged but unused
    
    # Key calculation using itertools.chain to flatten hypothetical zones
    zone_data = [[1, 2], [3, 4], [5]]
    flat_zone = list(itertools.chain(*zone_data))
    zone_bonus = sum(flat_zone) / 10.0  # 15/10 = 1.5
    
    # Final yield depends on base_yield, modifier, and zone_bonus
    final_yield = (base_yield * modifier) + zone_bonus
    
    # Print required output
    return final_yield

def main():
    # Simulated environmental data
    conditions = {
        'temperatures': [22, 24, 26, 23, 28, 27, 25],
        'humidity_levels': [60, 65, 70, 55, 80, 75, 68]
    }
    
    # Sensor readings (only four used)
    sensors = [0.45, 0.62, 0.33, 0.71]  # All within plausible range
    
    # Dead code paths
    signal_freq = [50, 60, 55, 65]
    diagnostic_stream = [-1, 0, 2, 3, -2]  # unused
    
    # Unused filtering
    cleaned = filter_outliers([10, 12, 11, 100, 13])  # 100 is outlier
    
    # Key execution point
    final_yield = compute_harvest(conditions, sensors)
    
    # Output result as required
    print(f"Target result: {final_yield}")

if __name__ == "__main__":
    main()