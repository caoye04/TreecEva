import math

# Simulated system telemetry and health monitoring with distractors
def collect_diagnostics():
    sensor_readings = {
        'voltage': [3.2, 3.4, 3.1, 2.9, 3.6],
        'temp_core': [72.1, 75.3, 77.8, 80.0, 85.2],
        'fan_speed': [1200, 1350, 1400, 1550, 1600],
        'power_cycles': 8,
        'uptime_hours': 127
    }

    # Irrelevant aggregation (distractor)
    avg_fan = sum(sensor_readings['fan_speed']) / len(sensor_readings['fan_speed'])
    total_cycles = sensor_readings['power_cycles'] * 24

    # Real-time anomaly detection (unused path - dead code)
    def check_anomaly(seq):
        return any(x > 80 for x in seq)

    # Unused but plausible computation
    peak_temp = max(sensor_readings['temp_core'])
    normalized_voltage = [round(v / 3.3, 2) for v in sensor_readings['voltage']]

    return sensor_readings

# Auxiliary function that appears important but is not central
def compute_efficiency_index(metrics):
    efficiency = 0
    for i in range(len(metrics['voltage'])):
        if metrics['voltage'][i] > 3.0:
            efficiency += 1
    return efficiency * 10

# Core data transformation pipeline
def transform_logs(raw_data):
    logs = []
    for i, t in enumerate(raw_data['temp_core']):
        # Apply decay factor to older readings (simulated)
        adjusted = t * (0.95 ** i)
        status_flag = 'HIGH' if adjusted > 75 else 'NORMAL'
        logs.append({'seq': i, 'val': round(adjusted, 2), 'flag': status_flag})
    
    # Red herring: unused transformation
    inverted_map = {i: round(100 / (t + 1)) for i, t in enumerate(raw_data['temp_core'])}

    return logs

# Critical processing function with key logic
system_thresholds = {
    'critical_temp': 75.0,
    'min_voltage': 3.0,
    'grace_period': 3
}

# Lambda for dynamic threshold adjustment (used once)
adjust_limit = lambda base, cycles: base + (cycles / 100)

# Main execution block
if __name__ == "__main__":
    raw_telemetry = collect_diagnostics()
    
    # Distractor variables (plausible but irrelevant)
    baseline_score = compute_efficiency_index(raw_telemetry)
    system_age_years = raw_telemetry['uptime_hours'] // 8760
    cycle_factor = raw_telemetry['power_cycles'] % 7

    # Transform data into time-series log
    data_log = transform_logs(raw_telemetry)
    
    # System state with mixed relevance
    system_state = {
        'active': True,
        'mode': 'diagnostic',
        'version': '2.1.8',
        'last_reset': None,
        'overheat_events': 0
    }

    # Simulated event counter (misleading intermediate)
    event_counter = 0
    for entry in data_log:
        if entry['flag'] == 'HIGH':
            event_counter += 1
            if entry['seq'] < system_thresholds['grace_period']:
                system_state['overheat_events'] += 1  # Only counts early entries

    # Update system state based on dynamic rule
    dynamic_cap = adjust_limit(system_thresholds['critical_temp'], raw_telemetry['power_cycles'])
    
    # Core diagnostic processor
    def process_metrics(log_entries, sys_state):
        if not sys_state['active']:
            return -999

        trigger_count = 0
        cumulative_deviation = 0.0
        recent_alerts = []

        for record in log_entries:
            # Key condition: only count post-grace period HIGH flags
            if record['seq'] >= system_thresholds['grace_period'] and record['flag'] == 'HIGH':
                trigger_count += 1
                # Deviation calculation
                excess = record['val'] - dynamic_cap
                if excess > 0:
                    cumulative_deviation += excess

            # Dead branch - never executed due to flag logic
            if record['flag'] == 'CRITICAL':
                recent_alerts.append(record['seq'])

        # Secondary check with conditional expression
        base_diagnostic = 100 if trigger_count == 0 else 100 - (trigger_count * 15)
        
        # Final adjustment using deviation (triggers floating-point result)
        final_adjustment = cumulative_deviation * 2.5
        
        # Critical assignment point
        final_diagnostic = base_diagnostic - final_adjustment
        
        # Distractor: unused comprehensive score
        comprehensive_health = {
            'score': final_diagnostic,
            'risk_level': 'LOW' if final_diagnostic > 80 else 'MODERATE' if final_diagnostic > 60 else 'HIGH'
        }
        
        return round(final_diagnostic, 6)

    # Execute critical statement
    final_diagnostic = process_metrics(data_log, system_state)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")