from collections import defaultdict, Counter

# Simulated system telemetry data with mixed signal types
def collect_signals(device_id, duration):
    signals = []
    for t in range(0, duration * 10, 1):
        phase = (t / 10) % 6.28
        signal_val = int(50 + 30 * ((t % 7) / 7) + 20 * abs(__import__('math').sin(phase)))
        signals.append({'time': t, 'value': signal_val, 'device': device_id})
    return signals

# Irrelevant auxiliary function – dead code path
def analyze_frequency_spectrum(raw_samples):
    fft_buffer = [0] * 128
    magnitude = 0
    for i in range(len(raw_samples)):
        if i < 128:
            fft_buffer[i] = raw_samples[i]['value'] * 0.5
    total_power = sum([x ** 2 for x in fft_buffer])
    return {'power': total_power, 'bins': fft_buffer}

# Misleading transformation – looks important but unused in final result
def compute_entropy(data_stream):
    freqs = defaultdict(int)
    for val in data_stream:
        freqs[val % 256] += 1
    total = len(data_stream)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

# Core diagnostic processor
def filter_anomalies(log_entries, threshold):
    anomalies = []
    window_avg = 0
    history = []
    for entry in log_entries:
        val = entry['value']
        history.append(val)
        if len(history) > 5:
            history.pop(0)
        if len(history) == 5:
            window_avg = sum(history) / 5
        if val > threshold and val > window_avg * 1.4:
            anomalies.append(entry)
    return anomalies

# Secondary metric calculator – partially relevant
def extract_trends(anomaly_list):
    trend_map = defaultdict(int)
    for item in anomaly_list:
        bucket = item['time'] // 10
        trend_map[bucket] += 1
    return dict(trend_map)

# Main processing pipeline
def process_metrics(telemetry_log, base_limit):
    # Step 1: Filter critical anomalies
    critical_events = filter_anomalies(telemetry_log, base_limit)
    
    # Distractor: Count character-like patterns in fake 'message traces'
    fake_messages = ["ERR_{}".format(ev['time']) for ev in critical_events]
    char_counter = Counter(''.join(fake_messages))
    rare_chars = [char for char, cnt in char_counter.items() if cnt < 2]
    
    # Step 2: Extract temporal trends
    trends = extract_trends(critical_events)
    
    # Step 3: Compute trend-weighted index
    weighted_index = 0
    for period, count in trends.items():
        weighted_index += count * (period + 1) * 10
    
    # Step 4: Apply correction factor based on trend distribution
    if trends:
        sorted_peaks = sorted(trends.values(), reverse=True)
        if len(sorted_peaks) > 2:
            top_two_ratio = sorted_peaks[0] / sorted_peaks[1] if sorted_peaks[1] > 0 else float('inf')
            weighted_index = int(weighted_index * (0.8 + 0.2 * min(top_two_ratio, 2)))
    
    # Step 5: Introduce decoy calculation with bitwise red herring
    decoy_key = 0
    for ch in rare_chars:
        decoy_key ^= ord(ch) << 2
    decoy_metric = (decoy_key & 0xFFFF) % 97
    
    # Final computation – only weighted_index matters
    adjustment = 1
    if decoy_metric > 50:
        adjustment = 2
    final_score = weighted_index // adjustment
    
    # Irrelevant sorting distraction
    _ = sorted([final_score, decoy_metric, len(rare_chars), base_limit], reverse=True)
    
    return final_score

# Generate input data
raw_telemetry = collect_signals(device_id=7, duration=60)
baseline_ref = 78

# Dead function call – misleading but harmless
_ = analyze_frequency_spectrum(raw_telemetry)

# Key execution point
final_diagnostic = process_metrics(raw_telemetry, baseline_ref)

# Output result
print(f"Target result: {final_diagnostic}")