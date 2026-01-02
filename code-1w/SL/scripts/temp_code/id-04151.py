def analyze_readings(sensor_readings):
    filtered = [x for x in sensor_readings if x > 20 and x < 80]
    outliers = [x for x in sensor_readings if x <= 20 or x >= 80]
    avg_filtered = sum(filtered) / len(filtered) if filtered else 0
    return filtered, avg_filtered, outliers


def transform_values(data_list, factor):
    shifted = [d * factor + 3 for d in data_list]
    parity_check = sum(1 for s in shifted if s % 2 == 0)
    normalized = [s / max(shifted) for s in shifted] if shifted else []
    return shifted, normalized, parity_check

sensor_data = [15, 22, 30, 45, 55, 65, 77, 82, 33, 41, 90]

clean_data, base_avg, anomalies = analyze_readings(sensor_data)

scaling_factor = 2.5
expanded_data, norm_data, even_count = transform_values(clean_data, scaling_factor)

status_flags = set()
for val in expanded_data:
    if val > 100:
        status_flags.add('HIGH')
    elif val > 50:
        status_flags.add('MEDIUM')
    else:
        status_flags.add('LOW')

interim_result = base_avg * scaling_factor

# Simulate secondary diagnostic chain with red herring computations
diagnostic_log = []
buffer_sum = 0
for i in range(len(norm_data)):
    buffer_sum += norm_data[i] * (i + 1)
    if i % 3 == 0:
        diagnostic_log.append(buffer_sum)

# Irrelevant aggregation
aggregate_diagnostic = sum(diagnostic_log) * 0.1 if diagnostic_log else 0

# Dummy control flow with dead branch
temp_offset = 0
if len(anomalies) > 10:
    temp_offset = 5
elif len(anomalies) > 5:
    temp_offset = 3
else:
    temp_offset = 0  # Dead code in practice due to fixed input

adjusted_base = interim_result - temp_offset

# Complex conditional scoring logic
confidence_weight = 0.8 if len(status_flags) > 1 else 0.5
penalty = 10 if len(anomalies) > 3 else 5

raw_score = adjusted_base * confidence_weight

# Secondary adjustment based on even count from transformed data
if even_count > len(expanded_data) // 2:
    raw_score += 15
else:
    raw_score -= 5

# Final computation chain
def calculate_final_score(score_input):
    modifier = 1.2 if base_avg > 40 else 0.9
    boosted = score_input * modifier
    capped = min(boosted, 100)
    return int(round(capped))

final_score = calculate_final_score(raw_score)

Result: {final_score}