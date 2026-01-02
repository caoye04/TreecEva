import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.6, 27.3, 26.8, 22.0, 20.5, 28.1, 29.4]
humidity_readings = [45, 52, 58, 61, 47, 55, 60, 50, 65, 70]
pressure_readings = [1013, 1015, 1012, 1008, 1005, 1009, 1011, 1014, 1007, 1003]

# Auxiliary metadata (mostly irrelevant)
sensor_ids = ['TH01', 'TH02', 'TH03', 'TH04', 'TH05', 'TH06', 'TH07', 'TH08', 'TH09', 'TH10']
locations = ['North', 'South', 'East', 'West', 'Center', 'Roof', 'Basement', 'Lab', 'Hall', 'Tower']
device_status = ['active', 'standby', 'active', 'active', 'error', 'active', 'standby', 'active', 'active', 'active']

# Distractor: unused transformation matrices
transform_A = [[1, 0], [0, 1]]
transform_B = [[0.98, 0.02], [0.03, 0.97]]
affine_offset = (0.1, -0.05)

# Irrelevant statistical counters
mode_counter = 0
median_tracker = []
entropy_approximation = 0.0

# Calibration parameters (only calibration_factor is relevant)
baseline_offset = 273.15
sampling_rate = 10  # Hz
calibration_factor = 0.89
smoothing_window = 3
noise_floor = 0.05

# Decoy function - appears useful but never called
def compute_thermal_index(temp, hum):
    return temp * (hum / 100) + 1.2

# Unused recursive helper for red herring
def binary_weight_sum(n):
    if n <= 1:
        return n
    return n % 2 + binary_weight_sum(n // 2)

# Real processing begins here
zipped_sensors = list(zip(temperature_readings, humidity_readings, pressure_readings, sensor_ids))

# Step 1: Filter out readings where temperature < 21 or status is not active (simulated via index)
filtered_data = []
for i, (temp, hum, pres, sid) in enumerate(zipped_sensors):
    loc_idx = i % len(locations)  # dummy assignment
    status = device_status[i] if i < len(device_status) else 'unknown'
    if temp >= 21 and status == 'active':
        filtered_data.append((temp, hum, pres))

# Step 2: Extract temperatures from filtered data
extracted_temps = [entry[0] for entry in filtered_data]

# Distractor: complex set operations with no impact
unique_temps = set(round(t) for t in extracted_temps)
even_hour_marks = {22, 24, 26, 28}
temp_categories = unique_temps & even_hour_marks  # intersection - misleading

# Step 3: Apply rolling average (relevant only to final step)
smoothed_temps = []
for j in range(len(extracted_temps)):
    start = max(0, j - smoothing_window + 1)
    segment = extracted_temps[start:j+1]
    avg = sum(segment) / len(segment)
    smoothed_temps.append(avg)

# Step 4: Compute weighted diagnostic score using calibration
aggregated_score = 0
for idx, val in enumerate(smoothed_temps):
    weight = 1 + (idx * 0.1)  # increasing importance over time
    adjusted = val * calibration_factor
    aggregated_score += adjusted * weight

# Step 5: Incorporate humidity deviation as secondary factor
reference_hum = 55
humidity_contributions = []
for _, hum, _ in filtered_data:
    deviation = abs(hum - reference_hum)
    normalized_dev = deviation / reference_hum
    humidity_contributions.append(normalized_dev)

# Distractor: use of itertools.cycle in a dead-end calculation
pulse_sequence = list(itertools.islice(itertools.cycle([1, -1]), len(humidity_contributions)))
dummy_signal = [a * b for a, b in zip(humidity_contributions, pulse_sequence)]

# Step 6: Final diagnostic computation
base_component = aggregated_score
penalty_component = sum(humidity_contributions) * 10
final_diagnostic = base_component - penalty_component

# Misleading print statements removed; only this matters
print(f"Target result: {final_diagnostic}")