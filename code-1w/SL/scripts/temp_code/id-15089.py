import itertools

def analyze_pattern(seq):
    # Irrelevant helper function (dead code path)
    return sum(1 for x in seq if x % 3 == 0)

def compute_checksum(arr):
    # Distractor function: looks important but unused in critical path
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= (val + i) * 3
    return checksum

def transform_entry(val):
    # Real transformation used in logic chain
    if val <= 0:
        return abs(val) * 2
    elif val % 2 == 0:
        return val // 2
    else:
        return val * 3 + 1

def filter_relevant_items(stream):
    # Uses list comprehension and string-related distraction
    labels = ['item_' + str(i) for i in range(len(stream))]  # Red herring: unused strings
    labeled_map = dict(zip(labels, stream))
    filtered = [v for k, v in labeled_map.items() if 'even' not in k]  # Always true, no 'even'
    return filtered

def build_lookup(keys, values):
    # Creates a decoy mapping with irrelevant data
    lookup = {k: v for k, v in zip(keys, values)}
    extra = {f'key_{i}': i*10 for i in range(5)}  # Unused extra entries
    lookup.update(extra)
    return lookup  # Never actually used later

def process_sequence(raw_data):
    temp_result = []
    
    # Step 1: Transform each element using Collatz-like logic
    for item in raw_data:
        transformed = transform_entry(item)
        temp_result.append(transformed)
    
    # Step 2: Apply moving average of window size 3 (with padding)
    padded = [0] + temp_result + [0]
    averaged = []
    for i in range(1, len(padded) - 1):
        avg_val = (padded[i-1] + padded[i] + padded[i+1]) / 3.0
        averaged.append(round(avg_val, 6))
    
    # Step 3: Flatten potential nested structure (unnecessary here, distractor)
    flattened = list(itertools.chain.from_iterable([(x,) for x in averaged]))
    
    # Step 4: Filter out values above threshold — this affects final result
    threshold_filtered = [x for x in flattened if x < 50]
    
    # Step 5: Accumulate using cross-dependency
    accumulator = 0
    history = []
    for val in threshold_filtered:
        if len(history) >= 2 and history[-1] > history[-2]:
            accumulator += val * 0.5
        else:
            accumulator += val * 1.1
        history.append(val)
    
    # Step 6: Final adjustment based on length parity
    if len(threshold_filtered) % 2 == 1:
        final_scale = 1.5
    else:
        final_scale = 1.2
    
    intermediate = int(accumulator * final_scale)
    
    # Misleading checksum calculation (never impacts output)
    fake_integrity = compute_checksum([int(x) for x in flattened if x.is_integer()])
    
    # Critical assignment
    final_output = intermediate - 75  # Key result
    
    return final_output

# Main execution block
if __name__ == '__main__':
    # Input data
    data = [-6, 12, 7, -3, 9, 1]
    
    # Dead assignments (distractors)
    stats_summary = analyze_pattern(data)
    key_set = ['a', 'b', 'c']
    value_set = [100, 200, 300]
    unused_lookup = build_lookup(key_set, value_set)
    metadata_tags = [tag.upper() for tag in key_set]  # Unused string manipulation
    
    # Relevant computation
    final_output = process_sequence(data)
    
    # Output result as required
    print(f"Target result: {final_output}")