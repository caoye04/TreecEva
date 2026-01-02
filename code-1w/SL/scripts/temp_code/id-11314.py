from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for a distributed system health monitor
def collect_telemetry(nodes):
    telemetry = defaultdict(list)
    for node_id, readings in nodes.items():
        for reading in readings:
            if reading > 0.5:
                telemetry['unstable'].append((node_id, reading))
            elif reading < 0.1:
                telemetry['critical'].append((node_id, reading))
            else:
                telemetry['stable'].append((node_id, reading))
    return telemetry

# Irrelevant helper: Counts transitions between states (not used in final result)
def count_state_transitions(trace):
    transitions = 0
    for i in range(len(trace) - 1):
        if trace[i] != trace[i + 1]:
            transitions += 1
    return transitions

# Core metric processor with red herring computations
def compute_stability_index(raw_data, threshold=0.75):
    peak_magnitude = max(raw_data)
    avg_response = sum(raw_data) / len(raw_data)
    
    # Distractor: complex but unused calculation
    harmonic_proxy = len(raw_data) / sum(1 / (x + 1e-9) for x in raw_data)
    entropy_shadow = -sum(p * math.log(p) for p in Counter(raw_data).values() if p > 0)
    
    # Relevant: weighted instability score
    instability_score = 0
    for val in raw_data:
        if val > threshold:
            instability_score += (val - threshold) ** 2
    
    # Red herring normalization (unused)
    normalized_instability = instability_score / (len(raw_data) + 1e-9) if instability_score > 0 else 0
    
    # ACTUAL used value
    return instability_score  # Key output

# Fake anomaly detector (dead code path)
def detect_anomalies(stream):
    anomalies = []
    moving_avg = [sum(stream[:i+1]) / (i+1) for i in range(len(stream))]
    for i, val in enumerate(stream):
        if abs(val - moving_avg[i]) > 0.5:
            anomalies.append(i)
    return anomalies  # Never actually used

# Main processing function with decoy arguments and misleading structure
def process_metrics(traces, load_profile, debug_mode=False, simulate_failure=False):
    # Unpack relevant data
    critical_events = [t for t in traces if t[1] < 0.1]
    high_load_periods = [load for load in load_profile if load > 0.8]
    
    # Distractor: builds unused summary
    event_counter = Counter([evt[0] for evt in critical_events])
    load_summary = {'max': max(load_profile), 'avg': sum(load_profile)/len(load_profile)}
    
    # Irrelevant nested loop simulating correlation check
    spurious_correlation = 0
    for event in critical_events:
        for load_snapshot in high_load_periods:
            if abs(event[1] - load_snapshot) < 0.05:
                spurious_correlation += 1

    # Decoy state machine (never executed due to condition)
    system_state_log = []
    if debug_mode:
        current_state = 'INIT'
        for _ in range(10):
            if current_state == 'INIT':
                current_state = 'WAIT'
            elif current_state == 'WAIT':
                current_state = 'ERROR'
            system_state_log.append(current_state)
    
    # Core logic: compute diagnostic from two sources
    trace_values = [t[1] for t in traces]
    index_a = compute_stability_index(trace_values)
    
    # Secondary metric with modular arithmetic red herring
    cycle_effect = sum(load_profile) % 7
    decay_factor = 0.9 ** len(high_load_periods)
    
    # Final computation - only index_a and decay_factor are actually used
    # Everything else was distraction
    intermediate_result = index_a * decay_factor  # Used
    fallback_metric = len(critical_events) + cycle_effect  # Unused
    
    final_diagnostic = int(intermediate_result * 1000)  # Deterministic integer output
    
    # PRINT REQUIRED AT END
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
node_data = {
    'N1': [0.05, 0.12, 0.88, 0.33],
    'N2': [0.03, 0.45, 0.91, 0.22],
    'N3': [0.11, 0.67, 0.76, 0.09],
    'N4': [0.02, 0.54, 0.83, 0.18]
}

# Extract health trace from telemetry (only values below 0.1 are critical)
telemetry_output = collect_telemetry(node_data)
health_trace = []
for status in ['critical', 'unstable', 'stable']:
    for entry in telemetry_output.get(status, []):
        health_trace.append(entry)

system_load = [0.81, 0.73, 0.89, 0.65, 0.92, 0.77, 0.84]

# Execute main logic
def main():
    final_diagnostic = process_metrics(health_trace, system_load)

main()