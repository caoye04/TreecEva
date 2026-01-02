import math

# Simulated network telemetry data
telemetry_stream = [14, 28, 19, 35, 22, 47, 13, 29, 31, 20, 36, 25]

# Irrelevant red herring: Audio processing constants (unused)
AUDIO_SAMPLE_RATE = 44100
AUDIO_BUFFER_SIZE = 1024
audio_phase = 0.0

# Signal preprocessing parameters (some relevant, some not)
THRESHOLD_A = 20
THRESHOLD_B = 30
NORMALIZATION_FACTOR = 1.75
DECAY_RATE = 0.88

# Distractor variables: Unused calibration coefficients
CALIBRATION_X = 0.91
CALIBRATION_Y = 1.03
CALIBRATION_Z = 0.87

# Raw signal buffer with noise filtering
signal_buffer = []
for val in telemetry_stream:
    if val > THRESHOLD_A:
        normalized = (val * NORMALIZATION_FACTOR) / 2.5
        # Conditional expression for minor adjustment
        adjusted = normalized * (1.1 if val > THRESHOLD_B else 0.95)
        signal_buffer.append(round(adjusted))
    elif val < 15:
        # Rare event path - never reached due to data
        signal_buffer.append(val * 2)

# Extraneous string manipulation - red herring
debug_tag = "DIAGNOSTIC_0x1A"
diag_code = debug_tag.lower().replace("diagnostic", "CORE").strip("_")
diag_length = len(diag_code)  # Unused

# Network state simulation with bitmasking and slicing
network_state = 0b11010110101

# Misleading bit shift chain
temp_mask = (network_state << 3) & 0b111111111111
temp_mask = (temp_mask >> 2) ^ 0b10101010
# Actual relevant transformation
active_nodes = bin(network_state).count('1')

# Decoy function - looks important but unused
def compute_entropy(data):
    total = sum(data)
    probs = [d / total for d in data]
    return -sum(p * math.log2(p) for p in probs if p > 0)

# Another decoy: complex but irrelevant list slicing
shadow_copy = telemetry_stream[::2][1:4][::-1]  # [28, 22, 19] reversed → [19, 22, 28]
shadow_sum = sum(shadow_copy)  # 69 - looks meaningful but unused

# Real computation begins here — aggregation logic
node_power_levels = [x % 7 for x in signal_buffer]  # Modular arithmetic
power_avg = sum(node_power_levels) / len(node_power_levels)

# Conditional expression in accumulation
energy_bias = power_avg * (1.25 if active_nodes > 6 else 0.8)

# Key function that computes final result
def aggregate_metrics(state, buffer):
    # Bit manipulation meets arithmetic
    bit_population = bin(state)[2:].count('1')
    offset = bit_population * 11
    
    # Summation with filtering
    valid_signals = [x for x in buffer if x > 15]
    base_score = sum(valid_signals)
    
    # String-based switch (idiomatic Python)
    mode_flag = "HIGH" if base_score > 120 else "LOW"
    
    # Complex conditional expression with slicing
    modifier = float(mode_flag == "HIGH") + 0.5 if buffer[-3:] != [0,0,0] else 0.25
    
    # Final calculation
    result = (base_score + offset) * modifier
    return int(result)

# Execution point of interest
final_diagnostic = aggregate_metrics(network_state, signal_buffer)

# Print required output
print(f"Target result: {final_diagnostic}")