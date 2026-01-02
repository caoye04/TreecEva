def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant diagnostic tracking (red herring)
diagnostic_log = [0] * 15
def log_diagnostics(tag, value):
    diagnostic_log[tag % 15] = value % 1000

# Unused transformation path
def transform_data(arr):
    return [x ** 2 % 7 for x in arr if x % 3 != 0]

# Decoy function that looks important but isn't used
def compute_checksum(data):
    chk = 0
    for i, val in enumerate(data):
        chk ^= (val + i) * 3
    return chk % 997

# Real processing begins here
def generate_entropy_burst(length, seed=7):
    result = []
    val = seed
    for _ in range(length):
        val = (val * 7891 + 13) % 65536
        result.append(val)
    return result

# Misleading accumulation (dead end)
cumulative_trace = []
temp_aggregate = 0
for step in range(5):
    temp_val = (step ** 4) // (step + 1)
    temp_aggregate += temp_val
    cumulative_trace.append(temp_aggregate)

# Core data initialization
base_sequence = [1, 3, 2, 7, 4, 6, 5, 9, 8]
ref_set = {x for x in base_sequence if x % 2 == 0}
diagnostics = generate_entropy_burst(10, seed=11)

# Simulated signal refinement (distraction)
signal_power = 0
for idx, val in enumerate(diagnostics[:8]):
    if idx % 3 == 0:
        signal_power += (val // 100) * (idx + 1)

# Another decoy structure
status_flags = {}
for k in ['A', 'B', 'C']:
    status_flags[k] = False

# Critical entropy trail generation
entropy_trail = []
running_sum = 0
for i in range(len(diagnostics)):
    running_sum += diagnostics[i]
    if i % 4 == 3:
        entropy_trail.append(running_sum % 1000)
        running_sum = 0

# Dead branch with plausible-looking logic
if len(entropy_trail) > 10:
    entropy_trail = entropy_trail[:5]
else:
    shadow_copy = entropy_trail[::-1]
    for j in range(len(shadow_copy)):
        shadow_copy[j] = (shadow_copy[j] + 50) % 800

# Key analysis using set operations and string-encoded states
state_vector = []
for num in diagnostics:
    bin_str = bin(num)[2:]
    ones = bin_str.count('1')
    zeros = bin_str.count('0')
    if ones > zeros:
        state_vector.append(1)
    else:
        state_vector.append(0)

# String-based pattern tagging (distractor)
pattern_tag = ""
for bit in state_vector[:10]:
    pattern_tag += ('P' if bit else 'Q')
pattern_tag = pattern_tag.replace('PQ', 'X').replace('QP', 'Y')

# Actual relevant computation chain starts here
effective_modes = set()
for x in diagnostics:
    mod_x = x % 17
    if mod_x in ref_set:
        effective_modes.add(mod_x)

mode_strength = sum(effective_modes) * len(effective_modes)

# Secondary validation via sequence peaks
peak_count = analyze_pattern(base_sequence)

# Finalize using combined metrics
log_diagnostics(12, mode_strength)  # Log side effect

def finalize_processing(diag, trail):
    a = sum(diag[i] for i in range(0, len(diag), 3)) % 10000
    b = len(trail) * 113
    c = mode_strength  # From outer scope
    d = peak_count * 200
    intermediate = (a + b) ^ c
    intermediate = (intermediate + d) % 50000
    return abs(intermediate - 15000)

# Execution point of interest
filtration_score = finalize_processing(diagnostics, entropy_trail)
print(f"Result: {filtration_score}")