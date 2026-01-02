import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.4, 25.1, 19.8, 27.6, 30.2, 22.7, 26.3, 28.9, 24.5, 21.0, 31.5, 20.8]
humidity_readings = [45, 52, 61, 48, 39, 57, 50, 44, 55, 60, 38, 53]
pressure_readings = [1013, 1015, 1012, 1008, 1017, 1010, 1005, 1014, 1011, 1009, 1007, 1016]

# Irrelevant auxiliary arrays (distractors)
elevation_zones = [120, 180, 95, 210, 75, 135, 160, 88, 205, 110, 65, 140]
wind_speeds_kmh = [12.5, 18.3, 9.7, 15.6, 22.1, 11.4, 16.8, 13.9, 17.2, 10.8, 24.3, 14.1]

# Misleading preprocessing with dead-end transformations
adjusted_temps = [round(t * 1.02 + 0.3) for t in temperature_readings]  # Distractor
normalized_humidity = [h / 100 for h in humidity_readings]  # Not used later

# Key processing: identify anomalous readings above thresholds
baseline_thresholds = {
    'temp_high': 27.0,
    'humidity_low': 45,
    'pressure_trend': -5
}

# Complex filtering with slicing and shifting windows
recent_slice = temperature_readings[-8:]  # Last 8 readings
window_averages = []
for i in range(len(recent_slice) - 3):
    window_averages.append(sum(recent_slice[i:i+4]) / 4)

# Secondary derived metric (red herring)
avg_stability_index = sum(abs(window_averages[i+1] - window_averages[i]) for i in range(len(window_averages)-1)) / len(window_averages)

# Actual signal extraction path
def detect_spikes(data, limit):
    spikes = []
    for i in range(1, len(data)-1):
        if data[i] > data[i-1] and data[i] > data[i+1] and data[i] > limit:
            spikes.append(i)
    return spikes

thermal_spike_indices = detect_spikes(temperature_readings, baseline_thresholds['temp_high'])

# Decoy function that looks important but isn't used
def calculate_entropy(seq):
    freqs = {}
    for val in seq:
        freqs[val] = freqs.get(val, 0) + 1
    probs = [f/len(seq) for f in freqs.values()]
    return -sum(p * math.log2(p) for p in probs)

# Real processing begins: filter data based on spike locations
filtered_data = [temperature_readings[i] for i in thermal_spike_indices]

# Generate threshold map using bitwise logic on truncated integers (advanced distractor)
bit_flags = 0
for temp in filtered_data:
    bit_flags |= int(temp) << 2

flag_analysis = ((bit_flags & 0xFF) ^ 0xAA) | 0x0F  # Obfuscated computation

# Threshold derivation via integer division and rounding
derived_level = round((flag_analysis / 4) // 1.75)

# Create threshold map (only 'level' is used later)
threshold_map = {
    'level': derived_level,
    'pattern': bin(flag_analysis)[2:],
    'score': flag_analysis % 100  # Dead-end variable
}

# Secondary irrelevant transformation chain
compressed_stream = ''
for h, p in zip(humidity_readings, pressure_readings):
    compressed_stream += f'{h:x}{p:o}'  # Hex + octal string mashup
summary_hash = len(compressed_stream) % 1000  # Unused result

# Core diagnostic processor (only uses filtered_data and threshold_map['level'])
def process_readings(readings, config_map):
    if not readings:
        return 0
    
    # Multi-step normalization
    base_ref = sum(readings) / len(readings)
    adjusted_ref = base_ref - 273.15 if base_ref > 100 else base_ref
    
    # Apply threshold logic
    trigger_count = 0
    for val in readings:
        if val > adjusted_ref + (config_map['level'] / 10):
            trigger_count += 1
    
    # Final transformation with slicing-based weighting
    weights = [0.8, 1.0, 1.2][:len(readings)] + [1.0] * max(0, len(readings) - 3)
    weighted_avg = sum(readings[i] * weights[i] for i in range(len(readings))) / sum(weights)
    
    # Critical output formula
    return int(weighted_avg * 100) + trigger_count * 10

# Execute key statement
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print final result as required
print(f"Result: {final_diagnostic}")