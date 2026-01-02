import itertools

def preprocess_signal(raw):    
    # Irrelevant transformation (dead code path)
    temp_buffer = [x * 0.9 for x in raw if x > 5]
    filtered = list(filter(lambda x: x % 2 == 1, raw))
    shifted = [(x << 1) for x in filtered]  # Bit manipulation red herring
    return shifted[:len(shifted)//2]  # Partial use, misleading truncation

# Misleading auxiliary function that is never called
def legacy_calibrate(data):
    return sum([d ** 0.5 for d in data]) / len(data)

# Unused but plausible-looking diagnostic
baseline_offset = 7
reference_map = {i: i**2 for i in range(10)}

# Real processing begins here
raw_sensor_data = [3, 7, 8, 12, 5, 11, 14, 6]

def decode_sequence(seq):
    # Split and recombine string representation as distraction
    seq_str = ''.join(map(str, seq))
    segments = [seq_str[i:i+2] for i in range(0, len(seq_str), 2)]
    joined = '-'.join(segments)
    char_count = len(joined.replace('-', ''))  # Useless count
    return [int(s) for s in segments if s.isdigit() and int(s) > 9]

intermediate = preprocess_signal(raw_sensor_data)

# Distractor: complex counting with no impact
freq_stats = {}
for num in raw_sensor_data:
    freq_stats[num] = freq_stats.get(num, 0) + 1

# Real logic hidden among noise
trimmed = decode_sequence(intermediate)

# Key control flow with early return red herring
status_flags = []
for val in intermediate:
    if val > 20:
        status_flags.append(True)
    else:
        status_flags.append(False)

# Decoy assignment
aggregate_metric = sum(intermediate) * 0.5 + 3  # Looks important

# Actual relevant computation buried
processed_data = [x for x in raw_sensor_data if x in intermediate]

# Another decoy using lambda and itertools
combinations = list(itertools.combinations_with_replacement([2,3], 2))
dummy_score = sum(a * b for a, b in combinations)  # Meaningless aggregation

# Core logic disguised as post-processing
flag_state = any(status_flags) and (len(trimmed) >= 1)

# Final analysis with conditional expression
final_diagnostic = 0
if flag_state:
    base = sum(processed_data)
    adjustment = len(raw_sensor_data) - len(processed_data)
    final_diagnostic = base * 2 - adjustment
else:
    final_diagnostic = -1

# Critical print statement
print(f"Result: {final_diagnostic}")