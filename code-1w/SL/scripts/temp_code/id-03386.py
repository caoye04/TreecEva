from itertools import combinations

def preprocess_data(entries):
    # Irrelevant transformation: convert all strings to uppercase
    processed = [entry.upper() for entry in entries if isinstance(entry, str)]
    return processed

def generate_pairs(items):
    # Distractor function: generates character pairs but not used in final logic
    return list(combinations(''.join(items), 2))

def calculate_final_score(raw_data):
    # Extract numeric values and ignore non-numeric
    numbers = [x for x in raw_data if isinstance(x, int) or isinstance(x, float)]
    
    # Track state with intermediate variables
    temp_results = {}
    temp_results['sum'] = sum(numbers)
    temp_results['count'] = len(numbers)
    
    # Compute average (used later)
    avg_val = temp_results['sum'] / temp_results['count'] if temp_results['count'] > 0 else 0
    
    # Apply weighting based on conditions
    weighted_vals = []
    for num in numbers:
        if num > avg_val:
            weighted_vals.append(num * 1.2)
        elif num == avg_val:
            weighted_vals.append(num * 1.0)
        else:
            weighted_vals.append(num * 0.85)
    
    # Secondary processing: count how many exceed threshold (semi-relevant)
    above_threshold = len([wv for wv in weighted_vals if wv > 50])
    
    # Real scoring logic: sum of weighted values multiplied by adjustment factor
    adjustment_factor = 0.9 if above_threshold > 2 else 1.1
    score_base = sum(weighted_vals)
    
    # Final computation
    final_score = score_base * adjustment_factor
    
    # Dead code path - never executed due to logic above
    if len(weighted_vals) == 0 and False:
        final_score = -999
        placeholder = [i ** 2 for i in range(10)]  # Unused list comprehension
    
    return final_score

def main():
    # Input data with mixed types (real and noise)
    raw_input = [23, 'hello', 45, 'world', 37, 52, 'test', 41, 39]
    
    # Preprocessing steps (some irrelevant)
    cleaned_strings = preprocess_data(raw_input)
    char_pairs = generate_pairs(cleaned_strings)  # Computed but unused
    
    # Core calculation
    final_score = calculate_final_score(raw_input)
    
    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()