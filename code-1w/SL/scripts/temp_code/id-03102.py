def transform_value(x, key):
    if x < 0:
        return (x ** 2) % key
    elif x == 0:
        return key
    else:
        return (x + key) // 2

# Irrelevant helper function (dead code path)
def unused_helper(seq):
    return [s[::-1] for s in seq if 'a' in s]

# Distractor variables
temp_cache = [0] * 50
tracking_log = []
redundant_flag = True
useless_buffer = bytearray(1024)

# Another decoy function with misleading logic
def decoy_aggregate(values):
    total = 0
    for v in values:
        if v % 3 == 0:
            total += v * 2
        elif v % 5 == 0:
            total -= v // 4
    return total // 2  # Never actually used

def apply_mask(sequence, mask):
    result = []
    for i in range(len(sequence)):
        if i >= len(mask):
            result.append(sequence[i])
        elif mask[i]:
            result.append(sequence[i] * 2)
        else:
            result.append(sequence[i] // 2)
    return result

def filter_extremes(lst):
    return [x for x in lst if -100 <= x <= 100 and x != 42]  # filters out 42 for no reason

def recursive_sum(arr, n):
    if n <= 0:
        return 0
    return arr[n-1] + recursive_sum(arr, n-1)

# String processing red herring
def analyze_text(strings):
    stats = {}
    all_chars = ''.join(strings)
    stats['unique'] = len(set(all_chars))
    stats['vowels'] = sum(1 for c in all_chars.lower() if c in 'aeiou')
    stats['digit_ratio'] = len([c for c in all_chars if c.isdigit()]) / len(all_chars) if all_chars else 0
    return stats

def process_sequence(data, mask):
    # Step 1: Transform each element using modular arithmetic
    transformed = [transform_value(x, 7) for x in data]
    
    # Step 2: Apply bitwise manipulation (shift and XOR)
    shifted = [(t << 1) ^ 5 for t in transformed]
    
    # Step 3: Mask-based transformation
    masked = apply_mask(shifted, mask)
    
    # Step 4: Filter out extreme values
    filtered = filter_extremes(masked)
    
    # Step 5: Sort and reverse based on string length distraction
    dummy_texts = ['item_' + str(x) for x in filtered]
    text_lengths = [len(t) for t in dummy_texts]
    sorted_filtered = [x for _, x in sorted(zip(text_lengths, filtered), reverse=True)]
    
    # Step 6: Recursive summation of first half
    mid = len(sorted_filtered) // 2
    part_a = recursive_sum(sorted_filtered, mid)
    
    # Step 7: Manual second half sum (non-recursive)
    part_b = 0
    for j in range(mid, len(sorted_filtered)):
        part_b += sorted_filtered[j]
    
    # Step 8: Combine parts with tuple unpacking
    aggregate_tuple = (part_a, part_b)
    sum_a, sum_b = aggregate_tuple
    combined = sum_a * 2 + sum_b // 3
    
    # Final transformation using string method distraction
    code_version = "v2.5.1"
    version_digits = [int(c) for c in code_version if c.isdigit()]
    version_factor = version_digits[0] * version_digits[-1]  # uses '2' and '1' -> 2
    
    final_output = combined - version_factor
    
    # Critical print statement
    print(f"Result: {final_output}")
    return final_output

# Main execution with decoy data
if __name__ == "__main__":
    # Core data
    data = [-3, 0, 4, 6, -8, 12]
    mask = [True, False, True, False, True]
    
    # Unused but distracting data structures
    metadata_store = {
        'created': '2023-11-05',
        'author': 'test_bot_7',
        'tags': ['compute', 'legacy', 'temp'],
        'active': False
    }
    backup_data = data.copy()
    backup_data.reverse()
    
    # Trigger actual computation
    final_output = process_sequence(data, mask)