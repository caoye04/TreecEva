from collections import defaultdict, Counter

# Simulated system telemetry data
timing_samples = [1.2, 0.8, 1.5, 2.3, 0.7, 1.1, 1.8, 0.9, 1.4, 2.1]
error_flags = [False, True, False, False, True, False, False, True, False, False]
phase_codes = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'A', 'B', 'C']

# Irrelevant auxiliary computation: signal integrity mockup
signal_levels = [abs(x * 0.9 + (i % 3)) for i, x in enumerate(timing_samples)]
baseline_shift = sum(signal_levels) / len(signal_levels) if signal_levels else 0
adjusted_signals = [s - baseline_shift for s in signal_levels]
decoherence_score = sum(s ** 2 for s in adjusted_signals[:5])

# Misleading diagnostic path (dead code branch)
def legacy_diagnostic(data):
    return sum(d * 0.5 for d in data if d > 1.0)

# Unused function meant to distract
def compute_resilience_index(seq):
    count = 0
    for i in range(1, len(seq)):
        if seq[i] != seq[i-1]:
            count += 1
    return count * 0.7

# Relevant processing begins here
def classify_latency(value):
    return 'high' if value > 1.6 else 'normal'

# Accumulate phase-wise statistics
phase_latency = defaultdict(list)
for t, p in zip(timing_samples, phase_codes):
    phase_latency[p].append(classify_latency(t))

# Flag anomaly sequences (red herring list)
anomaly_transitions = []
for i in range(1, len(error_flags)):
    if error_flags[i] and not error_flags[i-1]:
        anomaly_transitions.append(i)

# Real-time event clustering (distractor map)
event_clusters = defaultdict(int)
for i, flag in enumerate(error_flags):
    bucket = i // 3
    if flag:
        event_clusters[bucket] += 1

# Key intermediate structure: timing log with categorized delays
timing_log = {}
for phase, records in phase_latency.items():
    counter = Counter(records)
    timing_log[phase] = {
        'normal': counter.get('normal', 0),
        'high': counter.get('high', 0),
        'ratio': counter.get('high', 0) / len(records) if records else 0
    }

# System-wide flags from error context
system_flags = {
    'critical_phase': max(timing_log, key=lambda k: timing_log[k]['high']),
    'stability_index': sum(1 for f in error_flags if f) < 4,
    'phase_count': len(phase_latency)
}

# Secondary irrelevant transform: frequency domain mock
fft_peaks = [t * 2.1 for t in timing_samples[::2]]
fundamental_freq = max(fft_peaks) if fft_peaks else 0.0
harmonic_energy = sum(f ** 1.5 for f in fft_peaks)

# Decoy metric using string manipulation (unrelated)
code_names = [f"CHK{p}{i}" for i, p in enumerate(phase_codes)]
checksum_tags = ''.join([tag[2] + tag[3:] for tag in code_names if tag[1] == 'H'])
version_signature = checksum_tags.replace('A', 'X').split('X')

# Critical aggregation function
def aggregate_metrics(log, flags):
    base_score = 0
    penalty = 0
    
    for phase_data in log.values():
        base_score += phase_data['normal']
        if phase_data['ratio'] > 0.4:
            penalty += phase_data['high'] * 2
    
    # Conditional expression influencing final result
    adjustment = 1.5 if flags['stability_index'] else 0.8
    
    # Complex calculation with tuple unpacking
    critical_high = log[flags['critical_phase']]['high']
    normal_in_critical = log[flags['critical_phase']]['normal']
    ratio_val = log[flags['critical_phase']]['ratio']
    
    temp_series = [base_score, penalty, critical_high]
    score, fault_penalty, spike_count = (s * 1.1 for s in temp_series)
    
    # Final synthesis
    result = (score - fault_penalty * 3) + (spike_count * ratio_val * 10)
    return int(result * adjustment)

# Execution point of interest
final_diagnostic = aggregate_metrics(timing_log, system_flags)

# Print result as required
print(f"Target result: {final_diagnostic}")