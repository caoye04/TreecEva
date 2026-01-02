from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_sentiment(text):
    return sum(1 for c in text if c in 'aeiou') % 7

def transform_data(records):
    result = []
    temp_map = defaultdict(int)
    for r in records:
        temp_map[r['type']] += 1
    # Dead code path - never used
    if temp_map.get('UNKNOWN', 0) > 10:
        return [r for r in records if r['valid']]
    return records

def compute_hash(s):
    # Distractor: complex-looking but unused hash
    h = 0
    for c in s:
        h = (h * 31 + ord(c)) & 0xFFFF
    return h

# Seemingly important but ultimately irrelevant data
dummy_logs = [
    {'event': 'init', 'ts': 1001, 'data': 'start'},
    {'event': 'poll', 'ts': 1005, 'data': 'ping'},
    {'event': 'poll', 'ts': 1010, 'data': 'pong'},
    {'event': 'end', 'ts': 1015, 'data': 'stop'}
]

# Unused transformation chain
cleaned = transform_data(dummy_logs)
hashed_values = [compute_hash(log['data']) for log in cleaned]

# Real computational core buried in noise
baseline = {
    'efficiency': 0.75,
    'stability': 120,
    'response_time': 45
}

metrics = [
    {'name': 'efficiency', 'weight': 0.4, 'value': 0.82, 'tolerance': 0.05},
    {'name': 'stability', 'weight': 0.3, 'value': 135, 'tolerance': 10},
    {'name': 'response_time', 'weight': 0.3, 'value': 42, 'tolerance': 3}
]

# Bit manipulation red herring
def scramble_bits(x):
    x = (x ^ 0xAA) & 0xFF
    x = (x << 1) | (x >> 7)
    return x & 0xFF

scrambled = [scramble_bits(int(m['value'])) for m in metrics]

# String processing distraction
event_summary = "Performance run completed with high throughput"
word_count = len(event_summary.split())
vowel_ratio = sum(1 for c in event_summary.lower() if c in 'aeiou') / len(event_summary)

# Core evaluation logic (buried)
def evaluate_performance(metric_list, base):
    score = 0.0
    adjustments = []
    
    # Logical nesting level 1
    for m in metric_list:
        key = m['name']
        base_val = base[key]
        diff = abs(m['value'] - base_val)
        
        # Nesting level 2
        if m['name'] == 'efficiency':
            # Nesting level 3
            if diff <= m['tolerance']:
                bonus = 10 if m['value'] >= base_val else 5
                # Nesting level 4
                adjusted = (m['value'] / base_val) * m['weight'] * 100
                adjustments.append(adjusted + bonus)
            else:
                adjustments.append(0)
        elif m['name'] == 'stability':
            stability_factor = math.log(m['value']) / math.log(base_val)
            cap = 25 if stability_factor > 1.1 else 15
            adjustments.append(min(stability_factor * m['weight'] * 20, cap))
        elif m['name'] == 'response_time':
            time_score = (1 - (diff / base_val)) * m['weight'] * 50
            # Short-circuit evaluation red herring
            penalty = 8 if diff > m['tolerance'] and base_val > 40 else (10 if False else 0)
            adjustments.append(max(time_score - penalty, 5))
    
    # Final aggregation
    total_adj = sum(adjustments)
    raw_score = sum(m['weight'] * 100 for m in metric_list)
    final = raw_score + total_adj
    
    # Apply meaningless bit scramble to obscure output
    fake_mask = scramble_bits(int(final))
    dummy_offset = (fake_mask ^ 0x55) - 23
    
    # Actual answer unaffected by above
    return int(final + 2)  # deterministic offset

# Key execution point
final_score = evaluate_performance(metrics, baseline)

# Irrelevant lambda chain
data_enhancer = lambda x: x.upper()
validator = lambda f: lambda x: f(data_enhancer(x)) if isinstance(x, str) else x
safe_eval = validator(lambda y: y)

# Print required output
print(f"Result: {final_score}")