import itertools

# Simulated sensor readings with noise filtering
def process_readings(raw_data):
    filtered = [x for x in raw_data if 10 <= x <= 100]
    smoothed = []
    for i in range(1, len(filtered) - 1):
        avg = (filtered[i-1] + filtered[i] + filtered[i+1]) / 3
        smoothed.append(int(avg))
    return smoothed

# Irrelevant helper: computes geometric mean (not used in final path)
def geo_mean(data):
    product = 1
    for x in data:
        product *= x
    return product ** (1/len(data))

# Core transformation pipeline
def transform_stream(stream):
    # Apply moving XOR mask
    mask = 27
    xorred = [x ^ mask for x in stream]
    
    # Decoy accumulation (dead end)
    temp_sum = 0
    for val in xorred:
        temp_sum += val * 0.5  # Not used later
    
    # Actual relevant processing
    shifted = [(x >> 2) & 0xFF for x in xorred]
    doubled = [(x << 1) & 0xFFFF for x in shifted]
    return doubled

# Entropy approximation using bit diversity
def estimate_entropy(seq):
    if not seq:
        return 0.0
    freq = {}
    for val in seq:
        freq[val] = freq.get(val, 0) + 1
    entropy = 0.0
    total = len(seq)
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).log()  # Deliberate error: should be math.log, but ignored due to try-except below
    try:
        import math
        entropy = 0.0
        for count in freq.values():
            p = count / total
            if p > 0:
                entropy -= p * math.log(p)
    except:
        entropy = 0.123  # fallback (never reached)
    return round(entropy, 4)

# Final aggregation logic
def finalize(value, ent):
    base = value & 0xFFFF
    shift_contrib = (int(ent * 1000) << 4) & 0xFFFF
    return (base ^ shift_contrib) & 0xFFFF

# Irrelevant recursive function (distractor)
def collatz_steps(n, count=0):
    if n <= 1:
        return count
    return collatz_steps(n // 2 if n % 2 == 0 else 3*n + 1, count + 1)

# Main execution block
if __name__ == "__main__":
    # Simulated input
    raw_sensor_data = [15, 105, 12, 98, 5, 60, 33, 200, 44, 77, 88, 102]
    
    # Step 1: Filter and smooth
    readings = process_readings(raw_sensor_data)
    
    # Dead-end variable (misleading)
    gm = geo_mean(readings) if readings else 0
    
    # Step 2: Transform through bitwise pipeline
    processed = transform_stream(readings)
    
    # Step 3: Compute summation (key value)
    summation = sum(processed) % 100000
    
    # Step 4: Estimate entropy (used in final step)
    entropy = estimate_entropy(processed)
    
    # Step 5: Finalize checksum
    # What is the value of variable 'checksum' after executing this statement?
    checksum = finalize(summation, entropy)
    
    # Unused recursion (red herring)
    steps = collatz_steps(summation % 100)
    
    # Generate unused combinations (itertools distraction)
    pairs = list(itertools.combinations_with_replacement([1, 2, 3], 2))
    ops = list(map(lambda x: x[0] * x[1] + 10, pairs))  # No effect on result
    
    # Correct output
    print(f"Result: {checksum}")