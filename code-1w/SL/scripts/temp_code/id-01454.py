from collections import defaultdict, Counter
import itertools

# Simulated sensor data from multiple environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 61, 48, 55, 59, 43, 50, 54, 47]
pressure_readings = [1013, 1015, 1010, 1018, 1012, 1009, 1020, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7X', 'B9Y', 'C3Z', 'D8W', 'E2V']
lookup_matrix = [[i * j for j in range(5)] for i in range(5)]

# Mapping station IDs to regions (partially relevant)
station_regions = {
    'S01': 'North', 'S02': 'South', 'S03': 'East', 'S04': 'West', 'S05': 'Central'
}

# Misleading transformation (dead path)
def transform_legacy(code):
    return ''.join(sorted(code))

transformed_codes = [transform_legacy(c) for c in legacy_codes]  # Dead computation

# Real processing begins here
raw_data_stream = list(zip(temperature_readings, humidity_readings, pressure_readings))

# Add synthetic timestamps (irrelevant but plausible)
timestamps = [1640995200 + i*3600 for i in range(len(raw_data_stream))]

# Augment with dummy metadata
enriched_data = []
for ts, (temp, hum, pres) in zip(timestamps, raw_data_stream):
    enriched_data.append({
        'timestamp': ts,
        'temp_c': temp,
        'humidity_pct': hum,
        'pressure_hpa': pres,
        'status': 'valid' if temp > 20 else 'caution'  # Status not used later
    })

# Filter out readings below threshold (relevant filtering)
filtered_data = [entry for entry in enriched_data if entry['temp_c'] >= 21.0]

# Decoy statistical analysis (distractor)
avg_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_variance = sum((p - avg_pressure) ** 2 for p in pressure_readings) / len(pressure_readings)

# Threshold configuration map (critical for final result)
threshold_map = defaultdict(dict)
threshold_map['temp']['warning'] = 24.0
threshold_map['temp']['critical'] = 25.5
threshold_map['humidity']['high'] = 50

# Another red herring: unused string manipulation
delimiter = '-'.join(['X' * 3, 'Y' * 2])  # 'XXX-YY'
split_parts = delimiter.split('-')
recombined = ''.join(reversed(split_parts))  # 'YYXXX' – never used

# Core logic disguised among distractions
def analyze_trend(data_list):
    temps = [d['temp_c'] for d in data_list]
    diffs = [b - a for a, b in zip(temps, temps[1:])]
    return sum(1 for d in diffs if d > 0)

# Secondary unused function (misleading)
def calculate_dew_point(temp, humidity):
    return temp - ((100 - humidity) / 5)

# Real processing function
def process_readings(readings, thresholds):
    count_critical_temp = 0
    count_high_humidity = 0
    
    for reading in readings:
        temp = reading['temp_c']
        humidity = reading['humidity_pct']
        
        # Relevant conditions
        if temp > thresholds['temp']['critical']:
            count_critical_temp += 1
        if humidity > thresholds['humidity']['high']:
            count_high_humidity += 1
    
    # Diagnostic score calculation (actual answer source)
    base_score = count_critical_temp * 1000
    adjustment = count_high_humidity * 17
    penalty = len([r for r in readings if r['pressure_hpa'] < 1012]) * 3
    
    # Dummy use of itertools (plausible but irrelevant)
    combinations = list(itertools.combinations(['A','B','C'], 2))
    offset = len(combinations) * 0  # Always zero, but looks meaningful
    
    result = base_score + adjustment - penalty + offset
    return result

# Trigger decoy computations to increase interference
dew_points = [calculate_dew_point(t, h) for t, h in zip(temperature_readings[:3], humidity_readings[:3])]

temp_trend = analyze_trend(enriched_data)  # Used nowhere

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output the target result
print(f"Result: {final_diagnostic}")