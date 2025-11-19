import math

def signal_filter_optimizer(raw_coefficients):
    # Initialize DP table
    dp_table = {i: 0 for i in range(len(raw_coefficients) + 1)}
    
    # Encoding transformation using lambda
    encode = lambda x, i: round(x * math.sin(i * 0.1) + math.cos(i * 0.2), 3)
    
    # Dictionary comprehension for coefficient storage
    encoded_coeffs = {i: encode(coeff, i) for i, coeff in enumerate(raw_coefficients)}
    
    # Dynamic programming to find optimal filter path
    for i in range(1, len(raw_coefficients) + 1):
        dp_table[i] = max(dp_table[i-1], dp_table[i-1] + encoded_coeffs[i-1])
    
    # Calculate final gain using bit manipulation on DP result
    optimal_gain = int(dp_table[len(raw_coefficients)] * 1000) & 0xFF
    return optimal_gain

# Signal processing coefficients
coeffs = [1.2, -0.5, 0.8, -1.0, 1.5]
result = signal_filter_optimizer(coeffs)
print(f"Result: {result}")