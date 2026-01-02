from collections import defaultdict, Counter
import math

# Simulated sensor data processing with red herrings and complex control flow
def preprocess_signal(raw_samples):
    processed = []
    noise_floor = 0.041
    gain_compensation = 1.87

    for sample in raw_samples:
        if abs(sample) < noise_floor:
            continue  # Filter out low-amplitude noise
        compensated = sample * gain_compensation
        if compensated > 1.0:
            compensated = 1.0
        elif compensated < -1.0:
            compensated = -1.0
        processed.append(compensated)
    
    # Irrelevant transformation (dead code path)
    fft_magnitude = [math.sqrt(x*x) for x in processed if x != 0.5]  
    normalization_factor = sum(fft_magnitude) if fft_magnitude else 1.0
    normalized = [x / normalization_factor for x in fft_magnitude]  # Unused

    return processed

# Misleading auxiliary function (decoy)
def calculate_entropy(data):
    counts = defaultdict(int)
    for x in data:
        counts[round(x, 1)] += 1
    total = len(data)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy  # Computed but not used in main logic

def detect_anomalies(time_series):
    anomalies = []
    for i in range(1, len(time_series)-1):
        prev, curr, next_val = time_series[i-1], time_series[i], time_series[i+1]
        if curr > prev and curr > next_val and curr > 0.8:  # Local maxima above threshold
            anomalies.append(i)
    return anomalies if len(anomalies) > 2 else [0] * 5  # Padding to mislead size expectations

def build_threshold_map(pattern):
    # Real usage: builds weight map based on character frequency
    freq = Counter(pattern)
    base_map = defaultdict(float)
    total_chars = len(pattern)
    
    # Relevant logic
    for ch, count in freq.items():
        base_map[ch] = round(count / total_chars, 3)
    
    # Distractor computation (irrelevant)
    ascii_offset_sum = sum([ord(ch)**0.5 for ch in pattern if ch.isupper()])
    dummy_map = {ch: ord(ch) % 7 for ch in set(pattern)}  # Unused structure
    
    # Final threshold derived from frequency distribution
    avg_freq = sum(base_map.values()) / len(base_map)
    for ch in base_map:
        if base_map[ch] > avg_freq:
            base_map[ch] *= 1.25
    
    return base_map

def analyze_pattern(buffer, thresholds):
    score = 0
    phase_weights = []

    # Complex signal phase analysis (only some branches are relevant)
    for entry in buffer:
        key_char = entry['trigger']
        magnitude = entry['level']
        if key_char in thresholds:
            weight = thresholds[key_char] * magnitude
            if weight > 0.3:
                phase_weights.append(weight * 0.9)
            elif weight > 0.15:
                phase_weights.append(weight * 0.6)
            else:
                phase_weights.append(weight * 0.3)
    
    # Dead code: simulation of fallback mechanism
    if not phase_weights:
        phase_weights = [0.1] * len(thresholds)
        recovery_mode = True
        adjustment = sum([len(str(w)) for w in phase_weights])  # Useless calc
    
    # Core computation
    raw_total = sum(phase_weights)
    penalty = len([w for w in phase_weights if w < 0.2]) * 0.05
    adjusted_total = raw_total - penalty
    
    # Final diagnostic derived from adjusted signal
    final_diagnostic = int((adjusted_total * 10000) % 973 + 142)  # Deterministic result
    
    # Red herring: unused cryptographic hash simulation
    hash_accum = 0
    for i, w in enumerate(phase_weights):
        hash_accum ^= int(w * 100) << (i % 4)
    scrambled = (hash_accum ^ 0xFFFF) & 0xFFF  # Looks important, unused
    
    return final_diagnostic

# Main execution with layered distractions
if __name__ == '__main__':
    # Input data setup
    raw_input_stream = [
        -0.032, 0.12, 0.05, 0.88, -0.01, 0.44, 0.89, 0.91, 0.07, 0.52, 
        0.11, 0.85, 0.23, 0.93, 0.04, 0.59, 0.61, 0.71, 0.82, 0.94
    ]

    # Irrelevant symbolic mapping (distractor)
    symbol_registry = {
        'A': 'Alpha', 'B': 'Beta', 'C': 'Gamma', 'D': 'Delta'
    }
    priority_queue = [k for k in symbol_registry.keys()]
    priority_queue.sort(reverse=True)

    # Signal processing pipeline
    cleaned = preprocess_signal(raw_input_stream)
    
    # Anomaly detection (output not used in final result)
    spikes = detect_anomalies(cleaned)
    spike_energy = sum([cleaned[i]**2 for i in spikes if i < len(cleaned)])  # Dead end

    # Character pattern with meaningful frequency distribution
    trigger_sequence = "ABACABBACABDABACABA"
    threshold_map = build_threshold_map(trigger_sequence)

    # Construct signal buffer using processed signal magnitudes
    signal_buffer = []
    step = 0
    for val in cleaned:
        if val > 0.5:
            trigger = trigger_sequence[step % len(trigger_sequence)]
            signal_buffer.append({'level': abs(val), 'trigger': trigger})
            step += 1

    # Decoy entropy calculation (uses data but doesn't affect output)
    dummy_entropy = calculate_entropy(cleaned)
    
    # Key statement
    final_diagnostic = analyze_pattern(signal_buffer, threshold_map)
    
    # Output the required result
    print(f"Target result: {final_diagnostic}")