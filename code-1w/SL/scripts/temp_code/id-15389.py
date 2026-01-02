def normalize_values(raw_list):
    min_val = min(raw_list)
    max_val = max(raw_list)
    range_val = max_val - min_val if max_val != min_val else 1
    return [(x - min_val) / range_val for x in raw_list]

# Irrelevant helper function (dead code path)
def legacy_transform(seq):
    return [elem * 1.5 for elem in seq if elem > 0]

# String-based distractor data
diagnostic_tag = "ANALYSIS_COMPLETE_V2"
if diagnostic_tag.startswith("ANALYSIS") and diagnostic_tag.endswith("V2"):
    status_flag = 1
else:
    status_flag = 0

timestamp_log = "2023-11-05T14:23:10Z"
log_parts = timestamp_log.split('T')
date_part = log_parts[0]
time_part = log_parts[1].rstrip('Z')

# Main data processing
raw_data = [23, 45, 67, 89, 12, 34, 56]
weights = [0.1, 0.2, 0.15, 0.25, 0.05, 0.1, 0.1]

# Normalize data (relevant)
normalized_data = normalize_values(raw_data)

# Misleading intermediate computation (semi-relevant)
adjusted_data = []
for val in normalized_data:
    if val < 0.5:
        adjusted_data.append(val * 1.1)
    else:
        adjusted_data.append(val * 0.9)

# Additional distraction: string manipulation unrelated to final result
data_id = "DSET_7XG_2023"
segments = data_id.split('_')
version_code = segments[-1] if segments[-1].isdigit() else "NONE"

# Simulated confidence score (distractor)
confidence_numerator = sum(1 for x in normalized_data if x > 0.3)
confidence_score = confidence_numerator / len(normalized_data)

# Real calculation begins here
weighted_sum = 0.0
for i in range(len(adjusted_data)):
    weighted_sum += adjusted_data[i] * weights[i]

# Secondary adjustment based on pattern detection
pattern_match_count = 0
for i in range(1, len(raw_data)):
    if raw_data[i] > raw_data[i-1]:
        pattern_match_count += 1

# Use conditional expression for minor correction
trend_factor = 1.05 if pattern_match_count > len(raw_data) // 2 else 0.95

interim_result = weighted_sum * trend_factor

# Final scaling using string-derived condition (subtle but valid)
scaling_factor = 100 if 'V2' in diagnostic_tag else 50

final_score = int(interim_result * scaling_factor)

Result: final_score