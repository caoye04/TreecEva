import math
from collections import deque
def calculate_signal_sequence():
    # Initialize the sequence with given starting values
    signal_strength = [2, 3]
    
    # Generate the sequence up to 8 elements using the defined rule
    for i in range(2, 8):
        next_val = (signal_strength[i-1] + signal_strength[i-2]) * (i + 1)
        signal_strength.append(next_val)
    
    # Calculate mean and standard deviation for transformation
    n = len(signal_strength)
    mean_val = sum(signal_strength) / n
    variance = sum((x - mean_val) ** 2 for x in signal_strength) / n
    std_dev = math.sqrt(variance)
    
    # Apply transformation based on index parity
    transformed_signal = []
    for idx, val in enumerate(signal_strength, start=1):
        if idx % 2 == 0:  # Even index
            transformed_val = val - mean_val
        else:  # Odd index
            transformed_val = val + std_dev
        transformed_signal.append(transformed_val)
    
    return transformed_signal[7]

# Execute the function and print the result
final_value = calculate_signal_sequence()
print(f"Result: {final_value}")