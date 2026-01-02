from collections import defaultdict
import math

def analyze_flow(pattern, threshold):
    flow_counter = defaultdict(int)
    for item in pattern:
        flow_counter[item] += 1
    
    # Irrelevant transformation (distractor)
    normalized = {k: v / len(pattern) for k, v in flow_counter.items()}
    excess = sum(1 for v in flow_counter.values() if v > threshold)
    return excess

def validate_sequence(seq):
    # Semi-relevant check with side computation
    checksum = 0
    temp_vals = []
    for i, val in enumerate(seq):
        checksum += (i + 1) * val
        temp_vals.append(checksum % 17)
    return checksum % 13 == 0

def distribute_resources(items, multiplier):
    # Core logic partially used later
    base_alloc = [int(x * multiplier) for x in items]
    adjustment = sum(base_alloc) % 5
    
    # Dead code path (distractor)
    if adjustment > 10:
        base_alloc = [x + 1 for x in base_alloc]
    
    sorted_alloc = sorted(base_alloc, reverse=True)
    return sorted_alloc

def modular_shift(values, shift):
    shifted = []
    for v in values:
        shifted.append((v + shift) % 19)
    return shifted

def optimize_distribution(resources, limits):
    total = 0
    cap = 0
    
    # Real logic: count constrained resource pairs
    for key, val_list in resources.items():
        filtered = [v for v in val_list if v <= limits[key]]
        if len(filtered) >= 2:
            cap += filtered[0] * filtered[1]  # Product of first two valid
        else:
            cap += sum(filtered)
    
    # Red herring: complex but unused calculation
    dummy_agg = 0
    for lst in resources.values():
        running = 0
        for item in lst:
            running = (running * 3 + item) % 97
        dummy_agg += running
    
    # Final adjustment based on real cap
    if cap > 100:
        cap = int(math.sqrt(cap))
    elif cap > 50:
        cap = int(cap * 0.75)
    else:
        cap = cap + 10
    
    return cap

# Main execution block
if __name__ == "__main__":
    # Input data setup
    raw_pattern = [3, 7, 4, 7, 3, 8, 4, 7, 3, 9]
    constraint_limits = {'A': 5, 'B': 6, 'C': 8}
    
    # Distractor: unused statistical summary
    avg_val = sum(raw_pattern) / len(raw_pattern)
    variance = sum((x - avg_val) ** 2 for x in raw_pattern) / len(raw_pattern)
    entropy = -sum((v/len(raw_pattern)) * math.log2(v/len(raw_pattern)) 
                   for v in set(raw_pattern))
    
    # Build resource map (semi-processed)
    resource_map = defaultdict(list)
    resource_map['A'] = [2, 4, 6, 3]
    resource_map['B'] = [5, 8, 4, 7]
    resource_map['C'] = [9, 3, 2, 6]
    
    # Trigger irrelevant analysis (distraction)
    excess_groups = analyze_flow(raw_pattern, 2)
    sequence_valid = validate_sequence([1, 3, 2, 4])
    
    # Intermediate processing with partial relevance
    distributed = distribute_resources([2.1, 3.6, 1.8], 2.5)
    shifted = modular_shift(distributed, 4)
    
    # Key statement
    final_capacity = optimize_distribution(resource_map, constraint_limits)
    
    # Print result as required
    print(f"Result: {final_capacity}")