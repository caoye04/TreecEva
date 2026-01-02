from collections import defaultdict, Counter
import math

# Simulated system telemetry data
timestamps = [1623456780 + i*30 for i in range(200)]
raw_signals = [(1.8 * math.sin(t/1000) + 0.5 * math.cos(t/500) + 2.3) for t in timestamps]

# Irrelevant auxiliary signal processing (distractor)
spectral_components = []
for i in range(len(raw_signals)):
    if i % 17 == 0:
        phase_shift = math.pi / (i + 1) if i > 0 else 0
        spectral_components.append(math.sin(raw_signals[i] + phase_shift))

# Signal categorization (mixed relevant and irrelevant)
categories = []
for val in raw_signals:
    if val > 3.0:
        categories.append('CRITICAL')
    elif val > 2.0:
        categories.append('ELEVATED')
    elif val > 1.0:
        categories.append('NORMAL')
    else:
        categories.append('LOW')

category_count = Counter(categories)

# Fake anomaly detection (dead path)
anomalies = []
for i, val in enumerate(raw_signals):
    if i > 0 and abs(val - raw_signals[i-1]) > 1.5:
        anomalies.append(i)

# System thresholds (partially relevant)
system_thresholds = {
    'voltage': (1.5, 3.2),
    'current_rms': (0.8, 2.4),
    'frequency_jitter': (0.05, 0.18),
    'phase_noise': (0.3, 0.9)
}

# Log entry generation with metadata (relevant core)
log_entries = []
for i, val in enumerate(raw_signals):
    entry = {
        'id': f'LOG-{1000+i}',
        'timestamp': timestamps[i],
        'signal_value': round(val, 3),
        'quality_flag': i % 4 == 0,
        'diagnostics': {}
    }
    
    # Embedded diagnostic computations
    if val > system_thresholds['voltage'][1]:
        entry['diagnostics']['over_voltage'] = True
        entry['diagnostics']['recovery_window'] = int((val - 3.2) * 50)
    
    if i % 5 == 0:
        fft_proxy = (val ** 2) % 1.7
        entry['diagnostics']['harmonic_distortion'] = round(fft_proxy, 4)
    
    # Critical health indicator calculation (obfuscated)
    health_score = 0
    if val >= 2.0:
        health_score += 3
    if val >= 2.8:
        health_score += 2
    if val < 1.2:
        health_score -= 2
    if i % 10 == 0:
        health_score += 1  # periodic stabilization bonus
        
    entry['health_index'] = max(0, min(5, health_score))
    log_entries.append(entry)

# Decoy aggregation function (misleading)
def compute_stability_index(entries):
    total = 0
    for e in entries:
        if 'harmonic_distortion' in e['diagnostics']:
            total += e['diagnostics']['harmonic_distortion']
    return round(total / len(entries), 4)

stability_metric = compute_stability_index(log_entries)  # unused

# Real processing function with key logic buried
def process_metrics(log_data, thresholds):
    # Aggregation containers
    report = defaultdict(int)
    health_tally = [0]*6
    
    # Secondary signal transformation (distraction)
    derived_magnitude = 0.0
    for entry in log_data[::2]:  # every other entry
        derived_magnitude += math.sqrt(abs(entry['signal_value']))
    
    # Core analysis loop
    critical_events = 0
    cumulative_recovery = 0
    valid_health_sum = 0
    sample_count = 0
    
    for entry in log_data:
        h = entry['health_index']
        if h >= 0:  # always true, but obfuscates
            health_tally[h] += 1
            valid_health_sum += h
            sample_count += 1
        
        # Extract recovery windows from diagnostics
        if 'recovery_window' in entry['diagnostics']:
            window_val = entry['diagnostics']['recovery_window']
            if window_val > 0:
                critical_events += 1
                cumulative_recovery += window_val

        # Red herring: analyze quality flags
        q_flag = entry['quality_flag']
        report['flagged'] += 1 if q_flag else 0
        
        # Hidden dependency: count elevated harmonic distortion
        if 'harmonic_distortion' in entry['diagnostics']:
            hd = entry['diagnostics']['harmonic_distortion']
            if hd > 0.8:
                report['high_distortion'] += 1

    # Key computation chain (non-obvious)
    avg_recovery = cumulative_recovery / critical_events if critical_events > 0 else 0
    base_health = valid_health_sum / sample_count if sample_count > 0 else 0
    
    # Weighted fusion metric
    distortion_penalty = report['high_distortion'] * 0.3
    health_adjustment = (base_health * 1.8) - distortion_penalty
    
    # Final non-linear transformation
    final_score = int((health_adjustment * 100) + (avg_recovery * 2.5))
    
    # Tertiary validation (unused branch)
    if final_score > 500:
        scaling_factor = 0.9
    else:
        scaling_factor = 1.0
    
    # ACTUAL ANSWER COMPUTATION (critical)
    diagnostic_key = sum(1 for e in log_data if e['health_index'] == 5) * 17
    context_enhancer = len([e for e in log_data if e['signal_value'] > 3.1]) * 3
    final_diagnostic = diagnostic_key + context_enhancer - int(avg_recovery)
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(log_entries, system_thresholds)
print(f"Target result: {final_diagnostic}")