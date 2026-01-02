import itertools

def analyze_pattern(seq):
    # Irrelevant function analyzing patterns (dead end)
    counts = {}
    for k, g in itertools.groupby(seq):
        counts[k] = len(list(g))
    return {k: v for k, v in counts.items() if v > 2}

def validate_checksum(buffer):
    # Distractor: computes a checksum but not used in final result
    chk = 0
    for b in buffer:
        chk ^= b * 3
    return chk % 256

def transform_data(raw):
    # Mix of relevant and irrelevant transformations
    temp = [x * 2 + 1 for x in raw if x % 2 == 0]
    shifted = [(x >> 1) for x in temp]
    filtered = [x for x in shifted if x > 10]
    return filtered

def compute_entropy(values):
    # Red herring: looks important but unused
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values]
    from math import log2
    return -sum(p * log2(p) for p in probs if p > 0)

def build_lookup(keys):
    # Unused complex structure creation
    lookup = {k: str(k)[::-1] for k in keys}
    return {int(v): k for k, v in lookup.items()}

def process_metrics(data, cfg):
    # Core logic embedded with distractions
    base = [x for x in data if x in cfg['valid_ids']]
    
    # Meaningful transformation
    mapped = [((x * 3) // 2) for x in base]
    
    # Distractor variables
    temp_result = sum(x ** 2 for x in mapped) / len(mapped) if mapped else 0
    dummy_cache = {i: mapped[i] ** 0.5 for i in range(len(mapped)) if i % 2 == 0}
    
    # Key filtering based on string condition (uses string method)
    flag_str = cfg['mode_flag']
    enable_adjustment = 'boost' in flag_str.lower() and flag_str.endswith('ed')
    
    # Conditional path with early exit red herring
    if len(mapped) < 5:
        fallback = sum(mapped) * 2
        return fallback  # dead code in this case
    
    # Real computation branch
    adjusted = []
    for val in mapped:
        if val % 4 == 0:
            adjusted.append(val + 5)
        elif val % 3 == 0:
            adjusted.append(val - 2)
        else:
            adjusted.append(val)
    
    # Aggregation using dictionary operation
    freq = {}
    for a in adjusted:
        freq[a] = freq.get(a, 0) + 1
    
    # Final calculation
    unique_count = len(freq)
    avg_value = sum(adjusted) / len(adjusted)
    
    # The actual answer depends on both
    final_score = int(avg_value * unique_count)
    
    # Print required output
    print(f"Result: {final_score}")
    return final_score

# Main execution
if __name__ == '__main__':
    # Input setup
    data = list(range(15, 30))  # 15 to 29
    config = {
        'valid_ids': list(range(18, 30)),
        'mode_flag': 'performance_boosted',
        'threshold': 4.7
    }
    
    # Irrelevant preprocessing
    raw_buffer = [d % 255 for d in data]
    _ = validate_checksum(raw_buffer)
    _ = analyze_pattern([1, 1, 0, 0, 0, 1, 1, 1, 1])
    
    # Transform data through distractor pipeline
    transformed = transform_data(data)
    _ = compute_entropy(transformed)
    _ = build_lookup(config['valid_ids'])
    
    # Critical statement
    final_score = process_metrics(data, config)