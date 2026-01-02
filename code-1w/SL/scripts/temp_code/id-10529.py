import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 22.3, 20.9, 26.1, 24.7, 23.0, 21.4]
humidity_readings = [45, 52, 58, 41, 60, 55, 39, 50, 53, 47]
pressure_readings = [1013, 1015, 1012, 1018, 1010, 1014, 1020, 1016, 1011, 1017]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.021
dummy_matrix = [[1.2, 3.4], [5.6, 7.8]]
scaling_factor = 1.0

# Misleading preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]  # Never used

# Unused transformation function (red herring)
def frequency_transform(seq):
    return [math.sin(x * 0.1) for x in seq]  # Computationally irrelevant

# Decoy statistical analysis (distractor computation)
mean_temp = sum(temperature_readings) / len(temperature_readings)
variance_proxy = sum((x - mean_temp) ** 2 for x in temperature_readings) / len(temperature_readings)
entropy_approx = math.log(variance_proxy) if variance_proxy > 0 else 0

# Real processing begins here
valid_indices = set(i for i, t in enumerate(temperature_readings) if 20 <= t <= 25)
humid_enough = set(i for i, h in enumerate(humidity_readings) if h >= 50)
stable_pressure_idx = set(i for i, p in enumerate(pressure_readings) if abs(p - 1015) <= 5)

# Critical intersection: only readings meeting all three conditions are valid
core_indices = valid_indices & humid_enough & stable_pressure_idx

# Construct filtered dataset using list comprehension with complex filtering
filtered_data = [
    {
        'temp': temperature_readings[i],
        'humidity': humidity_readings[i],
        'pressure': pressure_readings[i],
        'quality_score': int(humidity_readings[i] >= 50) + int(abs(pressure_readings[i] - 1015) <= 5)
    }
    for i in range(len(temperature_readings))
    if i in core_indices
]

# Threshold map includes decoy keys to mislead attention
threshold_map = {
    'temp_baseline': 22.0,
    'humidity_ceiling': 60,
    'pressure_stability': 4,
    'dummy_key_ignored': 999,  # Red herring
    'quality_floor': 1
}

# Spurious unrelated calculation (distractor)
aggregate_entropy = 0.0
for entry in filtered_data:
    if entry['temp'] > 21:
        aggregate_entropy += math.log(entry['temp'])

# Another dead-end function (misdirection)
def compute_shadow_index(data_list):
    if not data_list:
        return -1
    shadow = 0
    for d in data_list:
        shadow += d.get('pressure', 0) % 7
    return shadow * 0.1  # Never called

# Real analysis logic
quality_sum = sum(entry['quality_score'] for entry in filtered_data)

# Conditional override simulation (irrelevant path)
simulated_override = False
override_value = -999
if quality_sum > 100:
    simulated_override = True  # This will never trigger
    override_value = 42

# Actual diagnostic computation
base_diagnostic = 0
for reading in filtered_data:
    base_diagnostic += int(reading['temp'] * (reading['humidity'] / 10))

# Secondary adjustment based on pressure consistency
pressure_consistency = all(
    abs(entry['pressure'] - 1015) <= threshold_map['pressure_stability']
    for entry in filtered_data
)

adjustment_factor = 2 if pressure_consistency else 1
final_diagnostic = base_diagnostic * adjustment_factor

# Spurious print statements (noise)
# print(f"Entropy: {entropy_approx}")
# print(f"Shadow Index would be: {compute_shadow_index(filtered_data)}")

# Critical output
print(f"Result: {final_diagnostic}")