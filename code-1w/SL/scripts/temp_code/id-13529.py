import itertools

def analyze_contributions(values):
    # Irrelevant function: computes nothing used in final result
    weighted = [v * (i + 1) for i, v in enumerate(values)]
    return sum(weighted) % 100

def compute_entropy(data):
    # Distractor: simulates information-theoretic calc, unused
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [d / total for d in data]
    entropy = 0.0
    for p in probs:
        if p > 0:
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 4)

def filter_outliers(seq, threshold=30):
    # Dead path: called but result ignored
    return [x for x in seq if x > threshold]

def transform_ratings(ratings):
    # Complex-looking transformation with red herring logic
    adjusted = []
    for r in ratings:
        if r < 10:
            adjusted.append(r ** 2)
        elif r % 2 == 0:
            adjusted.append(r // 2)
        else:
            adjusted.append(r + 5)
    # Actual relevant line buried in distraction
    temp_result = sum(adjusted[:3]) - sum(adjusted[3:])
    return temp_result  # Only this matters, rest is noise

def evaluate_performance(metrics, base):
    # Core logic hidden among multiple distractions
    
    # Irrelevant set operations
    unique_metrics = set(metrics)
    base_set = set(base)
    overlap = unique_metrics & base_set
    diff = unique_metrics - base_set
    
    # Misleading intermediate computations
    fake_aggregate = sum([m * 2 for m in metrics if m in overlap])
    dummy_flag = len(diff) > 2
    
    # Real computation starts here — depends on prior transform_ratings
    shifted = [abs(m - base[i % len(base)]) for i, m in enumerate(metrics)]
    
    # List comprehension that looks important but only some values matter
    derived = [x + 10 for x in shifted if x < 15]
    
    # Key step: use itertools to create permutations (only length used)
    perms = list(itertools.permutations(shifted[:2]))
    perm_count = len(perms)  # Used later
    
    # Another decoy: recursive counting (unused)
    def count_paths(n):
        if n <= 1:
            return 1
        return count_paths(n-1) + count_paths(n-2)
    
    _ = count_paths(5)  # Result discarded
    
    # Actual key logic
    primary_impact = transform_ratings(shifted)
    secondary_factor = perm_count * 2
    
    # Final deterministic computation
    final_score = primary_impact + secondary_factor
    
    # Print required at end
    print(f"Result: {final_score}")
    return final_score

# Main execution flow
if __name__ == "__main__":
    # Initialize with realistic domain values (e.g., system performance metrics)
    metrics = [8, 12, 7, 16, 9, 11]
    baseline = [6, 14, 10, 18]

    # Unused variables and distracting data structures
    historical_logs = {
        'week1': [7, 13, 9],
        'week2': [8, 11, 8],
        'week3': [9, 10, 7]
    }
    
    summary_stats = {
        'avg': 10.5,
        'peak': 18,
        'floor': 6
    }
    
    # Call irrelevant functions to increase interference
    _ = analyze_contributions([3, 5, 7, 2])
    _ = compute_entropy([4, 4, 2, 2])
    _ = filter_outliers(metrics, threshold=20)
    
    # Key assignment statement
    final_score = evaluate_performance(metrics, baseline)
