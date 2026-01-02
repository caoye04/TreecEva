import itertools

# Simulated sensor fusion and diagnostic engine with red herrings
def collect_sensor_data():
    raw_readings = [127, 63, 255, 31, 15, 7]
    processed = []
    for val in raw_readings:
        if val & 128:  # Check high bit
            processed.append(val ^ 128)  # Flip highest bit
        else:
            processed.append(val)
    return processed

# Irrelevant calibration function (dead code path)
def calibrate_sensors_v1(data):
    return [x * 0.98 for x in data]

# Another decoy transformation
system_offset = 42
offset_lookup = {i: i * 3 + system_offset for i in range(10)}

# Real processing begins here
signal_buffer = collect_sensor_data()

# Misleading noise filter (never used)
def temporal_filter(sequence):
    return [a - b for a, b in zip(sequence[1:], sequence[:-1])]

# Key pattern analysis logic
def generate_combinations(values):
    combos = []
    for r in range(2, 4):
        combos.extend(itertools.combinations(values, r))
    return combos

# Hash-like transformation using XOR folding
def fold_sequence(seq):
    result = 0
    for item in seq:
        result ^= item * 3
    return result % 1000

# Secondary red herring: power state emulation
power_states = ['active', 'idle', 'sleep']
current_mode = power_states[0]
power_cycle_count = 0
for _ in range(3):
    power_cycle_count += 1
    current_mode = power_states[power_cycle_count % 3]

# Now begin actual diagnostic chain
filtered_signals = [x for x in signal_buffer if x > 10]  # Remove small values
extended_signals = filtered_signals + [fold_sequence(filtered_signals)]

# Generate complex feature set with distractors
all_features = []
decoy_feature = 0
for i in range(5):  # Extra loop with partial relevance
    if i % 2 == 0:
        combo_set = generate_combinations(extended_signals)
        feature_hash = sum(fold_sequence(c) for c in combo_set[:100]) % 8000
        all_features.append(feature_hash)
    else:
        # Dead computation branch (decoy)
        decoy_feature += i ** 4

# Critical system key derived from bit manipulation
def compute_system_key(data):
    key = 0
    for val in data:
        key ^= (val << 1) | (val >> 7)
    return key & 0xFF

system_key = compute_system_key(signal_buffer)

# Data structure cross-reference red herring
index_map = {i: fold_sequence([i, system_key]) for i in range(3)}
lookup_cache = []
for idx in index_map:
    temp = []
    for _ in range(2):
        temp.append(idx * system_key)
    lookup_cache.append(temp)

# Actual collection point
collected_signals = extended_signals.copy()

# Add more irrelevant state
battery_level = 87
temperature_log = [23.5, 24.1, 22.9]
last_sync = "2023-11-05T14:32:00Z"

# Core diagnostic analyzer (only this affects final answer)
def analyze_pattern(signal_list, key):
    base_value = 0
    for num in signal_list:
        if num & 1:  # odd numbers
            base_value += num ^ key
        elif num % 4 == 0:
            base_value -= num & key
    # Final adjustment based on combination count
    combo_count = len(list(itertools.combinations(signal_list, 3)))
    return (base_value + combo_count) % 10000

final_diagnostic = analyze_pattern(collected_signals, system_key)
print(f"Result: {final_diagnostic}")