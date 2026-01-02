import itertools

# System diagnostics simulation for distributed sensor network
sensor_ids = [101, 102, 103, 104]
timestamps = [1623456000, 1623456060, 1623456120]
baseline_readings = [0.87, 0.93, 0.88, 0.91]

def generate_noise_factor(seed):
    # Irrelevant helper with misleading purpose
    return (seed * 0.01) % 0.5

def compute_signal_strength(signal, distance):
    # Unused function - red herring
    return signal / (distance ** 2)

def validate_checksum(data_chunk):
    # Distractor logic: looks important but unused in critical path
    return sum(data_chunk) % 256 == data_chunk[-1]

# Simulated network states with irrelevant transformations
raw_data_packets = []
for sid in sensor_ids:
    packet = [sid]
    for ts in timestamps:
        val = (sid + ts) % 100
        packet.append(val)
    packet.append(sum(packet) % 256)  # checksum (unused)
    raw_data_packets.append(packet)

# Decoy data structure
redundant_buffer = [[x * 0.1 for x in range(10)] for _ in range(5)]

# Real processing begins here
network_states = []
for i, reading in enumerate(baseline_readings):
    state_vector = []    
    for j in range(4):
        # Complex but partially relevant transformation
        temp_val = reading * (i + 1) * 100
        if j % 2 == 0:
            temp_val += 5
        else:
            temp_val -= 3
        state_vector.append(temp_val)
    network_states.append(state_vector)

# Irrelevant normalization routine
normalized_states = []
for vec in network_states:
    mag = sum(x**2 for x in vec) ** 0.5
    normalized_states.append([x/mag for x in vec])

# Weight matrix with decoy initialization
weights = []
for k in range(4):
    row = []
    for m in range(4):
        w = (k * m + 1) * 0.25
        if k == m:
            w += 0.1
        row.append(w)
    weights.append(row)

# Unused recursive diagnostic
def recursive_diagnose(depth, acc):
    if depth == 0:
        return acc
    return recursive_diagnose(depth - 1, acc + [depth * 2])

# Key computation buried in noise
intermediate_results = []
for idx in range(len(network_states)):
    row_result = 0
    for j in range(4):
        # Core calculation mixed with distractions
        contribution = network_states[idx][j] * weights[idx][j]
        adjustment = 0
        if idx > 0 and j < idx:
            adjustment = network_states[idx-1][j] * 0.1
        row_result += contribution - adjustment
    intermediate_results.append(row_result)

# Red herring: complex itertools usage with no impact
combinations = list(itertools.combinations_with_replacement([1,2], 3))
product_grid = list(itertools.product([0], repeat=2))

def analyze_pattern(seq):
    # Dead code path
    return max(seq) - min(seq)

# Final aggregation with misleading side calculations
auxiliary_sum = 0
for nr in normalized_states:
    auxiliary_sum += sum(nr[:2])

rolling_averages = []
for ir in intermediate_results:
    window_vals = [ir - 5, ir, ir + 3]
    avg = sum(window_vals) / len(window_vals)
    rolling_averages.append(avg)

# Critical statement
final_diagnostic = sum(rolling_averages) * 0.75

# Print required result
print(f"Result: {final_diagnostic}")