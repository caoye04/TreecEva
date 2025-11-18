def process_bioacoustic_signals():
    # Initialize Fibonacci sequence generator
    def fibonacci_sequence(n):
        a, b = 0, 1
        for _ in range(n):
            yield a
            a, b = b, a + b
    
    # Signal registry with initial values
    signal_registry = {
        'alpha': 15,
        'beta': 24,
        'gamma': 9
    }
    
    # Process signals using Fibonacci weights
    fib_weights = list(fibonacci_sequence(6))
    
    # Apply weighted transformations with short-circuit evaluation
    transformed_signals = {}
    for i, (key, value) in enumerate(signal_registry.items()):
        if key != 'delta' and value > 10:
            weighted_value = value * fib_weights[i] if i < len(fib_weights) else value
            transformed_signals[key] = weighted_value >> 1  # Right shift by 1 (equivalent to divide by 2)
        else:
            transformed_signals[key] = value << 1  # Left shift by 1 (equivalent to multiply by 2)
    
    # Calculate harmonic distortion using set operations
    original_keys = frozenset(signal_registry.keys())
    processed_keys = set(transformed_signals.keys())
    
    # Merge dictionaries with comprehension
    merged_registry = {k: signal_registry.get(k, 0) + transformed_signals.get(k, 0) 
                      for k in original_keys | processed_keys}
    
    # Apply lambda function for final distortion calculation
    distortion_calculator = lambda x, y: (x ** 2 + y ** 2) // (x + y) if x + y != 0 else 0
    
    # Calculate final metric using nested arithmetic operations
    harmonic_components = [
        distortion_calculator(merged_registry.get('alpha', 0), merged_registry.get('beta', 0)),
        distortion_calculator(merged_registry.get('gamma', 0), merged_registry.get('beta', 0)),
        sum(fib_weights[:4])
    ]
    
    # Final harmonic distortion metric
    harmonic_distortion_metric = (
        harmonic_components[0] * harmonic_components[1] + 
        harmonic_components[2] - 
        (max(signal_registry.values()) & min(transformed_signals.values()))  # Bitwise AND operation
    )
    
    return harmonic_distortion_metric

# Execute the bioacoustic signal processing
harmonic_distortion_metric = process_bioacoustic_signals()
print(f"Result: {harmonic_distortion_metric}")