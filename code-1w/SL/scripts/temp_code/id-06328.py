import math

# Simulated system metrics with irrelevant and relevant components
def collect_diagnostics():
    return {
        'cpu_load': 78,
        'mem_usage': 45,
        'disk_io': 120,
        'network_latency_ms': 40,
        'packet_loss_rate': 0.002,
        'temperature_c': 67,
        'fan_speed_rpm': 2300,
        'context_switches': 15000,
        'interrupts_per_sec': 980
    }

def normalize(value, min_val, max_val):
    # Normalize to [0,1] range
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

def transform_metric(key, value):
    # Some transformations are red herrings
    mapping = {
        'cpu_load': lambda x: normalize(x, 0, 100),
        'mem_usage': lambda x: normalize(x, 0, 100),
        'disk_io': lambda x: min(x / 200, 1.0),
        'network_latency_ms': lambda x: 1 - normalize(x, 0, 100),
        'packet_loss_rate': lambda x: max(0, 1 - x * 100),
        'temperature_c': lambda x: normalize(100 - x, 0, 100),  # Cooler is better
        'fan_speed_rpm': lambda x: None,  # Irrelevant metric - returns None
        'context_switches': lambda x: normalize(max(0, 20000 - x), 0, 20000),
        'interrupts_per_sec': lambda x: None  # Another irrelevant path
    }
    func = mapping.get(key)
    return func(value) if func else 0.0

def filter_relevant_metrics(metrics):
    # Only some keys are actually used
    relevant_keys = {'cpu_load', 'mem_usage', 'disk_io', 'network_latency_ms', 'packet_loss_rate'}
    return {k: v for k, v in metrics.items() if k in relevant_keys}

def calculate_health_vector(raw_metrics):
    # Apply transformation only on relevant metrics
    transformed = {}
    for k, v in raw_metrics.items():
        result = transform_metric(k, v)
        if result is not None:  # Filter out None results (distractor)
            transformed[k] = result
    return transformed

def apply_weighting(values, profile='balanced'):
    # Weight profiles - only one is actually used
    profiles = {
        'performance': {'cpu_load': 0.3, 'mem_usage': 0.25, 'disk_io': 0.2, 'network_latency_ms': 0.15, 'packet_loss_rate': 0.1},
        'stability':   {'cpu_load': 0.1, 'mem_usage': 0.1, 'disk_io': 0.2, 'network_latency_ms': 0.3, 'packet_loss_rate': 0.3},
        'balanced':    {'cpu_load': 0.2, 'mem_usage': 0.2, 'disk_io': 0.2, 'network_latency_ms': 0.2, 'packet_loss_rate': 0.2}
    }
    weights = profiles.get(profile, profiles['balanced'])
    weighted_sum = 0.0
    total_weight = 0.0
    for k, v in values.items():
        w = weights.get(k, 0.0)
        weighted_sum += v * w
        total_weight += w
    return weighted_sum / total_weight if total_weight > 0 else 0.0

def compute_derived_index(data):
    # This function is never called — dead code path (distractor)
    if 'disk_io' in data and 'cpu_load' in data:
        return (data['disk_io'] * data['cpu_load']) ** 0.5
    return -1

def adjust_for_anomalies(score, logs):
    # Logs contain irrelevant info; adjustment is conditional but unused
    threshold = 0.8
    penalty = 0.1
    if score > threshold and 'critical' in logs:
        return max(0, score - penalty)
    return score

def evaluate_performance(metrics_dict, weight_profile='balanced'):
    # Core logic begins here
    filtered = filter_relevant_metrics(metrics_dict)
    health_vector = calculate_health_vector(filtered)
    
    # Dead-end branch: uses a key that doesn't exist (misleading)
    if 'power_draw_w' in metrics_dict and metrics_dict['power_draw_w'] > 300:
        fallback = apply_weighting(health_vector, 'performance')
    else:
        # Actual execution path
        base_score = apply_weighting(health_vector, weight_profile)
        
        # Additional check that does nothing due to missing key (red herring)
        temp = metrics_dict.get('temperature_c')
        if temp and temp > 80:
            base_score *= 0.9
        
        # Final adjustment — always skipped because key isn't present
        log_status = metrics_dict.get('system_logs', [])
        final = adjust_for_anomalies(base_score, log_status)
        
        return final  # This is the actual return

# Irrelevant helper — never invoked
def generate_report_snapshot():
    return {"status": "OK", "timestamp": 1234567890}

# Global constants with distraction
MAX_THRESHOLD_LIMIT = 9999
TEMPORARY_BUFFER_SIZE = 512
DEBUG_MODE_ENABLED = False
SYSTEM_UPTIME_HOURS = 127

# Main execution flow
raw_data = collect_diagnostics()

# Inject fake key that looks important but isn't used
raw_data['power_draw_w'] = 280  # Below threshold, so condition fails anyway

# Add noise entry — misleading
raw_data['dummy_placeholder'] = float('nan')

# Weights are passed, but only 'balanced' matters
weights_config = {
    'selected_profile': 'balanced',
    'override_rules': [],
    'fallback_enabled': False
}

# Critical statement
final_score = evaluate_performance(raw_data, weights_config['selected_profile'])

# Print result as required
print(f"Target result: {final_score}")