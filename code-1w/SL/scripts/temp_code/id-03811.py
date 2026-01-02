import itertools

def analyze_signal(pattern, threshold=5):
    """Irrelevant function: simulates signal analysis with no impact on final result."""
    count = 0
    for val in pattern:
        if val > threshold:
            count += 1
    return count * 2  # Red herring computation

def transform_sequence(seq):
    """Distraction: applies bitwise and arithmetic transforms that are never used."""
    temp_result = []
    for i, x in enumerate(seq):
        transformed = (x ^ i) + 3
        if transformed % 2 == 0:
            temp_result.append(transformed // 2)
    return [t ** 2 for t in temp_result]  # Dead end

def preprocess_input(raw):
    """Relevant but indirect: prepares data, but only one output matters."""
    cleaned = [x for x in raw if x >= 0]
    offset = sum(cleaned) % 4
    shifted = [(x + offset) * 2 for x in cleaned]
    return shifted, offset

def filter_candidates(items, limit):
    """Unused function: included to mislead about filtering importance."""
    return [item for item in items if item < limit]

def compute_entropy(values):
    """Decoy metric: calculates entropy-like value not used in final logic."""
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 6)

def extract_segments(data, size=4):
    """Splits data into chunks – only length is later used indirectly."""
    segments = []
    for i in range(0, len(data) - size + 1, size//2):
        segments.append(data[i:i+size])
    return segments

def calculate_base_score(seq):
    """Partially relevant: returns a component used in final calculation."""
    avg = sum(seq) / len(seq)
    deviation_sum = sum(abs(x - avg) for x in seq)
    return int(avg + (deviation_sum % 7))

def derive_key_factor(metadata):
    """Crucial but hidden: extracts key factor from metadata structure."""
    factor = 1
    for k, v in metadata.items():
        if 'flag' in k:
            factor *= (v + 2)
    return factor

def calculate_optimal_yield(data_packet):
    """Main logic: combines base score and key factor correctly."""
    processed_list = data_packet['values']
    meta_info = data_packet['meta']
    
    # Step 1: Get base performance score
    base_score = calculate_base_score(processed_list)
    
    # Step 2: Extract multiplicative factor from metadata
    key_multiplier = derive_key_factor(meta_info)
    
    # Step 3: Apply conditional adjustment based on list properties
    adjustment = 3 if len(processed_list) > 6 else 1
    
    # Step 4: Use itertools to generate pairwise sums, take max as modifier
    pairs = list(itertools.combinations(processed_list, 2))
    pair_sums = [a + b for a, b in pairs]
    modifier = max(pair_sums) if pair_sums else 0
    
    # Step 5: Final yield formula
    final_yield = (base_score * key_multiplier + adjustment) * 2
    
    # Irrelevant post-processing (distractor)
    normalized = final_yield / (modifier + 1) if modifier else final_yield
    status_flag = 'OK' if normalized > 10 else 'LOW'
    
    return int(final_yield)  # Answer is here

# --- Main Execution ---
if __name__ == '__main__':
    # Raw input data
    raw_input = [3, -1, 4, 1, 5, -2, 9, 2]
    
    # Irrelevant signal pattern
    signal_pattern = [6, 7, 8, 4, 3, 9]
    signal_analysis = analyze_signal(signal_pattern)  # Unused
    
    # Preprocess the real data
    processed_data_list, shift_offset = preprocess_input(raw_input)
    
    # Transform sequence (dead end)
    dummy_transform = transform_sequence(processed_data_list)  # Nowhere used
    
    # Extract segments (only length matters indirectly)
    chunks = extract_segments(processed_data_list, size=4)
    segment_count = len(chunks)
    
    # Compute entropy (decoy metric)
    entropy_value = compute_entropy(processed_data_list)  # Not used
    
    # Build metadata with key flags
    context_meta = {
        'version': 2,
        'flag_alpha': 3,
        'config': 'X9',
        'flag_beta': 2,
        'debug_mode': False
    }
    
    # Assemble packet for processing
    input_packet = {
        'values': processed_data_list,
        'meta': context_meta,
        'count_hint': segment_count
    }
    
    # Filter candidates (unused path)
    filtered_vals = filter_candidates(processed_data_list, 10)  # Computed but ignored
    
    # Conditional expression for distraction
    mode_status = 'active' if shift_offset > 2 else 'standby'
    backup_level = 100 if mode_status == 'active' else 50  # Unused
    
    # Key execution point
    final_yield = calculate_optimal_yield(input_packet)
    
    # Print result
    print(f"Result: {final_yield}")