from itertools import combinations

# Simulated system performance metrics over time
def collect_metrics():
    raw_data = [120, 135, 142, 127, 139, 158, 145, 131]
    offsets = [i % 7 for i in range(len(raw_data))]
    processed = [raw_data[i] - offsets[i] + (i % 3) for i in range(len(raw_data))]
    return processed

# Legacy function – unused but looks relevant
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x / mean_val for x in data]

# Distractor: complex transformation with no impact
def generate_noise_patterns(n):
    pattern = []
    for i in range(n):
        temp = (i * 17) % 23
        if temp > 10:
            pattern.append(temp ** 0.5)
    return pattern

# Real computation begins here
metrics = collect_metrics()
baseline = sum(metrics) // len(metrics)

# Irrelevant set operations (distractor)
duplicate_check = set(metrics)
duplicates_found = len(metrics) - len(duplicate_check)
spurious_pairs = list(combinations(duplicate_check, 2))

# More red herrings
shadow_metrics = [x * 0.95 for x in metrics if x > baseline]
avg_shadow = sum(shadow_metrics) / len(shadow_metrics) if shadow_metrics else 0

# Bit manipulation decoy
bit_encoded = 0
for val in metrics[:4]:
    bit_encoded ^= (val << 2) | (val & 3)

# Actual logic buried within distractions
def analyze_trend(data, base):
    above_count = 0
    for val in data:
        if val >= base:
            above_count += 1
    return above_count > len(data) // 2

# Another irrelevant helper
def calculate_entropy(data):
    from math import log
    freq_map = {}
    for x in data:
        freq_map[x] = freq_map.get(x, 0) + 1
    total = len(data)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Core evaluation logic (looks similar to distractors)
def evaluate_performance(data, base):
    # Step 1: Count how many exceed baseline
    strong = [x for x in data if x >= base]
    weak = [x for x in data if x < base]
    
    # Step 2: Apply weighted contribution
    contribution = 0
    for i, val in enumerate(data):
        if val >= base:
            contribution += (val - base) * 1.2
        else:
            contribution -= (base - val) * 0.8
    
    # Step 3: Adjust by trend significance
    trend_weight = 1.5 if analyze_trend(data, base) else 0.7
    
    # Step 4: Final adjustment using combination logic
    combo_factor = len(list(combinations(strong, 2))) if len(strong) >= 2 else 1
    
    result = contribution * trend_weight + combo_factor
    
    # Misleading rounding attempt (not actually used in final path)
    rough_estimate = round(result, 1)
    
    return int(result)  # deterministic integer output

# Execution point of interest
final_score = evaluate_performance(metrics, baseline)

# Print required output
print(f"Target result: {final_score}")