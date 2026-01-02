def preprocess_segment(data, window_size):
    """Irrelevant preprocessing function for signal segments."""
    return [sum(data[i:i+window_size]) for i in range(len(data)-window_size+1)]


def compute_entropy(seq):
    """Computes Shannon entropy - used as red herring."""
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

# System configuration (some irrelevant)
SAMPLE_RATE = 1024
WINDOW_SIZE = 16
DEBUG_MODE = False
MAX_BUFFER_LEN = 256

# Signal pattern buffer with synthetic data
pattern_buffer = [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1]

# Threshold map for analysis (key input)
threshold_map = {"low": 2, "high": 7, "critical": 12}

# Irrelevant diagnostic logs
log_entries = [
    "ERR: Timeout on channel 3",
    "INFO: Calibration complete",
    "WARN: High variance in sector 7",
    "DEBUG: Buffer flush successful"
]
log_summary = ''.join(log_entries).upper()
error_count = log_summary.count("ERR")
warm_count = log_summary.count("WARN")

# Phantom state tracker (distractor)
current_state = {"phase": "idle", "pulses": 0, "jitter": 0.034}
state_history = []
for _ in range(3):
    current_state["pulses"] += 2
    state_history.append(current_state.copy())  # Shallow copy only

# Auxiliary data structures (mostly unused)
signal_stats = {
    "mean": 0.56,
    "std": 0.12,
    "kurtosis": 2.8
}

freq_spectrum = list(range(50, 500, 10))
spectral_peaks = set(freq_spectrum[::5])
background_noise = {x for x in freq_spectrum if x % 25 == 0}
active_bands = spectral_peaks - background_noise  # Unused

# Simulated packet stream (irrelevant)
packet_headers = [
    {'id': 101, 'flags': 0b101},
    {'id': 102, 'flags': 0b011},
    {'id': 103, 'flags': 0b110}
]
aggregated_flag = 0
for pkt in packet_headers:
    aggregated_flag ^= pkt['flags']  # Bitwise XOR accumulation (distraction)

# Real computation begins here
shifted_pattern = pattern_buffer[2:] + pattern_buffer[:2]  # Rotate left by 2
inverted_pattern = [1 - bit for bit in shifted_pattern]  # Bit flip

# Count transitions (0->1 or 1->0) in inverted pattern
transitions = 0
for i in range(len(inverted_pattern)):
    if inverted_pattern[i] != inverted_pattern[(i+1) % len(inverted_pattern)]:
        transitions += 1

# Extract every 3rd element using slicing
sampled_data = inverted_pattern[::3]
impulse_score = sum(sampled_data) * len(sampled_data)

# Set-based analysis of indices
one_indices = {i for i, val in enumerate(inverted_pattern) if val == 1}
zero_indices = {i for i, val in enumerate(inverted_pattern) if val == 0}
alternating_mask = one_indices.symmetric_difference({2, 4, 6, 8})  # Artificial mask
mask_influence = len(alternating_mask & zero_indices)  # Overlap measure

# Core logic masked within multiple operations
rolling_window_sum = 0
for i in range(0, len(inverted_pattern), 4):
    chunk = inverted_pattern[i:i+4]
    if len(chunk) == 4:
        # Binary to decimal interpretation
        binary_str = ''.join(map(str, chunk))
        decimal_val = int(binary_str, 2)
        rolling_window_sum += decimal_val

# Conditional modulation based on control thresholds
modulation_factor = 1
if rolling_window_sum > threshold_map["high"]:
    modulation_factor = 2
elif rolling_window_sum < threshold_map["low"]:
    modulation_factor = 0

# Final diagnostic calculation
baseline_metric = transitions + impulse_score
adjusted_metric = baseline_metric * modulation_factor
penalty = len(one_indices) % 5
final_diagnostic = adjusted_metric - penalty + mask_influence

# Dead code path (never executed due to fixed data)
if any(x > 20 for x in freq_spectrum):
    final_diagnostic *= 0.5

# Output result
print(f"Result: {final_diagnostic}")