from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_sensor_data = [127, 136, 118, 142, 131]
error_flags = [False, True, False, False, True]

def analyze_trend(values):
    trend_score = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend_score += 1
        elif values[i] < values[i-1]:
            trend_score -= 1
    return abs(trend_score)  # Distractor: absolute value hides direction

def compute_checksum(data):
    # Irrelevant cryptographic checksum (dead code path)
    chk = 0
    for val in data:
        chk ^= val * 17
    return chk % 256

def filter_anomalies(entries, threshold=130):
    anomalies = []
    for idx, entry in enumerate(entries):
        if entry > threshold:
            anomalies.append((idx, entry))
    return anomalies  # Used later, but index structure is misleading

class SystemMonitor:
    def __init__(self, baseline):
        self.baseline = baseline
        self.correction_factor = 0.89  # Unused in final calculation
        self.history = []

    def adjust_reading(self, value):
        # Distractor method - never invoked
        return (value - self.baseline) * self.correction_factor

    def log_event(self, code):
        self.history.append(code)

# Unused global variables - red herrings
system_status = {'state': 'active', 'mode': 'diagnostic', 'version': '3.7.1'}
debug_mode = True
temp_buffer = [0] * 10

# Main data structures
log_entries = defaultdict(list)
for ts, val, err in zip(timestamps, raw_sensor_data, error_flags):
    bucket = ts - (ts % 10)  # Group by 10-second intervals
    log_entries[bucket].append({'value': val, 'error': err})

# Secondary processing with decoy transformations
aggregated = {}
skew_metrics = []
for bucket, records in log_entries.items():
    values = [r['value'] for r in records]
    errors = [r['error'] for r in records]
    avg_val = sum(values) / len(values)
    aggregated[bucket] = {
        'mean': avg_val,
        'count': len(records),
        'has_error': any(errors),
        'checksum': compute_checksum(values)  # Computed but unused
    }
    if len(values) > 1:
        variance = sum((v - avg_val)**2 for v in values) / len(values)
        skew = sum(((v - avg_val)**3) for v in values) / (len(values) * variance**1.5 + 1e-8)
        skew_metrics.append(skew)

# Distractor: complex but irrelevant statistical normalization
normalized_skew = 0
if skew_metrics:
    raw_skew_mean = sum(skew_metrics) / len(skew_metrics)
    normalized_skew = math.erf(raw_skew_mean / 2.0)  # Dead end

# Critical threshold configuration (used in final logic)
system_thresholds = {
    'critical': 135,
    'warning': 125,
    'hysteresis': 10
}

# Decoy function that looks important but is unused
def evaluate_stability(metrics, weights=None):
    if not weights:
        weights = {'trend': 0.4, 'variance': 0.35, 'errors': 0.25}
    score = 0
    for m in metrics:
        score += m.get('trend', 0) * weights['trend']
    return round(score * 100, 2)

# Core processing function with key logic interwoven with noise
def process_metrics(logs, thresholds):
    diagnostic_code = 0
    critical_count = 0
    warning_count = 0
    total_samples = 0
    recent_errors = 0

    # Real logic mixed with irrelevant operations
    for bucket, records in logs.items():
        bucket_values = [r['value'] for r in records]
        max_val = max(bucket_values)
        min_val = min(bucket_values)
        total_samples += len(bucket_values)
        
        # Actual decision logic
        if max_val >= thresholds['critical']:
            critical_count += 1
        elif max_val >= thresholds['warning']:
            warning_count += 1
        
        # Extract error flags for temporal analysis
        bucket_errors = [r['error'] for r in records]
        if any(bucket_errors):
            recent_errors += 1
    
    # Distractor: elaborate bit manipulation with partial relevance
    status_word = 0
    status_word |= (critical_count << 4)
    status_word |= (warning_count << 2)
    status_word |= (recent_errors > 0)
    
    # Irrelevant floating point dance
    sample_ratio = total_samples / (len(logs) + 1e-8)
    adjusted_critical = critical_count * 1.75
    penalty_factor = 1 + (recent_errors * 0.15)
    
    # Key computation buried in noise
    base_score = (critical_count * 100) + (warning_count * 10)
    if recent_errors >= 2:
        base_score += 25
    elif recent_errors == 1:
        base_score += 10
    
    # Final adjustment using hysteresis value (actual usage)
    hysteresis_effect = system_thresholds['hysteresis'] // 5  # Integer division
    intermediate = base_score + (hysteresis_effect * 3)
    
    # Real answer derivation
    final_component = int(intermediate * 1.3)  # Conversion and scaling
    
    # Multiple assignments - distracts from flow
    diagnostic_code, _ = divmod(final_component, 997)
    
    # THIS IS THE ACTUAL ANSWER
    final_diagnostic = diagnostic_code + 50
    
    # Dead code branch that looks important
    if normalized_skew > 0.5:
        final_diagnostic = int(final_diagnostic * 0.9)
    
    return final_diagnostic

# Initialize monitor (unused)
monitor = SystemMonitor(baseline=120)
for flag in error_flags:
    if flag:
        monitor.log_event(1)

# Key statement
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Output result
print(f"Result: {final_diagnostic}")