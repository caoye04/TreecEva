def analyze_text_patterns(text_data):
    char_count = {}
    for char in text_data:
        if char.isalpha():
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    
    # Distractor: Unused frequency map
    frequency_map = {k: v / len(text_data) for k, v in char_count.items()}
    sorted_chars = sorted(char_count.keys())
    total_unique = len(sorted_chars)
    
    # Semi-relevant transformation
    weighted_sum = 0
    for i, c in enumerate(sorted_chars):
        weighted_sum += (i + 1) * char_count[c]
    
    return total_unique, weighted_sum


def calculate_efficiency(raw_input):
    # Misleading preprocessing
    cleaned = ''.join(filter(str.isalnum, raw_input)).upper()
    reversed_clean = cleaned[::-1]
    
    temp_values = []
    for i in range(len(reversed_clean)):
        if i % 2 == 0:
            temp_values.append(ord(reversed_clean[i]) - ord('A') + 1)
        else:
            temp_values.append((ord(reversed_clean[i]) - ord('0')) ** 2)
    
    # This sum is unused later — red herring
    dummy_sum = sum(x for x in temp_values if x > 5)
    
    # Actual relevant metric
    core_metric = sum(temp_values) // len(temp_values) if temp_values else 0
    return core_metric


def evaluate_performance(workload, defects):
    base = workload * 2.5
    penalty = 0
    
    if defects > 0:
        penalty = (defects ** 1.5) * 3
    
    result = base - penalty
    if result < 0:
        result = 0
    
    return int(result)

# Main execution block
input_string = "ReportGen_2024_Q2_Final_v2.pdf"

# Step 1: Text pattern analysis
unique_chars, pattern_score = analyze_text_patterns(input_string)

# Step 2: Efficiency calculation
efficiency_rating = calculate_efficiency(input_string)

# Step 3: Simulate performance metrics
productivity = efficiency_rating + unique_chars

# Distractor variables
redundant_flag = len(input_string) > 20
buffer_space = [0] * len(input_string)
temp_factor = None
for idx, ch in enumerate(input_string):
    if ch.isdigit():
        temp_factor = int(ch)
        break

errors = temp_factor or 3

# Key statement
final_score = evaluate_performance(productivity, errors)

print(f"Result: {final_score}")