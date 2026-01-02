from collections import defaultdict, Counter

# Simulated health monitoring system with signal processing and noise filtering

def analyze_rhythm(signal):
    if not signal:
        return 0
    rhythm_score = 0
    for i in range(1, len(signal)):
        if signal[i] > signal[i-1]:
            rhythm_score += 1
        elif signal[i] < signal[i-1]:
            rhythm_score -= 1
    return abs(rhythm_score)


def generate_baseline(length):
    # Irrelevant helper - generates dummy baseline (dead path in logic)
    return [0.5 * (i % 7) for i in range(length)]

# Unused intermediate variables (distractors)
decoy_weights = [0.1, 0.3, 0.6]
scaling_factor = 2.718
temp_cache = set()

# Real data input - vital signs over time
vital_reads = [
    [72, 75, 70, 68, 74],
    [80, 85, 88, 82, 79],
    [65, 63, 67, 70, 72],
    [90, 95, 92, 88, 85]
]

# Noise injection simulation (partially relevant but masked)
noise_profile = lambda x: (x ^ 3) & 1  # Bitwise red herring

# Signal extraction using rhythm analysis
extracted_signals = []
for readings in vital_reads:
    filtered = [x for x in readings if x > 65]  # Physiological threshold
    extracted_signals.append(analyze_rhythm(filtered))

# Data aggregation layer (relevant)
aggregated_diagnostics = defaultdict(int)
for idx, score in enumerate(extracted_signals):
    aggregated_diagnostics[f'window_{idx}'] = score

# Decoy computation path (never used)
shadow_metric = 0
for k in range(5):
    shadow_metric += (k * k) % 4

# Core threshold logic with conditional expression
threshold_func = lambda x: True if x >= 2 else False

# Secondary decoy function (misleading)
def compute_entropy(data):
    freqs = Counter(data)
    total = len(data)
    entropy = 0
    for count in freqs.values():
        p = count / total
        entropy -= p * p  # Not real entropy, but looks plausible
    return entropy

# Real processing function with multiple concepts
health_data = [1, 0, 1, 1, 0, 1, 1, 1]

def process_metrics(data, predicate):
    # Complex control flow with nesting and early returns
    if sum(data) == 0:
        return -1
    
    # Bit manipulation + arithmetic mix
    transformed = 0
    for bit in data:
        transformed = (transformed << 1) | bit
    
    # Logical masking with irrelevant shift
    mask = 0b1010101
    masked_value = transformed ^ mask  # XOR obfuscation
    
    # Conditional counting with lambda filter
    count_positive = len(list(filter(lambda x: x == 1, data)))
    
    # Multi-step diagnostic calculation
    base_diagnostic = masked_value * count_positive
    
    # Redundant but plausible-looking normalization
    normalization_shift = 2
    normalized = base_diagnostic >> normalization_shift
    
    # Final decision gate (short-circuit logic)
    if predicate(count_positive) and normalized > 10:
        adjustment = sum([i for i in range(count_positive)])  # Triangular number
        final_diagnostic = normalized + adjustment
    else:
        final_diagnostic = normalized - 1
    
    # Dead code branch (never reached due to structure)
    if False:
        fallback = compute_entropy(data)
        final_diagnostic = int(fallback * 100)
    
    return final_diagnostic

# Execution point of interest
final_diagnostic = process_metrics(health_data, threshold_func)
print(f"Target result: {final_diagnostic}")