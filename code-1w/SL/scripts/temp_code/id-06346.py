def analyze_pattern(seq, threshold):
    return sum(1 for x in seq if x > threshold) > len(seq) // 2

# Irrelevant signal preprocessing (red herring)
signal_buffer = [0.1, 0.4, 0.8, 0.2, 0.9]
normalized_power = [round(x ** 2 + 0.05, 2) for x in signal_buffer]
baseline_offset = sum(normalized_power) / len(normalized_power)

def encode_frame(data):
    # Unused encoding function (dead code path)
    return [d ^ 7 for d in data]

# Distractor variables with plausible but unused computations
sync_pulse = 23
pulse_sequence = [sync_pulse + i * 3 for i in range(5)]
checksum = 0
for p in pulse_sequence:
    checksum ^= p

# Core logic disguised among noise
transmission_key = 17
activation_sequence = [1, 0, 1, 1, 0, 1]

# Bit manipulation mixed with list logic
masked_key = transmission_key & 0b1111  # Truncates to 1-bit
shifted_activation = [(x << 1) ^ 1 for x in activation_sequence]

# Conditional expression (required feature)
feedback_state = 'active' if sum(shifted_activation) > 10 else 'standby'

# Simulated hardware state transitions (partially relevant)
current_state = 1
for bit in shifted_activation:
    current_state = (current_state ^ bit) & 1

# Decoy aggregation function
def aggregate_metrics(logs):
    total = 0
    for log in logs:
        if isinstance(log, int):
            total += log % 100
    return total

# Unused diagnostic chain
error_log = [101, 203, 405]
system_health = aggregate_metrics(error_log)

# Key recursive transformation (core concept)
def process_state(key, seq):
    if len(seq) <= 1:
        return seq[0] if seq else 0
    
    # Mixed arithmetic and bitwise ops
    mid = len(seq) // 2
    left = process_state(key, seq[:mid])
    right = process_state(key, seq[mid:])
    
    # Non-linear combination
    combined = (left + right + (key & 0b1)) % 7
    key = (key >> 1) | (combined << 4)  # Mutate key (ignored effect)
    
    return combined

# Secondary distractor: string-based analysis (irrelevant)
status_flag = 'OK'
diagnostic_token = ''.join([status_flag.lower(), '_PASS'])
token_value = sum(ord(c) for c in diagnostic_token) % 50

# Critical execution point
final_diagnostic = process_state(transmission_key, activation_sequence)

# Output requirement
print(f"Target result: {final_diagnostic}")