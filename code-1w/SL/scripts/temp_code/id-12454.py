from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_logs = [
    {'node': 'A', 'load': 0.6, 'errors': 2, 'priority': 'high'},
    {'node': 'B', 'load': 0.3, 'errors': 0, 'priority': 'medium'},
    {'node': 'C', 'load': 0.8, 'errors': 5, 'priority': 'high'},
    {'node': 'D', 'load': 0.7, 'errors': 1, 'priority': 'low'},
    {'node': 'E', 'load': 0.4, 'errors': 0, 'priority': 'medium'}
]

# Irrelevant helper (distractor)
def analyze_network_path(route):
    if len(route) > 3:
        return sum([ord(c) for c in route]) % 7
    return 0

# Unused function (dead code path)
def legacy_reweight(scores):
    adjusted = []
    for s in scores:
        if s > 0.5:
            adjusted.append(s * 0.9)
        else:
            adjusted.append(s * 1.2)
    return adjusted

# Decoy metric calculation
temp_weights = [0.8, 1.2, 0.9, 1.1]
weighted_sum = 0
for i in range(len(temp_weights)):
    weighted_sum += temp_weights[i] * (i + 1)
avg_weight = weighted_sum / len(temp_weights)  # Misleading intermediate

# Real processing begins here
def extract_metrics(logs):
    metrics = defaultdict(list)
    priority_map = {'low': 1, 'medium': 2, 'high': 3}
    
    for log in logs:
        node = log['node']
        load = log['load']
        errors = log['errors']
        priority = priority_map[log['priority']]
        
        # Compute composite risk score
        risk = (load * 0.6) + (errors * 0.3) + (1 / (priority + 1) * 0.1)
        metrics[node].append(risk)
        
        # Distractor: unused transformation
        normalized_risk = round(risk / (load + 0.1), 3)
        metrics[node].append(normalized_risk)
    
    return metrics

# Transform raw logs into structured metrics
raw_metrics = extract_metrics(telemetry_logs)

# Another red herring: frequency analysis of error counts (unused)
error_counts = [log['errors'] for log in telemetry_logs]
error_freq = Counter(error_counts)
max_error_frequency = max(error_freq.values())  # Not used later

# Extract only the primary risk values per node
primary_risks = []
for node, values in raw_metrics.items():
    primary_risks.append(values[0])  # Only first element is actual risk

# Simulate performance window filtering
active_window = [r for r in primary_risks if r > 0.45]

# Secondary filter based on arbitrary threshold
filtered_detections = list(filter(lambda x: x < 0.75, active_window))

# Auxiliary decoy calculation with bit manipulation (irrelevant)
bitmask = 0b101010
shifted_mask = bitmask << 3
inverted = ~shifted_mask & 0b11111111
checksum_decoy = (inverted ^ 0b00110011) % 9  # Nowhere used

# Core evaluation logic
metric_data = {
    'risks': primary_risks,
    'window_size': len(active_window),
    'baseline': sum(primary_risks) / len(primary_risks)
}

# Final scoring with controlled nesting and distractors
def evaluate_performance(data):
    base = data['baseline']
    adjustment = 0.0
    
    if data['window_size'] >= 3:
        adjustment += 0.15
        
        high_risk_count = 0
        for r in data['risks']:
            if r > 0.65:
                high_risk_count += 1
                
                # Nested distraction
                temp_val = math.log(r + 1) * 100
                if temp_val > 50:  # Always true
                    adjustment += 0.02
        
        if high_risk_count > 1:
            adjustment += 0.2
            
            # Complex conditional with short-circuit
            secondary_boost = (data['baseline'] > 0.5) and (len(data['risks']) == 5)
            if secondary_boost:
                adjustment += 0.1
    else:
        adjustment -= 0.1
    
    # Apply adjustment with precision
    final_raw = base + adjustment
    
    # Red herring: unused exponential scaling
    exp_scaled = math.exp(final_raw - 0.5)
    capped_score = min(exp_scaled, 10)  # Not used
    
    # Actual result computation
    rounded_final = round(final_raw * 1000)  # Scale to integer
    
    # Dead code block (never reached due to return)
    if rounded_final < 0:
        rounded_final = 0
    
    return rounded_final

# Execute key statement
target_result_var = evaluate_performance(metric_data)
final_score = target_result_var

# Output result
print(f"Result: {final_score}")