import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 26.7, 18.9, 20.2]
humidity_readings = [45, 52, 58, 61, 48, 55, 67, 70]
pressure_readings = [1013, 1015, 1010, 1008, 1017, 1020, 1005, 1003]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G5', 'H3']
station_names = ['North Ridge', 'East Bay', 'West Hill', 'South Point',
                  'Central Outpost', 'Upper Slope', 'Lower Basin', 'Mid Zone']

# Mapping station indices to maintenance cycles (unused red herring)
maintenance_schedule = {i: (i * 7 + 3) % 28 for i in range(8)}

# Data transformation: normalize and combine relevant readings
def normalize(values):
    mean_val = sum(values) / len(values)
    return [(v - mean_val) for v in values]

def filter_outliers(values, threshold=2.0):
    normalized = normalize(values)
    return [v for v, n in zip(values, normalized) if abs(n) < threshold]

# Irrelevant string processing (distractor)
def generate_status_tag(station_idx):
    code = legacy_codes[station_idx]
    name_part = station_names[station_idx][:2].upper()
    return f"{name_part}-{code}-{math.floor(humidity_readings[station_idx])}"

# Real processing begins here
filtered_temp = filter_outliers(temperature_readings)
filtered_humid = filter_outliers(humidity_readings)
filtered_press = filter_outliers(pressure_readings)

# Create composite dataset using tuple packing
raw_data_packets = []
for i in range(min(len(filtered_temp), len(filtered_humid), len(filtered_press))):
    packet = (
        filtered_temp[i],
        filtered_humid[i],
        filtered_press[i],
        generate_status_tag(i)  # included but not used in final logic
    )
    raw_data_packets.append(packet)

# Unused set operation (misleading intermediate)
active_tags = {packet[3] for packet in raw_data_packets}
duplicate_check = len(active_tags) != len(raw_data_packets)

# Process only numerical components
deep_processed = []
for temp, humid, press, tag in raw_data_packets:
    # Apply heat index approximation (real calculation)
    hi = temp + 0.55 * (6.11 * math.exp(5418 * (1/273 - 1/(273+temp))) - 10)
    # Normalize pressure relative to standard (1013.25 hPa)
    pn = (press - 1013.25) / 1013.25
    # Weighted environmental stress index
    esi = 0.6 * hi + 0.3 * humid + 0.1 * (100 * abs(pn))
    deep_processed.append(round(esi, 3))

# Threshold configuration map (critical for analysis)
threshold_map = {
    'warning': 28.5,
    'alert': 32.0,
    'critical': 35.0
}

# Unused dictionary transformation (red herring)
summary_stats = {
    'avg_stress': sum(deep_processed) / len(deep_processed),
    'max_stress': max(deep_processed),
    'min_stress': min(deep_processed),
    'variance': sum((x - sum(deep_processed)/len(deep_processed))**2 for x in deep_processed) / len(deep_processed)
}

# Destructuring assignment with irrelevant expansion
current_stress_level = deep_processed[-1]
*historical, latest = deep_processed  # tuple unpacking

# Linear search through processed values (relevant)
def count_exceedances(data, limit):
    count = 0
    for val in data:
        if val > limit:
            count += 1
    return count

exceed_alert = count_exceedances(deep_processed, threshold_map['alert'])
exceed_warning = count_exceedances(deep_processed, threshold_map['warning'])

# Main analysis function with dictionary-based decision logic
def analyze_readings(stress_values, thresholds):
    warning_level = thresholds['warning']
    alert_level = thresholds['alert']
    critical_level = thresholds['critical']
    
    # Compute cumulative risk score (actual answer source)
    base_score = 0
    for val in stress_values:
        if val >= critical_level:
            base_score += 5
        elif val >= alert_level:
            base_score += 3
        elif val >= warning_level:
            base_score += 1
    
    # Additional penalty factors (nested logic)
    length_factor = len(stress_values) // 3
    peak_factor = int(max(stress_values) // 10)
    trend = stress_values[-1] - stress_values[0]
    trend_penalty = 2 if trend > 3 else (1 if trend > 1 else 0)
    
    final_risk = base_score * (1 + 0.1 * length_factor) + peak_factor + trend_penalty
    
    # Dead code branch (decoy)
    if False:
        fallback = 0
        for ch in str(int(sum(stress_values)))):
            if int(ch) % 2 == 0:
                fallback += 1
        return fallback
    
    # Actual return
    return round(final_risk, 4)

# Processed data used in final call
processed_data = deep_processed

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

print(f"Result: {final_diagnostic}")