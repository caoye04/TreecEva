def preprocess_data(raw):
    cleaned = [x.strip().lower() for x in raw if len(x.strip()) > 0]
    filtered = [x for x in cleaned if x.startswith('a') or x.startswith('b')]
    return filtered

def transform_entries(entries):
    encoded = []
    temp_sum = 0
    
    for entry in entries:
        length_val = len(entry)
        vowel_count = sum(1 for c in entry if c in 'aeiou')
        transformed = (length_val ** 2) - (vowel_count * 3)
        encoded.append(transformed)
        
        # Distractor: accumulating but not used later
        temp_sum += transformed + vowel_count
        
    # Irrelevant sorting
    encoded.sort(reverse=True)
    return encoded

def analyze_pattern(seq):
    if len(seq) < 3:
        return 0
    
    count_peaks = 0
    for i in range(1, len(seq) - 1):
        if seq[i] > seq[i-1] and seq[i] > seq[i+1]:
            count_peaks += 1
    
    # Dead code path (never used)
    if count_peaks == 0:
        fallback = sum(seq) // len(seq) if seq else 0
        return fallback
        
    return count_peaks

def calculate_final_score(input_data):
    valid_data = preprocess_data(input_data)
    numeric_vals = transform_entries(valid_data)
    
    # Real computation path
    base_score = sum(numeric_vals)
    peak_count = analyze_pattern(numeric_vals)
    adjustment_factor = len(numeric_vals) if numeric_vals else 1
    
    # Misleading intermediate calculations
    avg_val = sum(numeric_vals) / len(numeric_vals) if numeric_vals else 0
    squared_mean = avg_val ** 2
    noise_offset = sum(i * 2 for i in range(len(numeric_vals))) % 5  # irrelevant
    
    # Final score depends only on base_score, peak_count, and adjustment_factor
    final_score = (base_score + (peak_count * 10)) // adjustment_factor
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

# Input data
raw_input = [' Apple ', 'Banana', 'Cherry', 'Apricot', 'Blueberry', ' Avocado ', 'Cucumber']

# Execution
final_score = calculate_final_score(raw_input)