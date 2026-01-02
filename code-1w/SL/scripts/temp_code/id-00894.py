from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing system with red herrings

def analyze_signal_strength(raw_readings):
    # Irrelevant function - never called in execution path
    return sum(abs(x) for x in raw_readings if x != 0)


def generate_lookup_table(n):
    # Dead code path - generated but unused
    table = {}
    for i in range(n):
        table[i] = (i ** 2 + 3 * i + 7) % 97
    return table

def validate_checksum(frame):
    # Distractor function: looks important but not used in critical path
    return sum(frame) ^ 0xFF == len(frame)


def filter_anomalies(data_stream, threshold=50):
    # This function is called but its result is partially ignored
    filtered = []
    anomalies_detected = 0
    for val in data_stream:
        if abs(val) > threshold:
            anomalies_detected += 1
        else:
            filtered.append(val * 0.95)  # Slight adjustment
    # Return includes irrelevant stats
    return filtered, {'count': anomalies_detected, 'ignored': 'debug_info'}


def compute_phase_shift(sequence):
    # Unused complex logic
    shift = 0
    for a, b in zip(sequence, sequence[1:]):
        shift += (a ^ b) & 0xF
    return shift


def extract_timing_windows(events, window_size=3):
    # Real but obfuscated usage
    windows = []
    for i in range(len(events) - window_size + 1):
        windows.append(events[i:i+window_size])
    return windows


def aggregate_metrics(timing_data, flags):
    # Core computation buried in distractions
    base_score = 0
    
    # Real contribution: sum of XOR-reduced windows
    reduced_values = []
    for window in timing_data:
        xor_val = 0
        for w in window:
            xor_val ^= w  # Actual relevant operation
        reduced_values.append(xor_val)
    
    # Real: average of squares of reduced values
    squared = [x**2 for x in reduced_values]
    base_score = sum(squared) / len(squared) if squared else 0
    
    # Fake modifiers that look impactful but are overridden
    temp_debug = {'stage1': base_score}
    adjustment_factor = 1.0
    
    # Multiple branches with only one affecting outcome
    if flags['mode'] == 'legacy':
        adjustment_factor = 0.8
    elif flags['mode'] == 'turbo':
        adjustment_factor = 1.2
    else:
        adjustment_factor = 1.0  # Neutral override
    
    # Red herring: bit manipulation that does nothing due to constant
    meta_flag = flags['debug'] ^ flags['active']
    decoy_value = (meta_flag << 4) & 0xFF
    final_adjustment = adjustment_factor  # Ignore decoy
    
    # Final result built from actual computation
    result = int(base_score * final_adjustment) + flags['offset']
    
    # Unused intermediate variables to distract
    diagnostic_trace = {
        'raw_input_hash': 0xABCD,
        'processing_mode': 'advanced',
        'decoy_metric': decoy_value
    }
    
    return result

# --- Main Execution with Misleading Setup ---
if __name__ == '__main__':
    # Sensor input simulation (real data)
    primary_feed = [12, -5, 8, 3, 19, -2, 7]
    secondary_feed = [4, 17, -9, 6, 11]  # Partially unused
    
    # Irrelevant preprocessing
    lookup = generate_lookup_table(50)  # Computed but unused
    checksum_valid = validate_checksum(primary_feed[:4])  # Computed, unused
    
    # Real filtering (but only first return value used)
    cleaned_primary, stats = filter_anomalies(primary_feed, threshold=10)
    
    # Real data transformation
    timing_windows = extract_timing_windows(cleaned_primary, window_size=3)
    
    # Fake signal analysis (dead end)
    phase_result = compute_phase_shift(secondary_feed)
    
    # Flags with misleading fields
    config_flags = {
        'mode': 'standard',
        'debug': True,
        'active': True,
        'offset': 42,
        'timeout': 3000,
        'retry_limit': 3,
        'buffer_size': 256
    }
    
    # Critical statement
    final_diagnostic = aggregate_metrics(timing_windows, config_flags)
    
    # Print required output
    print(f"Result: {final_diagnostic}")