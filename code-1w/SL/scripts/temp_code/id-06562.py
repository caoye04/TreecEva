from collections import defaultdict

def preprocess_items(raw_data, filter_threshold=3):
    processed = []
    temp_sum = 0
    
    for i, val in enumerate(raw_data):
        if val > filter_threshold:
            processed.append((i, val ** 2))
            temp_sum += val
    
    return processed

def calculate_total_weight(items):
    weights = defaultdict(float)
    total_weight = 0.0
    
    for index, value in items:
        if index % 2 == 0:
            weights[index] = value * 0.8
        else:
            weights[index] = value * 1.2
    
    for w in weights.values():
        total_weight += w
    
    return total_weight

def analyze_distribution(data):
    # Irrelevant helper function for diversity (distractor)
    freq = defaultdict(int)
    for x in data:
        freq[x] += 1
    return freq

# Main execution
raw_input = [2, 4, 5, 6, 3, 7]
processed_items = preprocess_items(raw_input)

# Key statement
total_weight = calculate_total_weight(processed_items)

Result: {total_weight}