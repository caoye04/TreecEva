from collections import defaultdict, Counter
import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 23.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 49]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1011]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = {'mode': 'legacy', 'override': False, 'calib_version': 'v2.1'}
device_compatibility_matrix = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]

# Misleading intermediate processing (dead path)
def legacy_calibrate(data):
    return [x * 0.98 for x in data]

# Unused transformation function (red herring)
def transform_to_zscore(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [(x - mean_val) / std_dev for x in values]

# Decoy metric calculation with no downstream impact
temp_zscores = transform_to_zscore(temperature_readings)
humidity_zscores = transform_to_zscore(humidity_readings)

# Real signal processing begins here
baseline_pressure = sum(pressure_readings[:3]) / 3
adjusted_temps = [round(t + (1013 - p) * 0.05, 2) for t, p in zip(temperature_readings, pressure_readings)]

def generate_phase_shift(sequence):
    """Apply cyclic phase shift based on index parity (bit manipulation logic)"""
    shifted = []
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            shifted.append(int(val * 2) & 0xFF)  # Bitwise AND as noise filter
        else:
            shifted.append(int(val * 1.5) | 0x0A)  # Bitwise OR for odd indices
    return shifted

def detect_anomalies(readings, threshold=1.5):
    """Detect outliers using rolling median (linear search variant)"""
    anomalies = []
    for i in range(2, len(readings)):
        window = readings[i-2:i+1]
        sorted_window = sorted(window)
        median = sorted_window[1]
        if abs(readings[i] - median) > threshold:
            anomalies.append(i)
    return anomalies if anomalies else [0]

# Anomaly detection on adjusted temperatures (used later)
temp_anomalies = detect_anomalies(adjusted_temps)

# Construct calibration sequence using itertools and list operations
calibration_indices = list(itertools.chain.from_iterable(
    [(i*2, i*2+1) for i in range(3) if i != temp_anomalies[0] % 3]
))

calibration_sequence = []
for idx in calibration_indices:
    if idx < len(adjusted_temps):
        calibration_sequence.append(adjusted_temps[idx])
    else:
        calibration_sequence.append(adjusted_temps[-1])

def evaluate_consistency(metrics):
    """Check numerical stability across metrics using boolean logic"""
    if not metrics:
        return False
    diffs = [abs(metrics[i+1] - metrics[i]) for i in range(len(metrics)-1)]
    return all(d < 1.0 for d in diffs) and len(metrics) >= 3

def aggregate_diagnostics(temp_data, hum_data):
    """Create diagnostic fingerprint using multiple assignment and tuple unpacking"""
    temp_stats = (min(temp_data), max(temp_data), round(sum(temp_data)/len(temp_data), 2))
    hum_stats = (min(hum_data), max(hum_data), round(sum(hum_data)/len(hum_data), 2))
    
    # Multiple simultaneous assignments (relevant)
    t_min, t_max, t_avg = temp_stats
    h_min, h_max, h_avg = hum_stats
    
    # Destructuring with irrelevant expansion
    spike_count = len([t for t in temp_data if t > t_avg + 0.5])
    stable_period = len(temp_data) - spike_count
    
    # Complex conditional expression (python idiom)
    risk_level = 'high' if (t_max > 25 and h_avg > 47) or spike_count > 2 else 'moderate' if t_avg > 24 else 'low'
    
    # Create composite diagnostic code (key result)
    diagnostic_code = int((t_avg * 100) + (h_avg * 10) + spike_count)
    
    # Dead code path: never executed due to constant condition (distractor)
    debug_snapshot = None
    if False:
        debug_snapshot = {
            'raw_temps': temperature_readings,
            'phase_shifted': generate_phase_shift(adjusted_temps),
            'distribution': Counter([int(t) for t in temp_data])
        }
    
    return diagnostic_code, risk_level, stable_period

def process_metrics(calib_seq, diagnostics):
    """Final processing with cross-concept integration"""
    # Unpacking returned tuple
    code, level, period = diagnostics
    
    # Build frequency map (collections.Counter)
    freq_map = Counter(calib_seq)
    
    # Identify dominant calibration value
    modal_value = freq_map.most_common(1)[0][0]
    
    # Apply non-linear adjustment
    adjusted_code = code
    if modal_value > 24.0:
        adjusted_code = int(adjusted_code * 1.05)
    elif modal_value < 23.0:
        adjusted_code = int(adjusted_code * 0.95)
    
    # Final bit manipulation (XOR with length-based mask)
    mask = (len(calib_seq) << 2) ^ 0xAA
    final_result = (adjusted_code ^ mask) + period
    
    # Red herring: unused conditional branch
    metadata_log = []
    if level == 'critical':
        metadata_log.append('EMERGENCY_OVERRIDE')
    
    return final_result

# Generate initial diagnostics (this matters)
diagnostics = aggregate_diagnostics(adjusted_temps, humidity_readings)

# Critical execution point
final_diagnostic = process_metrics(calibration_sequence, diagnostics)

# Print result as required
print(f"Target result: {final_diagnostic}")