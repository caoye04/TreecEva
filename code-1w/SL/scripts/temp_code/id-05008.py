import math

# Simulated sensor data from industrial machinery
def fetch_sensor_readings():
    return [789, 821, 645, 912, 777, 888, 612, 734, 698, 756]

# Noise filtering using median smoothing (irrelevant for final result)
def apply_noise_filter(data):
    filtered = []
    for i in range(len(data)):
        neighbors = data[max(0, i-1):min(len(data), i+2)]
        filtered.append(sorted(neighbors)[len(neighbors)//2])
    return filtered

# Legacy system compatibility wrapper (dead code path)
def legacy_normalize(x):
    return (x - min(data)) / (max(data) - min(data)) if 'data' in globals() else x

# Core transformation: extract digits and compute prime digit sum
def transform_readings(raw_values):
    prime_digits = {2, 3, 5, 7}
    total = 0
    for val in raw_values:
        while val > 0:
            digit = val % 10
            if digit in prime_digits:
                total += digit
            val //= 10
    return total

# Advanced compression algorithm (distractor)
def compress_data(seq):
    compressed = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i-1]:
            count += 1
        else:
            compressed.append((seq[i-1], count))
            count = 1
    if seq:
        compressed.append((seq[-1], count))
    return compressed

# Calculate system uptime penalty (misleading intermediate)
def calculate_uptime_penalty(start_time, logs):
    baseline = 100.0
    for log in logs:
        if log < start_time:
            baseline -= 0.5
    return max(baseline, 0)

# Main efficiency calculation (relevant function)
def calculate_efficiency(items, limit):
    weighted_sum = 0
    weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    
    # Process each item with index using enumerate (required feature)
    for idx, item in enumerate(items):
        if idx % 2 == 0:
            weighted_sum += item * weights[idx]
        else:
            weighted_sum += (item // 3) * weights[idx]
            
    # Secondary adjustment based on digit analysis
    digit_count = 0
    temp = int(weighted_sum)
    while temp > 0:
        digit_count += 1
        temp //= 10
    
    # Final adjustment using list comprehension and zip (required features)
    adjustments = [abs(a - b) for a, b in zip(items[:5], items[5:])]  
    adjustment_factor = sum(adjustments) / len(adjustments) if adjustments else 0
    
    final_score = weighted_sum - (adjustment_factor * digit_count)
    
    # Dead branch - never executed due to limit value
    if limit < 0:
        extra_penalty = 0
        for x in items:
            if x % 7 == 0:
                extra_penalty += 1
        final_score -= extra_penalty * 5
        
    return round(final_score, 4)

# Irrelevant helper: binary pattern analysis (red herring)
def analyze_bit_patterns(numbers):
    patterns = {}
    for n in numbers:
        bin_rep = bin(n)[2:]
        ones = bin_rep.count('1')
        zeros = bin_rep.count('0')
        patterns[n] = (ones, zeros, ones - zeros)
    return patterns

# Orchestration function with multiple distractions
def main_pipeline():
    global data
    data = fetch_sensor_readings()
    
    # Apply several irrelevant transformations
    filtered_data = apply_noise_filter(data)
    compressed = compress_data(filtered_data)
    bit_analysis = analyze_bit_patterns(data)
    
    # Transform data for prime digit processing (this modifies state but isn't used later)
    _ = transform_readings(data)
    
    # Uptime penalty calculation with fake logs (misleading computation)
    uptime_penalty = calculate_uptime_penalty(1000, [900, 950, 1050])
    
    # Key processing step: prepare data for efficiency calculation
    processed_data = []
    for x in data:
        if x > 700:
            processed_data.append(x - 600)
        else:
            processed_data.append(x - 500)
    
    threshold = 100  # Used in calculate_efficiency, influences control flow (dead branch not taken)
    
    # Critical statement
    efficiency_score = calculate_efficiency(processed_data, threshold)
    
    # Print required output
    print(f"Result: {efficiency_score}")
    
    # Unused variables (distractors)
    normalized = [legacy_normalize(x) for x in data]
    sorted_pairs = sorted(zip(data, filtered_data), key=lambda x: x[1])
    
    return efficiency_score

# Execute pipeline
main_pipeline()