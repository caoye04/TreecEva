import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [45, 48, 50, 55, 60, 53, 49, 51]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1009, 1011, 1014]

# Irrelevant auxiliary metrics (distractor variables)
wind_speed_estimates = [12.3, 14.1, 11.8, 16.5, 18.2, 13.4, 10.9, 15.7]
luminosity_samples = [8900, 9100, 8700, 9200, 9400, 8800, 8500, 9000]

# Noise injection function (dead code path - never called)
def apply_noise_filter(data, intensity=0.5):
    return [x + random.gauss(0, intensity) for x in data]

# Data transformation pipeline
def normalize_sensor_data(raw_values):
    min_val, max_val = min(raw_values), max(raw_values)
    return [(x - min_val) / (max_val - min_val) for x in raw_values]

def compute_moving_average(data, window=3):
    smoothed = []
    for i in range(len(data)):
        start = max(0, i - window + 1)
        smoothed.append(sum(data[start:i+1]) / (i - start + 1))
    return smoothed

# Red herring: unused complex transformation
def frequency_domain_analysis(signal):
    n = len(signal)
    transformed = [0] * n
    for k in range(n):
        real = sum(signal[t] * math.cos(2 * math.pi * k * t / n) for t in range(n))
        imag = sum(-signal[t] * math.sin(2 * math.pi * k * t / n) for t in range(n))
        transformed[k] = math.sqrt(real**2 + imag**2)
    return transformed

# Core processing functions
def extract_anomalies(readings, multiplier=1.5):
    median_val = sorted(readings)[len(readings)//2]
    mad = sorted([abs(x - median_val) for x in readings])[len(readings)//2]
    threshold = multiplier * mad
    return [i for i, x in enumerate(readings) if abs(x - median_val) > threshold]

def categorize_trend(values):
    if len(values) < 2:
        return 'insufficient'
    direction = 'rising' if values[-1] > values[0] else 'falling' if values[-1] < values[0] else 'stable'
    volatility = sum(abs(values[i+1] - values[i]) for i in range(len(values)-1)) / len(values)
    if volatility > 1.0:
        return direction + '_volatile'
    return direction

def integrate_multi_source(temp_data, hum_data, pres_data):
    # Normalize all sensor streams
    norm_temp = normalize_sensor_data(temp_data)
    norm_hum = normalize_sensor_data(hum_data)
    norm_pres = normalize_sensor_data(pres_data)
    
    # Compute composite index with weighted fusion
    composite = []
    weights = {'temp': 0.4, 'hum': 0.3, 'pres': 0.3}
    for t, h, p in zip(norm_temp, norm_h, norm_pres):
        fused = weights['temp'] * t + weights['hum'] * h + weights['pres'] * p
        composite.append(round(fused, 6))
    
    # Apply moving average filter
    filtered_composite = compute_moving_average(composite, window=2)
    
    # Extract trend pattern
    trend_category = categorize_trend(filtered_composite)
    
    # Identify anomalous indices
    anomalies = extract_anomalies(filtered_composite)
    
    return {
        'fused_signal': filtered_composite,
        'trend': trend_category,
        'outliers': anomalies,
        'length': len(filtered_composite),
        'version': '2.1'
    }

# Decoy function that processes unrelated data (never invoked)
def simulate_prediction_model(dataset):
    training_seq = [math.sin(i * 0.5) + 0.1*i for i in range(20)]
    forecast = [training_seq[-1] + 0.05 for _ in range(5)]
    confidence = sum(math.exp(-abs(x)) for x in forecast) / len(forecast)
    return {'projections': forecast, 'reliability': confidence}

# Threshold configuration map for diagnostic engine
threshold_map = {
    'critical': 0.85,
    'elevated': 0.65,
    'normal': 0.45,
    'low': 0.25
}

# Misleading intermediate calculation (dead computation)
baseline_correction = {
    'offset_thermal': 0.15,
    'offset_hygrometric': 0.08,
    'compensation_factor': 1.02
}
adjusted_offsets = {k: v * 1.1 for k, v in baseline_correction.items()}
discarded_intermediate = sum(adjusted_offsets.values()) * 0.5  # Unused result

# Process the primary sensor inputs
processed_data = integrate_multi_source(
    temperature_readings, 
    humidity_readings, 
    pressure_readings
)

# Secondary derived metrics (some used, some not)
statistical_moments = {
    'skewness_hint': (sum((x - sum(processed_data['fused_signal'])/len(processed_data['fused_signal']))**3 
                        for x in processed_data['fused_signal']) / len(processed_data['fused_signal'])) ** (1/3),
    'kurtosis_proxy': sum((x - sum(processed_data['fused_signal'])/len(processed_data['fused_signal']))**4 
                         for x in processed_data['fused_signal']) / len(processed_data['fused_signal'])
}

# Another red herring: set operations with no downstream effect
duplicate_check_set = set()
sequence_tracker = set()
for idx, val in enumerate(processed_data['fused_signal']):
    rounded_val = round(val, 3)
    if rounded_val in duplicate_check_set:
        sequence_tracker.add(idx)
    duplicate_check_set.add(rounded_val)

snapshot_registry = {'entry_' + str(i): True for i in range(len(processed_data['fused_signal']))}
validity_flags = {k: v for k, v in snapshot_registry.items() if 'entry_' in k}  # Unused dict comprehension

# Diagnostic analysis engine
def analyze_readings(system_state, thresholds):
    signal = system_state['fused_signal']
    trend = system_state['trend']
    outliers = system_state['outliers']
    
    # Calculate key health indicators
    mean_level = sum(signal) / len(signal)
    peak_value = max(signal)
    has_outliers = len(outliers) > 0
    
    # Determine severity category
    if peak_value > thresholds['critical']:
        severity = 'critical'
    elif mean_level > thresholds['elevated']:
        severity = 'elevated'
    elif mean_level > thresholds['normal']:
        severity = 'normal'
    else:
        severity = 'low'
    
    # Additional context from trend
    if 'volatile' in trend and severity in ['elevated', 'normal']:
        severity = 'elevated'
    
    # Weighted scoring model
    score_components = {
        'base': {'critical': 90, 'elevated': 60, 'normal': 30, 'low': 10}[severity],
        'trend_bonus': {'rising_volatile': -15, 'falling': 10, 'rising': 0}.get(trend, 0),
        'outlier_penalty': -12 if has_outliers else 0,
        'stability': 8 if len(signal) >= 6 else 0
    }
    
    # Final diagnostic score
    final_score = sum(score_components.values())
    
    # Dead logic branch: unreachable due to structure
    if False and 'debug' in system_state:
        debug_log = f"Final breakdown: {score_components}, Total: {final_score}"
    
    # Incorporate dictionary lookup for calibration offset (simulated)
    calibration_table = {i: 0.95 + i*0.01 for i in range(10)}
    sample_index = len(signal) % 10
    calibrated_score = final_score * calibration_table.get(sample_index, 1.0)
    
    # Set operation to determine flag conditions (only partially used)
    risk_factors = set()
    if has_outliers: risk_factors.add('instability')
    if 'volatile' in trend: risk_factors.add('variability')
    if severity == 'critical': risk_factors.add('extreme_levels')
    
    mitigation_needed = len(risk_factors) > 1
    
    # Final adjustment based on mitigation context
    adjustment = -5 if mitigation_needed else 0
    final_score += adjustment
    
    return int(round(final_score))

# Execute main diagnostic
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Result: {final_diagnostic}")