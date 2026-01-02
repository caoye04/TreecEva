def analyze_pattern(seq):
    """Irrelevant function analyzing sequence patterns."""
    if len(seq) < 5:
        return False
    count = 0
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            count += 1
    return count > 2

# Irrelevant data transformation
temp_buffer = [x ** 2 for x in range(15) if x % 3 != 0]
offset_map = {i: temp_buffer[i] % 7 for i in range(len(temp_buffer))}

# Distractor variables
counterfeit_sum = sum([i * 2 for i in temp_buffer if i < 50])
shadow_index = 0
for k in offset_map:
    shadow_index ^= k

def transform_key(val, shift=3):
    # Unused cryptographic-style distraction
    return ((val << shift) ^ 0xA3) & 0xFF

# Real computation begins here
raw_input = [8, 12, 16, 24, 32, 40]
evaluation_peaks = list(filter(lambda x: x > 20, raw_input))

baseline = 10
dynamic_weights = [0.5, 1.5, 2.0, 1.0, 0.8, 1.2]

# Misleading normalization path (dead end)
normalized = []
for val in raw_input:
    norm_val = val / (baseline + 1e-9)
    if norm_val > 1.5:
        normalized.append(round(norm_val, 2))

# Actual processing function
def process_metrics(data, weights):
    aggregate = 0.0
    adjustment_factor = 1.0
    
    # Nested logic with distractors
    for i in range(len(data)):
        if i % 2 == 0:
            temp = data[i] * weights[i]
            if temp > 30:
                adjustment_factor *= 1.1
        else:
            temp = data[i] + weights[i]
            adjustment_factor *= 0.95
        
        # Key slicing operation affecting final result
        subset = raw_input[1:4]
        slice_sum = sum(subset) / len(subset)
        
        # Boolean logic and case conversion red herring
        flag_str = "AbNoRmAl" if temp > 25 else "normal"
        upper_count = len([c for c in flag_str if c.isupper()])
        
        # Only this line contributes to accumulation
        aggregate += temp * (adjustment_factor if upper_count > 3 else 1.0)
    
    # Decoy mutation
    post_processed = [x * adjustment_factor for x in data]
    
    # Final adjustment using lambda (actual relevant use)
    scale_fn = lambda x: x * 0.85 if x > 100 else x * 1.05
    result = scale_fn(aggregate)
    
    # This variable is critical
    final_score = int(result + 0.5)  # Simulate rounding
    return final_score

# Unused recursive red herring
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

# Dead code path
if __name__ == "__main__":
    debug_mode = False
    if debug_mode:
        print("Debug:", counterfeit_sum)

# Trigger the actual computation
data = evaluation_peaks
weights = dynamic_weights[:len(evaluation_peaks)]
final_score = process_metrics(data, weights)

# Output the required result
print(f"Target result: {final_score}")