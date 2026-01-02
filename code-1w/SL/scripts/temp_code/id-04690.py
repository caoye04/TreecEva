import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return x * x + 2 * x + 1

# Decoy transformation table (misleading data)
transformation_table = {
    'A': 10, 'B': 25, 'C': 40, 'D': 55,
    'X': 100, 'Y': 200, 'Z': 300  # Distractor entries
}

# Real data for processing
data = [
    {'type': 'network', 'latency': 45, 'retries': 2, 'active': True},
    {'type': 'disk', 'latency': 120, 'retries': 1, 'active': False},
    {'type': 'network', 'latency': 30, 'retries': 0, 'active': True},
    {'type': 'memory', 'latency': 5, 'retries': 0, 'active': True}
]

# Misleading global counters (red herring)
global_counter_a = 0
global_counter_b = 0

# Complex processing pipeline with distractors
def analyze_entry(entry):
    base = entry['latency']
    penalty = 0
    
    # Conditional expression (required python feature)
    multiplier = 1.5 if entry['active'] else 0.1
    
    # Bit manipulation red herring
    magic_flag = (base & 7) ^ 3
    
    # Irrelevant computation chain
    temp_offset = (magic_flag << 2) % 9
    global_counter_a += temp_offset  # Dead usage
    
    # Actual logic: penalty based on retries and type
    if entry['retries'] > 0:
        penalty += entry['retries'] * 10
    
    # Logical operation chain with short-circuit distraction
    if entry['type'] == 'disk' or entry['type'] == 'network' and base > 40:
        penalty += 5
    
    return base * multiplier + penalty

# Higher-order function with lambda (required feature)
def create_filter(threshold):
    return lambda item: item['latency'] < threshold

# Unused filter creation (distractor)
low_latency_filter = create_filter(50)

# Main processing function
def process_metrics(entries):
    results = []
    total_weight = 0.0
    
    for e in entries:
        # Slicing distraction: irrelevant substring operation on type
        prefix = e['type'][:3] if len(e['type']) > 2 else e['type']
        suffix_code = hash(prefix) % 17  # Noise
        
        # Call to real analyzer
        score = analyze_entry(e)
        
        # Conditional expression used in aggregation
        weight = 2.0 if e['type'] == 'network' else 1.0
        total_weight += weight
        
        results.append(score * weight)
    
    # Real aggregation: weighted average
    aggregate = sum(results) / total_weight if total_weight > 0 else 0
    
    # Integer division and rounding (suggested paradigm)
    rounded = int(aggregate + 0.5)
    
    # Final adjustment based on logical condition
    adjustment = 15 if any(e['retries'] == 0 for e in entries) and all(isinstance(x, dict) for x in entries) else -5
    
    # Key computation step: final_score depends on multiple reasoning paths
    final_score = rounded + adjustment
    
    # Multiple data structures with cross-reference (decoy set)
    seen_types = set(e['type'] for e in entries)
    type_ranks = {t: idx for idx, t in enumerate(sorted(seen_types))}
    global_counter_b += type_ranks.get('network', 0)  # Irrelevant side effect
    
    return final_score

# Execution point of interest
final_score = process_metrics(data)

# Output result as required
print(f"Target result: {final_score}")