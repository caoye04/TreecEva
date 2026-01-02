import math

def preprocess_data(raw):
    # Irrelevant preprocessing (dead path)
    cleaned = [x for x in raw if x > 0]
    temp_sum = sum(cleaned)
    normalized = [x / temp_sum for x in cleaned]
    return normalized

def analyze_trends(series):
    # Misleading trend analysis with no impact on result
    increasing = 0
    for i in range(1, len(series)):
        if series[i] > series[i-1]:
            increasing += 1
    return increasing > len(series) // 2

def filter_outliers(arr, threshold=2.5):
    # Distractor: computes mean and std but not used in final logic
    mean_val = sum(arr) / len(arr)
    variance = sum((x - mean_val) ** 2 for x in arr) / len(arr)
    std_dev = math.sqrt(variance)
    filtered = [x for x in arr if abs(x - mean_val) / std_dev < threshold]
    return filtered  # Never actually used

def compute_entropy(values):
    # Red herring function - looks important but unused
    total = sum(values)
    probabilities = [(v / total) for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return entropy

def compute_final_score(data, weights):
    # Core logic begins
    base_scores = []
    for idx, (val, w) in enumerate(zip(data, weights)):
        adjusted = val * w
        if idx % 2 == 0:
            adjusted = math.ceil(adjusted)
        else:
            adjusted = math.floor(adjusted)
        base_scores.append(adjusted)
    
    # Intermediate transformation
    transformed = []
    for i, score in enumerate(base_scores):
        if i == 0:
            transformed.append(score)
        else:
            prev = transformed[-1]
            diff = abs(score - prev)
            if diff > 5:
                transformed.append(prev + 3)
            else:
                transformed.append(prev + diff // 2)
    
    # Accumulate using bit manipulation (key step)
    accumulator = 0
    for t in transformed:
        accumulator ^= t  # XOR accumulation
        accumulator = (accumulator << 1) & 0xFFFF  # Left shift with mask
    
    # Final adjustment based on set uniqueness
    unique_flags = set()
    for x in data:
        flag = int(math.log2(x + 1)) if x > 0 else 0
        unique_flags.add(flag)
    
    bonus = len(unique_flags) * 2
    final_score = accumulator + bonus
    
    # Dead code path - misleading return
    if final_score < 0:
        return -1  # Never reached
    
    return final_score

# Main execution
raw_input_data = [12, 8, 15, 3, 22, 6]
weights_list = [1.1, 0.9, 1.3, 0.7, 1.6, 0.5]

# Irrelevant variables (distractors)
data_copy = raw_input_data[:]
duplicate_check = {x: raw_input_data.count(x) for x in raw_input_data}
sorted_pairs = sorted(enumerate(raw_input_data), key=lambda x: x[1])

# Unused transformations
shifted_data = [x << 2 for x in raw_input_data]  # Bit-shifted but unused
scaled_weights = [w * 100 for w in weights_list]

# Call main computation
processed = preprocess_data(raw_input_data)
has_trend = analyze_trends(raw_input_data)
entropy_value = compute_entropy(weights_list)  # Computed but irrelevant
effective_data = filter_outliers(raw_input_data)  # Called but result discarded

# Critical execution point
final_score = compute_final_score(raw_input_data, weights_list)

# Output result
print(f"Result: {final_score}")