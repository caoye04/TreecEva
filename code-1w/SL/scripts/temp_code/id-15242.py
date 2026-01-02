from itertools import combinations

def analyze_risk(profile):
    risk_factors = [profile['age'] > 60, profile['bmi'] > 30, len(profile['conditions']) >= 2]
    return sum(risk_factors)

def generate_baseline(count):
    base = 1
    for i in range(2, count + 1):
        base += (i * (i - 1)) // 2
    return base

def preprocess_data(entries):
    cleaned = []
    temp_buffer = []
    for entry in entries:
        if 'status' in entry and entry['status'] == 'active':
            temp_buffer.append(entry)
    for item in temp_buffer:
        item['value'] = abs(item['value'])
        item['processed'] = True
        cleaned.append(item)
    return cleaned

def calculate_adjustment(signal):
    adjustment = 0
    for char in str(signal):
        if char.isdigit():
            adjustment += int(char)
    return adjustment if adjustment > 0 else 1

def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Irrelevant intermediate computation (distractor)
    temp_analysis = []
    for m in metrics:
        temp_analysis.append(m ** 2 + 1)
    avg_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0
    
    # Core logic with slicing distraction
    trimmed_metrics = metrics[1:-1]  # Remove first and last
    effective_metrics = [m * 0.9 for m in metrics]  # Apply damping
    
    # Actual contribution to result
    for i in range(len(effective_metrics)):
        weighted_sum += effective_metrics[i] * normalized_weights[i % len(normalized_weights)]
    
    # Secondary adjustment based on string pattern in auxiliary data
    tag = "health_v2.1"
    digit_sum = sum(int(c) for c in tag if c.isdigit())
    scaling_factor = 1 + (digit_sum * 0.1)
    
    final_value = weighted_sum * scaling_factor
    
    # Unused but plausible dead-end calculation (misleading)
    peak_window = max([sum(trimmed_metrics[i:i+2]) for i in range(len(trimmed_metrics)-1)], default=0)
    
    return round(final_value, 4)

# Main execution flow
if __name__ == "__main__":
    # Simulated input data
    user_profile = {
        'age': 68,
        'bmi': 32.5,
        'conditions': ['diabetes', 'hypertension'],
        'status': 'active'
    }
    
    raw_entries = [
        {'value': -150, 'status': 'active'},
        {'value': 200, 'status': 'inactive'},
        {'value': 180, 'status': 'active'},
        {'value': 220, 'status': 'active'}
    ]
    
    processed = preprocess_data(raw_entries)
    values = [item['value'] for item in processed]
    
    base_config = generate_baseline(len(values))
    signal_code = "A7B2"  # Used in adjustment
    adjustment = calculate_adjustment(signal_code)
    
    metrics = [v / adjustment for v in values]
    weights = [0.4, 0.3, 0.2, 0.1]
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Distractor: unused combination analysis
    combo_count = len(list(combinations(values, 2)))
    avg_combo_value = sum([sum(pair) for pair in combinations(values, 2)]) / combo_count if combo_count > 0 else 0
    
    # Output target result
    print(f"Result: {final_score}")