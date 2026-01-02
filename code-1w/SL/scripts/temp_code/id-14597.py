import math

# Irrelevant precomputed constants (distractors)
CALIBRATION_FACTOR = 0.873
REFERENCE_VOLTAGE = 3.3
MAX_ITERATIONS = 1000
TEMPORAL_OFFSET = 17

# System state simulation variables
class SensorNode:
    def __init__(self, id, status):
        self.id = id
        self.status = status
        self.buffer = []

    def collect_data(self, value):
        if len(self.buffer) < 5:
            self.buffer.append(value)
        else:
            self.buffer.pop(0)
            self.buffer.append(value)

# Unused function - red herring
def deprecated_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, int):
            checksum ^= item * 3
    return checksum % 256

# Recursive helper with actual relevance
def compute_entropy(seq, index=0):
    if index >= len(seq):
        return 0
    contribution = seq[index] * math.log(seq[index] + 1e-9) if seq[index] != 0 else 0
    return -contribution + compute_entropy(seq, index + 1)

# Misleading signal processing chain
def apply_filter(signal):
    filtered = []
    for i in range(len(signal)):
        if i == 0:
            filtered.append(signal[i])
        else:
            filtered.append((signal[i] + signal[i-1]) * 0.5)
    return filtered

# Core analysis logic
system_log = {"errors": [1, 0, 1, 1, 0], "uptime": 4762, "version": "2.4.1"}
quantum_buffer = [3, 1, 4, 1, 5, 9, 2, 6, 5]

# Dead code path - unused diagnostic mode
DIAGNOSTIC_MODE = False
if DIAGNOSTIC_MODE:
    print("Running in debug mode")
    for k, v in system_log.items():
        print(f"{k}: {v}")

# Decoy data structure manipulation
temp_analysis = {}
for i, val in enumerate(quantum_buffer):
    temp_analysis[f"sample_{i}"] = {
        "raw": val,
        "squared": val ** 2,
        "modular": val % 4
    }

# Actual critical computation begins here
active_nodes = []
for i in range(3):
    node = SensorNode(f"N{i}", "active" if i % 2 == 0 else "standby")
    if node.status == "active":
        active_nodes.append(node)

for i, val in enumerate(quantum_buffer):
    for node in active_nodes:
        node.collect_data(val * (i % 3 + 1))

# Real but obscured calculation path
buffer_sum = sum(quantum_buffer)
shifted_sum = buffer_sum >> 2  # Divide by 4 using bit shift

# Dictionary-based state mapping with relevant and irrelevant entries
state_weights = {
    "critical": 10,
    "warning": 5,
    "info": 1,
    "debug": 0,  # Unused level
    "unknown": -1
}

error_count = sum(system_log["errors"])
base_score = state_weights["warning"] * error_count

# Linear search through quantum buffer for pattern (actually used)
peak_count = 0
for val in quantum_buffer:
    if val > 5:
        peak_count += 1

# Entropy calculation is actually needed
entropy_value = compute_entropy(quantum_buffer)

# Red herring: complex but unused filter chain
filtered_buffer = apply_filter(quantum_buffer)
scaled_filtered = [x * 1.5 for x in filtered_buffer if x > 3]

# Final analysis function that combines key elements
def analyze_system_state(data, log):
    # Nested dictionary operations
    error_level = "critical" if log["errors"][0] == 1 else "info"
    weight = state_weights[error_level]
    
    # Modular arithmetic with rounding
    raw_metric = (sum(data) % 7) * math.sqrt(len(data))
    adjusted_metric = round(raw_metric, 3)
    
    # Use of recursion result
    entropy_influence = int(abs(entropy_value))
    
    # Multiple conditionals with one determining path
    if len(data) > 8 and peak_count >= 3:
        if weight == 10:
            multiplier = 3
        else:
            multiplier = 2
    else:
        multiplier = 1
    
    # Integration of multiple concepts
    intermediate = (adjusted_metric + entropy_influence) * multiplier
    
    # Final computation - only this matters
    final = int(intermediate) + (log["uptime"] % 23)
    
    # Dead code block - misleading return path
    if final < 0:
        return -final  # Never reached
    
    return final

# Execute critical statement
final_diagnostic = analyze_system_state(quantum_buffer, system_log)

# Print result as required
print(f"Target result: {final_diagnostic}")