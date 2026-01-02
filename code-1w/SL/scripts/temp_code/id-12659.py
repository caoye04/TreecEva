import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 22.7, 25.3, 20.4, 21.9, 26.0, 24.8, 23.0]
humidity_readings = [45, 50, 55, 60, 65, 70, 52, 48, 58, 63]
pressure_readings = [1013, 1015, 1010, 1020, 1008, 1018, 1012, 1016, 1009, 1014]

# Irrelevant transformation: normalize humidity to arbitrary scale (distractor)
normalized_humidity = [(h - 30) / 70 for h in humidity_readings]

# Misleading intermediate: compute dew point approximations (unused later)
dew_points = [temp - ((100 - hum) / 5) for temp, hum in zip(temperature_readings, humidity_readings)]

# Decoy function: appears useful but never called
def analyze_trend(data):
    return sum(1 for i in range(1, len(data)) if data[i] > data[i-1])

# Real processing begins: flag anomalous temperatures
anomaly_threshold = 25.0
anomalous_mask = [temp > anomaly_threshold for temp in temperature_readings]

# Use list comprehension with zip to pair data (core step)
sensor_tuples = list(zip(temperature_readings, humidity_readings, pressure_readings, anomaly_mask))

# Filter only non-anomalous readings using itertools and condition (key filtering)
filtered_data = [s for s in sensor_tuples if not s[3]]

# Extraneous bit manipulation: rotate pressure values (red herring)
rotated_pressures = [(p << 1 | p >> 11) & 0xFFF for p in pressure_readings]

# Dummy aggregation: sum of squared normalized humidity (dead end)
sum_sq_norm_hum = sum(x**2 for x in normalized_humidity)

# Core diagnostic logic
bit_flags = []
for temp, hum, press, is_ano in filtered_data:
    # Compute composite index with bitwise mix
    temp_code = int(temp * 10) & 0xFF
    hum_code = hum & 0xFF
    flag = (temp_code ^ hum_code) >> 4
    bit_flags.append(flag)

# Another decoy: attempt clustering via string conversion (irrelevant)
cluster_labels = [str(f).zfill(2) + 'X' for f in bit_flags]

# Real reduction: fold flags using XOR folding
folded_diagnostic = 0
for b in bit_flags:
    folded_diagnostic ^= b

# Secondary processing path: emulate checksum on original indices (unused alternative)
index_checksum = sum(i * p for i, p in enumerate(pressure_readings)) % 1000

# Final processing function
def process_readings(data):
    base_value = 0
    for entry in data:
        t, h, p, _ = entry
        # Mix arithmetic and bitwise ops
        contribution = (int(t) << 2) ^ (h | (p & 0xFF))
        base_value += contribution % 97
    return base_value * len(bit_flags)  # depends on outer scope (intentional)

# Critical execution point
final_diagnostic = process_readings(filtered_data)

# Output result as required
print(f"Result: {final_diagnostic}")