import itertools

def analyze_pattern(sequence):
    count = 0
    trend_values = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend_values.append(1)
        elif sequence[i] < sequence[i-1]:
            trend_values.append(-1)
        else:
            trend_values.append(0)
    
    # Distractor: Calculate fluctuation index (not used later)
    fluctuation_index = sum(1 for x, y in zip(trend_values, trend_values[1:]) if x != y)

    direction_streaks = []
    current_streak = 0
    for val in trend_values:
        if val != 0:
            if current_streak == 0 or (current_streak > 0 and val == 1) or (current_streak < 0 and val == -1):
                current_streak += val
            else:
                direction_streaks.append(current_streak)
                current_streak = val
    if current_streak != 0:
        direction_streaks.append(current_streak)
    
    net_momentum = sum(direction_streaks)
    return net_momentum


def transform_input(raw_list):
    # Apply filtering and scaling
    filtered = [x for x in raw_list if x % 2 == 1]  # Keep only odd numbers
    scaled = [x * 3 + 2 for x in filtered]
    
    # Irrelevant transformation chain
    temp_analysis = [abs(x - 10) for x in scaled]
    avg_deviation = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    normalized = [x - avg_deviation for x in scaled]  # Not actually used
    
    # Return meaningful transformed data
    return [int(x) for x in scaled]


def calculate_final_score(data_chunk):
    base_total = 0
    adjustment_factor = 0
    
    # Multiple assignment and unpacking - relevant
    n = len(data_chunk)
    mid_idx = n // 2
    left_half, right_half = data_chunk[:mid_idx], data_chunk[mid_idx:]
    
    # Bitwise interference - semi-relevant
    xor_probe = 0
    for val in data_chunk:
        xor_probe ^= (val & 7)  # Mask to lower 3 bits
    
    # Real logic: sum with conditional weights
    weighted_sum = 0
    for i, val in enumerate(data_chunk):
        if i % 3 == 0:
            weighted_sum += val * 2
        elif i % 5 == 0:
            weighted_sum += val
        else:
            weighted_sum -= val // 4
    
    # Additional distraction: entropy-like calculation (unused)
    from collections import Counter
    freqs = Counter(data_chunk)
    import math
    dummy_entropy = -sum((freq / n) * math.log2(freq / n) for freq in freqs.values()) if n > 0 else 0
    
    # Key dependency on analyze_pattern
    momentum = analyze_pattern(data_chunk)
    base_total = weighted_sum + momentum * 10
    
    # Final adjustment via external logic
    if len(data_chunk) > 5:
        adjustment_factor = len(left_half) ^ len(right_half)  # XOR of sizes
    else:
        adjustment_factor = n
    
    final_score = base_total + adjustment_factor * 2
    return final_score

# Main execution
raw_input_data = [4, 7, 6, 9, 8, 11, 10, 13, 12]
processed_data = transform_input(raw_input_data)
# Critical statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")