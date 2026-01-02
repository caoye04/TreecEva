def generate_key_schedule(seed):
    return [(seed * i + 31) % 256 for i in range(1, 9)]

fragments = [
    [104, 101, 108, 108, 111],
    [119, 111, 114, 108, 100],
    [103, 111, 111, 100, 98],
    [108, 117, 99, 107, 33]
]

# Irrelevant transformation (dead-end path)
shadow_map = list(map(lambda x: sum(v ** 0.5 for v in x if v > 100), fragments))

# Misleading intermediate computations
offsets = [sum(fragment) % 256 for fragment in fragments]
temp_weights = [abs(off - 128) for off in offsets]

key_schedule = generate_key_schedule(17)

# Core processing with lambda and modular arithmetic
def process_fragments(frags, keys):
    result = 0
    for i, frag in enumerate(frags):
        block_sum = 0
        for j, val in enumerate(frag):
            # Case conversion mimicry via arithmetic modulation
            masked = val ^ keys[j % len(keys)]  # Bitwise interference
            adjusted = (masked + (i * j)) % 256
            if adjusted > 128:
                adjusted = 256 - adjusted  # Inversion logic
            block_sum += adjusted
        block_sum = (block_sum * (i + 1)) % 65536
        
        # Distractor: unused conditional branch
        if block_sum < 100:
            block_sum = (block_sum + 50) % 65536  # Never triggers
            
        result ^= block_sum
    
    # Final non-linear transform with lambda
    finalizer = lambda x: (x ^ (x >> 4) ^ (x << 3)) & 0xFFFF
    return finalizer(result) % 100000

checksum = process_fragments(fragments, key_schedule)

# Extra red herring variables
entropy_proxy = sum(offsets) * len(key_schedule)
symbol_table = {i: chr(65 + (i % 26)) for i in range(20)}

print(f"Result: {checksum}")