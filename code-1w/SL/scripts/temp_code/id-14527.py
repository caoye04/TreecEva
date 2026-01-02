def analyze_frequency(bands):
    # Irrelevant frequency analysis with decoy computations
    avg = sum(bands) / len(bands)
    deviation = sum(abs(b - avg) for b in bands) / len(bands)
    normalized = [round((b - avg) / deviation * 100) for b in bands]
    return normalized

# Decoy signal data and unused transformation chains
raw_readings = [0.87, 1.02, 0.93, 1.11, 0.76]
bands = [int(x * 100) for x in raw_readings]
freq_analysis = analyze_frequency(bands)

# Unused but plausible-looking correction algorithm
apply_correction = lambda x, c: x + (c * 0.05) if x < 95 else x - (c * 0.02)

correction_map = {k: apply_correction(v, 2) for k, v in enumerate(freq_analysis)}

# Real processing chain begins here — heavily masked by prior noise
signal_chain = [3, 7, -2, 8, 5, 1, 9, 4]
key_threshold = 6

filter_critical = lambda val: val > 0 and (val & (val - 1)) == 0  # Power of two check

# Simulate packet validation (distractor)
def validate_packet(seq):
    total = 0
    for x in seq:
        if x < 0:
            total -= x
        elif x % 3 == 0:
            total += x * 2
    return total  # Never actually used

# Unused recursive red herring
def decode_recursive(arr, idx=0, acc=0):
    if idx >= len(arr):
        return acc
    if arr[idx] % 2 == 0:
        return decode_recursive(arr, idx + 1, acc ^ arr[idx])
    else:
        return decode_recursive(arr, idx + 1, acc + arr[idx])

# Core logic disguised among distractions
def process_transmission(chain, threshold):
    # Step 1: filter positive values
    filtered = [x for x in chain if x > 0]
    
    # Step 2: square each value
    squared = [x ** 2 for x in filtered]
    
    # Step 3: mask with bitwise XOR using threshold
    masked = [x ^ threshold for x in squared]
    
    # Step 4: apply modulo wrap to simulate signal bounce
    wrapped = [x % 100 for x in masked]
    
    # Step 5: extract only powers of two
    power_of_two = [x for x in wrapped if filter_critical(x)]
    
    # Step 6: find max or default to 1
    candidate = max(power_of_two) if power_of_two else 1
    
    # Step 7: multiply by length of original chain (not filtered)
    result = candidate * len(chain)
    
    # Step 8: final adjustment based on threshold parity
    if threshold % 2 == 0:
        result -= 5
    else:
        result += 3
        
    return result

# Critical execution point
final_signal = process_transmission(signal_chain, key_threshold)

# Output the target result
print(f"Result: {final_signal}")