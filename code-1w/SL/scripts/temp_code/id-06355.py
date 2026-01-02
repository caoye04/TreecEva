from collections import defaultdict, Counter

def analyze_pattern(sequence):
    count = defaultdict(int)
    for item in sequence:
        count[item] += 1
    return dict(count)

def compute_entropy(values):
    total = sum(values)
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * __import__('math').log2(p)
    return round(entropy, 6)

def validate_checksum(data):
    # Irrelevant validation with decoy logic
    checksum = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            checksum += val * 2
        elif i % 5 == 0:
            checksum -= val
    return checksum % 100

def process_segment(segment):
    # Dead code path - never actually used in final calculation
    temp_result = 0
    for s in segment:
        if len(s) > 3:
            temp_result += len(s) * 2
    return temp_result

def build_lookup(keys):
    # Distractor: builds unused lookup table
    lookup = {}
    for k in keys:
        lookup[k] = hash(k) % 100
    return lookup

def transform_data(arr):
    # Real transformation: XOR with index and filter odd positions
    transformed = []
    for idx, val in enumerate(arr):
        if idx % 2 == 0:
            transformed.append(val ^ idx)  # Bitwise manipulation
    return transformed

def recursive_reduce(nums, depth=0):
    # Core relevant recursion
    if depth >= 3 or len(nums) == 1:
        return nums[0] if nums else 0
    new_nums = []    
    for i in range(len(nums) - 1):
        new_nums.append((nums[i] + nums[i+1]) // 2)
    return recursive_reduce(new_nums, depth + 1)

def flag_anomalies(records):
    # Unused anomaly detector (red herring)
    flags = []
    for r in records:
        if r.startswith('ERR') or r.endswith('FAIL'):
            flags.append(True)
    return len(flags)

def main():
    # Input data
    raw_signal = [12, 8, 14, 6, 9, 11, 7]
    metadata_tags = ['SYS_INIT', 'CORE_1', 'IO_POLL', 'NET_TX']
    log_entries = ['OK', 'OK', 'RETRY', 'OK', 'FAIL']

    # Irrelevant transformations (distractors)
    tag_hashmap = build_lookup(metadata_tags)
    anomaly_count = flag_anomalies(log_entries)
    dummy_process = process_segment(metadata_tags)

    # Actual computation chain begins
    t_signal = transform_data(raw_signal)  # Step 1: bitwise transform
    
    # Extract frequency distribution (collections.Counter)
    freq = Counter(t_signal)                # Step 2: count frequencies
    freq_vals = list(freq.values())
    
    # Compute entropy (decoy - not used later)
    signal_entropy = compute_entropy(freq_vals)
    
    # Validate checksum (irrelevant result)
    chksum = validate_checksum(raw_signal)
    
    # Critical path: recursive reduction on transformed signal
    reduced_value = recursive_reduce(t_signal)  # Step 3: multi-step reduction
    
    # Secondary transformation using string methods on decoy data
    tag_stats = ''.join(metadata_tags).count('I')  # Counts 'I' in concatenated tags
    
    # Final diagnostic computed from reduced value and entropy side-channel
    # Note: entropy not used — red herring!
    final_diagnostic = reduced_value * 17 + 5
    
    # Print required output
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute
result = main()