from collections import defaultdict

# Simulate industrial batch processing with quality filtering and efficiency calculation
def preprocess_batches(raw_inputs):
    processed = []
    temp_log = defaultdict(int)
    for item in raw_inputs:
        if item['temp'] < 80 and item['purity'] >= 0.85:
            adjusted_yield = item['base_yield'] * (1 + item['catalyst_efficiency'])
            temp_log['qualified'] += 1
            processed.append({
                'id': item['id'],
                'yield': adjusted_yield,
                'grade': 'A' if adjusted_yield > 90 else 'B'
            })
        else:
            temp_log['rejected'] += 1  # distractor: logged but not used later
    return processed

def filter_high_grade(loads):
    high_grade = [load for load in loads if load['grade'] == 'A']
    low_grade_count = len(loads) - len(high_grade)  # semi-relevant, not directly used
    return sorted(high_grade, key=lambda x: x['yield'], reverse=True)

def calculate_optimal_yield(enriched_data):
    peak_yields = [entry['yield'] for entry in enriched_data]
    cumulative = 0
    decay_factor = 0.95
    for i, yld in enumerate(peak_yields):
        if i % 2 == 0:
            cumulative += yld * decay_factor ** i
        else:
            cumulative -= yld * 0.05  # minor penalty on odd indices
    adjustment = len(peak_yields) * 0.1
    final_yield = int(cumulative - adjustment)  # deterministic integer result
    
    # Distractor computations below
    dummy_sum = sum((x * 1.01 for x in peak_yields if x > 100))  # irrelevant generator
    metadata_snapshot = {'entries': len(peak_yields), 'version': '2.1a'}  # unused dict
    overflow_flag = False
    for val in peak_yields:
        if val > 150:
            overflow_flag = True  # dead logic path
            break
    
    return final_yield

# Input data - fixed seed for determinism
raw_batch_data = [
    {'id': 'B001', 'base_yield': 85, 'temp': 78, 'purity': 0.87, 'catalyst_efficiency': 0.12},
    {'id': 'B002', 'base_yield': 95, 'temp': 85, 'purity': 0.90, 'catalyst_efficiency': 0.08},
    {'id': 'B003', 'base_yield': 88, 'temp': 75, 'purity': 0.92, 'catalyst_efficiency': 0.10},
    {'id': 'B004', 'base_yield': 92, 'temp': 79, 'purity': 0.86, 'catalyst_efficiency': 0.15},
    {'id': 'B005', 'base_yield': 96, 'temp': 74, 'purity': 0.95, 'catalyst_efficiency': 0.14}
]

# Execution pipeline
validated_loads = preprocess_batches(raw_batch_data)
top_tier = filter_high_grade(validated_loads)
final_yield = calculate_optimal_yield(top_tier)
print(f"Result: {final_yield}")