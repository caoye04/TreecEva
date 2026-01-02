import math

# Simulated sensor data from environmental monitoring stations
def generate_noise(length):
    return [abs((i * 73) % 101 - 50) / 10.0 for i in range(length)]

def preprocess_signal(raw_signal):
    filtered = []
    for x in raw_signal:
        if x > 3.5:
            filtered.append(x * 0.8)
        elif x < 1.0:
            filtered.append(x + 0.6)
        else:
            filtered.append(x)
    return filtered

def compute_entropy(values):
    # Irrelevant function - acts as decoy for information-theoretic analysis
    freq_map = {}
    for v in values:
        bin_val = int(v * 10) % 8
        freq_map[bin_val] = freq_map.get(bin_val, 0) + 1
    entropy = 0.0
    total = len(values)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def validate_checksum(data):
    # Unused validation logic - dead code path
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= int(val * 10) % 256
    return checksum == 0x5A

def rolling_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        avg = sum(series[start:i+1]) / (i - start + 1)
        smoothed.append(round(avg, 3))
    return smoothed

def detect_spikes(signal, threshold_multiplier=2.5):
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    std_dev = math.sqrt(variance)
    spike_threshold = mean_val + threshold_multiplier * std_dev
    spikes = [1 if x > spike_threshold else 0 for x in signal]
    return spikes, spike_threshold

def shift_cipher(text, shift):
    # Distractor: string manipulation unrelated to main logic
    result = ''
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    return result

def count_characters(text):
    # Another distractor - character counting with no impact
    counts = {}
    for c in text.lower():
        if c.isalpha():
            counts[c] = counts.get(c, 0) + 1
    return counts

def linear_search(arr, target):
    # Simulated search used in a misleading context
    for idx, val in enumerate(arr):
        if abs(val - target) < 0.001:
            return idx
    return -1

def build_lookup_table(keys, offset=100):
    # Dictionary operation - partially relevant
    table = {}
    for k in keys:
        table[k] = (k * 31) % offset + 1
    return table

def analyze_pattern(data_stream, config_thresholds):
    # Core logic begins here
    processed = preprocess_signal(data_stream)
    rolled = rolling_average(processed, window=4)  # Smoothing
    
    # Bit manipulation red herring
    magic_flag = (len(rolled) << 2) ^ 0xFF
    temp_key = (magic_flag & 0xFFFF) >> 3
    
    # Real work: find dominant frequency band
    bins = [0] * 10
    for val in rolled:
        bin_idx = min(int(val), 9)
        bins[bin_idx] += 1
    
    # Use dictionary to map bin counts to significance levels
    significance_map = build_lookup_table(range(10), offset=50)
    total_significance = 0
    for i, count in enumerate(bins):
        if count > 0:
            total_significance += significance_map[i] * count
    
    # Spike detection
    spikes, spike_limit = detect_spikes(rolled)
    spike_count = sum(spikes)
    
    # Decoy conditional that looks important but doesn't affect output
    if compute_entropy(rolled) > 2.0 and validate_checksum(rolled):
        total_significance *= 1.2
    
    # Linear search for threshold crossover point
    reference_level = config_thresholds['base'] * 1.4
    index_of_interest = linear_search(rolled, reference_level)
    if index_of_interest == -1:
        index_of_interest = len(rolled) // 2
    
    # Final computation
    adjustment_factor = math.cos(math.pi * spike_count / 20)
    intermediate = total_significance * adjustment_factor
    
    # Key statement
    final_diagnostic = int(intermediate + index_of_interest * 2.718)
    
    # Never-used variables to increase interference
    encrypted_log = shift_cipher("diagnostic_run_complete", temp_key % 26)
    char_freq = count_characters(encrypted_log)
    anomaly_score = sum(char_freq.values()) * 0.5
    
    return final_diagnostic

# Main execution
if __name__ == "__main__":
    raw_sensor_input = generate_noise(35)
    thresholds = {
        'base': 2.1,
        'warning': 3.4,
        'critical': 4.8
    }
    final_diagnostic = analyze_pattern(raw_sensor_input, thresholds)
    print(f"Result: {final_diagnostic}")