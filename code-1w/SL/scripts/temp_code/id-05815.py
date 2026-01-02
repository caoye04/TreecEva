from collections import defaultdict
import math

# Irrelevant data setup (distractor)
default_user_config = defaultdict(lambda: 'N/A')
default_user_config['timeout'] = 30
default_user_config['retries'] = 3

# Misleading performance indicators (red herring)
legacy_metrics = [0.85, 0.91, 0.76, 0.88]
adjusted_weights = list(map(lambda x: x ** 0.5, legacy_metrics))

# Core data structures
event_log = [
    {'type': 'click', 'value': 4},
    {'type': 'hover', 'value': 1},
    {'type': 'click', 'value': 5},
    {'type': 'scroll', 'value': 2},
    {'type': 'click', 'value': 3}
]

# Unused transformation (dead code path)
transformed_log = []
for event in event_log:
    if event['type'] == 'hover':
        transformed_log.append({**event, 'value': event['value'] * 2})
    else:
        transformed_log.append(event)

# Real processing begins here
action_counts = defaultdict(int)
for event in event_log:
    action_counts[event['type']] += 1

# Compute derived metrics
primary_actions = action_counts['click']
secondary_actions = sum(v for k, v in action_counts.items() if k != 'click')

# Simulated baseline calibration (distractor)
calibration_factor = 1.0
for i in range(5):
    calibration_factor *= 0.95  # Decays to ~0.77

# Auxiliary calculation with decoy result
temp_result = 0
for i in range(primary_actions):
    temp_result += math.sin(i) * math.cos(i)
temp_result = round(temp_result, 4)  # This goes nowhere

# Bit manipulation red herring
bit_fiddling = primary_actions ^ 15
bit_fiddling |= 42
bit_fiddling &= ~8

# Actual metric computation chain
raw_total = sum(event['value'] for event in event_log)
avg_per_action = raw_total / len(event_log)

def calculate_efficiency(counts, total):
    bonus = 1.0
    if counts['click'] > 2:
        bonus += 0.1
    if counts['scroll'] >= 1:
        bonus += 0.05
    return total * bonus

efficiency_score = calculate_efficiency(action_counts, avg_per_action)

# Another misleading intermediate
fake_aggregate = 0
for k, v in action_counts.items():
    fake_aggregate += v * (ord(k[0]) % 7)
fake_aggregate /= 10

# Baseline definition (appears important but only partially used)
baseline = {
    'min_interactions': 3,
    'target_average': 2.5,
    'efficiency_floor': 2.0
}

# Key function combining multiple concepts
def evaluate_performance(metrics, base):
    score = efficiency_score  # Capture outer scope
    
    # Conditional adjustments (control flow + arithmetic)
    if metrics['click'] >= base['min_interactions']:
        score *= 1.2
    
    if raw_total > base['target_average'] * 4:
        score *= 1.1
    
    # Logical short-circuit red herring
    debug_flag = False
    if debug_flag and score < 0:
        score = base['efficiency_floor']
    
    # Final adjustment using bit count (unusual but valid)
    click_bits = bin(metrics['click']).count('1')
    score += click_bits * 0.25
    
    return score

# Execution point of interest
final_score = evaluate_performance(action_counts, baseline)

# Output requirement
print(f"Result: {final_score}")