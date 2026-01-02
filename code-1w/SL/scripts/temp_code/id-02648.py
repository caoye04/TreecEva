import math

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(i > 0 for i in x) if isinstance(x, list) else False

# Distractor variables
temp_cache = [0] * 100
scaling_factor = 1.618
decoys = {'a': 10, 'b': 20, 'c': 30}

# Real data used in computation
data = [3, 5, 8, 13, 21, 34]

# Misleading configuration with irrelevant fields
config = {
    'threshold': 7,
    'mode': 'fast',
    'padding': True,
    'transform': lambda x: (x ** 2) % 9,
    'offset': 0,
    'debug': True,
    'weights': [0.1, 0.2, 0.3],  # unused
    'limit': 5
}

# Unused recursive function (decoy)
def bad_recursion(n):
    if n <= 1:
        return n
    return bad_recursion(n-1) + bad_recursion(n-2)

# Real processing begins here
def apply_mask(seq, func):
    return [func(x) for x in seq if x % 2 == 1]  # only odd values processed

# Bit manipulation red herring
current_flag = 0b1010
flag_history = []
for _ in range(3):
    current_flag ^= 0b1111
    flag_history.append(current_flag)

# Actual pipeline
mask_func = lambda x: (x * 2) ^ 5  # double then XOR with 5
filtered = [x for x in data if x > config['threshold']]
sliced_part = filtered[1:]  # remove first element

# Modular arithmetic and slicing mixed
mod_step = list(map(lambda x: (x + 7) % 17, sliced_part))
reversed_chunk = mod_step[::-1]  # reverse using slice

# Dictionary-based transformation
mapper = {i: round(math.sin(i) * 100) for i in range(15)}
mapped_vals = [mapper[x] for x in reversed_chunk if x in mapper]

# Accumulate with offset from config
acc = config['offset']
for val in mapped_vals:
    acc += val * 2

# Secondary distractor: complex unused expression
useless_compound = sum([math.log(1 + x, 2) for x in temp_cache[:10] if x != 5]) if temp_cache else 0

# Final processing function
def process_pipeline(input_data, cfg):
    # Step 1: filter values greater than threshold
    stage1 = [x for x in input_data if x > cfg['threshold']]
    
    # Step 2: shift left by 1 bit (equivalent to *2), but only for primes
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    stage2 = [n << 1 for n in stage1 if is_prime(n)]
    
    # Step 3: apply modular squaring
    stage3 = [(n ** 2) % 19 for n in stage2]
    
    # Step 4: slice middle three elements
    mid_start = len(stage3) // 2 - 1
    stage4 = stage3[mid_start:mid_start+3]
    
    # Step 5: map through dictionary of precomputed sine values (reuse mapper)
    global mapper
    stage5 = [mapper[x] if x in mapper else 0 for x in stage4]
    
    # Step 6: reduce with alternating sum
    result = 0
    for i, v in enumerate(stage5):
        result += v if i % 2 == 0 else -v
    
    # Final adjustment
    return result + 100

# Execute main logic
final_output = process_pipeline(data, config)

# Output result
print(f"Target result: {final_output}")