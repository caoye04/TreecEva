import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return (x ** 2 + 3 * x + 1) % 7

# Misleading transformation chain
def decoy_transform(sequence):
    temp = [s ^ 5 for s in sequence]  # Bitwise red herring
    return [t * 2 for t in temp if t > 10]  # Filters out most elements

# Auxiliary function with partial relevance
def normalize_values(arr):
    max_val = max(arr) if arr else 1
    return [round(v / max_val, 6) for v in arr]

# Core logic disguised among distractions
def apply_mask(data, key=13):
    masked = []
    for i, val in enumerate(data):
        if i % 2 == 0:
            masked.append(val ^ (key * 3))  # XOR with derived constant
        else:
            masked.append(val + (key // 2))
    return masked

# Another irrelevant utility
def simulate_legacy_mode(config):
    return sum([len(str(c)) for c in config]) * 0.5  # Never actually used

# Conditional expression and data refinement
def refine_step(values):
    adjusted = [v + 1 for v in values]
    # Conditional expression determining scaling factor
    scale = 1.5 if sum(adjusted) > 50 else 0.8
    return [round(v * scale) for v in adjusted]

# Main processing pipeline with nested logic
def process_pipeline(raw_input):
    # Step 1: Initial filtering
    filtered = [x for x in raw_input if x % 3 != 1]
    
    # Step 2: Apply non-linear transformation
    transformed = [int(math.log(v + 1, 2)) if v > 0 else 0 for v in filtered]
    
    # Step 3: Normalize before masking (distractor step)
    normalized = normalize_values(transformed)
    
    # Step 4: Convert back to integers for bit operations
    reintegized = [int(v * 100) for v in normalized]
    
    # Step 5: Apply actual mask (key operation)
    masked_data = apply_mask(reintegized, key=7)
    
    # Step 6: Refine using conditional scaling
    refined = refine_step(masked_data)
    
    # Step 7: Secondary filter based on parity
    final_candidates = [f for f in refined if f % 4 == 2]
    
    # Step 8: Aggregate with weighted sum (answer depends on this)
    total = 0
    for idx, num in enumerate(final_candidates):
        weight = 2 if idx % 2 == 0 else 0.5
        total += num * weight
    
    # Final output computed via multi-step reasoning
    final_output = int(total // 1.5)  # Integer division and rounding
    
    # Distraction: unused variables
    debug_trace = [filtered, transformed, normalized]
    audit_log = f"Processed {len(filtered)} items"
    
    return final_output

# Setup input with meaningful name
sensor_readings = [15, 0, 22, 9, 33, 4, 18, 12]
data_chunk = sensor_readings[:]

# Execute main logic
final_output = process_pipeline(data_chunk)

# Output result as required
print(f"Result: {final_output}")