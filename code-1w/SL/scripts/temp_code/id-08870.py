import math

# Simulated sensor array data from environmental monitoring stations
temperature_readings = [23.5, 19.0, 27.3, 22.1, 30.5, 18.2, 25.7, 24.3, 20.8, 26.9]
humidity_readings = [45, 60, 52, 67, 33, 70, 58, 48, 63, 55]
pressure_readings = [1013, 1009, 1015, 1020, 1005, 1018, 1010, 1014, 1007, 1016]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G3', 'H6', 'I5', 'J0']
lookup_map = {code: idx * 1.5 for idx, code in enumerate(legacy_codes)}

# Misleading transformation chain (dead path)
transformed_codes = list(map(lambda x: x.lower().replace('a', 'z'), legacy_codes))
decoded_values = [sum(ord(c) for c in code) for code in transformed_codes]
aggregated_hash = sum(decoded_values) % 1000

# Real processing begins
valid_indices = []
for i in range(len(temperature_readings)):
    if temperature_readings[i] > 20 and humidity_readings[i] < 65:
        valid_indices.append(i)

# Secondary filter based on pressure trend (consecutive rising)
stable_pressure_count = 0
for j in range(1, len(pressure_readings)):
    if pressure_readings[j] >= pressure_readings[j-1]:
        stable_pressure_count += 1

# Only use indices where both temp/humidity and pressure trend align
filtered_indices = [i for i in valid_indices if i < stable_pressure_count]

# Extract filtered sensor data
filtered_data = []
for idx in filtered_indices:
    record = {
        'temp': temperature_readings[idx],
        'hum': humidity_readings[idx],
        'press': pressure_readings[idx]
    }
    filtered_data.append(record)

# Decoy function (never called)
def analyze_legacy_pattern(data):
    total = 0
    for item in data:
        if item['temp'] > 25:
            total += int(item['hum'] * 0.7)
    return total * 1.2

# Unused statistical summary (distractor)
mean_temp = sum(temperature_readings) / len(temperature_readings)
median_hum = sorted(humidity_readings)[len(humidity_readings)//2]
max_pressure = max(pressure_readings)

# Core processing function with slicing and lambda
adjustment_factor = lambda x: round(math.log(x['temp']) * (x['hum'] / 10), 4)

def process_readings(readings):
    if not readings:
        return 0.0
    
    # Apply adjustment using lambda and collect diagnostics
    diagnostics = []
    for entry in readings:
        adj = adjustment_factor(entry)
        adjusted_value = entry['temp'] + adj
        diagnostics.append(adjusted_value)
    
    # Use slicing to exclude first and last (edge instability)
    trimmed_diagnostics = diagnostics[1:-1] if len(diagnostics) > 2 else diagnostics
    
    # Final aggregation
    if trimmed_diagnostics:
        final_score = sum(trimmed_diagnostics) / len(trimmed_diagnostics)
    else:
        final_score = diagnostics[0] if diagnostics else 0.0
    
    # Additional red herring: complex bit manipulation with no effect
    magic_offset = 0
    for d in diagnostics:
        bits = int(d * 100) ^ 0xFF
        magic_offset += (bits >> 2) & 0x3F
    
    # Actual return (magic_offset is ignored)
    return round(final_score, 4)

# Key execution point
final_diagnostic = process_readings(filtered_data)

# Output result as required
print(f"Target result: {final_diagnostic}")