import math

def analyze_redundant_data(data):
    # Irrelevant function - dead code path
    temp = [x ** 2 for x in data if x > 5]
    temp = [t for t in temp if t % 3 == 0]
    return sum(temp) // len(temp) if temp else 0

def compute_ghost_metric(arr):
    # Misleading computation with no real impact
    ghost = 0
    for i in range(len(arr)):
        ghost += arr[i] * (-1) ** i
    ghost *= 1.5
    return ghost

def preprocess_signal(signal):
    # Distractor: signal processing that isn't used later
    filtered = [s for s in signal if abs(s) > 0.5]
    normalized = [s / max(filtered) for s in filtered]
    transformed = [math.sin(x) for x in normalized]
    return [round(t, 3) for t in transformed]

def calculate_entropy(values):
    # Unused advanced calculation
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

def evaluate_performance(metrics, baseline):
    # Core logic begins
    adjusted = []
    for m in metrics:
        if m < baseline:
            adjusted.append(m * 1.2)
        elif m == baseline:
            adjusted.append(m)
        else:
            adjusted.append(m * 0.9)
    
    # Real transformation affecting final result
    growth_factors = [round(adjusted[i] / metrics[i], 2) for i in range(len(metrics))]
    
    # Conditional branching with early exit red herring
    if sum(growth_factors) > 5.0:
        temp_result = sum(adjusted) * 0.8
        if temp_result < 100:
            return int(temp_result)  # Dead end due to condition not met
    
    # Actual path taken
    offset = 0
    for gf in growth_factors:
        if gf > 1.0:
            offset += 1
    
    # Key intermediate (misleading name)
    core_value = sum(adjusted) + offset * 10
    
    # Decoy bitwise manipulation
    decoy_flag = 0b1010 ^ 0b1100
    decoy_flag <<= 2
    decoy_flag |= 0b11
    
    # Final adjustment based on logical condition
    penalty = 0
    if core_value > 200 and len([x for x in metrics if x > baseline]) >= 2:
        penalty = 25
    
    final_score = core_value - penalty
    
    # This print is required for traceability
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data
    raw_data = [8, 12, 10, 7, 15]
    baseline_reference = 10
    
    # Irrelevant preprocessing
    _ = analyze_redundant_data(raw_data)
    _ = compute_ghost_metric(raw_data)
    signal_input = [0.3, 0.7, 0.6, 0.9]
    _ = preprocess_signal(signal_input)
    _ = calculate_entropy(raw_data)
    
    # Critical execution point
    final_score = evaluate_performance(raw_data, baseline_reference)
    
    # Output result as per requirement
    print(f"Target result: {final_score}")