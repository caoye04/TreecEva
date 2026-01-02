def analyze_sequence(data):
    filtered = [x for x in data if x % 3 == 0 and x > 0]
    shifted = [x >> 1 for x in filtered]
    return shifted

sequence = list(range(1, 50))
sequence.append(-9)
sequence.append(60)

# Irrelevant transformation
inverted = [1/x for x in sequence if x != 0]
smoothed = [sum(sequence[i:i+3]) / 3 for i in range(len(sequence) - 2)]

# Distractor variables
avg_inverted = sum(inverted) / len(inverted)
total_shift = sum(smoothed[::3])

# Core logic begins
processed = analyze_sequence(sequence)

# Simulate analysis log with metadata
analysis_log = {}
for idx, val in enumerate(processed):
    if val < 10:
        status = 'LOW'
    elif val < 20:
        status = 'MEDIUM'
    else:
        status = 'HIGH'
    
    # Store redundant info
    analysis_log[f'entry_{idx}'] = {
        'raw': val,
        'squared': val ** 2,
        'status': status,
        'index_plus_one': idx + 1
    }

# Misleading accumulation
phantom_total = 0
for entry in analysis_log.values():
    if entry['raw'] % 2 == 0:
        phantom_total += entry['squared'] * 0.1

# Another distraction: unused helper
def validate_entry(entry):
    return entry['raw'] > 0 and entry['status'] in ['LOW', 'MEDIUM']

# Real computation chain
base_values = [e['raw'] for e in analysis_log.values()]
threshold_mask = [1 if v > 10 else 0 for v in base_values]
adjusted = [v * (1 + 0.1 * m) for v, m in zip(base_values, threshold_mask)]

# Final rating calculation
magnitude_factor = sum(adjusted) // len(adjusted)
discount = len([v for v in base_values if v < 5])
correction = 1.5 if discount > 3 else 1.0

interim = magnitude_factor - discount
final_score = 0  # initialization

# Key statement
final_score = calculate_rating(analysis_log)

# This function uses only specific parts of the log
def calculate_rating(log):
    raw_vals = [entry['raw'] for entry in log.values()]
    high_count = sum(1 for v in raw_vals if v >= 20)
    mid_count = sum(1 for v in raw_vals if 10 <= v < 20)
    return (high_count * 7) + (mid_count * 3)

# Print result as required
print(f"Result: {final_score}")