def analyze_trend(values):
    trend = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            trend += 1
        elif values[i] < values[i-1]:
            trend -= 1
    return trend

# Irrelevant helper function (dead code path)
def unused_normalization(arr):
    total = sum(arr)
    return [x / total for x in arr] if total != 0 else arr

def calculate_entropy(counts):
    from math import log2
    total = sum(counts.values())
    entropy = 0.0
    for count in counts.values():
        if count > 0:
            p = count / total
            entropy -= p * log2(p)
    return round(entropy, 4)

def calculate_final_score(data, weights):
    # Track state across multiple steps
    temp_results = {}
    
    # Step 1: Count occurrences of each category
    category_counts = {k: 0 for k in data.keys()}
    for key in data:
        category_counts[key] += len(data[key])
    
    # Misleading intermediate calculation (not used later)
    avg_length = sum(len(v) for v in data.values()) / len(data) if data else 0
    dummy_flag = avg_length > 5
    
    # Step 2: Analyze trend in first series
    first_series = data.get('A', [])
    trend_value = analyze_trend(first_series)
    
    # Step 3: Compute entropy of distribution
    entropy = calculate_entropy(category_counts)
    
    # Step 4: Apply weights to selected metrics
    weighted_trend = trend_value * weights.get('trend', 0)
    weighted_entropy = entropy * weights.get('entropy', 1.5)
    
    # Step 5: Use dictionary operations for aggregation
    temp_results['trend'] = weighted_trend
    temp_results['entropy'] = weighted_entropy
    temp_results['base_count'] = category_counts.get('A', 0) * 2
    
    # Final score computation (key execution point)
    final_score = 0
    for key, value in temp_results.items():
        if key == 'trend':
            final_score += value * 1.1
        elif key == 'entropy':
            final_score += value * 2.0
        else:
            final_score += value
    
    # Extra distraction: unused transformation
    transformed = {k: v * 1.5 for k, v in category_counts.items()}
    total_transformed = sum(transformed.values())
    adjustment = total_transformed % 7 if total_transformed > 0 else 0
    
    # Return final score without using adjustment (red herring)
    return int(round(final_score))

# Main execution
if __name__ == '__main__':
    data = {
        'A': [3, 5, 7, 8, 6],
        'B': [2, 4, 6],
        'C': [1, 9],
        'D': [5, 5, 5]
    }
    weights = {
        'trend': 3,
        'entropy': 2
    }
    
    # Extraneous precomputation
    total_elements = sum(len(v) for v in data.values())
    max_length_key = max(data, key=lambda k: len(data[k]))
    
    final_score = calculate_final_score(data, weights)
    print(f"Result: {final_score}")