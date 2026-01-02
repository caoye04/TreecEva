import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw_data = [i * 0.5 + (i % 7) for i in range(12)]
    offset = 3.14
    scaled_data = [x * 1.2 + offset for x in raw_data]
    return scaled_data

# Irrelevant helper - dead code path
def deprecated_filter(x):
    return x > 5 and x < 9

# Unused transformation chain
def transform_legacy(data):
    temp_result = [math.sin(x / 10) for x in data]
    filtered = [y for y in temp_result if y > 0.1]
    return [z * 2 for z in filtered]

# Distractor: complex but unused signal function
def generate_noise(samples):
    noise = []
    for i in range(len(samples)):
        phase = i % 4
        if phase == 0:
            noise.append(0.3)
        elif phase == 1:
            noise.append(-0.2)
        else:
            noise.append(0.05)
    return [s + n for s, n in zip(samples, noise)]

# Real processing begins here
processed_samples = []
def process_signal(raw):
    global processed_samples
    temp_cache = {}
    cleaned = [round(x, 2) for x in raw if x > 4.0]  # filter and clean

    # Bit manipulation red herring
    magic_key = 0b1010
    for i in range(len(cleaned)):
        shifted = i << 2
        masked = shifted & magic_key
        temp_cache[i] = masked

    # Actual relevant transformation
    transformed = []
    for val in cleaned:
        if val % 1 == 0:
            transformed.append(int(val) ^ 3)  # XOR with 3
        else:
            transformed.append(round(val + 1.5, 2))
    processed_samples = transformed
    return transformed

# Diagnostic engine with conditional logic distractions
def evaluate_health(metrics):
    baseline = 7.5
    deviations = 0
    for m in metrics:
        if isinstance(m, float):
            if abs(m - baseline) > 2.0:
                deviations += 1
        elif isinstance(m, int):
            if m < 0 or m > 15:
                deviations += 1
    return deviations < 3  # health threshold

# Another decoy function - looks important but unused
def compute_entropy(data):
    freq_map = {}
    for d in data:
        freq_map[d] = freq_map.get(d, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Core analysis function - actually used
threshold_reference = {k: k * 0.7 for k in range(1, 10)}
def analyze_signal(signal_list):
    score = 0
    for item in signal_list:
        if isinstance(item, int):
            # Check against threshold map
            key = item % 9 + 1
            if item > threshold_reference[key]:
                score += key
        elif isinstance(item, float):
            if item.is_integer():
                score += int(item) % 5
            else:
                score += int(item // 1) % 4
    flag = evaluate_health(signal_list)
    if flag:
        score *= 2
    else:
        score += 5
    # Final computation
    adjustment = (score & 0b111)  # bitwise mask with last 3 bits
    final_score = score - adjustment + 10
    return final_score

# Execution flow with irrelevant setup
raw_samples = collect_samples()
legacy_filtered = transform_legacy(raw_samples)  # unused
noisy_signal = generate_noise(raw_samples)  # unused

# Key execution point: real processing
process_signal(raw_samples)
final_diagnostic = analyze_signal(processed_samples)
print(f"Target result: {final_diagnostic}")