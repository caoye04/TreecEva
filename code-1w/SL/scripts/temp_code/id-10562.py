def analyze_sensor(node_id, readings):
    """Irrelevant helper that looks important but isn't used."""
    return sum(readings) / len(readings)


def transform_signal(signal_data, factor=1.5):
    """Distractor function: transforms signal but not part of main logic."""
    return [x * factor for x in signal_data if x > 0]

# Unused constants (red herring)
CALIBRATION_OFFSET = -0.75
MAX_TOLERANCE = 98.6
RETRY_LIMIT = 3

# Simulated sensor data with mixed types (some relevant, some not)
sensor_nodes = ['A1', 'B2', 'C3', 'D4']
temp_readings = [23.5, 24.1, 19.8, 22.0, 25.3, 18.7, 20.2, 21.9]
humidity_readings = [45, 48, 55, 60, 52, 44, 50, 53]
pressure_readings = [1013, 1015, 1009, 1018, 1020, 1010, 1014, 1016]

# Misleading intermediate computation (dead path)
avg_pressure = sum(pressure_readings) / len(pressure_readings)
adjusted_humidity = [h - 5 for h in humidity_readings if h > 40]

# Key data structure: list of tuples with sensor ID and composite score
node_diagnostics = []
for i, node in enumerate(sensor_nodes):
    temp_index = i * 2  # Indexing pattern
    score = (temp_readings[temp_index] * 1.2) + (humidity_readings[temp_index] * 0.8)
    node_diagnostics.append((node, score))

# Red herring: complex-looking transformation with no impact
decoy_map = {node: round(score ** 0.5, 3) for node, score in node_diagnostics}

# Real processing begins: filter nodes above threshold
threshold_map = {'A1': 45.0, 'B2': 46.0, 'C3': 44.0, 'D4': 47.0}
filtered_data = []

for label, value in node_diagnostics:
    baseline = threshold_map[label]
    if value > baseline:
        # Apply non-linear correction
        corrected = (value - baseline) ** 2 + 10
        filtered_data.append(corrected)

# Secondary distractor: unused recursive function
def recursive_sum(arr, n=-1):
    if n == -1: n = len(arr)
    if n == 0: return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# Linear search for anomalies (partially relevant)
anomaly_flags = []
for val in temp_readings[:6]:
    if val < 20.0 or val > 25.0:
        anomaly_flags.append(True)
    else:
        anomaly_flags.append(False)

# Another red herring: zip and enumerate on unrelated data
zipped_meta = list(zip(enumerate(temp_readings[::2]), humidity_readings))
processed_metas = []
for (idx, temp), humid in zipped_meta:
    processed_metas.append(f'{node_diagnostics[idx][0]}:{temp+huminf}')

# Core logic: process only filtered_data through final function
def process_readings(data_list, config):
    total = 0.0
    for val in data_list:
        if val < 15.0:
            total += val * 1.1
        elif val >= 15.0 and val < 25.0:
            total += val * 1.3
        else:
            total += val * 0.9  # Dominant path
    return int(total)  # Final result is integer

# Execution point of interest
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print required output
print(f"Result: {final_diagnostic}")