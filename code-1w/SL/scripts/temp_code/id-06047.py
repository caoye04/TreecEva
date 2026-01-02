import math

# Simulated system telemetry (mostly irrelevant)
telemetry_data = [0.1, 0.4, 0.9, 1.2, 0.7, 0.3]
baseline_offset = sum(t for t in telemetry_data if t > 0.5)
normalized_bias = math.log(baseline_offset + 1) if baseline_offset > 0 else 0

# Red herring: unused function
def decrypt_signal(x):
    return (x * 17) ^ 0xFF

# Irrelevant transformation chain
raw_checksum = 0
for i in range(len(telemetry_data)):
    raw_checksum ^= int(telemetry_data[i] * 100)
    raw_checksum = (raw_checksum + i) % 256

# Dummy state tracker (dead code path)
class StateTracker:
    def __init__(self):
        self.history = []
        self.active = False

    def update(self, val):
        if self.active:
            self.history.append(val)

tracker = StateTracker()

# Core logic disguised among distractions
activation_map = {i: (i ** 2) % 7 for i in range(1, 10)}
logic_flow = [1, 3, 4, 7, 8]

# Unused but plausible-looking intermediate
temp_weights = list(map(lambda x: math.sin(x * 0.5) + 1, activation_map.keys()))

# Decoy calculation with misleading name
system_coherence = sum(activation_map[k] * 0.3 for k in activation_map if k % 2 == 1)

# Conditional expression with real impact
adjustment_factor = 1.5 if len(logic_flow) > 4 else 0.8

# Real computation buried in noise
aggregate_key = 0
for val in logic_flow:
    if val in activation_map:
        aggregate_key += activation_map[val]

# Bit manipulation red herring
packed_flags = 0
for shift in [1, 3, 4]:
    packed_flags |= (1 << shift)
    packed_flags &= ~((1 << (shift - 1)) | 0x02)

# Critical threshold derived via indirect method
threshold_seed = sum(math.ceil(math.cos(i) + 1) for i in range(1, 6))
activation_threshold = threshold_seed * 2.5

# Real processing function (uses lambda and conditional expressions)
def process_metrics(flow, thresh):
    base = sum(activation_map[v] for v in flow)
    modifier = (lambda x: x * 1.2 if x > 10 else x * 0.8)(base)
    # Final adjustment using conditional expression
    return modifier + (5 if any(v > 6 for v in flow) else -3)

# Secondary decoy function that looks important
def validate_chain(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1))

# Unused diagnostic set
redundant_diagnostics = {
    'integrity': validate_chain(logic_flow),
    'entropy': math.log(len(logic_flow) + 1),
    'checksum': raw_checksum
}

# Key execution point — this is where the real answer is computed
final_diagnostic = process_metrics(logic_flow, activation_threshold)

# Output must be printed exactly once
print(f"Result: {final_diagnostic}")