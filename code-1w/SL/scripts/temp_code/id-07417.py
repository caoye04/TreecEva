from collections import defaultdict, Counter

# Simulate industrial batch processing with quality control and yield optimization
def analyze_batch_composition(batch):
    element_count = defaultdict(int)
    impurities = []
    total_elements = 0

    for item in batch:
        category = item % 5
        if category == 0:
            element_count['alpha'] += 1
        elif category == 1:
            element_count['beta'] += 1
        elif category in (2, 3):
            impurities.append(item)
        else:
            element_count['gamma'] += 1
        total_elements += 1

    purity_score = (total_elements - len(impurities)) / total_elements if total_elements > 0 else 0
    return dict(element_count), purity_score, impurities

def compute_stability_factor(history):
    trend = [abs(history[i] - history[i-1]) for i in range(1, len(history))] if len(history) > 1 else [0]
    avg_fluctuation = sum(trend) / len(trend)
    stability = 1 / (1 + avg_fluctuation)
    
    # Distractor computation: irrelevant to final result
    hypothetical_cases = [x * 0.95 for x in history]
    adjusted_baseline = sum(hypothetical_cases) / len(hypothetical_cases) if hypothetical_cases else 0
    
    return stability, adjusted_baseline  # Only stability is used later

def calculate_optimal_yield(data_map):
    raw_entries = data_map.get('entries', [])
    historical_performance = data_map.get('history', [])
    
    # Irrelevant transformation
    normalized_entries = [x // 3 + 1 for x in raw_entries if x > 0]
    entry_counter = Counter(normalized_entries)
    
    # Real processing begins
    batch_results = []
    for i in range(0, len(raw_entries), 7):  # Process in chunks of 7
        chunk = raw_entries[i:i+7]
        composition, purity, _ = analyze_batch_composition(chunk)
        alpha = composition.get('alpha', 0)
        beta = composition.get('beta', 0)
        gamma = composition.get('gamma', 0)
        
        if purity < 0.6:
            yield_contribution = (alpha + beta) * 0.8
        else:
            yield_contribution = (alpha * 1.2) + (beta * 0.9) + (gamma * 1.5)
        
        batch_results.append(yield_contribution)
    
    # Aggregate batch results
    total_theoretical = sum(batch_results)
    
    # Apply stability correction
    stability_factor, _ = compute_stability_factor(historical_performance)
    adjusted_yield = total_theoretical * stability_factor
    
    # Final adjustment based on threshold logic
    if adjusted_yield > 50:
        adjusted_yield *= 0.92
    elif adjusted_yield > 30:
        adjusted_yield *= 0.96
    else:
        adjusted_yield *= 1.0
    
    # Misleading intermediate calculation (dead end)
    shadow_projection = sum([x ** 0.5 for x in historical_performance]) * 1.1
    projected_loss_rate = (shadow_projection / (adjusted_yield + 1)) * 0.05
    
    return round(adjusted_yield, 4)

# Main execution block
if __name__ == '__main__':
    process_data = {
        'entries': [23, 15, 8, 12, 5, 19, 4, 7, 14, 3, 11, 6, 9],
        'history': [4.2, 4.6, 4.1, 4.8, 4.4, 4.7, 4.3],
        'metadata': {
            'version': '2.1',
            'calibration_offset': 0.03,
            'detection_threshold': 0.85
        }
    }

    # Distractor variables
    temp_analysis = [x * 2 for x in process_data['history']]
    baseline_shift = sum(temp_analysis) / len(temp_analysis)
    reference_matrix = [[i + j for j in range(3)] for i in range(3)]
    
    # Key statement
    final_yield = calculate_optimal_yield(process_data)
    
    print(f"Result: {final_yield}")