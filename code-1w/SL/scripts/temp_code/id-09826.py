import math

# Sensor calibration constants (some are decoys)
CALIBRATION_A = 0.872
CALIBRATION_B = 1.045
UNUSED_CALIBRATION_X = 2.991
UNUSED_CALIBRATION_Y = 0.0034

# Simulated environmental sensor readings over time
time_series_data = [
    [1.2, 0.9, 1.4, 2.1, 1.8],
    [0.8, 1.1, 1.3, 1.0, 0.7],
    [2.3, 2.5, 2.1, 2.4, 2.6],
    [1.0, 0.8, 1.1, 1.3, 1.2]
]

# Irrelevant auxiliary data - red herring
device_metadata = {
    'serial': 'SN7890-XYZ',
    'firmware': 'v2.3.1',
    'location_id': 405,
    'last_sync': '2023-08-14'
}

# Misleading intermediate processing function (never called)
def legacy_process(x):
    return [val ** 0.5 for val in x if val > 1.0]

# Unused transformation matrix
TRANSFORMATION_MATRIX = [
    [0.9, 0.1],
    [0.2, 0.8]
]

# Core processing pipeline

def filter_outliers(readings, threshold=1.8):
    """Filter values above threshold; used in main flow"""
    filtered = []
    for segment in readings:
        clean_segment = [val for val in segment if val <= threshold]
        filtered.append(clean_segment)
    return filtered

def compute_rolling_average(data, window=2):
    """Compute rolling average within each sublist"""
    averages = []
    for series in data:
        if len(series) < window:
            continue
        avg_window = [sum(series[i:i+window]) / window for i in range(len(series) - window + 1)]
        averages.extend(avg_window)
    return averages

def apply_calibration(signal_list, mode='A'):
    """Apply calibration based on mode"""
    factor = CALIBRATION_A if mode == 'A' else CALIBRATION_B
    return [x * factor for x in signal_list]

# Decoy function that looks important but isn't used
def encrypt_sequence(seq):
    encrypted = 0
    for i, val in enumerate(seq):
        encrypted += int(val * 100) << i
    return hex(encrypted)

# Main analysis logic
def generate_diagnostics(logs):
    # Step 1: Filter outlier sensor spikes
    cleaned_logs = filter_outliers(logs)
    
    # Step 2: Compute rolling statistics
    moving_averages = compute_rolling_average(cleaned_logs)
    
    # Step 3: Apply primary calibration
    calibrated_signals = apply_calibration(moving_averages, mode='A')
    
    # Step 4: Detect valid signal peaks
    peak_count = 0
    cumulative_energy = 0.0
    for sig in calibrated_signals:
        if sig > 1.05:  # Threshold for valid detection
            peak_count += 1
            cumulative_energy += sig
    
    # Step 5: Generate diagnostic score
    if peak_count == 0:
        return 0.0
    base_score = cumulative_energy / peak_count
    
    # Step 6: Apply logarithmic normalization
    normalized_diagnostic = math.log(base_score * 2.718)  # Add Euler's number to obscure logic
    
    # Step 7: Round to nearest integer for final reporting
    return int(round(normalized_diagnostic))

# Unused recursive function - red herring
def fibonacci_threshold(n, limit=10):
    if n <= 1 or limit <= 0:
        return n
    return fibonacci_threshold(n-1, limit-1) + fibonacci_threshold(n-2, limit-1)

# Simulate raw log preprocessing (this is actually used)
raw_anomalies = [item for sublist in time_series_data for item in sublist if item > 2.0]
processed_logs = filter_outliers(time_series_data)

# Additional distraction: unused list of status codes
SYSTEM_STATUS_CODES = {
    200: 'OK',
    409: 'Conflict',
    503: 'Unavailable',
    777: 'CalibrationLocked',
    999: 'DiagnosticOverride'
}

# Critical execution point
final_diagnostic = generate_diagnostics(processed_logs)
print(f"Result: {final_diagnostic}")