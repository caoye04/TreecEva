from collections import defaultdict, Counter
import itertools

# Simulated sensor data processing with diagnostic evaluation
def collect_readings():
    raw_samples = [127, 64, 255, 32, 96, 160, 224, 80]
    processed = []
    for val in raw_samples:
        if val > 128:
            processed.append(val >> 2)
        elif val == 128:
            processed.append(32)
        else:
            processed.append(val << 1)
    return processed

# Irrelevant helper: computes unused statistical moment
def compute_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / n
    if variance == 0:
        return 0
    skew = sum((x - mean) ** 3 for x in data) / n
    return skew / (variance ** 1.5) if variance > 0 else 0

# Dead function: never called but looks important
def decrypt_sequence(seq):
    return [seq[i] ^ (i * 7) % 256 for i in range(len(seq))]

# Distractor transformation chain
def apply_filter_chain(data):
    temp_a = [x | 15 for x in data]
    temp_b = [x & 240 for x in temp_a]
    temp_c = [x ^ 170 for x in temp_b]
    # This result is discarded; part of red herring
    return temp_c

# Core transformation logic used in execution
def transform_signal(readings):
    result = []
    freq = Counter(readings)
    for r in readings:
        if freq[r] > 1:
            result.append(r + 10)
        else:
            result.append(r - 5)
    return result

# Real data processing path
def generate_baseline_profile(data):
    profile = defaultdict(int)
    for i, val in enumerate(data):
        profile[i % 4] += val
    return list(profile.values())

# Conditional transformation based on bit patterns
def analyze_bit_groups(values):
    group_counts = [0] * 4
    for v in values:
        if (v >> 5) & 1:
            group_counts[0] += 1
        if (v >> 3) & 3 == 3:
            group_counts[1] += 1
        if bin(v).count('1') % 2 == 0:
            group_counts[2] += 1
        if v & (v - 1) == 0 and v > 0:
            group_counts[3] += 1
    return group_counts

# Main analysis function that contributes to final answer
def evaluate_stability(metrics):
    score = 0
    for m in metrics:
        if m > 50:
            score += m // 10
        elif m > 25:
            score += m // 5
        else:
            score -= 1
    return score * 2

# Critical recursive pattern matcher
def count_pattern_recursive(seq, index=0, acc=0):
    if index >= len(seq):
        return acc
    current = seq[index]
    if current > 100:
        next_acc = acc + (current % 17)
    elif current > 50:
        next_acc = acc + (current % 7) * 2
    else:
        next_acc = acc - 1
    return count_pattern_recursive(seq, index + 1, next_acc)

# Central coordination function
def analyze_pattern(data, thresh):
    # Step 1: Filter by threshold
    filtered = [x for x in data if x > thresh]
    
    # Step 2: Compute frequency-based weights
    weight_map = {k: v * 3 for k, v in Counter(filtered).items()}
    weighted_vals = [weight_map[x] for x in filtered]
    
    # Step 3: Apply conditional offset using set logic
    unique_vals = set(weighted_vals)
    offsets = set()
    for w in unique_vals:
        if w % 4 == 0:
            offsets.add(w // 4)
    adjusted = [w + (len(offsets) if w in offsets else 0) for w in weighted_vals]
    
    # Step 4: Aggregate via itertools grouping
    sorted_adj = sorted(adjusted)
    grouped = [list(group) for k, group in itertools.groupby(sorted_adj, key=lambda x: x // 10)]
    reduced = [sum(g) // len(g) if g else 0 for g in grouped]
    
    # Step 5: Recursive evaluation on reduced set
    recursive_trace = count_pattern_recursive(reduced)
    
    # Step 6: Final adjustment using stability score
    stability = evaluate_stability(reduced)
    final_score = recursive_trace + (stability // 5)
    
    # Irrelevant side computation (distractor)
    phantom_links = [reduced[i] ^ reduced[-i-1] for i in range(len(reduced)) if i != len(reduced)//2]
    linkage_strength = sum(phantom_links) / len(phantom_links) if phantom_links else 0
    
    # Final result (only this matters)
    return final_score

# Unused but plausible-looking diagnostics
def validate_consistency(pattern):
    return all(p % 2 == 0 for p in pattern if p > 30)

# --- Execution Flow ---
if __name__ == "__main__":
    # Collect initial sensor readings
    sensor_data = collect_readings()  # [254, 128, 63, 192, 192, 40, 160, 160]
    
    # Apply actual transformation
    transformed_data = transform_signal(sensor_data)
    
    # Generate baseline (unused, distractor)
    baseline = generate_baseline_profile(transformed_data)
    
    # Analyze bit distribution (computed but not used)
    bit_analysis = analyze_bit_groups(transformed_data)
    
    # Apply filter chain (result discarded - red herring)
    filtered_noise = apply_filter_chain(transformed_data)
    
    # Compute skewness (irrelevant statistic)
    skew = compute_skewness(transformed_data)
    
    # Set threshold based on heuristic
    threshold = (sum(transformed_data) // len(transformed_data)) - 10
    
    # CRITICAL EXECUTION POINT
    final_diagnostic = analyze_pattern(transformed_data, threshold)
    
    # Output target result
    print(f"Result: {final_diagnostic}")