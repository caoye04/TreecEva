import math

# Irrelevant helper function (decoy)
def unused_helper(x):
    return sum(i ** 2 for i in x if i % 3 == 0)

# Misleading data transformation chain
def transform_signal(signal):
    filtered = [s * 0.9 for s in signal if s > 10]
    normalized = [f / max(filtered) for f in filtered]
    return [round(n, 3) for n in normalized]

# Unused but plausible-looking processing step
def rolling_average(values, window=3):
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

# Core logic disguised among distractors
def analyze_pattern(seq):
    count_a = 0
    count_b = 0
    temp_result = []
    for i, val in enumerate(seq):
        if i % 2 == 0 and val % 4 == 0:
            count_a += 1
        elif val > 50:
            temp_result.append(val)
            count_b += val // 10
    # Red herring: this modifies state but isn't used in final answer
    temp_result = list(map(lambda x: x - 5, temp_result))
    return count_a * 7 + (count_b % 13)

# Secondary path with misleading intermediate output
def compute_risk_factor(arr):
    base = sum(1 for x in arr if x < 0)
    bonus = len([x for x in arr if x > 100])
    adjustment = math.log(bonus + 1) * 10 if bonus else 0
    return base * 15 - adjustment  # Not used in final result

# Key function buried in complexity
def evaluate_performance(raw_data):
    # Slice operation with meaningful selection
    data_slice = raw_data[5:15]  # Critical use of slicing
    
    # Distractor: unrelated transformation
    shifted = [(x << 2) ^ 5 for x in raw_data if x % 7 == 0]
    masked_sum = sum(shifted[:4]) if len(shifted) >= 4 else 0
    
    # Another decoy computation using string methods on digit strings
    id_str = "ID_" + "".join(str(len(raw_data)))
    checksum = sum(ord(c) for c in id_str if c.isdigit())
    
    # Real computation chain
    factor_x = analyze_pattern(data_slice)
    factor_y = len(set(data_slice)) * 3
    
    # Conditional expression with logical operations
    adjustment = 10 if all(x > 0 for x in data_slice) and any(x > 75 for x in data_slice) else -5
    
    # Final score calculation (answer point)
    final_score = factor_x + factor_y + adjustment
    
    # Dead code branch (never executed due to above condition structure)
    if len(data_slice) > 20 and False:  # Always false
        fallback = sum(data_slice) / len(data_slice)
        final_score = int(fallback)
    
    return final_score

# Main execution block
if __name__ == "__main__":
    # Input data designed to trigger specific logic paths
    sensor_readings = [12, 44, 67, 89, 34, 92, 16, 88, 4, 76, 55, 23, 41, 18, 99, 105, 3, 7, 29]
    
    # Unused derived arrays (distractors)
    high_freq = [x for x in sensor_readings if x in {89, 92, 88, 105}]
    scaled_data = list(map(lambda x: x * 1.1, sensor_readings))
    
    # String method used as noise
    label = "sensor_log_v2.txt"
    extension = label.split('.')[-1].upper()  # Irrelevant
    
    # Actual target computation
    final_score = evaluate_performance(sensor_readings)
    
    # Output required format
    print(f"Result: {final_score}")