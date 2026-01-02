import itertools

# Simulated system performance metrics (some are relevant, others are distractions)
raw_data = [120, 85, 90, 77, 105, 44, 63, 98, 71, 88]

# Irrelevant transformations - red herring computations
decoy_transform_1 = [x ** 0.5 for x in raw_data if x % 2 == 0]
decoy_transform_2 = [x for x in raw_data if x > 80]
decoy_aggregate = sum(decoy_transform_1) * len(decoy_transform_2) // 2 if decoy_transform_2 else 0

# Actual signal extraction: only every third element is valid input
effective_values = raw_data[::3]  # indices 0, 3, 6, 9 -> [120, 77, 63, 88]

# Weight initialization - some weights are decoys
weight_pool = [0.1, 0.15, 0.2, 0.25, 0.3]
weights = weight_pool[1:4]  # actual weights used: [0.15, 0.2, 0.25]

# Misleading normalization path (never actually used)
normalized_raw = [round(x / sum(raw_data), 3) for x in raw_data]
scaling_factor = 1.0
if sum(normalized_raw) > 0.8:
    scaling_factor *= 0.9
    temp_adjust = [x * scaling_factor for x in normalized_raw]

# Another distraction: combinatoric exploration of invalid combinations
invalid_combos = list(itertools.combinations(weight_pool, 2))
penalty_shift = 0
for combo in invalid_combos:
    if combo[0] + combo[1] > 0.4:
        penalty_shift += 1  # This increments but isn't directly used later

# Real processing begins here
baseline_metrics = [x for x in effective_values if x >= 70]  # Filter: [120, 77, 63→excluded, 88] → [120, 77, 88]

# Hidden correction: index alignment shift due to filtering
aligned_metrics = [
    baseline_metrics[0] * 0.9,   # adjusted 120 → 108.0
    baseline_metrics[1],           # 77 unchanged
    (baseline_metrics[2] + baseline_metrics[1]) / 2  # synthetic third metric: (88+77)/2 = 82.5
]

# Auxiliary irrelevant function (never called in critical path)
def calculate_entropy(data):
    from math import log
    total = sum(data)
    probs = [x / total for x in data]
    return -sum(p * log(p) for p in probs if p > 0)

# Critical evaluation function
def evaluate_performance(metrics, w):
    # Metrics: [108.0, 77, 82.5], Weights: [0.15, 0.2, 0.25]
    # Note: weight length matches metric length (3)
    weighted_sum = sum(m * w[i] for i, m in enumerate(metrics))
    
    # Additional logic: apply bonus if any metric exceeds 100
    bonus = 5.0 if any(m > 100 for m in metrics) else 0
    
    # Apply modular adjustment based on sum of digits in total length
    control_key = len(str(len(raw_data)))  # len("10") = 2 → control_key = 1
    modulation = (int(sum(metrics)) % 7) / 10 if control_key == 1 else 0  # 287 % 7 = 2 → 0.2
    
    return weighted_sum + bonus + modulation

# Dead code path - misleading recursive structure
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2)  # unused

cached_result = recursive_distractor(7)  # computed but never used

# Trigger the actual evaluation
final_score = evaluate_performance(aligned_metrics, weights)

# Output result as required
print(f"Target result: {final_score}")