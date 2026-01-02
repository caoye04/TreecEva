def compute_integrity_score(sequence):
    n = len(sequence)
    base_offset = 23
    temp_buffer = [0] * n
    accumulator = 0
    
    # Initialize buffer with transformed ASCII values
    for i in range(n):
        temp_buffer[i] = (ord(sequence[i]) + base_offset) % 91
        if temp_buffer[i] % 2 == 0:
            accumulator += temp_buffer[i] // 2
        else:
            accumulator -= temp_buffer[i] // 3

    # Misleading secondary processing (dead-end path)
    shadow_copy = temp_buffer[::-1]  # reversed, unused later
    for j in range(len(shadow_copy)):
        shadow_copy[j] = (shadow_copy[j] * 2) ^ 5  # irrelevant transformation

    # Actual computation path
    checksum = 17
    for k in range(1, n + 1):
        segment = sequence[:k]  # slicing used
        length_factor = len(segment)
        ascii_sum = sum(ord(c) for c in segment)
        intermediate = (ascii_sum * length_factor + k) % 89
        
        # Core update step — target execution point here
        checksum = (checksum * 3) % 97
        checksum = (checksum + intermediate) % 97
    
    # Distractor: complex but unused combinatorics
    def count_palindromic_substrings(s):
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    count += 1
        return count
    
    # Final red herring calculation
    pal_count = count_palindromic_substrings(sequence)
    adjustment = pal_count % 10 if pal_count > 10 else 0
    checksum = (checksum - adjustment) % 97  # minor adjustment, still deterministic

    print(f"Result: {checksum}")
    return checksum

# Execute with fixed input
compute_integrity_score("Crypt0")