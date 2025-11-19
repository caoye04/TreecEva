import math

def signal_processing_optimizer(signal_data):
    n = len(signal_data)
    dp_table = [0] * (n + 1)
    
    # Initialize base cases
    dp_table[0] = 0
    if n > 0:
        dp_table[1] = abs(signal_data[0])
    
    # Dynamic programming recurrence
    for i in range(2, n + 1):
        # Current signal contribution
        current_signal = abs(signal_data[i-1])
        
        # Option 1: Take current signal plus best from two steps back
        option1 = current_signal + dp_table[i-2] if i >= 2 else current_signal
        
        # Option 2: Skip current signal, take previous best
        option2 = dp_table[i-1]
        
        # Store optimal choice
        dp_table[i] = max(option1, option2)
    
    return dp_table[n]

def adaptive_filter_coefficient(noise_profile):
    # Apply mathematical transformation to noise profile
    transformed = [math.log(abs(x) + 1) for x in noise_profile if x != 0]
    
    # Short-circuit evaluation for early termination
    if not transformed or all(x < 0.001 for x in transformed):
        return 0
    
    # Calculate coefficient using dynamic programming
    coefficient = signal_processing_optimizer(transformed)
    return coefficient

# Main execution
interference_signals = [3, -1, 4, -1, 5, 9, -2, 6, 5, 3, 5]

# Process primary noise cancellation
primary_attenuation = adaptive_filter_coefficient(interference_signals)

# Apply secondary enhancement using matrix operations
enhancement_matrix = [[0.8, 0.2], [0.3, 0.7]]
signal_vector = [primary_attenuation, sum(interference_signals)]

# Matrix-vector multiplication for enhanced attenuation
enhanced_attenuation = sum(enhancement_matrix[0][j] * signal_vector[j] for j in range(len(signal_vector)))

# Final optimization with conditional logic
optimal_attenuation = enhanced_attenuation if enhanced_attenuation > primary_attenuation else primary_attenuation + 1.5

print(f"Result: {round(optimal_attenuation, 4)}")