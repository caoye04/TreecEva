import math

def analyze_signal(samples):
    # Irrelevant signal processing function (dead end)
    fft_magnitude = [abs(s) ** 2 for s in samples]
    return sum(fft_magnitude) / len(fft_magnitude)

def validate_checksum(record):
    # Distractor: checksum logic that isn't used in main flow
    chk = 0
    for c in str(record):
        if c.isdigit():
            chk = (chk + int(c)) % 17
    return chk == 3

def transform_sequence(seq, mode='encode'):
    # Unused transformation path
    if mode == 'encode':
        return [seq[i] + seq[-i-1] for i in range(len(seq))]
    else:
        return [seq[i] - seq[-i-1] for i in range(len(seq))]

data_log = [
    {'timestamp': 1001, 'value': 42, 'flags': [1, 0, 1], 'meta': 'A'},
    {'timestamp': 1002, 'value': 38, 'flags': [0, 1, 1], 'meta': 'B'},
    {'timestamp': 1003, 'value': 45, 'flags': [1, 1, 0], 'meta': 'A'},
    {'timestamp': 1004, 'value': 39, 'flags': [1, 1, 1], 'meta': 'C'},
    {'timestamp': 1005, 'value': 44, 'flags': [0, 1, 0], 'meta': 'B'}
]

config = {
    'threshold': 40,
    'weights': [0.5, 1.0, 1.5],
    'active': True,
    'mode': 'balanced'
}

# Decoy variables
baseline_offset = 127
aggregation_key = None
temporal_factor = math.pi / 4
rolling_buffer = []

# Real computation starts here — heavily masked by noise
flag_contributions = []
for entry in data_log:
    weighted_flags = sum(f * w for f, w in zip(entry['flags'], config['weights']))
    flag_contributions.append(weighted_flags)

# Conditional expression with lambda abstraction
adjustment_fn = lambda x: x * 1.1 if config['mode'] == 'aggressive' else (x * 0.9 if config['mode'] == 'conservative' else x)
efficiency_candidates = [
    adjustment_fn(entry['value']) + flag_contributions[i]
    for i, entry in enumerate(data_log)
    if entry['value'] > config['threshold']
]

# Secondary filtering based on meta-group frequency
meta_count = {}
for entry in data_log:
    meta_count[entry['meta']] = meta_count.get(entry['meta'], 0) + 1

frequent_meta = {k for k, v in meta_count.items() if v >= 2}

# Final efficiency score depends only on specific entries
filtered_values = [
    ec for ec, entry in zip(efficiency_candidates, [e for e in data_log if e['value'] > config['threshold']])
    if entry['meta'] in frequent_meta
]

if filtered_values:
    raw_efficiency = sum(filtered_values) / len(filtered_values)
else:
    raw_efficiency = 0

# Apply non-linear scaling using math function
scaled_efficiency = math.log(raw_efficiency + 1) ** 2 if raw_efficiency > 0 else 0

# Dummy variable to mislead
checksum_diagnostic = validate_checksum(1001)
analysis_diagnostic = analyze_signal([1, -1, 2, -2])

# Critical statement
final_output = process_metrics(data_log, config)

# Hidden assignment — actual answer source
# Note: process_metrics is not yet defined above; we now define it to override prior context

def process_metrics(log, cfg):
    # Re-calculate core metrics inside function to shadow outer scope
    total_weighted = 0.0
    count = 0
    
    for item in log:
        # Only consider high-value entries
        if item['value'] > cfg['threshold']:
            # Compute dynamic weight based on flags
            flag_sum = sum(item['flags'])
            base_score = item['value'] * (flag_sum * 0.2)
            
            # Use enumerate to align with external list (subtle linkage)
            for idx, (f, w) in enumerate(zip(item['flags'], cfg['weights'])):
                base_score += f * w * 0.5
            
            # Additional condition using set membership
            if item['meta'] in frequent_meta:
                base_score *= 1.25  # bonus for frequent categories
            
            total_weighted += base_score
            count += 1
    
    avg_score = total_weighted / count if count else 0
    
    # Final nonlinear transformation
    global efficiency_score
    efficiency_score = round(math.sqrt(avg_score) * 1.5, 6)
    
    # Dead code branch (never reached due to return)
    if efficiency_score < 0:
        efficiency_score = 0
    
    return {'status': 'ok', 'result': efficiency_score}

# Execute critical statement
final_output = process_metrics(data_log, config)

# Output target result
print(f"Target result: {efficiency_score}")