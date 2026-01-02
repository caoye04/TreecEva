from itertools import permutations, cycle

def analyze_pattern(seq, threshold):
    count = 0
    temp_sum = 0
    for val in seq:
        if val > threshold:
            count += 1
            temp_sum += val
    return temp_sum if count >= 3 else 0

def apply_filter(data_stream, mode=1):
    filtered = []
    noise_floor = 15
    for x in data_stream:
        if mode == 1:
            if x & 1:  # odd values only
                filtered.append(x * 0.9)
        elif mode == 2:
            if x > noise_floor:
                filtered.append(x * 1.1)
    return [int(y) for y in filtered]

def process_transmission(raw_sequence, factor):
    # Step 1: Initial transformation with distractor logic
    shifted = [(x << 1) + 2 for x in raw_sequence]  # bit shift and offset (distractor)
    
    # Step 2: Use itertools to generate permutation-based checksum (only first used)
    perm_gen = permutations([shifted[0], shifted[1], shifted[2]], 3)
    checksum = sum(sum(p) % 10 for p in perm_gen) % 7
    
    # Step 3: Apply filter on original sequence
    cleaned = apply_filter(raw_sequence, mode=1)
    
    # Step 4: Analyze pattern on a transformed version
    amplified = [x * factor for x in raw_sequence]
    trigger = analyze_pattern(amplified, threshold=25)
    
    # Step 5: Conditional modification based on checksum and trigger
    if checksum > 3:
        adjustment = 4
    else:
        adjustment = -2
    
    # Step 6: Main signal computation
    base_signal = sum(cleaned) + trigger // 10
    final_signal = base_signal ^ adjustment  # XOR with adjustment (key operation)
    
    # Distractor variables and dead-end computations
    history_log = []
    for i in range(2):
        history_log.append(f"Entry_{i}")  # Irrelevant logging
    temp_cycle = cycle([1, 2])
    next(temp_cycle)  # Unused iterator
    
    return final_signal

# Main execution
signal_sequence = [8, 12, 22, 30, 16]
correction_factor = 1.8
misc_data = {"offset": 100, "limit": None}  # Unused structure

intermediate_result = [x ** 0.5 for x in signal_sequence]  # Computed but unused

final_signal = process_transmission(signal_sequence, correction_factor)
print(f"Result: {final_signal}")