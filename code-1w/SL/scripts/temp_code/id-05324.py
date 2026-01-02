import itertools

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.4, 25.1, 19.8, 30.2, 27.5, 22.0, 35.6, 28.3, 24.7]
humidity_readings = [45, 52, 60, 30, 58, 48, 25, 55, 50]
pressure_readings = [1013, 1009, 1015, 1020, 1010, 1014, 1005, 1018, 1012]

# Irrelevant auxiliary arrays (distractor)
sound_levels = [65, 70, 55, 80, 75, 60, 85, 72, 68]
luminance = [300, 800, 1200, 500, 900, 400, 100, 600, 700]

# Mapping of station IDs to geographical zones (mixed use and red herring)
station_zones = {0: 'forest', 1: 'urban', 2: 'coastal', 3: 'desert', 4: 'mountain',
                   5: 'wetland', 6: 'tundra', 7: 'savanna', 8: 'jungle'}

# Decoy transformation (never used in final logic)
def transform_pressure(pressure_list):
    return [p * 0.75 + 10 for p in pressure_list if p > 1010]

# Misleading intermediate calculation with plausible but unused result
elevated_humidity_stations = [i for i, h in enumerate(humidity_readings) if h > 50]

# Real processing begins here — filtering based on composite criteria
deviation_index = []
for i, temp in enumerate(temperature_readings):
    expected_humidity = 60 - abs(temp - 25) * 2  # Ideal humidity drops as temp moves from 25°C
    humidity_gap = abs(humidity_readings[i] - expected_humidity)
    deviation_index.append((i, humidity_gap))

# Filter stations where deviation exceeds dynamic threshold (core logic path)
filtered_stations = [idx for idx, gap in deviation_index if gap > 8]

# Extract corresponding raw data for these stations
filtered_data = []
for i in filtered_stations:
    record = {
        'id': i,
        'temp': temperature_readings[i],
        'humidity': humidity_readings[i],
        'zone': station_zones[i],
        'risk_factor': 0
    }
    # Compute risk factor using bitwise interaction of index and humidity (bit manipulation distractor)
    record['risk_factor'] = (i << 2) ^ int(record['humidity']) & 7
    filtered_data.append(record)

# Threshold map built from unused pressure data — looks important but only partially relevant
typical_pressure = sum(pressure_readings) / len(pressure_readings)
threshold_map = {}
for zone in set(station_zones.values()):
    # Only 'desert' and 'tundra' thresholds are actually used later; others are decoys
    base_offset = {'desert': -30, 'tundra': -40}.get(zone, -10)
    threshold_map[zone] = typical_pressure + base_offset

# Dead function — included to suggest complex calibration logic
def calibrate_sensor_array(raw_list, factor=1.05):
    return [x * factor for x in raw_list]

# Core processing function with list comprehension and zip usage
def process_readings(data_records, thresholds):
    aggregate_score = 0
    
    # Use of zip to pair temperature and humidity across filtered records
    paired_metrics = list(zip(
        [r['temp'] for r in data_records],
        [r['humidity'] for r in data_records]
    ))
    
    # Complex scoring with nested conditionals and arithmetic
    for record in data_records:
        zone = record['zone']
        t = record['temp']
        h = record['humidity']
        
        # Only desert and tundra contribute to final score; others skip
        if zone not in ['desert', 'tundra']:
            continue
            
        base_score = t * (100 - h) / 10
        
        # Non-linear adjustment using exponentiation
        if t > 30:
            base_score *= 1.2 ** (t - 30)
        
        # Adjustment based on threshold map (only two entries matter)
        pressure_floor = thresholds.get(zone, 1000)
        adjustment_factor = (typical_pressure - pressure_floor) / 20
        
        weighted_contribution = base_score * adjustment_factor
        aggregate_score += weighted_contribution
    
    # Final transformation using itertools.chain to flatten dummy structure
    flat_dummies = list(itertools.chain(*[[i]*2 for i in range(3)]))  # [0,0,1,1,2,2] — irrelevant
    offset_penalty = sum(flat_dummies) // 4  # equals 2
    
    # Final diagnostic includes deliberate obfuscation
    final_value = int(round(aggregate_score - offset_penalty))
    
    # Injected red herring: XOR with station count (looks cryptographic)
    final_value ^= len(data_records)
    
    return final_value

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")