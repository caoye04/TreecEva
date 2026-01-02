from collections import defaultdict, Counter

def preprocess_records(records):
    processed = []
    temp_sum = 0
    
    for i, record in enumerate(records):
        if i % 2 == 0:
            temp_sum += sum(record)
        
        transformed = [x * 2 for x in record if x > 3]
        processed.append(transformed)
    
    # Irrelevant aggregation
    avg_temp = temp_sum / (len(records) // 2 + 1) if len(records) > 0 else 0
    return processed


def analyze_distribution(data):
    freq_map = defaultdict(int)
    total_elements = 0
    
    for row in data:
        for val in row:
            freq_map[val] += 1
            total_elements += 1
    
    # Misleading statistical computation
    if total_elements > 10:
        mean_val = sum(freq_map.keys()) / len(freq_map)
        variance_proxy = sum((k - mean_val) ** 2 for k in freq_map.keys()) / len(freq_map)
    else:
        mean_val = 0
        variance_proxy = 0
    
    return freq_map


def calculate_final_score(data):
    score = 0
    zero_count = 0
    
    for idx, group in enumerate(data):
        if len(group) > 0:
            # Core scoring logic
            base = sum(group)
            penalty = 0
            
            for val in group:
                if val % 4 == 0:
                    penalty += 1
            
            adjusted = base - penalty
            score += adjusted * (idx + 1)
        else:
            zero_count += 1
    
    # Distractor: unused complex expression
    correction_factor = (zero_count ** 2 + 1) if zero_count > 0 else 1
    
    return int(score)

# Main execution
raw_data = [
    [1, 5, 3, 8],
    [2, 6],
    [4, 7, 9],
    [3, 5, 12],
    [10]
]

processed_data = preprocess_records(raw_data)
frequencies = analyze_distribution(processed_data)
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")