import math

# Simulated sensor data processing with embedded logic puzzle
def collect_readings():
    raw = [127, 255, 192, 64, 96, 130, 200]
    processed = []
    for val in raw:
        if val & 128:  # Check high bit
            processed.append(val ^ 17)
    return processed

# Irrelevant helper - distractor function
def calculate_checksum(data):
    checksum = 0
    for d in data:
        checksum = (checksum + d) % 257
    return checksum * 2  # Misleading path

# Noise filter - partially relevant but not used in final result
def apply_filter(sequence):
    return [x for x in sequence if x > 100]

# Core pattern analyzer - contains key logic
def analyze_pattern(seq, limit):
    temp_result = 0
    history = []
    
    # Complex transformation chain
    for i in range(len(seq)):
        shifted = seq[i] >> 2
        if i % 2 == 0:
            transformed = (shifted ^ 15) + (i * 3)
        else:
            transformed = (shifted | 7) - i
        
        # Conditional expression - required python feature
        adjusted = transformed + 10 if transformed < limit else transformed - 5
        
        # Accumulate based on bit condition
        if bin(adjusted).count('1') % 2 == 1:
            temp_result -= adjusted
        else:
            temp_result += adjusted
        
        history.append(abs(transformed))
    
    # Secondary manipulation on history (distraction)
    avg_history = sum(history) / len(history) if history else 0
    noise_floor = math.floor(avg_history * 0.1)
    
    # Red herring calculation - looks important
    diagnostic_score = 0
    for h in history:
        if h > avg_history:
            diagnostic_score += 1
    
    # Decoy assignment - misleading intermediate
    final_diagnostic = temp_result + noise_floor - diagnostic_score
    
    # Actual answer depends only on temp_result and one conditional adjustment
    # All above distractions are irrelevant
    if temp_result > 0:
        final_diagnostic = temp_result + 5
    else:
        final_diagnostic = temp_result - 3
    
    return final_diagnostic

# Unused recursive function - dead code path
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)

# Unused matrix operation - decoy data structure
redundant_matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]
sparse_total = sum(sum(row) for row in redundant_matrix)

# Initialization parameters
def main():
    readings = collect_readings()           # [110, 238, 205, 79, 111, 147, 215]
    threshold = 120
    scaling_factor = 1.5  # Unused parameter
    
    # Linear search for first element above threshold - actual use
    found_index = -1
    for idx, val in enumerate(readings):
        if val > threshold:
            found_index = idx
            break
    
    # Modify threshold based on index - affects final outcome
    if found_index != -1:
        threshold = threshold - (found_index * 8)
    
    # Key execution point
    final_diagnostic = analyze_pattern(readings, threshold)
    
    # Print required output
    print(f"Result: {final_diagnostic}")

main()