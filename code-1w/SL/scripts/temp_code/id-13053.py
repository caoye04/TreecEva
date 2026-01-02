from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for a distributed system health monitor
def collect_telemetry(nodes):
    raw_readings = defaultdict(list)
    for node_id, metrics in nodes.items():
        for metric_name, values in metrics.items():
            raw_readings[metric_name].extend(values)
    return raw_readings

# Irrelevant auxiliary function - decoy for resource tracking
def track_resources(usage_log):
    cpu_peak = 0
    mem_records = []
    for entry in usage_log:
        if entry['cpu'] > cpu_peak:
            cpu_peak = entry['cpu']
        mem_records.append(entry['memory'])
    avg_mem = sum(mem_records) / len(mem_records) if mem_records else 0
    return {'peak_cpu': cpu_peak, 'avg_memory': avg_mem}

# Core signal processing with embedded distractions
def preprocess_signal(raw_data):
    filtered = []
    noise_floor = 0.15
    for val in raw_data:
        if abs(val) > noise_floor:
            filtered.append(abs(val))
    # Distractor: frequency analysis (unused later)
    freq_analysis = Counter([round(x, 1) for x in filtered])
    dominant_freq = freq_analysis.most_common(1)[0][1] if freq_analysis else 0
    return [x ** 2 for x in filtered]  # Energy normalization

# Red herring function - appears important but unused in critical path
def compute_stability_index(timestamps):
    if len(timestamps) < 2:
        return 0.0
    intervals = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    variance = sum((x - sum(intervals)/len(intervals))**2 for x in intervals) / len(intervals)
    return round(math.exp(-variance), 4)

# Primary diagnostic engine with multiple layers
def generate_health_signature(telemetry):
    signature = []
    critical_bands = ['vibration', 'thermal', 'current', 'pressure']
    
    for band in critical_bands:
        if band in telemetry:
            signal = preprocess_signal(telemetry[band])
            if signal:
                rms = math.sqrt(sum(signal) / len(signal))
                # Misleading intermediate calculation (not used in final result)
                decibel_level = 20 * math.log10(rms + 1e-9)
                normalized_score = max(0, min(100, 10 * rms))
                signature.append(normalized_score)
            else:
                signature.append(0)
        else:
            signature.append(-1)
    
    # Inject artificial damping factor (distractor)
    damping = math.cos(len(signature))
    weighted_sum = sum(s * (0.8 ** i) for i, s in enumerate(signature))
    return [round(weighted_sum, 3)] + signature  # First element is aggregated index

# Threshold calibration with dead code paths
def calibrate_thresholds(base_config, environment='standard'):
    defaults = {
        'vibration': 4.2,
        'thermal': 85.0,
        'current': 15.5,
        'pressure': 98.6
    }
    
    # Unused environmental adjustments (dead path)
    adjustments = {}
    if environment == 'harsh':
        adjustments = {'vibration': 1.3, 'thermal': 5.0}
    elif environment == 'optimized':
        adjustments = {'current': -1.0, 'pressure': 2.0}
    
    # This branch is never reached in current execution - red herring
    if base_config.get('adaptive', False):
        return {k: v * 1.1 for k, v in defaults.items()}
    
    return defaults  # Always returns defaults due to missing adaptive flag

# Main analysis with complex logic chain
def analyze_metrics(health_vec, limits):
    # Extended reasoning with multiple steps
    if not health_vec or not limits:
        return -999
    
    aggregate = health_vec[0]  # Previously computed RMS-aggregated index
    component_scores = health_vec[1:]
    
    # Step 1: Count how many components exceed hypothetical thresholds
    threshold_exceedances = 0
    reference_keys = ['vibration', 'thermal', 'current', 'pressure']
    for i, key in enumerate(reference_keys):
        if i < len(component_scores) and component_scores[i] > 0:
            threshold_value = limits.get(key, 100)
            if component_scores[i] > threshold_value:
                threshold_exceedances += 1
    
    # Step 2: Calculate decay-corrected trend (but only use conditionally)
    trend_correction = 0
    if len(component_scores) >= 3:
        recent_avg = sum(component_scores[-3:]) / 3
        baseline = component_scores[0]
        raw_trend = recent_avg - baseline
        # Apply exponential smoothing factor (distraction)
        for _ in range(2):
            raw_trend = raw_trend * 0.85
        trend_correction = int(abs(raw_trend))
    
    # Step 3: Bit manipulation for fault pattern encoding (critical step)
    fault_code = 0
    for i, score in enumerate(component_scores):
        if score > 0:
            bit = (int(score) >> 2) & 1  # Extract third least significant bit of integer part
            fault_code |= (bit << i)
    
    # Step 4: Conditional override based on aggregate (red herring branch)
    emergency_override = False
    test_value = aggregate * 1.5
    if test_value > 200:  # Impossible under current data
        emergency_override = True
    
    # Step 5: Final diagnostic computation
    base_diagnostic = aggregate * 10
    adjustment_factor = (threshold_exceedances * 7) + (fault_code % 13)
    
    # Step 6: Apply adjustment with modulo stabilization
    final_value = int(base_diagnostic - adjustment_factor)
    
    # Step 7: Sanity clamping
    if final_value < -500:
        final_value = -500
    elif final_value > 500:
        final_value = 500
    
    return final_value

# Simulated input data
node_metrics = {
    'sensor_node_01': {
        'vibration': [-0.2, 0.3, -0.4, 0.1],
        'thermal': [0.5, -0.6, 0.7],
        'current': [-0.1, 0.2],
        'pressure': [0.4, -0.3, 0.5, 0.6]
    },
    'sensor_node_02': {
        'vibration': [0.1, -0.05],
        'thermal': [0.8, -0.9, 1.0],
        'current': [0.3],
        'status': [1, 1, 0]  # Irrelevant metric
    }
}

usage_logs = [
    {'cpu': 65, 'memory': 1.2},
    {'cpu': 70, 'memory': 1.5},
    {'cpu': 75, 'memory': 1.3}
]

timestamps = [1000, 1050, 1100, 1150, 1200]

# Execution pipeline
raw_telemetry = collect_telemetry(node_metrics)
signature = generate_health_signature(raw_telemetry)
thresholds = calibrate_thresholds({'base': 'default'}, environment='standard')
final_diagnostic = analyze_metrics(signature, thresholds)

# Critical output
print(f"Result: {final_diagnostic}")