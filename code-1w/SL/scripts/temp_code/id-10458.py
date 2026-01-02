from collections import defaultdict, Counter
import math

def analyze_distribution(values):
    count = Counter(values)
    total = len(values)
    entropy = 0
    for v in count.values():
        p = v / total
        entropy -= p * math.log2(p)
    return entropy

def normalize_weights(w):
    total = sum(w)
    return [x / total for x in w]

def filter_outliers(nums, threshold=2):
    mean = sum(nums) / len(nums)
    std = (sum((x - mean) ** 2 for x in nums) / len(nums)) ** 0.5
    return [x for x in nums if abs(x - mean) <= threshold * std]

def calculate_final_score(data, weight_map):
    # Extract sequences
    raw_sequence = [item['value'] for item in data]
    
    # Misleading intermediate: process categories but not used in final score
    category_map = defaultdict(list)
    for item in data:
        category_map[item['category']].append(item['value'])
    category_avg = {k: sum(v) / len(v) for k, v in category_map.items()}
    
    # Distractor: compute distribution entropy (not used)
    _ = analyze_distribution(raw_sequence)
    
    # Filter outliers from raw sequence
    cleaned_sequence = filter_outliers(raw_sequence)
    
    # Weighted scoring
    weighted_sum = 0
    for i, val in enumerate(cleaned_sequence):
        if i % 2 == 0:
            weighted_sum += val * weight_map.get('even_weight', 1.0)
        else:
            weighted_sum += val * weight_map.get('odd_weight', 0.8)
    
    # Apply scaling based on length retention
    retention_ratio = len(cleaned_sequence) / len(raw_sequence)
    adjusted_score = weighted_sum * retention_ratio
    
    # Extra distraction: simulate unused complexity
    temp_result = [x ** 2 for x in cleaned_sequence if x > 0]
    _ = sum(temp_result) / len(temp_result) if temp_result else 0
    
    # Final computation
    final_score = int(adjusted_score + 0.5)  # Round to nearest integer
    
    return final_score

# Main execution
if __name__ == '__main__':
    data_set = [
        {'value': 15, 'category': 'A'},
        {'value': 22, 'category': 'B'},
        {'value': 8, 'category': 'A'},
        {'value': 31, 'category': 'C'},
        {'value': 19, 'category': 'B'},
        {'value': 5, 'category': 'A'},
        {'value': 42, 'category': 'D'},  # outlier
        {'value': 17, 'category': 'B'}
    ]
    
    weights = {
        'even_weight': 1.2,
        'odd_weight': 0.9
    }
    
    # Unused variables and computations (distraction)
    summary_stats = {
        'max_val': max(item['value'] for item in data_set),
        'min_val': min(item['value'] for item in data_set),
        'range': None
    }
    summary_stats['range'] = summary_stats['max_val'] - summary_stats['min_val']
    
    # Key execution point
    final_score = calculate_final_score(data_set, weights)
    print(f"Target result: {final_score}")