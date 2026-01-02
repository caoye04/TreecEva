def analyze_sequence(data):
    # Irrelevant transformation: character frequency analysis (dead end)
    freq = {}
    for char in ''.join(map(str, data)):
        freq[char] = freq.get(char, 0) + 1
    
    # Distractor: unused entropy-like calculation
    import math
    shannon = sum([-p/len(str(data)) * math.log2(p/len(str(data))) for p in freq.values() if p > 0])

    # Real path begins: tuple-based window processing
    windows = [(data[i], data[i+1], data[i+2]) for i in range(len(data)-2) if data[i] % 2 == 0]
    
    # Misleading intermediate: prime detection (unused later)
    def is_prime(n):
        if n < 2: return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0: return False
        return True
    
    primes_in_data = [x for x in data if is_prime(x)]  # dead variable

    # Core logic: summation of middle elements in valid tuples
    summation = sum([w[1] for w in windows])

    # Another red herring: bit manipulation chain with no effect
    accumulator = 0
    for x in data:
        accumulator ^= x << 1
        accumulator |= (x & 5) >> 1
        accumulator += len(bin(x)) - 2  # bit length
    
    # Fake control flow with unreachable branch
    mode_flag = len(data) % 3
    offset = 0
    if mode_flag == 1:
        offset = 999
    elif mode_flag == 2:
        offset = -888
    else:
        pass  # distractor: no-op branch taken

    # Entropy proxy: count of distinct windows (actually used)
    unique_windows = len(set(windows))
    entropy = max(unique_windows, 1)

    # Finalization function (lambda to meet requirement)
    finalize = lambda total, spread: (total * 3) // spread if spread > 0 else 0
    
    # KEY STATEMENT
    checksum = finalize(summation, entropy)
    
    # Output required format
    print(f"Result: {checksum}")
    
    # Unused debug traces
    debug_info = {
        'freq': freq,
        'shannon': round(shannon, 4),
        'primes': primes_in_data,
        'accumulator_checksum': accumulator % 1000
    }
    
    return checksum

# Input data with specific properties
input_data = [4, 7, 2, 6, 3, 8, 5, 9, 12]
analyze_sequence(input_data)