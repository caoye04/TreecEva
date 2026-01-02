import math

# Simulated sensor array diagnostics with noise filtering and pattern analysis
def collect_sensor_data():
    raw_values = [127, 255, 63, 191, 31, 159, 95, 223]
    timestamps = [1000, 1005, 1010, 1015, 1020, 1025, 1030, 1035]
    metadata = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    
    # Irrelevant transformation (distractor)
    scaled_meta = [ord(m) * 2 for m in metadata]
    temp_correction = sum(scaled_meta) / len(scaled_meta)
    
    return list(zip(raw_values, timestamps, metadata))


def filter_noise(data_sequence):
    cleaned = []
    noise_floor = 32
    spike_threshold = 200
    
    # Decoy variables (misleading intermediate values)
    average_energy = 0
    cumulative_power = 0
    
    for val, ts, meta in data_sequence:
        if val > noise_floor and val < spike_threshold:
            cleaned.append((val, ts))
    
    # Dead computation path (unused)
    if len(cleaned) > 5:
        adjusted_avg = sum(v for v, _ in cleaned) / len(cleaned)
        variance = sum((v - adjusted_avg)**2 for v, _ in cleaned)
    
    return cleaned


def reconstruct_waveform(signal_pairs):
    waveform = []
    prev = 0
    
    for value, _ in signal_pairs:
        delta = value - prev
        phase_shift = int(math.sin(delta * 0.01) * 10)
        waveform.append(value + phase_shift)
        prev = value
    
    # Unused but plausible-looking transformation
    envelope = max(waveform) - min(waveform)
    normalized = [w / (envelope + 1e-8) for w in waveform]
    
    return waveform


def detect_anomalies(series):
    anomalies = []
    for i, x in enumerate(series):
        if i == 0:
            continue
        diff = abs(x - series[i-1])
        if diff > 70:
            anomalies.append(i)
    
    # Red herring: complex statistical check that isn't used
    if len(anomalies) > 0:
        mean_gap = sum(abs(series[j] - series[j-1]) for j in range(1, len(series)))
        predicted_next = series[-1] + (mean_gap / (len(series) - 1))
    
    return anomalies if len(anomalies) <= 3 else [len(series)]


def compress_data(seq):
    # Bit manipulation decoy
    packed = 0
    for i, v in enumerate(seq):
        packed |= (v & 0xF) << (4 * (i % 8))
    
    # Hash-like checksum (not actually used in final result)
    checksum = sum(seq) ^ len(seq)
    
    return [x for x in seq if x % 2 == 1]  # Return only odd values


def calculate_entropy(values):
    from collections import Counter
    count = Counter(values)
    total = len(values)
    entropy = 0.0
    for c in count.values():
        p = c / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)


def group_by_phase(readings):
    groups = {'alpha': [], 'beta': [], 'gamma': []}
    for i, val in enumerate(readings):
        if i % 3 == 0:
            groups['alpha'].append(val)
        elif i % 3 == 1:
            groups['beta'].append(val)
        else:
            groups['gamma'].append(val)
    
    # Distracting aggregation
    sizes = {k: len(v) for k, v in groups.items()}
    total_elements = sum(sizes.values())
    
    return groups


def analyze_readings(signal_chain):
    # Key logic steps
    grouped = group_by_phase(signal_chain)
    alpha_vals = grouped['alpha']
    beta_vals = grouped['beta']
    gamma_vals = grouped['gamma']
    
    # Real computation chain
    a_sum = sum(alpha_vals)
    b_prod = 1
    for x in beta_vals:
        b_prod *= (x % 7 + 1)  # Prevent zero
    
    g_max = max(gamma_vals) if gamma_vals else 0
    
    # Composite diagnostic score (this is the answer)
    base_score = a_sum + (b_prod % 100) - g_max
    
    # More red herrings
    avg_val = sum(signal_chain) / len(signal_chain)
    peak_to_peak = max(signal_chain) - min(signal_chain)
    stability_index = math.cos(peak_to_peak * 0.01)
    
    final_score = base_score + int(stability_index * 10)
    
    # This looks important but is unused
    if final_score > 100:
        normalized_diagnostic = final_score / 2.5
    elif final_score < 0:
        normalized_diagnostic = abs(final_score) ** 0.5
    
    return final_score

# Main execution flow
sensor_log = collect_sensor_data()
processed_signals = filter_noise(sensor_log)
raw_wave = reconstruct_waveform(processed_signals)
anomaly_list = detect_anomalies(raw_wave)
filtered_wave = compress_data(raw_wave)
entropy_metric = calculate_entropy(filtered_wave)
final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")