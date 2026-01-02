import math

# Irrelevant helper function (decoy)
def compute_entropy(data):
    return sum([-p * math.log2(p) for p in data if p > 0])

# Unused transformation map
token_map = {i: chr(97 + (i % 26)) for i in range(50)}

# Simulated sensor readings with noise
def generate_signal(baseline, length=100):
    return [baseline + math.sin(i / 10) * 5 + ((i ** 2) % 3) for i in range(length)]

raw_readings = generate_signal(23.7, 80)

# Apply moving average filter (partially relevant but obfuscated path)
smoothed = [
    sum(raw_readings[i:i+5]) / 5
    for i in range(len(raw_readings) - 4)
]

# Extract every third reading (red herring)
third_sample = [smoothed[i] for i in range(0, len(smoothed), 3)]

# Normalize around mean (distraction)
mean_val = sum(smoothed) / len(smoothed)
normalized = [x - mean_val for x in smoothed]

# Bit manipulation decoy: fold normalized values into bit buckets
bit_fold = 0
for val in normalized[:10]:
    shifted = int(abs(val)) << 1
    bit_fold ^= shifted & 0b11111

# Real processing begins: slice central segment
central_window = normalized[10:50]

# Transform via nonlinear compression
transformed_data = [
    math.atan(x * 0.1) * 10 for x in central_window if abs(x) > 0.5
]

# Secondary filtering based on parity of index (misleading)
parity_filtered = [
    transformed_data[i] for i in range(len(transformed_data))
    if i % 2 == 1
]

# Decoy statistical analysis
median_like = sorted(parity_filtered)[len(parity_filtered)//2] if parity_filtered else 0
deviation_proxy = sum([abs(x - median_like) for x in parity_filtered]) / len(parity_filtered) if parity_filtered else 0

# Key threshold derived from bit_fold (seemingly random but deterministic)
key_threshold = (bit_fold % 7) + 1.5

# Core logic hidden in apparent noise
def analyze_pattern(signal_chunk, threshold):
    count_above = 0
    cumulative = 0.0
    trend_bursts = 0
    prev = 0

    for i, val in enumerate(signal_chunk):
        if val > threshold:
            count_above += 1
            cumulative += val
        # Detect rising edge bursts
        if i > 0 and val > signal_chunk[i-1] and val > threshold:
            trend_bursts += 1
        prev = val

    # Final score combines multiple factors
    if count_above == 0:
        return 0.0
    balance_factor = cumulative / count_above
    burst_ratio = trend_bursts / (count_above + 1)
    return (balance_factor * 100) + (burst_ratio * 50)

# Critical execution point
filtration_score = analyze_pattern(transformed_data, key_threshold)

# Dead code path (never executed)
if False:
    backup_score = compute_entropy([x/10 for x in transformed_data])
    filtration_score = max(filtration_score, backup_score)

# Print final result as required
print(f"Result: {filtration_score}")