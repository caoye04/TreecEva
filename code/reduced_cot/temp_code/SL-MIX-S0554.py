def fibonacci_sequence(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

fabric_patterns = ['A1B2', 'C3D4', 'E5F6']
char_weights = fibonacci_sequence(16)
quality_score = 0

for pattern_idx, pattern in enumerate(fabric_patterns):
    pattern_checksum = 0
    for char_idx, char in enumerate(pattern):
        ascii_val = ord(char)
        weight = char_weights[char_idx]
        pattern_checksum += ascii_val * weight
    
    if pattern_checksum % 2 == 0:
        quality_score += pattern_checksum // 2
    else:
        quality_score += pattern_checksum * 3 + 1

print(f"Result: {quality_score}")