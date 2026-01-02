import itertools

# System health monitoring simulation with obfuscating computations

def generate_synthetic_log(n):
    return [(i * i + 31) % 256 for i in range(n)]

def calculate_entropy(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    entropy = 0.0
    total = len(data)
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified pseudo-entropy
    return round(entropy, 4)

def xor_fold(data):
    result = 0
    for val in data:
        result ^= val
    return result & 0xFF

def extract_critical_flags(state_vector):
    # Real path: extracts mode flags
    flag = 0
    for i, val in enumerate(state_vector):
        if i % 5 == 0 and val > 50:
            flag |= (val >> 4) & 0x0F
    return flag

# Irrelevant helper - distractor
def smooth_data(signal):
    smoothed = []
    for i in range(len(signal)):
        neighbors = signal[max(0, i-1):min(i+2, len(signal))]
        smoothed.append(sum(neighbors) / len(neighbors))
    return [round(x, 2) for x in smoothed]

# Unused function - red herring
def validate_signature(structure):
    base = sum(structure) * 7
    return (base ^ 0xCAFE) % 1024

# Real processing chain
log_data = generate_synthetic_log(97)
log_checksum = xor_fold(log_data)  # Key value

# Distractor variables
filtered_log = [x for x in log_data if x % 3 != 0]
decoy_entropy = calculate_entropy(filtered_log)
smoothed_log = smooth_data(log_data[:20])

# System state with multiple fields (only some are relevant)
system_state = [
    127, 45, 89, 211, 64,
    183, 92, 77, 151, 205,
    33, 166, 74, 199, 58
]

# Compute auxiliary metrics (some irrelevant)
state_sum = sum(system_state)
state_xor = 0
for x in system_state:
    state_xor ^= (x * 3) & 0xFF

# Real logic buried here
mode_flag = extract_critical_flags(system_state)

# More distractions
snapshot = system_state[::3]
reversed_snap = list(reversed(snapshot))
fake_digest = sum(reversed_snap) ^ 0xFFFF

# Conditional expression - python feature
health_weight = 0.8 if len(log_data) > 50 else 0.5
temp_bias = (log_checksum + mode_flag) * health_weight

# Complex but ultimately unused transformation
combinations = list(itertools.combinations([system_state[i] for i in range(0, len(system_state), 4)], 2))
decoy_pairs_score = sum(a ^ b for a, b in combinations) % 1000

# Core diagnostic logic
adjusted_metric = (log_checksum + (mode_flag << 2)) & 0xFF

# Secondary adjustment using conditional expression
secondary_adjust = system_state[0] if adjusted_metric > 100 else system_state[-1]
final_diagnostic = adjusted_metric + (secondary_adjust // 4)

# Dead code path - never executed
if False:
    backup_system = [x ^ 0xAA for x in system_state]
    final_diagnostic = sum(backup_system) % 512

# Print target result
Result: {final_diagnostic}