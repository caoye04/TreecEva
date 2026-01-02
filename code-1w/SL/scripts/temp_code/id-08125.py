import math

def analyze_component_load(x):
    if x < 10:
        return x * 1.5
    elif x < 25:
        return x * 1.2 + 3
    else:
        return x * 0.8 + 10

def validate_readings(readings):
    valid_count = 0
    total = 0
    for r in readings:
        if 5 <= r <= 100:
            valid_count += 1
            total += r
    return valid_count > 0 and (total / valid_count) > 15

data_log = [
    {'sensor': 'A1', 'values': [12, 15, 8, 23], 'timestamp': 1623456789},
    {'sensor': 'B2', 'values': [45, 13, 17, 29], 'timestamp': 1623456792},
    {'sensor': 'C3', 'values': [8, 5, 14, 31], 'timestamp': 1623456795}
]

system_status = {
    'core_temp': 67,
    'voltage': 3.3,
    'fan_speed': 2200,
    'uptime_hours': 142,
    'maintenance_due': False
}

# Extraneous helper function with misleading relevance
def calculate_health_index(temp, voltage):
    base = temp * 0.7
    adjusted = base + (voltage * 5) if voltage < 3.5 else base - 10
    return round(adjusted, 2)

# Distractor variables
thermal_margin = 100 - system_status['core_temp']
drift_compensation = 0.95 if system_status['voltage'] > 3.2 else 1.05
reference_ratio = (system_status['uptime_hours'] % 24) / 8

# Intermediate processing with irrelevant computations
aggregated_load = 0
peak_value = 0
reading_validity = []

for entry in data_log:
    raw_values = entry['values']
    max_val = max(raw_values)
    if max_val > peak_value:
        peak_value = max_val
    
    # Compute load per component (relevant)
    component_base = sum(v for v in raw_values if v > 10)
    adjusted_load = analyze_component_load(component_base)
    aggregated_load += adjusted_load

    # Irrelevant validation branch (not used later)
    status_check = validate_readings(raw_values)
    reading_validity.append(status_check)

# Unused dictionary aggregation (distractor)
count_summary = {entry['sensor']: len(entry['values']) for entry in data_log}
total_entries_processed = sum(count_summary.values())

# Core metric calculation — this affects final answer
average_load = aggregated_load / len(data_log)

temperature_factor = 1.0
if system_status['core_temp'] > 60:
    temperature_factor = 0.9
elif system_status['core_temp'] < 50:
    temperature_factor = 1.1

voltage_factor = system_status['voltage'] / 3.3

# Efficiency score depends on load, temp, and voltage
intermediate_score = average_load * temperature_factor * voltage_factor

# Final nonlinear adjustment using conditional expression
final_adjustment = 1.25 if peak_value > 25 else 0.9

# Key assignment: efficiency_score is critical
efficiency_score = intermediate_score * final_adjustment

# Simulate auxiliary telemetry (dead code path)
if system_status['fan_speed'] > 2000:
    cooling_efficiency = "optimal"
else:
    cooling_efficiency = "suboptimal"

aux_data = {"checksum": 0, "version": "2.1", "mode": "diagnostic"}
aux_data["diagnostic_flag"] = True if efficiency_score > 35 else False

# Unrelated string operation (distractor)
system_tag = f"SYS-{system_status['uptime_hours'] // 24}D-{int(system_status['voltage'] * 10)}V"

# Final output computation — uses efficiency_score but wraps it
final_output = process_metrics(data_log, system_status) if 'process_metrics' in globals() else efficiency_score

# Since process_metrics is not defined, fallback occurs; print actual target
print(f"Result: {efficiency_score}")