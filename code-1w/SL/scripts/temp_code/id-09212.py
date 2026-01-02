from collections import defaultdict, Counter

# Simulated sensor data stream with noise
data_stream = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 2, 3, 5, 7, 11, 13, 17, 19, 23]

# Irrelevant statistical counters (distractors)
mean_approx = sum(data_stream) / len(data_stream)
variance_guess = sum((x - mean_approx) ** 2 for x in data_stream) / len(data_stream)
median_like = sorted(data_stream)[len(data_stream)//2]
mode_guess = max(set(data_stream), key=data_stream.count)

# Noise filter (partially relevant but overcomplicated)
filtered_noise = [x for x in data_stream if x > mean_approx - variance_guess ** 0.5]

# Frequency analysis using defaultdict (core component)
frequency_map = defaultdict(int)
for value in filtered_noise:
    frequency_map[value] += 1

# Secondary transformation map (distractor)
transformed_energy = {}
for k, v in frequency_map.items():
    transformed_energy[k * 2 + 1] = v ** 2 - 1

# Prime detector (misleading path)
def is_decoy_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Unused recursive function (dead code path)
def useless_recursion(x):
    if x <= 1:
        return 1
    return x * useless_recursion(x - 2)

# Threshold logic with conditional expression (key control)
baseline = 3
adjustment_factor = 1.5 if len(frequency_map) > 10 else 0.8
threshold = (sum(frequency_map.values()) / len(frequency_map)) * adjustment_factor

# Auxiliary counter for rare patterns (partially distracting)
rare_patterns = Counter([k for k, v in frequency_map.items() if v < 2])
common_patterns = {k: v for k, v in frequency_map.items() if v >= 2}

# Core analysis function with embedded logic chain
def analyze_pattern(freq_data, thresh):
    total_weight = 0
    penalty = 0
    bonus = 0

    # Logical cascade with interdependencies
    for val, count in freq_data.items():
        if count > thresh:
            if val % 2 == 0:
                total_weight += val * count
            else:
                total_weight += val * 1.5
        elif count == 1:
            if is_decoy_prime(val):
                bonus += val // 3
            else:
                penalty += val % 7
        else:
            total_weight -= count

    # Complex conditional expression (required python feature)
    final_score = ((total_weight + bonus) - penalty) if total_weight > 0 else (bonus * 2) - abs(penalty)
    
    # Additional red herring calculation
    decay_rate = 0.95
    projected_loss = final_score * (decay_rate ** len(freq_data))
    recovery_factor = sum(transformed_energy.values()) / 100 if transformed_energy else 0
    
    # Return only the core diagnostic score (truth path)
    return int(final_score)

# Critical execution point
intermediate_dump = dict(frequency_map)  # checkpoint (irrelevant)
diagnostic_score = analyze_pattern(frequency_map, threshold)

# Final output
print(f"Result: {diagnostic_score}")