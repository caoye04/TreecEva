import math

# Simulated sensor array diagnostics with noise filtering and data transformation

def collect_readings():
    raw_readings = [127, 64, 255, 32, 192, 16, 8, 4]
    noise_floor = 10
    filtered = [x for x in raw_readings if x > noise_floor]
    return filtered


def apply_calibration(data, factor=1.05):
    calibrated = []
    for val in data:
        adjusted = int(val * factor)
        # Simulate bit-level correction
        if adjusted & 1:
            adjusted ^= 1  # Ensure even values only
        calibrated.append(adjusted)
    return calibrated


def compute_entropy(data):
    total = sum(data)
    probs = [d / total for d in data]
    entropy = -sum(p * math.log2(p) for p in probs if p > 0)
    return round(entropy, 6)


def transform_signal(x):
    # Unused distractor function – simulates signal processing
    return (x >> 2) ^ (x << 1) & 255


def generate_checksum(arr):
    # Red herring: complex-looking but unused checksum logic
    chk = 0
    for i, v in enumerate(arr):
        chk ^= (v + i) * 3
    chk %= 10000
    return chk

# Irrelevant auxiliary data structures
offset_table = {i: (i * 17) % 23 for i in range(15)}
temp_log = {'status': 'ok', 'reads': 0, 'errors': [], 'mode': 'passive'}

# Real execution begins here
sensor_data = collect_readings()

# Distractor block: appears important but unused
if len(sensor_data) > 5:
    temp_log['mode'] = 'active'
    dummy_analysis = [transform_signal(x) for x in sensor_data]

# Actual relevant path
transformed_data = apply_calibration(sensor_data, factor=1.02)

# Bit manipulation layer: mask and shift pattern
masked_data = [(x & 0b11111100) >> 2 for x in transformed_data]  # Extract middle bits

# Conditional expression usage
config = {
    'threshold': 50,
    'debug_mode': False,
    'version': '2.1'
}

# Lambda for dynamic filtering
validator = lambda val: val >= config['threshold']

# Another red herring: dead code path
if config.get('validate_input'):
    verified_data = [x for x in masked_data if validator(x)]
else:
    verified_data = masked_data[:]  # Default fallback

# Compute secondary metric (distractor)
mean_value = sum(masked_data) / len(masked_data) if masked_data else 0
std_deviation = (sum((x - mean_value) ** 2 for x in masked_data) / len(masked_data)) ** 0.5 if masked_data else 0

# Core diagnostic processor
process_metrics = lambda data, cfg: (
    sum(
        (i + 1) * (d ^ 7)  # Position-weighted XOR transformation
        for i, d in enumerate(data[:8])
        if d % 3 != 0  # Filter condition
    ) + int(compute_entropy(data) * 100)
)

# Key assignment statement
final_diagnostic = process_metrics(transformed_data, config)

# Print result as required
print(f"Result: {final_diagnostic}")