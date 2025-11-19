def simulate_circuit(input_signal):
    # Apply initial transformation using bitwise operations
    stage1 = (input_signal << 2) & 0xFF  # Shift left by 2, mask to 8 bits
    
    # Apply logical conditions
    if (stage1 > 100) and not (stage1 & 0x0F == 0):  # Check if greater than 100 and lower nibble is non-zero
        stage2 = stage1 ^ 0x55  # XOR with 0x55
    else:
        stage2 = stage1 | 0xAA  # OR with 0xAA
    
    # Apply another transformation based on parity
    if (bin(stage2).count('1') % 2) == 0:  # Check if even parity
        stage3 = stage2 & 0xF0  # Mask upper nibble
    else:
        stage3 = stage2 | 0x0F  # Set lower nibble
    
    # Final adjustment using a lambda function
    adjust = lambda x: ((x >> 1) & 0x7F) if x > 128 else (x << 1)
    final_signal = adjust(stage3)
    
    return final_signal

# Simulate with input signal 0b11010110 (214 in decimal)
input_signal = 0b11010110
final_signal = simulate_circuit(input_signal)
print(f'Result: {final_signal}')