import math

# Simulated system metrics and benchmark thresholds
def generate_metrics():
    raw_data = [127, 255, 64, 192, 31]
    processed = []
    for val in raw_data:
        if val & 1:
            processed.append(val ^ 10)
        else:
            processed.append(val >> 2)
    return set(processed)

# Irrelevant transformation - red herring
def transform_sequence(seq):
    shifted = [s << 1 for s in seq]
    normalized = [sh % 100 for sh in shifted]
    return [abs(n - 50) for n in normalized]

# Decoy function that looks important but isn't used
def compute_legacy_score(data):
    total = 0
    for d in data:
        if d > 40:
            total += int(math.sqrt(d))
        else:
            total -= d // 8
    return total * 3

# Auxiliary filtering - partially relevant
def filter_outliers(values, threshold=35):
    clean = {v for v in values if v > threshold}
    return clean if len(clean) > 3 else values

# Secondary metric calculation - distractor with side computation
def derive_auxiliary_index(items):
    index_val = 0
    for i, item in enumerate(items):
        if i % 3 == 0:
            index_val += item % 17
        elif item % 2 == 0:
            index_val -= (item & 15)
    return index_val + 1000  # misleading large number

# Core evaluation logic
def evaluate_performance(metrics, reference):
    base = sum(metrics)
    adjustment = 0
    
    # Conditional branching with nested logic
    if len(metrics) >= 4:
        diff_set = metrics - reference
        if diff_set:
            adjustment += max(diff_set) // 2
        else:
            adjustment -= min(metrics)
            
        temp = set()
        for m in metrics:
            temp.add(m * 2 if m < 80 else m - 10)
            
        if len(temp) > 4:
            adjustment += len(temp.intersection(metrics))

        # Key computational step
        for ref in reference:
            if ref in metrics and ref % 4 == 0:
                adjustment *= 2
                break
    
    score = base + adjustment
    
    # Multiple assignments - obfuscation
    score_copy = score
    score_backup = score_copy
    final_normalized = int(math.floor(score_copy / 1.05))
    
    return final_normalized

# Unused utility - dead code path
def validate_checksum(data_list):
    checksum = 0
    for idx, num in enumerate(data_list):
        checksum ^= (num + idx) * 3
    return format(checksum, 'b').count('1')

# Main execution flow
if __name__ == '__main__':
    # Generate primary metric set
    metric_set = generate_metrics()
    
    # Transform but don't use - red herring
    dummy_sequence = transform_sequence(list(metric_set))
    
    # Create reference benchmark data
    benchmark_data = filter_outliers({x + 5 for x in metric_set}, threshold=40)
    
    # Compute auxiliary index (not used in final score)
    aux_index = derive_auxiliary_index(list(benchmark_data))
    
    # Evaluate performance using correct logic
    final_score = evaluate_performance(metric_set, benchmark_data)
    
    # Print result as required
    print(f"Target result: {final_score}")