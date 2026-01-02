def preprocess_signal(raw):    
    # Irrelevant signal smoothing (red herring)
    smoothed = [x * 0.9 for x in raw]
    normalized = [x / max(smoothed) for x in smoothed]  # Unused
    return [int(x) for x in raw]  # Only this matters

# Misleading auxiliary function (dead path)
def calculate_entropy(data):
    from math import log
    freq = {}
    total = len(data)
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p, 2)
    return round(entropy, 3)

# Decoy transformation chain
def transform_v1(seq):
    return [x ^ 3 for x in seq]  # Never called

def transform_v2(seq):
    return [x << 1 for x in seq]  # Never used

# Core processing
threshold_map = {    
    'low': 15,
    'high': 75,
    'critical': 100
}

status_flags = [False, True, False, True]
dummy_counter = 0
for i in range(4):
    if status_flags[i]:
        dummy_counter += i * 2  # Distractor computation

dummy_counter *= 3  # More noise

raw_sensor_data = [20, 50, 30, 80, 10, 60, 90]
processed_data = preprocess_signal(raw_sensor_data)

# Another distraction: character counting in fake logs
system_log = "ERR@23|WRN@45|INF@12|ERR@67"
error_count = system_log.count("ERR")
warning_count = system_log.count("WRN")
log_diagnostics = {'errors': error_count, 'warnings': warning_count}  # Unused structure

# Bit manipulation decoy
bitmask = 0b10101010
inverted_mask = bitmask ^ 0xFF  # Looks important, not used

# Actual analysis logic
def analyze_readings(readings, limits):
    low_t, high_t, crit_t = limits['low'], limits['high'], limits['critical']
    stats = {
        'below_low': 0,
        'in_range': 0,
        'above_high': 0,
        'critical': 0
    }
    
    temp_buffer = []
    for val in readings:
        # Simulated multi-step classification with string-based tagging
        tag = ''
        if val < low_t:
            stats['below_low'] += 1
            tag = 'L'
        elif val < high_t:
            stats['in_range'] += 1
            tag = 'M'
        elif val < crit_t:
            stats['above_high'] += 1
            tag = 'H'
        else:
            stats['critical'] += 1
            tag = 'C'
        temp_buffer.append(f"{val}{tag}")  # String method use: concatenation simulation
    
    # Use of string method: join to form diagnostic token
    token_string = ''.join(temp_buffer)
    char_code_sum = sum(ord(c) for c in token_string if c.isalpha())  # Character counting logic
    
    # Final computation: mix of bitwise and arithmetic
    base_score = stats['critical'] * 1000 + stats['above_high'] * 100
    modifier = char_code_sum & 0xFF  # Use last 8 bits of char sum
    final_score = base_score + modifier
    
    # Red herring: unused nested structure
    debug_snapshot = {
        'input_length': len(readings),
        'token_len': len(token_string),
        'checksum': sum(readings) ^ modifier
    }
    
    return final_score

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Result: {final_diagnostic}")