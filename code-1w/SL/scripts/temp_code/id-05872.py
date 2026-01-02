from collections import defaultdict, Counter
import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.4, 25.1, 22.8, 26.5, 24.7, 23.9, 25.6, 24.3, 26.1, 25.0]
humidity_readings = [45, 52, 58, 48, 60, 55, 50, 54, 62, 57]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1016, 1011, 1017, 1019, 1010]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7X', 'B9Y', 'C3Z', 'D8W', 'E2V']
error_flags = {code: idx * 17 for idx, code in enumerate(legacy_codes)}

# Misleading preprocessing path (dead code)
def validate_legacy_integrity(flags):
    checksum = 0
    for key, val in flags.items():
        checksum += val ^ len(key)
    return checksum % 13 == 0

is_valid = validate_legacy_integrity(error_flags)  # Unused result

# Core data aggregation
sensor_data = []
for i in range(len(temperature_readings)):
    record = {
        'temp': temperature_readings[i],
        'humid': humidity_readings[i],
        'press': pressure_readings[i],
        'station_id': f'ST{i+1}',
        'index_key': i
    }
    sensor_data.append(record)

# Decoy transformation (never used)
stale_transform = [math.sin(x['humid'] * 0.1) for x in sensor_data]

# Actual filtering logic based on dynamic thresholds
dynamic_threshold = sum(humidity_readings) / len(humidity_readings) + 2.5
filtered_data = [entry for entry in sensor_data if entry['humid'] > dynamic_threshold]

# Red herring: complex unused dictionary structure
threshold_map = defaultdict(lambda: defaultdict(dict))
for zone in ['NORTH', 'SOUTH', 'EAST', 'WEST']:
    for param in ['temp', 'humid']:
        base = 25 if param == 'temp' else 50
        for mode in ['MIN', 'MAX', 'CRIT']:
            if mode == 'MIN':
                threshold_map[zone][param][mode] = base - 5
            elif mode == 'MAX':
                threshold_map[zone][param][mode] = base + 10
            else:
                threshold_map[zone][param][mode] = base * 2

# Another decoy function with recursive distraction
def compute_entropy(seq, depth=0):
    if depth >= 3 or len(seq) <= 1:
        return round(math.log(len(seq) + 1), 3) if seq else 0.0
    mid = len(seq) // 2
    left = seq[:mid]
    right = seq[mid:]
    return compute_entropy(left, depth + 1) + compute_entropy(right, depth + 1)

entropy_score = compute_entropy(humidity_readings)  # Not used

# Real processing begins here — meaningful use of collections.Counter
def process_readings(data_list, thresholds):
    if not data_list:
        return -1
    
    # Extract temperature values for analysis
    temps = [item['temp'] for item in data_list]
    temp_counter = Counter(temps)
    
    # Find most common temperature band (floor value)
    floor_temps = [math.floor(t) for t in temps]
    floor_counter = Counter(floor_temps)
    primary_band = floor_counter.most_common(1)[0][0]
    
    # Compute adjusted mean within dominant band
    band_members = [t for t in temps if math.floor(t) == primary_band]
    raw_mean = sum(band_members) / len(band_members)
    
    # Apply correction based on station count
    station_diversity = len(set(item['station_id'] for item in data_list))
    corrected_mean = raw_mean * (station_diversity / len(data_list))
    
    # Final diagnostic includes bitwise manipulation of rounded components
    int_part = int(round(corrected_mean * 100))
    decimal_part = int((corrected_mean * 100) % 100)
    
    # Bitwise combination: XOR integer and decimal parts, then shift
    combined = (int_part ^ decimal_part) << 1
    final_value = combined - 1000  # Offset to create non-trivial result
    
    return final_value

# Additional misleading intermediate
aggregate_humid = sum([x['humid'] for x in sensor_data]) // len(sensor_data)  # Integer division

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Result: {final_diagnostic}")