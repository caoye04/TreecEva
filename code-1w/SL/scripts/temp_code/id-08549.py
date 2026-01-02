def analyze_trend(data, threshold):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return sum(trend) > threshold

# Irrelevant helper function (decoy)
def normalize_vector(v):
    magnitude = sum(x**2 for x in v) ** 0.5
    return [x / magnitude for x in v] if magnitude else v

# Unused transformation (dead code path)
def shift_cipher(text, key=3):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - base + key) % 26 + base)
        else:
            result += char
    return result

# Misleading intermediate calculation (red herring)
initial_weights = [0.1, 0.2, 0.3, 0.4]
adjusted_weights = [w * 1.5 for w in initial_weights]
scaled_weights = [w / sum(adjusted_weights) for w in adjusted_weights]

# Real computation begins
baseline = [78, 85, 88, 90, 87]
metrics = [82, 89, 91, 94, 88]

# Distractor: Bit manipulation with no impact
flag = 0b1010
mask = 0b1100
flag ^= mask
flag <<= 2

# Linear search embedded in conditional logic
def find_deviation_index(values, ref):
    for idx in range(len(values)):
        if abs(values[idx] - ref[idx]) > 3:
            return idx
    return -1

# Another irrelevant list operation
aux_data = [x for x in range(10, 40, 3)]
filtered_aux = aux_data[::2]  # Slicing - required feature
processed_aux = [y * 2 for y in filtered_aux if y % 4 != 0]

# Core logic hidden among noise
def evaluate_performance(observed, expected):
    differences = [a - b for a, b in zip(observed, expected)]
    positive_drift = len([d for d in differences if d > 0])
    negative_drift = len([d for d in differences if d < 0])
    net_drift = positive_drift - negative_drift
    
    # Conditional branching with slicing distraction
    if net_drift >= 2:
        subset = differences[1:4]
        boost = sum(subset) * 0.5
    else:
        boost = 0
    
    base_score = sum(differences) * 0.8
    adjustment = 5 if analyze_trend(observed, 2) else -3
    
    # Final meaningful computation
    final_score = int(base_score + boost + adjustment)
    
    # Dead assignment (distractor)
    temp_result = final_score * 1.05
    
    return final_score

# Trigger execution
dummy_call = shift_cipher("hello", 5)
unused_trend = analyze_trend(baseline, 1)

final_score = evaluate_performance(metrics, baseline)
print(f"Target result: {final_score}")