from collections import defaultdict, Counter

# Irrelevant data structures and computations (distractors)
useless_stats = [i ** 2 for i in range(15) if i % 3 != 0]
dummy_map = {'alpha': 0, 'beta': [], 'gamma': set()}
phantom_counter = Counter(['x', 'y', 'z'] * 7)

# Decoy function that looks important but is never called
def calculate_robustness(data):
    return sum((x ^ 3) & 7 for x in data) // len(data)

# Unused transformation pipeline
transform_chain = [
    lambda x: x + 2,
    lambda x: x * x,
    lambda x: x >> 1
]

# Real logic begins: system performance evaluation under noise conditions
noise_levels = [0.1, 0.3, 0.05, 0.2]
signal_data = [42, 38, 45, 40, 36]

# Simulate adaptive filtering process
def apply_adaptive_filter(signals, noise_profile):
    filtered = []
    for s in signals:
        temp = s
        for n in noise_profile:
            temp -= int(s * n)
        filtered.append(temp)
    return filtered

# Apply filter to get cleaned signal
cleaned_signal = apply_adaptive_filter(signal_data, noise_levels)

# Misleading accumulation path (dead code)
temp_accumulator = 0
for val in useless_stats[:10]:
    temp_accumulator += val % 4

# Core metric computation
baseline = sum(cleaned_signal) / len(cleaned_signal)
variance = sum((x - baseline) ** 2 for x in cleaned_signal) / len(cleaned_signal)
efficiency_ratio = (baseline / (variance + 1))

# Bit manipulation mask based on signal characteristics
bit_flags = 0
for idx, val in enumerate(cleaned_signal):
    if val > baseline:
        bit_flags |= (1 << idx)

# Spurious intermediate calculation (red herring)
checksum = sum(phantom_counter.values()) * 2 - len(dummy_map)

# Real evaluation metrics
def build_performance_metrics(cleaned, efficiency, flags):
    metrics = defaultdict(float)
    metrics['avg'] = sum(cleaned) / len(cleaned)
    metrics['stability'] = 1 / (variance + 0.1)
    metrics['complexity'] = bin(flags).count('1')
    metrics['efficiency'] = efficiency
    
    # Fake complexity additions
    debug_info = {'stage': 'final', 'valid': True}
    temp_result = [x for x in cleaned if x > 35]
    metrics['debug'] = len(temp_result)  # unused later
    
    return metrics

# Construct metrics
evaluation_data = list(range(8))
synthetic_weights = [i * 0.5 for i in evaluation_data]

metrics = build_performance_metrics(cleaned_signal, efficiency_ratio, bit_flags)

# Secondary decoy analysis (never used)
analysis_grid = [[i + j for j in range(4)] for i in range(4)]
grid_sum = sum(sum(row) for row in analysis_grid)

# Benchmark reference with irrelevant combinatorics
def generate_combinations(n, r):
    if r == 0 or n == r:
        return 1
    return generate_combinations(n-1, r-1) + generate_combinations(n-1, r)

reference_benchmark = {
    'base': 40,
    'tolerance': 3.5,
    'weight_factor': 0.8,
    'combo_ref': generate_combinations(8, 3)  # 56, computed but mostly irrelevant
}

# Real scoring logic buried in distractions
def evaluate_performance(met, bench):
    score = 0
    score += met['avg'] * 0.3
    score += met['stability'] * 15
    score += met['complexity'] * 4
    score += met['efficiency'] * 2
    
    # Conditional adjustment based on hidden rule
    if met['avg'] >= bench['base'] - bench['tolerance']:
        score *= bench['weight_factor']
    else:
        score *= 1.1
    
    # Red herring: unused bitwise adjustment
    dummy_mask = 0b101010
    alternate = (int(score) ^ dummy_mask) & 0xFF
    
    return score

# Final execution point
final_score = evaluate_performance(metrics, reference_benchmark)

# Output result as required
print(f"Target result: {final_score}")