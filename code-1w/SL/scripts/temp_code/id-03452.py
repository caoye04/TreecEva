def calculate_performance(data):
    base = len(data)
    valid_entries = 0
    total_value = 0.0
    
    # Filter valid entries based on format (e.g., non-empty strings with digits)
    for entry in data:
        if isinstance(entry, str) and entry.strip().isdigit():
            valid_entries += 1
            total_value += int(entry)
    
    # Compute average of valid numeric entries
    avg_value = total_value / valid_entries if valid_entries > 0 else 0
    
    # Apply performance multiplier based on data quality ratio
    quality_ratio = valid_entries / base if base > 0 else 0
    multiplier = 1.5 if quality_ratio >= 0.7 else 1.1
    
    # Final score calculation
    final_score = avg_value * multiplier
    
    # Irrelevant distraction: counting uppercase letters (not used in logic)
    dummy_count = sum(1 for s in data if isinstance(s, str) and s.isupper())
    
    return final_score

# Input dataset
input_data = ['100', '200', 'abc', '300', '', '400', '500']

result = calculate_performance(input_data)
print(f"Result: {result}")