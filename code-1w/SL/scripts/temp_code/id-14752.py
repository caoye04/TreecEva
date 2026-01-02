def analyze_pattern(sequence):
    # Irrelevant analysis function (dead end)
    count = 0
    for i in range(len(sequence)):
        if sequence[i] % 3 == 0:
            count += 1
    return count

# Distractor variables
temp_buffer = [x**2 for x in range(15)]
offset_map = {i: i * 3 + 1 for i in range(10)}
useless_sum = sum(offset_map.values()) // 2

# Real data
raw_input = [18, 24, 30, 42, 50, 60, 75, 90]
scaling_factor = 0.75

# Misleading transformation chain
transformed = []
for index, val in enumerate(raw_input):
    if index % 2 == 0:
        transformed.append(val * scaling_factor)
    else:
        transformed.append(val + 10)

# Decoy filtering (never used later)
filtered_out = [x for x in transformed if x > 50 and x % 10 == 0]

# Real processing begins: zip with offset shifts
displacement = [2, 3, 1, 4, 0, 2, 3, 1]
data = [a - b for a, b in zip(raw_input, displacement)]

# Threshold logic with modular arithmetic and comparisons
base_threshold = 20
thresholds = []
for i in range(8):
    threshold_val = (base_threshold + i * 3) % 25
    if i % 4 == 0:
        threshold_val *= 1.1
    thresholds.append(round(threshold_val, 2))

# Secondary distractor: recursive bit counter (unused)
def count_set_bits(n):
    if n <= 0:
        return 0
    return (n & 1) + count_set_bits(n >> 1)

bit_analysis = [count_set_bits(x) for x in raw_input]

# Core calculation function
def calculate_final_score(values, limits):
    score = 0
    penalty = 0
    
    for idx, (v, lim) in enumerate(zip(values, limits)):
        if v > lim * 2:
            score += v // 3
        elif v > lim:
            score += v // 5
        else:
            penalty += idx
    
    # Critical interference: extra nested logic that looks important but isn't fully used
    adjustment = 0
    for i in range(len(values)):
        if i % 3 == 0 and values[i] % 2 == 1:
            adjustment += 1
    # But only part of it matters:
    if penalty > 10:
        adjustment -= 1

    # Actual key computation
    final_score = score - penalty * 2 + (adjustment * 5)
    
    # Red herring: modifying a variable that's not used
    temp_result = final_score * 1.05
    return int(final_score)

# Execution point of interest
final_score = calculate_final_score(data, thresholds)

# Output result as required
print(f"Target result: {final_score}")