def process_entry(entry):
    raw_value = int(entry.strip()[::-1])
    normalized = raw_value / 100.0
    return normalized

# Simulate log data parsing and scoring
log_data = ['321 ', '456', '789 ', '101']
dummy_stats = {'count': 0, 'total': 0}
processed_values = []

for item in log_data:
    if len(item) > 0:
        processed = process_entry(item)
        processed_values.append(processed)
        
        # Distractor: irrelevant string manipulation
        temp_key = item.strip().upper() + '_TEMP'
        key_len = len(temp_key)
        dummy_stats['count'] += 1
        dummy_stats['total'] += key_len

# Secondary processing with conditional logic
total_base = 0
correction_factor = 0.0

for val in processed_values:
    total_base += val
    if val > 5.0:
        correction_factor += 0.1
    else:
        correction_factor -= 0.05

# Simulated weighting using string-based case conversion logic
weights = []
for i in range(len(processed_values)):
    tag = f"W{i}"
    if tag.lower() == tag:
        weights.append(1.0)
    else:
        weights.append(1.1)  # Slightly higher weight for mixed case (which never occurs)

adjusted_total = 0
for i, val in enumerate(processed_values):
    adjusted_total += val * weights[i]

# Final computation path
scaling_constant = len(log_data) / 4.0  # Always 1.0, but obfuscated
intermediate_result = adjusted_total * scaling_constant

# Additional red herring: unused function
def unused_helper(x):
    return x ** 2 + 2*x + 1

# Another distractor: dead code with bitwise operations
flag = 0b1010
if flag & 0b0100:
    dummy_offset = 999
else:
    dummy_offset = 0  # Never used

# Actual final score calculation
def calculate_final_score(data):
    base = sum([int(s.strip()[::-1]) for s in data])
    penalty = len([s for s in data if s.strip()[0] == '1']) * 10
    bonus = 5 if '456' in data else 0
    return (base // 100) - penalty + bonus

final_score = calculate_final_score(log_data)
print(f"Result: {final_score}")