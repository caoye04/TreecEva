from collections import Counter, defaultdict

def analyze_frequency(text):
    # Irrelevant helper function for string analysis (not used in final result)
    words = text.lower().split()
    return Counter(words)

def extract_numeric_patterns(data_list):
    # Extract numbers but with some distractions
    temp_result = []
    for item in data_list:
        if isinstance(item, str) and item.isdigit():
            temp_result.append(int(item))
        elif isinstance(item, int):
            temp_result.append(item * 2)  # Distraction: double integers (not actually needed)
    return temp_result

def filter_and_transform(values):
    # Actual core logic hidden among noise
    valid_numbers = [v for v in values if v > 0]  # Only positive values matter
    squared_evens = [x**2 for x in valid_numbers if x % 2 == 0]
    shifted_odds = [(x + 1) for x in valid_numbers if x % 2 == 1]
    combined = squared_evens + shifted_odds
    return sorted(combined)

def calculate_adjusted_score(data):
    # Core scoring logic
    base_sum = sum(data)
    penalty = len([x for x in data if x < 10]) * 2
    bonus = len([x for x in data if x > 20]) * 3
    raw_score = base_sum + bonus - penalty
    adjustment_factor = 0.95
    return int(raw_score * adjustment_factor)

# Main execution flow
raw_input = ['5', '12', 'abc', '25', '8', '30', 'xyz', '15']

# Step 1: Use string methods to clean input
filtered_strings = [s.strip() for s in raw_input if isinstance(s, str) and s.strip().isdigit()]
distraction_text = "The quick brown fox jumps over the lazy dog"
word_freq = analyze_frequency(distraction_text)  # Dead-end computation

# Step 2: Convert to mixed-type list with irrelevant transformations
intermediate_values = [int(x) for x in filtered_strings]
doubled_ints = [x * 2 for x in intermediate_values]  # Distractor list

# Step 3: Extract and process numerics (with misleading path)
extracted = extract_numeric_patterns(raw_input)  # Includes doubled ints (misleading)

# Step 4: Filter and transform the correct dataset
processed_data = filter_and_transform(intermediate_values)

# Step 5: Calculate final score from processed data
final_score = calculate_adjusted_score(processed_data)

# Output result
print(f"Result: {final_score}")