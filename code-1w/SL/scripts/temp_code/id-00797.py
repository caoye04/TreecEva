import math

# Simulated system telemetry and diagnostic module
def analyze_phase_shift(frequency, amplitude, phase):
    # Irrelevant signal processing function (dead path)
    return (amplitude ** 2) * math.sin(phase + frequency)

def compute_entropy(sequence):
    # Unused entropy calculation for distraction
    freq_map = {}
    for item in sequence:
        freq_map[item] = freq_map.get(item, 0) + 1
    entropy = 0.0
    total = len(sequence)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 3)

def shift_register_update(state, mask=0b1011):
    # Bit manipulation red herring
    shifted = (state << 3) & 0xFFFF
    return shifted ^ mask

def validate_checksum(record):
    # Decoy validation logic
    checksum = 0
    for char in str(record):
        checksum += ord(char) % 7
    return checksum % 5 == 0

# Core diagnostic engine
def extract_timings(log_entries):
    timestamps = []
    for entry in log_entries:
        if 'timestamp' in entry and entry['status'] == 'ACTIVE':
            timestamps.append(entry['timestamp'])
    return timestamps

def calculate_jitter(timestamps):
    if len(timestamps) < 2:
        return 0.0
    differences = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps)-1)]
    mean_delta = sum(differences) / len(differences)
    variance = sum((d - mean_delta) ** 2 for d in differences) / len(differences)
    return round(math.sqrt(variance), 4)

def evaluate_stability_factor(jitter_value, threshold=15.75):
    if jitter_value == 0:
        return 100.0
    stability = max(0, (threshold - jitter_value) / threshold * 100)
    return round(stability, 2)

def aggregate_metrics(log_data, state_vector):
    # Extract relevant timing points
    valid_timestamps = extract_timings(log_data)
    jitter = calculate_jitter(valid_timestamps)
    
    # Real computation path
    base_score = evaluate_stability_factor(jitter)
    
    # Distractor: unused combinatorics
    n, r = len(valid_timestamps), 2
    if n >= r:
        combinations = math.factorial(n) // (math.factorial(r) * math.factorial(n - r))
    else:
        combinations = 0
    
    # Use dictionary and enumerate with zip (required Python features)
    status_map = {0: 'ERROR', 1: 'STANDBY', 2: 'ACTIVE', 3: 'OVERLOAD'}
    active_count = 0
    for idx, code in enumerate(state_vector):
        if code == 2:
            active_count += 1
    
    # Simulated hardware flags
    flags = [0b1010, 0b0110, 0b1100]
    masked_flags = [f & 0b0111 for f in flags]
    
    # Real dependency: final result depends on base_score and active modules
    module_bonus = active_count * 3.25
    penalty = len([f for f in masked_flags if f == 0b110]) * 1.75
    
    # Final diagnostic calculation
    final_diagnostic = base_score + module_bonus - penalty
    
    # Dead print statements for distraction
    # print(f'Debug: combinations={combinations}, entropy=N/A')
    # print(f'Flags processed: {masked_flags}')
    
    return round(final_diagnostic, 4)

# Simulated input data
timing_log = [
    {'timestamp': 100, 'status': 'ACTIVE', 'node': 'A1'},
    {'timestamp': 112, 'status': 'ACTIVE', 'node': 'B2'},
    {'timestamp': 128, 'status': 'ACTIVE', 'node': 'C3'},
    {'timestamp': 140, 'status': 'ACTIVE', 'node': 'D4'},
    {'timestamp': 165, 'status': 'ACTIVE', 'node': 'E5'},
    {'timestamp': 178, 'status': 'ACTIVE', 'node': 'F6'}
]

system_state = [1, 2, 0, 2, 3, 2, 1, 2]  # 2 = ACTIVE module

# Trigger key computation
final_diagnostic = aggregate_metrics(timing_log, system_state)

# Output target result
print(f"Target result: {final_diagnostic}")