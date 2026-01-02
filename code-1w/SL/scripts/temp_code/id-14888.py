import math

# Irrelevant helper function (dead code path)
def unused_calculator(x):
    return (x ** 2 + 3 * x + 5) % 7

# Distractor variables
temp_cache = [0] * 100
buffer_flag = True
offset_lookup = {i: i * 3 + 1 for i in range(10)}
scaling_factor = 2.718
dummy_matrix = [[i * j for j in range(5)] for i in range(5)]

# Relevant data structure initialization
data_stream = [12, 3, 8, 1, 9, 7, 14]

# Misleading transformation chain
transformed = []
for val in data_stream:
    if val % 2 == 0:
        transformed.append(val // 2)
    else:
        transformed.append(val * 3 + 1)

# Decoy statistical summary
mean_val = sum(transformed) / len(transformed)
median_approx = sorted(transformed)[len(transformed)//2]
mode_candidate = max(set(transformed), key=transformed.count)

# Real processing begins here — nested logic with early returns
def analyze_pattern(seq):
    history = {}
    total_shift = 0
    
    for i, num in enumerate(seq):
        # Bit manipulation red herring
        bit_weight = bin(num).count('1')
        temp_cache[i % 10] += bit_weight
        
        # Actual logic: track cumulative product of primes
        is_prime = True
        if num < 2:
            is_prime = False
        for divisor in range(2, int(math.sqrt(num)) + 1):
            if num % divisor == 0:
                is_prime = False
                break
        
        if is_prime:
            total_shift += num
            if num not in history:
                history[num] = 0
            history[num] += 1
    
    # Early return based on irrelevant condition
    if len(history) > 10:
        return -999
    
    # Actual result: sum of prime numbers
    return total_shift

# Another decoy function using dictionary operations
status_map = {}
def update_status(code, msg):
    status_map[code] = msg.upper().replace(' ', '_')
    return len(status_map)

# Initialize map with nonsense entries
for k in ['INIT', 'LOAD', 'FAIL']:
    update_status(k, f'dummy {k.lower()} message')

# Core logic hidden among distractions
def process_sequence(stream):
    # Tuple unpacking distraction
    a, b, *rest = stream
    offset = a - b
    
    # Dictionary used for frequency counting (real use)
    freq_count = {}
    for x in stream:
        freq_count[x] = freq_count.get(x, 0) + 1
    
    # Conditional mutation based on distractor flag
    intermediate = []
    for v in stream:
        if v in freq_count and freq_count[v] > 0:
            # Apply transformation only once per value
            intermediate.append(v ^ offset)  # XOR with offset
            freq_count[v] = 0  # mark as processed
    
    # Nested loop with break and continue red herrings
    accumulator = 0
    for n in intermediate:
        for shift in range(3):
            candidate = (n >> shift)
            if candidate == 0:
                break
            if candidate % 3 == 0:
                continue
            accumulator += candidate
    
    # Final step: combine with analysis result
    prime_sum = analyze_pattern(stream)
    final_value = accumulator * 2 - prime_sum
    
    # Dead branch that never executes due to logic
    if buffer_flag and False:  # always false
        final_value += scaling_factor
    
    return final_value

# Execution point of interest
final_output = process_sequence(data_stream)
print(f"Target result: {final_output}")