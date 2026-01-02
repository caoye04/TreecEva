import math

def analyze_signal_strength(signal_data, threshold=0.75):
    strong_signals = []
    weak_signals = []
    for idx, val in enumerate(signal_data):
        if val > threshold:
            strong_signals.append((idx, val))
        else:
            weak_signals.append((idx, val))
    return strong_signals, weak_signals


def calculate_phase_shift(frequency, time_delay):
    return (2 * math.pi * frequency * time_delay) % (2 * math.pi)


def generate_harmonic_interference(harmonics):
    interference_pattern = []
    for h in range(1, harmonics + 1):
        phase = calculate_phase_shift(h * 50, 0.01)
        interference_pattern.append(math.sin(phase))
    return interference_pattern

# Distractor: Irrelevant signal processing function
def decrypt_channel_encoding(encoded_seq):
    decoded = []
    for i, x in enumerate(encoded_seq):
        decoded.append(x ^ (i % 256))
    return decoded

# Distractor: Unused error simulation
def simulate_packet_loss(loss_rate, packet_count):
    import random
    lost = 0
    for _ in range(packet_count):
        if random.random() < loss_rate:
            lost += 1
    return lost

# Core logic with multiple concepts
transmission_matrix = [
    [1.2, 0.8, 1.5],
    [0.9, 1.1, 1.3],
    [1.0, 0.7, 1.6]
]

baseline_frequencies = [440, 880, 1320]
efficiency_log = [0.88, 0.91, 0.85]

# Misleading intermediate calculation (not used in final result)
avg_efficiency = sum(efficiency_log) / len(efficiency_log)
temp_correction_factor = math.log(avg_efficiency + 1) * 100

# Distractor: Fake optimization path
def deprecated_optimization(mat):
    total = 0
    for row in mat:
        for v in row:
            total += v ** 0.5
    return total * 0.1

# Real optimization function
def optimize_bandwidth(matrix, logs):
    adjusted = []
    for i, (row, log_val) in enumerate(zip(matrix, logs)):
        row_sum = 0
        for j, elem in enumerate(row):
            # Apply non-linear gain based on position and log efficiency
            if i == j:
                row_sum += elem * log_val * math.exp(0.1 * i)
            else:
                row_sum += elem * (1 - 0.1 * j)
        adjusted.append(row_sum)
    
    # Secondary transformation using enumerate and conditional logic
    transformed = []
    for idx, val in enumerate(adjusted):
        if val > 1.0:
            transformed.append(val * efficiency_log[idx] + 0.05)
        else:
            transformed.append(val)
    
    # Final aggregation with bit manipulation red herring
    raw_total = sum(transformed)
    bit_mask = (1 << 5) - 1  # 31, looks important but unused
    scaling_factor = 1.75 + (len(transmission_matrix) * 0.05)
    
    # Actual final computation
    result = raw_total * scaling_factor
    
    # Dead code branch - never executed
    if False:
        backup = 0
        for x in generate_harmonic_interference(5):
            backup += abs(x)
        result = backup * 10
    
    return result

# Execution flow with hidden dependencies
signal_dataset = [0.6, 0.82, 0.91, 0.67, 0.74]
_, _ = analyze_signal_strength(signal_dataset)

# Irrelevant harmonic generation
_ = generate_harmonic_interference(4)

# Key execution point
final_bandwidth = optimize_bandwidth(transmission_matrix, efficiency_log)

# Output result as required
print(f"Result: {final_bandwidth}")