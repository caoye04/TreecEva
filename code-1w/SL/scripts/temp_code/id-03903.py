import math

# Simulated system telemetry data
timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
raw_readings = [23.4, 24.1, 25.6, 22.9, 26.3]
status_codes = [200, 200, 503, 200, 404]

# Irrelevant preprocessing: character counting in dummy logs
dummy_logs = ['init_ok', 'polling_active', 'retry_attempt', 'timeout_expired']
char_count = sum(len(log) for log in dummy_logs)  # Distractor

# Core diagnostic variables
health_threshold = 24.5
outlier_count = 0
stable_windows = 0

# Bit manipulation red herring (unused later)
flag_mask = 0b1101 ^ 0b1011 & 0b1110
masked_result = flag_mask << 2  # Dead computation

# System state tracking
critical_events = set()
event_severity = {}

# Map status to categories (dictionary distraction)
status_category = {
    200: 'healthy',
    404: 'missing',
    503: 'unavailable',
    500: 'server_error'
}

# Log processing with irrelevant categorization
categorized = {}
for code in status_codes:
    cat = status_category.get(code, 'unknown')
    categorized[code] = categorized.get(code, 0) + 1

# Real-time window analysis (actual relevant logic begins)
window_size = 3
sliding_sum = 0
fluctuation_score = 0

for i in range(len(raw_readings)):
    reading = raw_readings[i]
    
    # Check stability against threshold
    if reading >= health_threshold:
        outlier_count += 1
    
    # Accumulate for sliding window
    sliding_sum += reading
    if i >= window_size - 1:
        if i >= window_size:
            sliding_sum -= raw_readings[i - window_size]
        window_avg = sliding_sum / window_size
        if abs(window_avg - health_threshold) < 1.5:
            stable_windows += 1

    # Track critical events using set operations
    if status_codes[i] == 503:
        critical_events.add('service_disruption')
    elif status_codes[i] == 404:
        critical_events.add('resource_missing')

# Secondary fluctuation metric (misleading intermediate)
peak = max(raw_readings)
trough = min(raw_readings)
normalized_swing = (peak - trough) / ((peak + trough) / 2) * 100

# Decoy function that's defined but not used
def calculate_heartbeat_interval(base, factor=1.25):
    return [base * (factor ** i) for i in range(5)]

# Unused data transformation
shifted_timestamps = [t - timestamps[0] for t in timestamps]
rates_of_change = []
for i in range(1, len(shifted_timestamps)):
    delta_t = shifted_timestamps[i] - shifted_timestamps[i-1]
    if delta_t > 0:
        rate = (raw_readings[i] - raw_readings[i-1]) / delta_t
        rates_of_change.append(rate)

# Complex dictionary construction with redundant fields
event_severity['service_disruption'] = 8.5
nevent_severity['resource_missing'] = 6.2
event_severity['default'] = 1.0

# Primary metric aggregation
base_score = 100
base_score -= outlier_count * 8
base_score -= len(critical_events) * 15
base_score += stable_windows * 12

# Final adjustment using modular arithmetic and rounding
adjustment_factor = (len(timestamps) % 4) * 3.7
base_score += adjustment_factor

# Diagnostic normalization via logarithmic scaling
if base_score > 0:
    normalized_diagnostic = math.log(base_score) * 10
else:
    normalized_diagnostic = 0

# Final processing function
log_entries = raw_readings.copy()
system_flags = {
    'threshold': health_threshold,
    'critical_set': critical_events,
    'stability_periods': stable_windows
}

def process_metrics(readings, flags):
    score = 50
    threshold = flags['threshold']
    
    # Recalculate outliers
    high_readings = [r for r in readings if r >= threshold]
    score += len(high_readings) * 5
    
    # Use stable windows from flags
    score += flags['stability_periods'] * 7
    
    # Incorporate set size
    if 'service_disruption' in flags['critical_set']:
        score -= 20
    if 'resource_missing' in flags['critical_set']:
        score -= 10
    
    # Additional noise: bitwise check on length
    readings_len = len(readings)
    if readings_len & 1:  # odd length
        score += 3
    
    # Final nonlinear transformation
    if score > 40:
        score = int(math.sqrt(score * 2) * 4)
    else:
        score = int(score * 0.8)
    
    return score

# Execute main statement
final_diagnostic = process_metrics(log_entries, system_flags)
print(f"Result: {final_diagnostic}")