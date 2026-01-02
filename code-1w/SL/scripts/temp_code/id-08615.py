def analyze_telemetry(data_log):
    base_offset = sum([x % 7 for x in data_log if x > 0])
    filtered = [x for x in data_log if x != 0]
    shift_factor = len(filtered) // 4
    return base_offset - shift_factor

# Simulate system diagnostics
telemetry_data = [12, -3, 0, 9, 15, -7, 4, 8]
calibration = 5

# Extraneous computation - irrelevant to final result
noise_floor = 0
for i in range(len(telemetry_data)):
    if telemetry_data[i] < 0:
        noise_floor += abs(telemetry_data[i]) ** 0.5

# Primary metric pipeline
raw_metrics = [x * 2 + calibration for x in telemetry_data if x > 0]
adjustments = [x // 3 for x in raw_metrics if x % 2 == 0]

# Distractor block: dead logic path (never executed due to condition)
if len(adjustments) < 2:
    adjustments.append(analyze_telemetry(telemetry_data))
elif len(adjustments) > 10:
    adjustments = [x * 10 for x in adjustments]

# String manipulation distraction (no effect on numerical result)
system_tag = "PERF-DEBUG"
status_flag = system_tag.lower().replace("-", "_").upper()

# Core processing with meaningful operations
aggregated = sum(raw_metrics) / len(raw_metrics) if raw_metrics else 0
metric_sum = sum(adjustments)

# Conditional adjustment based on size
if len(raw_metrics) >= 5:
    metric_sum += int(aggregated // 4)

# Final composition using list and arithmetic logic
metrics = {
    'base': int(aggregated),
    'bonus': len([x for x in raw_metrics if x > 10]),
    'penalty': metric_sum
}

# Key statement
final_score = process_performance(metrics, adjustments)

# Supporting function (defined after use, but valid in Python when called later)
def process_performance(met, adj):
    base_val = met['base'] + met['bonus']
    penalty_correction = sum([x % 5 for x in adj])
    temp_result = base_val * 0.9
    
    # Another distraction: unused intermediate calculation
    peak = max(adj) if adj else 0
    normalized_peak = round(peak / 2.5, 2) if peak else 0
    
    # Actual formula
    result = base_val - met['penalty'] + penalty_correction
    return int(result)

print(f"Result: {final_score}")