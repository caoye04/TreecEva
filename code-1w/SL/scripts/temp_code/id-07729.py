from collections import defaultdict, Counter
import math

def analyze_pattern(sequence):
    # Irrelevant function - dead code path
    freq = Counter(sequence)
    return sum(v ** 2 for v in freq.values())

def validate_input(data):
    # Misleading validation with decoy logic
    if not data:
        return False
    if len(set(data)) == 1:
        return False
    return all(isinstance(x, int) and x >= 0 for x in data)

def transform_entry(val, shift=3):
    # Bit manipulation red herring
    shifted = (val << 1) ^ 5
    normalized = abs(shifted) % 100
    return normalized if normalized > 10 else normalized + 10

def compute_weighted_average(items):
    # Unused complex averaging logic
    total, weight_sum = 0, 0
    for i, v in enumerate(items):
        weight = math.exp(-0.1 * i)
        total += v * weight
        weight_sum += weight
    return total / weight_sum if weight_sum else 0

def filter_outliers(values, cutoff=25):
    # Distractor: modifies copy, not used later
    avg = sum(values) / len(values)
    return [v for v in values if abs(v - avg) <= cutoff]

def evaluate_threshold_crossings(seq, limits):
    # Complex but irrelevant crossing detector
    crossings = 0
    for i in range(1, len(seq)):
        for limit in sorted(limits):
            if seq[i-1] < limit <= seq[i]:
                crossings += 1
    return crossings

def accumulate_metrics(records):
    # Dead-end aggregation with string processing distraction
    stats = defaultdict(int)
    labels = []
    for r in records:
        category = f"group_{r % 3}"
        stats[category] += 1
        labels.append(category.replace('_', '-'))
    label_str = ''.join(labels)
    vowel_count = sum(1 for c in label_str if c in 'aeiou')
    return dict(stats), vowel_count

def process_results(data, config):
    # CORE FUNCTION - actual answer computation hidden here
    
    # Step 1: Clean and prepare
    cleaned = [x for x in data if x is not None]
    
    # Step 2: Apply non-linear transformation (key step)
    transformed = []
    for val in cleaned:
        temp = val
        if val % 2 == 0:
            temp = int(math.sqrt(val)) if val > 0 else 0
        else:
            temp = int(math.log(val + 1, 2))
        transformed.append(temp)
    
    # Step 3: Count frequency (collections.Counter used as required)
    freq = Counter(transformed)
    
    # Step 4: Extract most common value
    mode_val = freq.most_common(1)[0][1]  # frequency of most common
    
    # Step 5: Compute secondary metric from distractor logic
    magnitude = sum(1 for x in transformed if x > 2)
    
    # Step 6: Use string method to create conditional flag (required feature)
    control_flag = "priority_high" if str(mode_val).count('1') > 0 else "normal"
    
    # Step 7: Conditional adjustment based on flag
    adjustment = 0
    if control_flag.startswith("priority"):
        adjustment = 5
    
    # Step 8: Final score calculation (answer)
    base_score = mode_val * magnitude
    final_score = base_score + adjustment
    
    # Irrelevant side computations (red herrings)
    _ = evaluate_threshold_crossings(transformed, config)
    _ = accumulate_metrics(cleaned)
    _ = compute_weighted_average(transformed)
    
    return final_score

# Main execution block
if __name__ == '__main__':
    # Input data
    raw_data = [16, 8, 16, 3, 8, 16, None, 7, 3, 8, 16, 31, 15]
    thresholds = [5, 10, 15, 20]
    
    # Dead assignments - misleading intermediate values
    preliminary = sum(x for x in raw_data if x) // 4
    snapshot = [transform_entry(x) for x in raw_data if x]
    baseline = filter_outliers(snapshot)
    
    # Key statement
    final_score = process_results(raw_data, thresholds)
    
    # Output result
    print(f"Result: {final_score}")