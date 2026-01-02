import itertools

# Simulated sensor fusion module for environmental monitoring system
def collect_sensor_data():
    raw_sequences = [
        [1.2, 0.9, 1.5, 2.1, 1.8, 2.4, 3.0, 2.7],
        [0.8, 1.1, 1.0, 0.7, 0.5, 0.6, 0.9, 1.3],
        [2.5, 2.7, 2.3, 2.6, 2.8, 2.4, 2.2, 2.9]
    ]
    labels = ['temp', 'humidity', 'pressure']
    labeled_data = {labels[i]: raw_sequences[i] for i in range(len(labels))}
    return labeled_data

# Irrelevant transformation - simulates unused calibration routine
def calibrate_sensors(data_map, factor=1.05):
    calibrated = {}
    for key, values in data_map.items():
        calibrated[key] = [v * factor for v in values]
    temp_snapshot = calibrated['temp'][:]
    humidity_offset = sum(temp_snapshot) / len(temp_snapshot)
    return calibrated  # dead return, not used

# Filtering logic with red herring conditions
def filter_anomalies(seq, low_bound=0.6, high_bound=2.5):
    cleaned = []
    anomaly_flags = []
    for idx, val in enumerate(seq):
        if low_bound <= val <= high_bound:
            cleaned.append(val)
            anomaly_flags.append(False)
        else:
            cleaned.append(None)
            anomaly_flags.append(True)
    validated = [x for x in cleaned if x is not None]
    return validated

# Decoy function - appears important but unused in final flow
def compute_rolling_average(data, window=3):
    rolled = []
    for i in range(len(data) - window + 1):
        window_avg = sum(data[i:i+window]) / window
        rolled.append(round(window_avg, 3))
    return rolled

# Core processing with distractors and set operations
def process_readings(dataset, config_map):
    temp_data = dataset['temp']
    hum_data = dataset['humidity']
    pres_data = dataset['pressure']

    # Distractor: complex but unused aggregation
    all_pairs = list(itertools.product(temp_data[:4], hum_data[:4]))
    pair_summaries = [{'sum': a+b, 'diff': abs(a-b)} for a, b in all_pairs]
    significant_pairs = [p for p in pair_summaries if p['sum'] > 2.0]

    # Real logic begins: apply dynamic thresholds from config
    threshold_set = set(config_map.values())
    base_ref = config_map['temp_min']
    adjusted_values = []

    for reading in temp_data:
        if reading > base_ref:
            adjusted_values.append(reading ** 1.1)
        else:
            adjusted_values.append(reading ** 0.9)

    # Use set difference to exclude outlier influences (real step)
    valid_range_set = set(range(int(min(threshold_set)), int(max(threshold_set)) + 1))
    influence_mask = set([int(x) for x in hum_data if x < 1.0])
    net_influences = valid_range_set - influence_mask  # meaningful operation

    # Secondary transformation on pressure (distractor)
    pressure_mods = {i: pres_data[i] % 1.5 for i in range(len(pres_data))}
    mod_values = list(pressure_mods.values())
    sorted_mods = sorted(mod_values, reverse=True)

    # Key computation path
    growth_factor = len(net_influences) * 0.75
    signal_energy = sum([x * growth_factor for x in adjusted_values])

    # Final diagnostic calculation (answer point)
    final_diagnostic = int(round(signal_energy + len(significant_pairs) * 0.1 - sum(sorted_mods[:2])))
    return final_diagnostic

# Bootstrap execution sequence
data_pool = collect_sensor_data()

# Dead code path - simulates configuration validation
config_specs = {
    'calibration_needed': False,
    'version': '2.1a',
    'temp_min': 1.0,
    'humid_optimal': 0.8,
    'pressure_adj': 2.5
}

# Unused alternate filtering
if config_specs['calibration_needed']:
    data_pool = calibrate_sensors(data_pool)

# Apply real filtering on each stream (only temp matters in end-to-end)
filtered_data = {}
for key, values in data_pool.items():
    filtered_data[key] = filter_anomalies(values)

# Threshold map used in process_readings
threshold_map = {
    'temp_min': 1.0,
    'bound_high': 2.5,
    'scale_factor': 1.8
}

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)
print(f"Result: {final_diagnostic}")