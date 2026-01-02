import math

# Irrelevant helper function (dead code path)
def unused_helper(arr):
    return [x ** 2 for x in arr if x % 2 == 0]

# Misleading transformation with decoy logic
def decoy_transform(seq):
    temp = []
    for i, val in enumerate(seq):
        if val > 5:
            temp.append(math.log(val) * i)
        else:
            temp.append(val + 3)
    return temp  # Never used in final computation

# Real processing chain
def apply_mask(values, mask):
    return [v for v, m in zip(values, mask) if m]

def compute_weighted_sum(vals):
    weights = [0.1, 0.2, 0.3, 0.4]  # Fixed weight pattern
    return sum(v * w for v, w in zip(vals, weights))

def filter_and_map(data):
    filtered = [x for x in data if x % 2 == 1]  # Keep only odds
    mapped = [math.sqrt(x) for x in filtered]  # Square root of odd numbers
    normalized = [m / max(mapped) for m in mapped]  # Normalize to [0,1]
    return normalized

def generate_control_signal(length):
    # Generates a control bit array (not actually used but looks important)
    signal = [int((i + 1) % 3 == 0) for i in range(length)]
    return signal

def process_sequence(raw_data):
    # Step 1: Clean and extract relevant elements
    cleaned = [x for x in raw_data if isinstance(x, int) and x > 0]
    
    # Step 2: Transform via multiple stages
    transformed = filter_and_map(cleaned)
    
    # Step 3: Create synthetic mask based on length
    mask = [True if i % 2 == 0 else False for i in range(len(transformed))]
    masked_values = apply_mask(transformed, mask)
    
    # Step 4: Compute weighted sum
    intermediate_result = compute_weighted_sum(masked_values)
    
    # Step 5: Apply final scaling using constant derived from bit manipulation
    scale_factor = (17 & 29) ^ 5  # Bitwise: 17 & 29 = 17, 17 ^ 5 = 20
    final_output = intermediate_result * scale_factor
    
    # Decoy variables that look important but aren't used further
    debug_snapshot = {'size': len(cleaned), 'max_val': max(cleaned)}
    audit_log = f"Processed {len(cleaned)} items into {len(transformed)} features."
    
    return final_output

# Main execution block
if __name__ == '__main__':
    # Input data with mixed types and irrelevant entries
    data = [4, 'ignore', 9, None, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169]
    
    # Call decoy function (produces result but not used)
    decoy_result = decoy_transform([x for x in data if isinstance(x, int)])
    
    # Generate unused control signal
    control_bits = generate_control_signal(len(data))
    
    # Real processing
    final_output = process_sequence(data)
    
    # Output target variable
    print(f"Result: {final_output}")