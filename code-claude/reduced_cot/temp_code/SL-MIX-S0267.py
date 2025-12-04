import itertools

# Satellite signal processing algorithm
def calculate_error(signal, offset):
    # Error calculation for signal alignment
    return sum((s - offset) ** 2 for s in signal)

# Main signal processing function
def process_signal_batch(signals):
    # Primary signals from three different satellites
    primary_signals = [4, 7, 9, 3, 5]
    secondary_signals = [2, 8, 6, 1, 7]
    tertiary_signals = [5, 3, 8, 2, 6]
    
    # Combined signal processing
    combined_primary = primary_signals[1:4]  # Extract subset of primary signals
    reversed_secondary = secondary_signals[::-1]  # Reverse secondary signals
    
    # Calculate potential offset values
    potential_offsets = list(range(-3, 8))
    reference_value = sum(combined_primary) // len(combined_primary)
    
    # Process all signals with various offsets
    error_values = []
    effective_values = []
    
    # Generate test combinations
    test_combinations = list(itertools.product([0, 1], repeat=3))
    selected_combination = test_combinations[4]  # Using specific combination
    
    # Apply selected processing mode
    processed_signal = []
    for i in range(len(primary_signals)):
        if i < len(primary_signals) - 2:  # Avoid index error
            weighted_value = primary_signals[i] * 0.6 + secondary_signals[i] * 0.4
            processed_signal.append(round(weighted_value))
        else:
            processed_signal.append(primary_signals[i])
    
    # Calculate error values for different offsets
    for offset in potential_offsets:
        calibration_factor = offset + selected_combination[1]  # Add combination factor
        error = calculate_error(processed_signal, calibration_factor)
        
        # Store values for analysis
        error_values.append(error)
        effective_values.append(offset)
    
    # Find offset with minimum error
    min_error = min(error_values)
    min_error_idx = error_values.index(min_error)
    
    # Determine optimal offset
    optimal_offset = effective_values[min_error_idx]
    
    # Apply some additional processing that doesn't affect the result
    alternative_approach = sum(tertiary_signals) / len(tertiary_signals)
    hybrid_offset = (optimal_offset + alternative_approach) / 2
    
    print(f"Result: {optimal_offset}")
    return optimal_offset

# Process a batch of signals
result = process_signal_batch([1, 2, 3, 4, 5])