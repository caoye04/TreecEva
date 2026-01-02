from collections import defaultdict, Counter
from itertools import cycle, islice

def simulate_sensor_readings(length):
    # Irrelevant helper function: simulates sensor noise
    return [i ^ (i >> 1) for i in range(length)]

def generate_checksum(data):
    # Distractor function: computes XOR checksum (not used in final result)
    chk = 0
    for x in data:
        chk ^= x * 3
    return chk % 1000

def preprocess_logs(raw_logs):
    # Misleading preprocessing with nested logic
    cleaned = []
    temp_store = defaultdict(int)
    for entry in raw_logs:
        if entry < 0:
            continue
        temp_store[entry] += 1
        if temp_store[entry] % 2 == 0:
            cleaned.append(entry * 2)
    return cleaned[:len(cleaned)//2]

def evaluate_stability(metrics):
    # Dead-end analysis path: looks important but unused
    rolling_avg = 0
    for i, val in enumerate(metrics):
        rolling_avg += (val - rolling_avg) / (i + 1)
    return rolling_avg > 50

def analyze_pattern(log_entries, config_thresholds):
    # Core logic buried in distractions
    state_tracker = defaultdict(list)
    flags = [False] * len(log_entries)
    shift_key = config_thresholds['base'] ^ config_thresholds['offset']

    # Real computation begins
    for idx, val in enumerate(log_entries):
        rotated = ((val << 3) & 0xFF) | (val >> 5)  # Bit manipulation
        state_tracker[val].append(rotated)

    # Extract frequency and apply threshold filter
    freq_map = Counter(log_entries)
    valid_seeds = []
    for k, v in freq_map.items():
        if v >= config_thresholds['minimum_count']:
            valid_seeds.append(k)

    # Secondary filtering based on bit criteria
    refined = []    
    for seed in valid_seeds:
        if (seed & shift_key) & 1:  # Use LSB of bitwise AND
            refined.append(seed)

    # Accumulate diagnostic value through cycle-based transformation
    pattern_cycle = cycle(refined)
    accumulator = 0
    for item in islice(pattern_cycle, 200):
        accumulator += item ^ shift_key

    diagnostic_score = accumulator % 784657  # Deterministic large integer

    # Red herring: complex-looking normalization (unused)
    normalized = diagnostic_score / (len(log_entries) or 1)
    confidence = len(refined) > 0 and normalized > 10.0

    return diagnostic_score

# --- Main Execution with Heavy Interference ---

# Irrelevant data generation
raw_sensor_data = simulate_sensor_readings(512)
checksum = generate_checksum(raw_sensor_data)  # Unused value

# Distractor variables
system_status = {'state': 'nominal', 'flags': [], 'version': 0xABC}
event_counter = defaultdict(lambda: 0)
for i in range(100):
    event_counter[f'evt_{i % 10}'] += 1

# Real input preparation (buried)
log_sequence = []
for i in range(1, 150):
    if i % 3 == 0:
        log_sequence.append(i * 4)
    elif i % 5 == 0:
        log_sequence.append(i * 2)
    else:
        log_sequence.append(i)

# Apply irrelevant preprocessing (looks like it's cleaning data)
processed_logs = preprocess_logs(log_sequence)

# Configuration that matters
thresholds = {
    'base': 23,
    'offset': 45,
    'minimum_count': 2
}

# Dead-end stability check
is_stable = evaluate_stability(processed_logs)  # Not used later

# Key execution point
final_diagnostic = analyze_pattern(log_sequence, thresholds)

# Output requirement
print(f"Target result: {final_diagnostic}")