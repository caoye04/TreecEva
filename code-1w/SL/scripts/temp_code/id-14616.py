import itertools

# Simulate multi-stage industrial processing with filtering and yield calculation
def preprocess_input(raw_batches):
    filtered = []
    for batch in raw_batches:
        if len(batch) < 3:
            continue
        temp = [x for x in batch if x > 0]
        if sum(temp) == 0:
            temp = [0.1]  # fallback
        normalized = [x / sum(temp) for x in temp]
        filtered.append(normalized)
    return filtered

# Irrelevant helper - dead code path (distractor)
def legacy_conversion(x):
    return (x * 9/5) + 32  # Fahrenheit conversion, unused

# Decoy function that looks important but isn't used in main logic
def calculate_efficiency_score(data):
    score = 0
    for seq in data:
        for val in seq:
            if val > 0.5:
                score += 1.5
            else:
                score -= 0.1
    return score * 0.77

# Real computation chain
def transform_sequence(seq):
    shifted = seq[1:] + [seq[0]]  # rotation
    paired = list(zip(seq, shifted))
    products = [a * b for a, b in paired]
    return [p * 2 for p in products]  # amplification step

def aggregate_metrics(transformed_list):
    flat = [item for sublist in transformed_list for item in sublist]
    window_sums = [sum(flat[i:i+3]) for i in range(0, len(flat), 3)]
    adjusted = [w * 0.9 for w in window_sums]
    return adjusted

# Core algorithm
def calculate_optimal_yield(metrics):
    base = 0
    for m in metrics:
        if m > 1.0:
            base += m ** 0.5
        else:
            base += m * m
    return int(base * 1000) // 7  # deterministic integer mapping

# Misleading intermediate variables
initial_tuning_factor = 0.88
buffer_capacity = 256
active_channels = [True, False, True, True, False]
dummy_mask = [1 if i % 2 == 0 else 0 for i in range(10)]

# Primary data input (real)
raw_material_batches = [
    [10, 20, 30],
    [5, 15],
    [7, 14, 21, 28],
    [],
    [100]
]

# Processing pipeline starts here
processed_data = preprocess_input(raw_material_batches)

temp_storage = []
for entry in processed_data:
    result = transform_sequence(entry)
    temp_storage.append(result)

consolidated_metrics = aggregate_metrics(temp_storage)

# Red herring: complex-looking but unused combinatorics
cross_combinations = list(itertools.product([1,2], repeat=3))
permutation_count = len(list(itertools.permutations('ABC')))
shuffled_slices = [str(x)[::-1] for x in cross_combinations]  # irrelevant string reversal

# Actual target computation
final_yield = calculate_optimal_yield(consolidated_metrics)

# Output requirement
print(f"Result: {final_yield}")