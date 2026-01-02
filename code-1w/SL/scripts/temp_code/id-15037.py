def process_buffer(data, mode='fast'):
    # Irrelevant transformation chain (dead path)
    shadow_map = {i: (i * 3 + 7) % 256 for i in range(100)}
    temp_accum = sum(shadow_map[k] for k in shadow_map if k % 7 == 0)
    
    # Distractor: complex but unused computation
    entropy_pool = []
    for i in range(len(data)):
        if data[i] % 5 == 0:
            entropy_pool.append((data[i] ^ i) % 127)
    
    # Real processing begins here
    state = {'value': 1024, 'count': 0, 'history': []}
    
    for x in data:
        if x <= 0:
            continue
        # Modular arithmetic with bit manipulation
        transformed = (x ^ 0xAAAA) % 17
        if transformed % 3 == 0:
            state['value'] = (state['value'] + transformed * 2) % 9973
        elif transformed % 3 == 1:
            state['value'] = (state['value'] * (transformed + 1)) % 9973
        else:
            state['value'] = (state['value'] + (transformed ^ 5)) % 9973
        
        state['count'] += 1
        state['history'].append(state['value'])
    
    # Sorting irrelevant data (distractor)
    sorted_entropy = sorted(entropy_pool, reverse=True) if entropy_pool else [0]
    decoy_result = sum(sorted_entropy[i] * (i+1) for i in range(len(sorted_entropy)))

    # Recursion for hash finalization (actual logic)
    def finalize_hash(s):
        if s['count'] == 0:
            return 1
        if s['count'] == 1:
            return s['value'] * 2
        # Recursive reduction on history
        def reduce(seq):
            if len(seq) <= 1:
                return seq[0] if seq else 1
            mid = len(seq) // 2
            left = reduce(seq[:mid])
            right = reduce(seq[mid:])
            return (left * 3 + right * 2 + 7) % 9973
        
        recursive_contribution = reduce(s['history'])
        return (s['value'] + recursive_contribution) % 9973

    # Unused function (red herring)
    def validate_integrity(buf):
        return sum(buf) % 256 == 0

    # Critical statement
    checksum = finalize_hash(state)
    
    # Print result as required
    print(f"Result: {checksum}")

# Input data with meaningful structure
input_data = [12, 25, 38, 41, 50, 63, 76, 89, 92, 105, 118, 131, 144, 157, 170]
process_buffer(input_data)