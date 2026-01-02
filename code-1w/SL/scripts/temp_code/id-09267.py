def compute_integrity_score(data):
    # Irrelevant transformation: base conversion attempt
    encoded = []
    for x in data:
        if x % 2 == 0:
            encoded.append(x // 2)
        else:
            encoded.append(3 * x + 1)
    
    # Distractor: unused recursive function for summing powers
    def rec_power_sum(n, p):
        return 1 if n == 0 else n**p + rec_power_sum(n-1, p)
    
    # Unused variable: mimics cryptographic salt
    salt_value = 54321
    magic_factor = 7
    temp_result = 0
    
    # Real computation begins: simulate cyclic redundancy with bit mixing
    checksum = 0
    offset = 113
    sequence = [d % 256 for d in data if d > 0]  # Normalize to byte range
    
    # Dead code path: simulates alternative algorithm
    if len(sequence) > 100:
        fallback = sum(sequence) % 65536
        return fallback

    # Another red herring: enumerates but doesn't use index in meaningful way (at first)
    for i, val in enumerate(sequence):
        if i % 3 == 0:
            checksum += val
        elif i % 3 == 1:
            checksum = (checksum + (val << 1)) % 65536
        else:
            # This is the critical line — only matters in last iteration
            checksum = (checksum * 3) ^ sequence[i]
            
        # Decoy operation: looks like it affects checksum but uses local shadow
        checksum_temp = checksum + magic_factor
        
        # Additional distraction: zipping unrelated sequences
        indices = list(range(len(sequence)))
        for idx, (a, b) in enumerate(zip(sequence, indices)):
            if a == b and a < 10:
                temp_result ^= a

    # Final irrelevant adjustment
    final_mask = 0xFFFF
    checksum = checksum & final_mask
    
    # Output required result
    print(f"Result: {checksum}")

# Input data crafted so that only last iteration matters for answer
input_data = [12, -5, 45, 0, 192, 256, 7, 33, 89, 100, 55, 231]
compute_integrity_score(input_data)