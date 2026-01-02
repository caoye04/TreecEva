from collections import Counter
def calculate_final_score(raw_data):
    # Preprocess data: filter valid entries and count frequencies
    valid_entries = [x for x in raw_data if 10 <= x <= 100]
    counts = Counter(valid_entries)
    
    # Compute base score using frequency-weighted sum
    base_score = sum(key * freq for key, freq in counts.items())
    
    # Apply adjustment based on distribution skew
    unique_count = len(counts)
    adjustment = base_score // (unique_count + 1) if unique_count > 3 else base_score // 2
    
    # Final nonlinear transformation
    final_score = (base_score - adjustment) ** 0.5
    return int(final_score)

# Input data with mixed valid and invalid values
data = [15, 20, 25, 15, 30, 20, 8, 105, 35, 35, 40]
final_score = calculate_final_score(data)
print(f"Result: {final_score}")