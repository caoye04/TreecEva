from itertools import cycle

# System parameters for resource allocation simulation
def calculate_load_factor(usage, peak):
    return usage / peak if peak > 0 else 0

def adjust_capacity(base, log_entries):
    adjustment = 0
    history = {}
    for entry in log_entries:
        timestamp, load, threshold = entry
        if load > threshold * 0.8:
            adjustment += 2
        elif load < threshold * 0.3:
            adjustment -= 1
        
        # Irrelevant tracking (distractor)
        key = timestamp // 1000
        if key not in history:
            history[key] = []
        history[key].append(load)
    
    # Dummy computation on history (dead logic path)
    avg_spikes = 0
    for k, values in history.items():
        peaks = [v for v in values if v > 80]
        if peaks:
            avg_spikes += sum(peaks) / len(peaks)
    
    # Actual capacity rule: base + net adjustment
    return base + adjustment

# Simulated telemetry data
telemetry_logs = [
    (1623456000, 85, 100),
    (1623456060, 45, 100),
    (1623456120, 20, 100),
    (1623456180, 90, 100),
    (1623456240, 10, 100),
    (1623456300, 75, 100)
]

# Auxiliary state tracking (partially irrelevant)
current_state = {'active': True, 'mode': 'auto', 'version': '2.1'}
state_cycle = cycle(['idle', 'active', 'standby'])
for _ in range(3):
    next(state_cycle)

# Environmental factors (distraction variables)
temperature_bias = 23.5
pressure_factor = 1.02
latency_buffer = [0.1, 0.3, 0.2]

# Core configuration
base_capacity = 50
modifier_log = telemetry_logs

# Secondary calculation with no impact (red herring)
effective_latency = sum(latency_buffer) / len(latency_buffer)
normalized_temp = temperature_bias * pressure_factor

# Key execution point
final_capacity = adjust_capacity(base_capacity, modifier_log)

# Tracking unrelated metric (distractor)
diagnostic_report = {
    'checksum': 0,
    'anomalies': [],
    'version': current_state['version']
}
for i, log in enumerate(modifier_log):
    if log[1] < 30:
        diagnostic_report['anomalies'].append(i)
diagnostic_report['checksum'] = len(diagnostic_report['anomalies']) * 17

# Output target result
print(f"Result: {final_capacity}")