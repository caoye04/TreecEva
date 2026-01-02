from collections import defaultdict, Counter

# Simulated system benchmark data with mixed metrics
def generate_test_data():
    return [
        {'ops': 120, 'errors': 2, 'priority': 'high', 'mode': 'async'},
        {'ops': 85, 'errors': 0, 'priority': 'medium', 'mode': 'sync'},
        {'ops': 200, 'errors': 5, 'priority': 'high', 'mode': 'async'},
        {'ops': 95, 'errors': 1, 'priority': 'low', 'mode': 'sync'},
        {'ops': 150, 'errors': 3, 'priority': 'medium', 'mode': 'async'}
    ]

def analyze_modes(data):
    # Irrelevant helper: counts execution modes (distractor)
    mode_count = defaultdict(int)
    for entry in data:
        mode_count[entry['mode']] += 1
    return mode_count

def extract_priorities(data):
    # Semi-relevant: extracts priorities but not directly used later
    priority_list = [item['priority'] for item in data]
    counter = Counter(priority_list)
    high_count = counter['high']
    return high_count  # Only this returned value is indirectly used

def compute_efficiency(ops, errors):
    # Core logic: computes efficiency score per entry
    if ops == 0:
        return 0.0
    base_efficiency = ops / (1 + errors)
    penalty = 0.1 * errors
    return max(base_efficiency - penalty, 0)

def calculate_performance(dataset):
    total_efficiency = 0.0
    adjustment_factor = 0.0
    high_priority_count = extract_priorities(dataset)  # Calls function with side extraction
    
    # Misleading intermediate calculation (only adjustment matters)
    temp_values = []
    for item in dataset:
        raw_score = item['ops'] - item['errors'] * 2
        temp_values.append(raw_score)  # Collected but not used
    
    # Actual core computation
    efficiency_scores = []
    for item in dataset:
        score = compute_efficiency(item['ops'], item['errors'])
        efficiency_scores.append(score)
    
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores)
    
    # Adjustment based on high-priority task volume
    if high_priority_count >= 2:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.9
    
    # Final performance score
    final_raw = avg_efficiency * adjustment_factor
    rounded_result = round(final_raw, 3)
    
    # Dead code path - never executed due to fixed data
    if False and len(dataset) > 10:
        fallback = sum(temp_values) / 10
        rounded_result = fallback
    
    return rounded_result

# Main execution flow
dataset = generate_test_data()
mode_analysis = analyze_modes(dataset)  # Distractor call
baseline_ops = sum(entry['ops'] for entry in dataset)  # Irrelevant summary
error_total = sum(entry['errors'] for entry in dataset)  # Unused metric
final_score = calculate_performance(dataset)
print(f"Result: {final_score}")