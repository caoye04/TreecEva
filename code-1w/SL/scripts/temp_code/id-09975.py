import math

# Simulated sensor array diagnostics with interference

def collect_diagnostics(raw_samples):
    normalized = [x / max(raw_samples) for x in raw_samples]
    filtered = list(filter(lambda x: x > 0.1, normalized))
    return [round(x, 3) for x in filtered]


def transform_sequence(seq, factor):
    # Irrelevant transformation path (dead code)
    return [int(x * factor) % 7 for x in seq]


def compute_entropy(values):
    # Misleading statistical distraction
    probs = [v / sum(values) for v in values]
    return round(-sum(p * math.log2(p) for p in probs), 4)


def generate_checksum(data):
    # Decoy function – looks important but unused in critical path
    checksum = 0
    for i, val in enumerate(data):
        checksum ^= int(val * 100) + i
    return checksum % 1000


def recursive_reduce(n, acc=0):
    # Red herring recursion with no impact on final result
    if n <= 0:
        return acc
    return recursive_reduce(n - 2, acc + (n % 3))

# Spurious data structures
auxiliary_map = {i: chr(65 + (i * 3) % 26) for i in range(15)}
temporary_buffer = []
for k in range(8):
    temporary_buffer.append(f"temp_{k % 3}:{pow(k, 3) - 2 * k}")

# Real signal processing begins
raw_sensor_data = [
    1024, 512, 768, 256, 896, 384, 640, 128, 704, 576, 
    960, 320, 832, 448, 768, 192, 672, 544, 800, 352
]

# Step 1: Normalize and filter
processed_data = collect_diagnostics(raw_sensor_data)

# Step 2: Define dynamic threshold logic (critical)
thresh_ref = [0.25, 0.3, 0.35]
threshold_func = lambda x: x > thresh_ref[len(thresh_ref) // 2]

# Step 3: Analyze readings — this is where the answer comes from
def analyze_readings(readings, predicate):
    high_freq = [r for r in readings if predicate(r)]
    low_freq = [r for r in readings if not predicate(r)]
    
    # Nested logic chain
    if len(high_freq) >= 5:
        base_score = sum(high_freq) * 1000
        adjustment = 0
        for val in low_freq:
            adjustment += int(math.sin(val * math.pi) * 100)
        base_score -= abs(adjustment)
        
        # Multi-step computation with dependencies
        temp_result = base_score
        for _ in range(2):
            temp_result = int(temp_result * 0.95)  # Decay factor applied twice
        
        # Final transformation using bit manipulation
        final_shift = temp_result >> 2
        masked = final_shift & 0xFFFF
        return masked if masked < 50000 else masked - 10000
    else:
        return compute_entropy(readings)  # Dead branch due to data

# Execute critical statement
final_diagnostic = analyze_readings(processed_data, threshold_func)

# Print required output
print(f"Result: {final_diagnostic}")