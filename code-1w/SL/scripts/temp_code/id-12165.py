def analyze_material_weights():
    raw_samples = [105, 213, 98, 412, 307, 199, 254]
    sample_codes = ['A7', 'B2', 'C9', 'D4', 'E1', 'F8', 'G6']
    
    # Extract numeric part from codes and pair with weights
    code_digits = [int(code[-1]) for code in sample_codes]
    paired_data = list(zip(raw_samples, code_digits))
    
    # Apply adjustment: divide weight by last digit if odd, else multiply by 2
    adjusted_weights = []
    for weight, digit in paired_data:
        if digit % 2 == 1:
            adjusted_weights.append(weight / digit)
        else:
            adjusted_weights.append(weight * 2)
    
    # Filter out any weight over 500 and round to nearest integer
    filtered_weights = [round(w) for w in adjusted_weights if w <= 500]
    
    # Further process: subtract index position from each weight
    processed_weights = [w - i for i, w in enumerate(filtered_weights)]
    
    total_weight = sum(processed_weights)
    return total_weight

result = analyze_material_weights()
print(f"Result: {result}")