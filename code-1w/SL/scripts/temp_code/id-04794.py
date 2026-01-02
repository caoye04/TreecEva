def analyze_pattern(sequence):
    counts = {}
    for item in sequence:
        counts[item] = counts.get(item, 0) + 1
    return counts

def normalize_values(values):
    total = sum(values)
    return [v / total for v in values]

def calculate_final_score(raw_data, limits):
    # Step 1: Filter data within threshold bounds (relevant)
    filtered = [x for x in raw_data if limits[0] < x < limits[1]]
    
    # Step 2: Compute frequency distribution (partially relevant)
    freq = analyze_pattern(filtered)
    frequencies = list(freq.values())
    
    # Step 3: Normalize frequencies (distraction - not used later)
    normalized_freq = normalize_values(frequencies) if frequencies else [0]
    
    # Step 4: Extract even-indexed elements (semi-relevant)
    indexed_samples = [filtered[i] for i in range(0, len(filtered), 2)]
    
    # Step 5: Compute pairwise XOR on consecutive elements (relevant)
    xor_chain = 0
    for i in range(len(indexed_samples) - 1):
        xor_chain ^= (indexed_samples[i] ^ indexed_samples[i+1])
    
    # Step 6: Use set operations to find unique transitions (distractor)
    pairs = set(zip(filtered, filtered[1:]))
    transition_count = len(pairs)
    dummy_metric = sum({p[0] for p in pairs})  # unused
    
    # Step 7: Combine arithmetic and logical conditions (key logic)
    base_score = sum(indexed_samples)
    adjustment = 0
    if len(filtered) > 5:
        adjustment += 10
    if len(pairs) % 2 == 0:
        adjustment -= 3
    
    # Step 8: Final computation (this assigns final_score)
    final_score = (base_score + xor_chain + adjustment) % 97
    
    # Irrelevant string manipulation (dead code path)
    status_msg = "Processing complete" if final_score > 0 else "Error"
    log_entry = " -> ".join([status_msg, str(final_score)])
    
    # Unused variables (distractors)
    max_freq = max(frequencies) if frequencies else 0
    avg_filtered = sum(filtered) / len(filtered) if filtered else 0
    
    return final_score

# Main execution
raw_input = [12, 15, 12, 18, 15, 22, 18, 25, 12]
data = [x + 1 for x in raw_input]  # Transform input
thresholds = (13, 25)
interim_set = set(data)
count_summary = {k: data.count(k) for k in interim_set}

# Key statement
final_score = calculate_final_score(data, thresholds)
print(f"Result: {final_score}")