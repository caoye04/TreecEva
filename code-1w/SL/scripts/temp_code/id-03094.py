import itertools

# Simulated sensor data stream with redundant and relevant fields
data_stream = [
    {'temp': 22.1, 'pressure': 101.3, 'vibration': 0.45, 'timestamp': 1620000000, 'aux_1': 88, 'status': 'OK'},
    {'temp': 23.5, 'pressure': 101.5, 'vibration': 0.47, 'timestamp': 1620000060, 'aux_1': 89, 'status': 'OK'},
    {'temp': 25.0, 'pressure': 102.0, 'vibration': 0.55, 'timestamp': 1620000120, 'aux_1': 90, 'status': 'WARNING'},
    {'temp': 26.3, 'pressure': 102.8, 'vibration': 0.67, 'timestamp': 1620000180, 'aux_1': 91, 'status': 'OK'},
    {'temp': 24.8, 'pressure': 103.0, 'vibration': 0.72, 'timestamp': 1620000240, 'aux_1': 92, 'status': 'ALERT'}
]

# Redundant helper function that calculates average but isn't used in final logic
def calc_avg(seq):
    return sum(seq) / len(seq)

# Misleading intermediate variables (distractors)
total_aux = sum(item['aux_1'] for item in data_stream)
status_counts = {status: 0 for status in ['OK', 'WARNING', 'ALERT']}
for item in data_stream:
    status_counts[item['status']] += 1

# Lambda to filter high vibration readings (used once)
high_vibration_filter = lambda x: x['vibration'] > 0.5

# Extract relevant metrics using itertools and filtering
relevant_readings = list(filter(high_vibration_filter, data_stream))
interpolated_gaps = list(itertools.pairwise([r['temp'] for r in relevant_readings]))

# Compute temperature delta across high-vibration periods
temp_deltas = [abs(pair[1] - pair[0]) for pair in interpolated_gaps]

# Efficiency metric based on stability during stress conditions
if temp_deltas:
    stability_factor = 100 - (sum(temp_deltas) * 10)
else:
    stability_factor = 100

# Multiple assignment distraction
baseline, deviation, efficiency_score = 90, 5, 0

# Complex conditional with nested logic tracking
if len(relevant_readings) >= 2:
    if stability_factor > 85:
        efficiency_score = baseline + deviation
    elif stability_factor > 70:
        efficiency_score = baseline
    else:
        efficiency_score = baseline - deviation - 10
else:
    efficiency_score = 50

# Dead code path - never executed due to data, but looks plausible
if all(item['status'] == 'OK' for item in data_stream):
    efficiency_score = max(efficiency_score, 95)

# Final processing step where target variable is determined
final_output = process_metrics(data_stream) if 'process_metrics' in globals() else efficiency_score

# Function definition placed after usage (legal in Python if not called before)
def process_metrics(stream):
    # Recompute efficiency score again for consistency
    rel = list(filter(lambda x: x['vibration'] > 0.5, stream))
    deltas = [abs(rel[i+1]['temp'] - rel[i]['temp']) for i in range(len(rel)-1)]
    factor = 100 - (sum(deltas) * 10) if deltas else 100
    base, dev = 90, 5
    if len(rel) >= 2:
        if factor > 85:
            score = base + dev
        elif factor > 70:
            score = base
        else:
            score = base - dev - 10
    else:
        score = 50
    return score

# Update final_output correctly now that function is defined
final_output = process_metrics(data_stream)

# Print result as required
print(f"Result: {efficiency_score}")