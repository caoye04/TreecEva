from itertools import combinations

def preprocess_input(raw_values):
    # Transform input through multiple steps
    normalized = [x % 100 for x in raw_values if x > 0]
    filtered = [x for x in normalized if x % 2 == 0]
    sorted_vals = sorted(filtered, reverse=True)
    return sorted_vals


def analyze_patterns(seq):
    # Find all 3-element subsequences with decreasing values
    count = 0
    for combo in combinations(seq, 3):
        if combo[0] > combo[1] > combo[2]:
            count += 1
    return count


def calculate_entropy(values):
    # Irrelevant helper function (dead code path)
    import math
    if len(values) == 0:
        return 0.0
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * math.log(prob)
    return round(entropy, 4)


def calculate_final_score(data):
    base_score = sum(data)
    pattern_bonus = analyze_patterns(data) * 10
    
    # Apply transformations with distractor variables
    temp_result = 0
    running_sum = 0
    for i in range(len(data)):
        if i % 2 == 0:
            temp_result += data[i] * 2
        else:
            temp_result -= data[i]
            
    adjustment_factor = len(data) // 2 if len(data) > 2 else 1
    
    # Dummy tracking variables (not used in final result)
    max_seen = max(data) if data else 0
    min_seen = min(data) if data else 0
    avg_temp = temp_result / len(data) if data else 0
    
    # Final computation
    final_score = base_score + pattern_bonus - adjustment_factor
    
    # Additional irrelevant bitwise manipulation
    mask = 0b1101
    masked_score = final_score ^ mask & 0xF
    
    return final_score

# Main execution
raw_input_data = [150, -5, 98, 42, 67, 88, 13, 54, 72, -10, 91]
processed_data = preprocess_input(raw_input_data)

# Extraneous slicing and character counting distraction
subset_slice = processed_data[1:6]
distraction_text = "Analysis Report Q3"
char_count = len(distraction_text.replace(" ", ""))

# Another unused recursive helper
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")