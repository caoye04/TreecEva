import itertools

# Irrelevant helper function (dead code path)
def unused_checksum(arr):
    return sum(x ^ 255 for x in arr) % 100

# Misleading transformation chain
def decoy_transform(seq):
    temp = [x * 3 + 7 for x in seq if x % 2 == 0]
    temp = [t - 5 for t in temp if t > 20]
    return sorted(temp, reverse=True)

# Unused recursive red herring
def bad_fib(n):
    return n if n <= 1 else bad_fib(n-1) + bad_fib(n-2)

# Real processing components
def extract_valid_entries(logs):
    return [entry['value'] for entry in logs if entry.get('active') and entry['value'] > 0]

def apply_filter_chain(signal):
    # Nonlinear filter with conditional expression
    filtered = [(x >> 2) if (x % 4 == 0) else (x + 1) for x in signal]
    return [f for f in filtered if f in range(50, 150)]

def compute_weighted_sum(series):
    weights = itertools.cycle([1, -0.5, 0.25])
    weighted = sum(val * next(weights) for val in series)
    return round(weighted, 6)

# Main pipeline
def process_pipeline(stream):
    raw_data = stream.copy()
    
    # Distraction: irrelevant bit manipulation
    shift_mask = 255
    masked_data = [d ^ shift_mask for d in raw_data[:10]]
    _ = [d << 2 for d in masked_data]  # Computed but unused
    
    # Create decoy summary (never used)
    decoy_summary = {
        'max_shifted': max(masked_data) if masked_data else 0,
        'min_decoy': min(decoy_transform(raw_data))
    }
    
    # Actual logic begins here
    config_flags = {'debug': False, 'strict': True, 'version': 3}
    if config_flags['version'] >= 3:
        extracted = extract_valid_entries([
            {'value': x, 'active': (x % 3 != 0)} for x in raw_data
        ])
        
        if len(extracted) > 5:
            filtered = apply_filter_chain(extracted)
            
            # Secondary filter: only keep numbers present in Fibonacci-like sequence
            fib_set = set()
            a, b = 1, 1
            while a < 200:
                fib_set.add(a)
                a, b = b, a + b
            
            refined = [num for num in filtered if num in fib_set]
            
            # Final computation
            if refined:
                adjustment_factor = 2.5 if any(r % 13 == 0 for r in refined) else 1.8
                intermediate = compute_weighted_sum(refined) * adjustment_factor
                final_output = int(intermediate + 0.5)  # Round to nearest integer
                return final_output
    
    return -999  # Fallback (not reached in this case)

# Simulated sensor data stream (real input)
data_stream = [144, 12, 98, 89, 76, 55, 44, 34, 21, 13, 8, 5, 3, 2, 1, 0, 99, 169]

# Trigger execution
temp_var_x = decoy_transform(data_stream)  # Red herring call
unused_checksum(data_stream)  # Another distraction

final_output = process_pipeline(data_stream)
print(f"Target result: {final_output}")