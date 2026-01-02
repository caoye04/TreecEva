import math

# Simulated sensor array data (irrelevant initial setup)
sensor_raw = [0.78, 0.45, 0.91, 0.12, 0.67]
offsets = [0.1, -0.05, 0.2, 0.0, -0.1]

def calibrate(x, o):
    return max(0.0, min(1.0, x + o))

calibrated = [calibrate(sensor_raw[i], offsets[i]) for i in range(len(sensor_raw))]

# Irrelevant signal smoothing block (dead path)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data)-1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Unused but plausible transformation
temporal_weights = [0.1, 0.2, 0.4, 0.2, 0.1]
filtered = [calibrated[i] * temporal_weights[i] for i in range(len(calibrated))]

# Real processing begins: transform raw with non-linear activation
def sigmoid(x):
    return 1 / (1 + math.exp(-x * 10))

transformed_data = [sigmoid(x - 0.5) for x in calibrated]

# Bit manipulation red herring (unused later)
status_code = 0b101010
mask = 0b111100
masked_status = status_code & mask
parity_check = bin(masked_status).count('1') % 2

# Decoy metric computation
baseline_score = sum(transformed_data) / len(transformed_data)
deviation_penalty = sum((x - baseline_score)**2 for x in transformed_data)

# Weighting function using lambda (required feature)
weight_function = lambda x: 0.5 + 0.5 * math.sin(math.pi * x)
weights = [weight_function(i / 4) for i in range(5)]

# Another decoy: circular buffer simulation (distractor)
circular_buffer = [0]*3
for i in range(10):
    circular_buffer[i % 3] = i * 0.1
buffer_sum = sum(circular_buffer)

# Core accumulation logic (critical path)
def aggregate_metrics(values, w):
    acc = 0.0
    for i in range(len(values)):
        # Introduce bitwise XOR on float bits via int cast (mixed paradigm)
        magic_factor = (i ^ 3) * 0.1
        weighted_val = values[i] * w[i] * (1 + magic_factor)
        acc += weighted_val
    # Non-linear final adjustment
    return acc ** 1.5

# Final computation
final_diagnostic = aggregate_metrics(transformed_data, weights)

# Output result as required
print(f"Target result: {final_diagnostic}")