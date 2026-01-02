from collections import defaultdict, Counter

# Simulated sensor data ingestion pipeline
def ingest_sensor_stream():
    raw_samples = [
        (1001, 23.5, 'C'), (1002, -1.2, 'X'), (1003, 0.0, 'C'),
        (1004, 45.1, 'F'), (1005, 18.9, 'C'), (1006, 32.0, 'X'),
        (1007, 21.8, 'C'), (1008, -5.4, 'F'), (1009, 19.3, 'C')
    ]
    return raw_samples

def validate_temperature(temp, unit):
    if unit == 'C':
        return -273.15 < temp <= 1000.0
    elif unit == 'F':
        return -459.67 < temp <= 1832.0
    else:
        return False

# Irrelevant transformation - decoy function
def transform_coordinates(pairs):
    return [(y * 2, x // 100) for x, y in pairs if x % 2 == 0]

# Data cleaning with red herring logic
def clean_data(records):
    errors_detected = 0
    cleaned = []
    id_log = set()
    
    for record in records:
        sensor_id, temp, unit = record
        
        # Distractor: tracking duplicate IDs (not used later)
        if sensor_id in id_log:
            errors_detected += 1
            continue
        id_log.add(sensor_id)
        
        # Actual filtering condition
        if validate_temperature(temp, unit) and unit in ['C', 'F']:
            # Red herring: modifying temp in a way that gets overridden
            adjusted_temp = temp + 273.15 if unit == 'C' else temp
            adjusted_temp = (temp - 32) * 5/9 if unit == 'F' else temp
            cleaned.append((sensor_id, round(adjusted_temp, 2), unit))
    
    # Dead code path - never accessed in normal execution
    if errors_detected > 100:
        fallback = sum(x[0] for x in cleaned) % 7
        return [(s, t + fallback, u) for s, t, u in cleaned]
    
    return cleaned

# Bit manipulation decoy - unused but plausible
def compute_checksum(data_chunk):
    checksum = 0
    for item in data_chunk:
        if isinstance(item, tuple):
            for val in item:
                if isinstance(val, (int, float)):
                    checksum ^= int(abs(val)) & 0xFF
    return checksum << 1

# Main processing with multiple distractions
def process_readings(data_slice, config_map):
    # Unused configuration map (plausible but irrelevant)
    min_thresh = config_map.get('min', -50)
    max_thresh = config_map.get('max', 50)
    priority_band = config_map.get('band', (0, 30))
    
    # Real computation begins
    temperatures = [temp for _, temp, _ in data_slice]
    
    # Distractor: complex counting with unused result
    unit_counter = Counter([unit for _, _, unit in data_slice])
    anomaly_score = 0
    for val in temperatures:
        if val < min_thresh or val > max_thresh:
            anomaly_score += 1
    
    # More red herrings: sorting and bit operations
    sorted_temps = sorted(temperatures)
    mid_index = len(sorted_temps) // 2
    median_temp = (sorted_temps[mid_index] + sorted_temps[~mid_index]) / 2
    
    # Decoy bit manipulation
    magic_key = (int(median_temp) ^ 0xAB) & 0xF0
    magic_key = (magic_key >> 4) | (magic_key << 4)
    
    # Actual critical calculation
    base_value = 0
    for i, t in enumerate(temperatures):
        if i % 2 == 0 and t > 0:
            base_value += t * 1.8
        else:
            base_value -= t * 0.2
    
    # Final computation with misleading components
    diagnostic_weight = len(temperatures) * 0.7
    stability_factor = abs(sorted_temps[-1] - sorted_temps[0])
    
    # The real answer computation
    final_diagnostic = int(base_value - diagnostic_weight + stability_factor)
    
    # Dead code - unreachable under normal conditions
    if magic_key < 0:
        final_diagnostic *= -1
    
    return final_diagnostic

# Orchestration with setup distractions
def main_pipeline():
    # Initial data load
    samples = ingest_sensor_stream()
    
    # Irrelevant coordinate transformation (decoy)
    ids_and_temps = [(s, t) for s, t, u in samples]
    transformed = transform_coordinates(ids_and_temps)
    
    # Checksum computation - not used in final path
    security_tag = compute_checksum(samples)
    
    # Cleaning the data
    filtered_data = clean_data(samples)
    
    # Configuration map with plausible but partially unused entries
    threshold_map = defaultdict(float)
    threshold_map.update({'min': -40, 'max': 60, 'band': (5, 35), 'gain': 1.5})
    
    # Key statement where answer is determined
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

if __name__ == "__main__":
    main_pipeline()