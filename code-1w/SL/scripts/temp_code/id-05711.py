import math

# Simulated sensor data and configuration
def configure_sensors(calibration_mode=False):
    base_offsets = [0.1, -0.3, 0.25, 0.4]
    gain_factors = [1.05, 0.98, 1.02, 1.1]
    return dict(zip(['s1', 's2', 's3', 's4'], zip(base_offsets, gain_factors)))

# Irrelevant helper: used only in dead code path
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [(x - mean_val) / (max(data) - min(data)) for x in data]

# Misleading signal processor (dead function - never called)
def analyze_peaks(signal_list):
    peaks = []
    for i in range(1, len(signal_list) - 1):
        if signal_list[i] > signal_list[i-1] and signal_list[i] > signal_list[i+1]:
            peaks.append(i)
    return len(peaks) * 0.5

# Core logic: filtering and transformation
def filter_noise(signal, threshold):
    return [x for x in signal if abs(x) >= threshold]

# Signal enrichment with metadata (dictionary usage)
def enrich_data(cleaned, source_id):
    stats = {
        'count': len(cleaned),
        'sum': sum(cleaned),
        'energy': sum(x**2 for x in cleaned),
        'source': source_id
    }
    # Distractor computation
    temp_debug = [math.sin(x) for x in cleaned[:3]]
    _ = sum(temp_debug)  # unused
    return stats

# Main processing pipeline
def process_signals(threshold, raw_bundle):
    aggregated_energy = 0
    false_alarms = 0  # decoy counter

    config_map = configure_sensors()

    for sensor_id, readings in raw_bundle.items():
        offset, gain = config_map.get(sensor_id, (0.0, 1.0))

        # Apply gain and offset (calibration)
        calibrated = [gain * x + offset for x in readings]

        # Filter based on dynamic threshold
        filtered = filter_noise(calibrated, threshold)

        # Early exit condition (rare case - not triggered in this input)
        if len(filtered) == 0 and 'debug' in sensor_id:
            return -999

        # Enrich and extract energy
        enriched = enrich_data(filtered, sensor_id)
        energy_contribution = enriched['energy']

        # Conditional accumulation
        if energy_contribution > 50:
            aggregated_energy += int(energy_contribution // 10)
        else:
            aggregated_energy += int(energy_contribution // 5)

        # Decoy branch: never taken due to data
        if sensor_id.startswith('invalid'):
            false_alarms += 1

        # Bit manipulation red herring
        mask = 0b1101
        _ = energy_contribution ^ mask  # irrelevant

    # Complex conditional expression
    final_adjustment = (aggregated_energy if aggregated_energy % 2 == 0 
                        else (aggregated_energy + 1) * 1.5)

    # String-based switch (distractor)
    mode_flag = 'fast' if aggregated_energy > 100 else 'normal'
    scaling_factor = 1.0
    if 'fast' in mode_flag:
        temp_scale = ''.join([str(int(c) * 2) for c in '111'])  # '222'
        scaling_factor = 1.1

    # Final output calculation
    result = final_adjustment * scaling_factor

    # Key assignment point
    final_output = int(round(result))

    return final_output

# Global constants (some irrelevant)
MAX_BUFFER_SIZE = 1024
DEBUG_MODE = False
filter_threshold = 0.75

# Input data setup
raw_data = {
    's1': [2.1, -1.3, 0.4, 3.2, -0.1],
    's2': [1.8, -2.5, 0.6, 0.2],
    's3': [3.0, 1.1, -4.2, 0.8],
    's4': [-1.5, 2.7, 0.3, -3.1]
}

# Unused but plausible-looking data structure
auxiliary_logs = [
    {'event': 'init', 'ts': 1001, 'level': 'INFO'},
    {'event': 'poll', 'ts': 1005, 'level': 'DEBUG'}
]

# Trigger main computation
final_output = process_signals(filter_threshold, raw_data)
print(f"Result: {final_output}")