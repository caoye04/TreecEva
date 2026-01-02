import math

# Irrelevant helper function (dead code path)
def unused_transform(x):
    return [i * 2 for i in x if i % 3 == 0]

# Distractor variables
temp_cache = [0] * 100
buffer_data = list(range(50))
offset_correction = 7
scaling_factor = 2.5

# Misleading intermediate computation
defect_count = 0
for i in range(15):
    defect_count += (i * i) % 4

# Core logic disguised among noise
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

# Simulated sensor readings with noise
def generate_noisy_readings():
    base = [1, 2, 3, 4, 5]
    noise = [math.sin(i) for i in range(len(base))]
    return [b + n for b, n in zip(base, noise)]

readings = generate_noisy_readings()
calibrated = [round(r, 1) for r in readings]

# Red herring: checksum that is never used
total_checksum = sum(calibrated) * scaling_factor

# Real data structure involved in computation
data = [6, 8, 10, 12, 15, 18, 20, 24, 30]

# Auxiliary function with distractor logic
def filter_and_map(seq):
    # Irrelevant pre-processing
    masked = [x ^ 5 for x in seq]  # Bitwise red herring
    filtered = [x for x in masked if x > 10]
    # Actual relevant transformation
    processed = []
    for val in filtered:
        if any(val % p == 0 for p in primes[:4]):  # Divisible by first 4 primes
            processed.append(val // 2)
    return processed

# Another decoy function
def analyze_distribution(vals):
    mean = sum(vals) / len(vals)
    variance = sum((x - mean) ** 2 for x in vals) / len(vals)
    return {'mean': mean, 'variance': variance}

# Unused but plausible-sounding analysis
stats = analyze_distribution(buffer_data)

# Key processing function
# This contains the actual logic leading to the answer
def process_sequence(seq):
    # Step 1: Extract even numbers greater than 8
    step1 = [x for x in seq if x % 2 == 0 and x > 8]
    
    # Step 2: Apply modular arithmetic transformation
    step2 = [x % 7 for x in step1]
    
    # Step 3: Map using conditional expression
    step3 = [y if y < 5 else y - 3 for y in step2]
    
    # Step 4: Accumulate with offset
    accumulation = 0
    for val in step3:
        accumulation += val * 2
    
    # Step 5: Adjust using prime-based correction
    prime_correction = sum(1 for p in primes if p < accumulation)
    
    # Step 6: Final transformation
    result = accumulation - prime_correction + len(step3)
    
    # Irrelevant string manipulation (distractor)
    log_tag = "PROCESSED_" + "_".join([str(z) for z in step3])
    debug_info = log_tag.lower().replace('_', '-')
    
    return result

# Execution point of interest
final_output = process_sequence(data)

print(f"Target result: {final_output}")