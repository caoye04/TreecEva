from collections import defaultdict, Counter

def analyze_metrics(raw_data, thresholds):
    stats = defaultdict(float)
    counts = Counter()
    
    for key, values in raw_data.items():
        total = sum(values)
        count = len(values)
        avg = total / count if count > 0 else 0
        
        stats[f'{key}_mean'] = avg
        stats[f'{key}_total'] = total
        counts[key] = count
        
        # Irrelevant transformation (distractor)
        squared_devs = [(x - avg) ** 2 for x in values]
        variance = sum(squared_devs) / count if count > 0 else 0
        stats[f'{key}_variance'] = variance

    # Dummy logic with no impact on final result
    temp_results = []
    for k, v in stats.items():
        if 'total' in k:
            temp_results.append(v * 0.95)
    
    return stats, counts

def calculate_performance(data):
    # Primary computation path
    benchmark_stats, item_counts = analyze_metrics(data['sequences'], data['thresholds'])
    
    # Extract meaningful totals
    sequence_a_total = benchmark_stats.get('A_total', 0)
    sequence_b_total = benchmark_stats.get('B_total', 0)
    
    # Real calculation contributing to answer
    base_score = sequence_a_total * 1.5 + sequence_b_total * 0.8
    
    # Red herring: complex but unused scoring
    unused_scores = []
    for i in range(3):
        dummy_val = (base_score / (i + 1)) ** 0.5
        unused_scores.append(dummy_val)
    
    adjustment = len(item_counts) * 10
    
    # Final score depends only on base_score and adjustment
    final_score = int(base_score + adjustment)
    
    # Print required output format
    print(f"Result: {final_score}")
    return final_score

def main():
    # Input data
    benchmark_data = {
        'sequences': {
            'A': [4, 8, 12, 16],
            'B': [5, 10, 15],
            'C': [1, 2, 3]  # Unused in final score
        },
        'thresholds': {'min_val': 1, 'max_val': 20}
    }
    
    # Spurious variables (distractors)
    metadata_log = {'version': '2.1', 'run_id': 'xyz789'}
    debug_trace = [sum(vals) for seq, vals in benchmark_data['sequences'].items() if seq != 'C']
    
    # Key execution point
    final_score = calculate_performance(benchmark_data)

if __name__ == '__main__':
    main()