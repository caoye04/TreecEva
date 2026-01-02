def compute_diagnostic_score():
    raw_data = [84, 92, 78, 99, 65, 88, 91]
    weights = [0.2, 0.3, 0.1, 0.4, 0.25, 0.15, 0.35]
    
    # Normalize data using modular arithmetic
    normalized = [(raw_data[i] + i) % 100 for i in range(len(raw_data))]
    
    # Apply weighted influence (only some elements are relevant)
    weighted_values = [normalized[i] * weights[i] for i in range(len(normalized))]
    
    # Checksum based on logical and bitwise operations
    checksum = 0
    for val in raw_data:
        if val > 80 and (val & 1):  # odd values greater than 80
            checksum += val % 13
    
    # Irrelevant distraction: secondary metric not used in result
    avg_normalized = sum(normalized) / len(normalized)
    deviation_score = abs(avg_normalized - 85)
    
    # Final score mapping
    final_scores = [10, 15, 20, 25, 30, 35, 40][::-1]  # reversed via slicing
    threshold = 75
    
    # Key computation step
    result = final_scores[checksum % 7] * (threshold // 10)
    
    print(f"Result: {result}")

compute_diagnostic_score()