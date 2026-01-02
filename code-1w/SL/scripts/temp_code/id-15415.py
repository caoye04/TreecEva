def analyze_sequence(data):
    temp_result = 0
    for i in range(len(data)):
        if data[i] % 3 == 0 and data[i] % 5 != 0:
            temp_result += data[i] * 2
        elif data[i] % 7 == 0:
            temp_result -= data[i] // 3
    return temp_result

# Irrelevant helper function (dead code path)
def unused_validator(x):
    return all(v > 0 for v in x) and len(x) < 100

# Misleading metric calculation
def compute_legacy_metric(values):
    aggregate = 0
    for val in values:
        if val < 50:
            aggregate += val ** 0.5
    return aggregate * 1.5  # Decoy result

# Core logic disguised among distractors
def generate_baseline(shift, factor):
    base = 0
    for i in range(3, 10, 2):
        base += (i + shift) * factor
    return base // 2

def evaluate_performance(log, adj):
    total = 0
    penalty = 0
    
    # Real data processing
    for entry in log:
        if 'status' in entry and entry['status'] == 'active':
            total += entry['value']
            if entry['flags'] & 0x1:
                penalty += 5
    
    # Bit manipulation relevant to final result
    adjusted_total = (total >> 2) ^ 0xFF
    
    # Conditional adjustment using logical ops
    modifier = adj if adj > 0 else 1
    if adj % 2 == 0 and total > 100:
        modifier += 3
    
    intermediate = (adjusted_total + modifier) & 0xFFFF
    
    # Distractor: complex but unused transformation
    shadow_copy = [{k: v*2 for k, v in item.items()} for item in log if item.get('temp', 0) > 10]
    
    # Actual answer derivation
    final_score = (intermediate - penalty) * 3
    
    # Dead branch with misleading comment
    if False:  # This is never executed
        final_score = sum(len(str(v)) for v in log[0].values())  # Red herring
        
    return final_score

# Setup with mixed relevance
raw_data = [15, 21, 9, 35, 40, 18]
dummy_analysis = analyze_sequence(raw_data)
legacy_val = compute_legacy_metric(raw_data)
baseline = generate_baseline(4, 3)

# Real input construction
metrics_log = [
    {'value': 68, 'status': 'active', 'flags': 0x1, 'temp': 5},
    {'value': 72, 'status': 'inactive', 'flags': 0x0, 'temp': 12},
    {'value': 55, 'status': 'active', 'flags': 0x3, 'temp': 8},
    {'value': 81, 'status': 'active', 'flags': 0x1, 'temp': 3}
]

adjustment_factor = 7

# Critical execution point
final_score = evaluate_performance(metrics_log, adjustment_factor)

# Print required output
print(f"Result: {final_score}")