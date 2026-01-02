import itertools

def analyze_pattern(seq):
    # Irrelevant function - dead code path
    return sum(a * b for a, b in zip(seq, seq[1:]))

def utility_check(items):
    # Distractor logic - not used in final computation
    total = 0
    for item in items:
        if item > 5:
            total += item // 2
    return total

def transform_data(values):
    # Complex but partially irrelevant transformation
    shifted = [(v << 1) ^ 3 for v in values]
    filtered = [x for x in shifted if x % 7 != 0]
    return filtered[:len(filtered)//2] if filtered else [0]

def validate_entry(record):
    # Unused validation function (decoy)
    return all(isinstance(v, int) and v >= 0 for v in record.values())

def compute_weighted_sum(arr, weights=None):
    # Heavily distractive weighting logic
    if weights is None:
        weights = [i ** 0.5 for i in range(1, len(arr) + 1)]
    weighted = [a * w for a, w in zip(arr, weights)]
    return round(sum(weighted), 4)

def core_evaluation(dataset):
    # Key recursive helper
    def recurse_evaluate(chunk, depth=0):
        if depth >= 3 or len(chunk) == 0:
            return 1 if depth % 2 == 0 else -1
        pivot = chunk[len(chunk)//2]
        left = [x for x in chunk if x < pivot]
        right = [x for x in chunk if x > pivot]
        return pivot + recurse_evaluate(left, depth+1) - recurse_evaluate(right, depth+1)
    
    base = 0
    for group in dataset:
        base += recurse_evaluate(group)
    return base

def process_results(data, config):
    # Main function with critical logic embedded
    temp_cache = {}
    result_chain = []
    
    for idx, segment in enumerate(data):
        # Real computation begins here
        a = sum(segment) // len(segment)
        b = len([x for x in segment if x % 2 == 0])
        c = a * b + (idx ** 2)
        
        # Store in cache (some entries never used)
        temp_cache[f'interim_{idx}'] = c * 17
        
        # Only every second index contributes to actual result
        if idx % 2 == 0:
            result_chain.append(c)
    
    # Actual answer depends only on this part
    raw_value = sum(result_chain)
    
    # Distractor: complex dictionary operations
    stats = {
        'count': len(temp_cache),
        'max_interim': max(temp_cache.values()) if temp_cache else 0,
        'flags': [k for k in temp_cache if '3' in k],
        'meta': { 'level': config.get('level', 1), 'mode': config['mode'] }
    }
    
    # Irrelevant itertools usage (red herring)
    permutations = list(itertools.permutations([1, 2, 3], 2))
    bonus = 0
    for p in permutations:
        if p[0] < p[1]:
            bonus += p[1] - p[0]
    
    # Final score uses only raw_value, everything else is distraction
    final_score = raw_value + stats['meta']['level'] * 10
    
    # This print must be included as per format requirement
    print(f"Result: {final_score}")
    return final_score

# Ground truth execution context
if __name__ == "__main__":
    data = [
        [4, 8, 12],      # avg=8, even_count=3 -> 8*3 + 0 = 24
        [5, 7, 9],       # skipped (odd index)
        [2, 6, 10, 14],  # avg=8, even_count=4 -> 8*4 + 4 = 36
        [1, 3, 5]        # skipped (odd index)
    ]
    config = {
        'level': 4,
        'mode': 'advanced',
        'debug': True,
        'timeout': 30
    }
    
    # Critical execution point
    final_score = process_results(data, config)