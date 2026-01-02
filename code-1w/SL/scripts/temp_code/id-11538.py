def calculate_weighted_harmonics():
    # Simulate sensor weights and harmonic frequency response
    weights = [0.8, 1.2, 0.5, 1.6, 0.9]
    frequencies = [50, 60, 100, 120, 400]  
    harmonics = []
    
    for freq in frequencies:
        if freq <= 60:
            harmonics.append(1.0)
        elif freq <= 120:
            harmonics.append(0.75)
        else:
            harmonics.append(0.4)

    # Irrelevant auxiliary variable (minimal distraction)
    avg_frequency = sum(frequencies) / len(frequencies)
    
    # Key computation using zip and generator expression
    total_harmonic_weight = sum(weights[i] * harmonics[i] for i in range(len(weights)))
    
    # Print result as required
    print(f"Result: {total_harmonic_weight}")

    return total_harmonic_weight

# Execute function
result = calculate_weighted_harmonics()