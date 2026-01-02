import math

# Simulated network diagnostic system with data corruption recovery and health scoring

def decode_signal_integrity(raw_packets):
    if not raw_packets:
        return 0
    valid_segments = [p for p in raw_packets if len(p) > 3]
    total_power = sum([sum([ord(c) for c in p[:3]]) for p in valid_segments])
    return total_power % 97

def validate_checksum(frame_sequence):
    checksum = 0
    for seq in frame_sequence:
        checksum ^= sum(ord(seq[i]) * (i + 1) for i in range(len(seq)))
    return checksum % 53

# Irrelevant helper - decoy function
def calculate_bandwidth_efficiency(data_rate, latency):
    efficiency = (data_rate * 0.87) / (latency + 1e-5)
    normalization = math.log(efficiency + 1) if efficiency > 0 else 0
    return round(normalization, 3)

# Unused error simulation path
error_injection_mode = False
if error_injection_mode:
    raise RuntimeError("Simulated hardware fault")

def reconstruct_data_stream(corrupted_log, recovery_key):
    recovered = []
    for entry in corrupted_log:
        shifted = ''.join(chr((ord(c) - recovery_key) % 128) for c in entry)
        recovered.append(shifted)
    return recovered

# System constants (some are red herrings)
system_baseline = 42
scaling_factor = 1.61803  # Golden ratio - unused distraction
padding_offset = 2048       # Used only in dead code
noise_threshold = 0.001     # Unused parameter

# Simulated input data - network packet log with encoding artifacts
distorted_log = [
    "abcX1!", "mnopZ3@", "xyzA9#", "qrstB2$", "uvwxY5%"
]

frame_sequence = ["ACK", "SYN", "FIN", "RST", "PSH"]
raw_power_readings = [12.4, 13.1, 11.8, 14.2, 10.9]

# Step 1: Decode signal integrity from packets
signal_quality = decode_signal_integrity(distorted_log)  # Expected: 45

# Step 2: Validate transmission checksum
transmission_validity = validate_checksum(frame_sequence)  # Expected: 18

# Step 3: Compute entropy-based noise estimation (distractor)
noise_profile = ''.join([f[:2] for f in frame_sequence])
entropy_score = sum(ord(c) for c in noise_profile) % 100  # Red herring: 32

# Step 4: Reconstruct corrupted state log using key 5
reconstructed_log = reconstruct_data_stream(distorted_log, recovery_key=5)

# Step 5: Extract health indicators from reconstructed data
health_indicators = []
for line in reconstructed_log:
    if line.startswith('v'):
        health_indicators.append(ord(line[1]) - ord('a'))
    elif line.endswith('#'):
        health_indicators.append(int(line[-2]))

# Step 6: Compute system_health as sum of health indicators
system_health = sum(health_indicators)  # Only one entry ends with '#' → 'A9#' → 9

# Step 7: Build network state log using slicing and transformations
network_state_log = []
for i, item in enumerate(reconstructed_log):
    segment = item[i % len(item):][:5]  # slicing with dynamic start
    numeric_value = sum(ord(ch) for ch in segment) % 1000
    network_state_log.append(numeric_value)

# Step 8: Aggregate metrics using dictionary-based weighting
metric_weights = {
    'base': 0.3,
    'signal': 0.4,
    'health': 0.3
}

# Introduce set operations - collect unique high-value states
high_state_threshold = 300
recent_high_states = {val for val in network_state_log if val > high_state_threshold}
state_breadth = len(recent_high_states)  # Distractor metric: 3

# Actual aggregation
aggregate_metrics = lambda log, health: (
    metric_weights['base'] * (log[0] if log else 0) +
    metric_weights['signal'] * signal_quality +
    metric_weights['health'] * health
)

# Step 9: Apply environmental correction based on power variance
power_variance = max(raw_power_readings) - min(raw_power_readings)
corrective_factor = 0
if power_variance > 3.0:
    corrective_factor = int(power_variance * 2)  # 3.3 → 6
else:
    corrective_factor = -5

# Step 10: Compute final diagnostic score
final_diagnostic = aggregate_metrics(network_state_log, system_health) + corrective_factor

# Dead code branch - misleading alternative logic
if len(network_state_log) < 3:
    final_diagnostic *= 0.5  # Never executed

# Unused data transformation - creates irrelevant intermediate
shadow_copy = network_state_log[::-1]
shadow_weights = {i: v * 0.1 for i, v in enumerate(shadow_copy)}

# Print result as required
print(f"Result: {final_diagnostic}")