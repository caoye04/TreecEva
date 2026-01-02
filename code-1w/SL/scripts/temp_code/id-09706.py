import math

def analyze_pattern(seq):
    # Irrelevant function: analyzes sequence but not used in final calculation
    return sum(1 for a, b in zip(seq, seq[1:]) if a < b)

def dummy_transform(x):
    # Dead code path: never called
    return [i ** 2 for i in x if i % 2 == 0]

def evaluate_threshold(values, limit=50):
    # Distractor logic: computes something unrelated
    count = 0
    for v in values:
        if v > limit:
            count += 1
    return count > len(values) // 2

def compute_entropy(arr):
    # Misleading intermediate: looks important but unused
    total = sum(arr)
    probs = [(x / total) for x in arr if x > 0]
    return -sum(p * math.log2(p) for p in probs)

def filter_outliers(data, factor=1.5):
    # Unused but plausible preprocessing
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    low, high = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in data if low <= x <= high]

def normalize_vector(vec):
    norm = math.sqrt(sum(x**2 for x in vec))
    return [x / norm for x in vec] if norm else vec

def recursive_reduce(lst):
    # Key helper: actually used
    if len(lst) <= 1:
        return lst[0] if lst else 0
    mid = len(lst) // 2
    left = recursive_reduce(lst[:mid])
    right = recursive_reduce(lst[mid:])
    return (left * right) + 1

def process_metrics(data, weights):
    # Core logic with distractions embedded
    adjusted = [d * w for d, w in zip(data, weights)]
    
    # Red herring: create complex-looking but unused transformations
    temp_result = [math.sin(x) + math.cos(x) for x in adjusted]
    derived_mask = [1 if abs(x) > 0.5 else 0 for x in temp_result]
    masked_sum = sum(a * m for a, m in zip(adjusted, derived_mask))
    
    # Actual relevant computation begins here
    magnitude = math.sqrt(sum(x**2 for x in adjusted))
    unit_vec = [x / magnitude for x in adjusted]
    
    # Conditional expression used as required
    scale_factor = 10 if len(unit_vec) > 3 else 5
    
    # Bit manipulation red herring
    magic_key = 0
    for i, val in enumerate(unit_vec):
        shifted = int(abs(val * 100)) << 1
        magic_key ^= shifted
    
    # Real signal: recursive reduction on transformed data
    base_values = [int(abs(x * 100)) for x in unit_vec]
    reduced = recursive_reduce(base_values)
    
    # Final score depends only on this chain
    final_score = (reduced * scale_factor) - (magic_key % 100)  # minor influence to mislead
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == "__main__":
    # Input data with meaningful names
    sensor_readings = [12.4, 8.7, 15.2, 6.1, 9.3]
    calibration_weights = [0.85, 1.05, 0.92, 1.18, 0.79]
    
    # Irrelevant preprocessing
    filtered_data = filter_outliers(sensor_readings, 7.0)
    normalized_data = normalize_vector(sensor_readings)
    entropy = compute_entropy([int(x) for x in sensor_readings])
    
    # Key assignment
    final_score = process_metrics(sensor_readings, calibration_weights)
    
    # Additional distraction
    pattern_strength = analyze_pattern([int(x*10) % 10 for x in normalized_data])