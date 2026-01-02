def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = 0
    error_flags = set()
    temp_sum = 0.0

    for entry in logs:
        if 'ERROR' in entry:
            error_flags.add(entry.split('-')[1])
        elif 'DATA' in entry:
            value = int(entry.split(':')[1])
            temp_sum += value ** 0.5
            valid_count += 1

    avg_processed = temp_sum / valid_count if valid_count > 0 else 0
    return avg_processed, len(error_flags)


def compute_baseline(reference_data):
    # Irrelevant helper with dead logic path
    if not reference_data:
        return 0
    squared_values = [x ** 2 for x in reference_data]
    filtered = [s for s in squared_values if s > 50]
    return sum(filtered) // len(filtered) if filtered else 0


def evaluate_risk(exposure_levels):
    risk_level = 0
    high_threshold = 75
    for level in exposure_levels:
        if level > high_threshold:
            risk_level += 1
    adjustment = -0.1 * risk_level
    return round(adjustment, 4)

# Main execution context
log_data = [
    'INFO: System initialized',
    'DATA: 16', 'DATA: 25', 'DATA: 36',
    'ERROR-CRITICAL: Failed',
    'DATA: 49', 'DATA: 64',
    'WARNING: High load',
    'ERROR-NETWORK: Timeout'
]

ref_inputs = [3, 5, 7, 8, 9]
baseline_metric = compute_baseline(ref_inputs)  # Unused later but computed

productivity, error_count = analyze_efficiency(log_data)
risk_factor = evaluate_risk([60, 82, 78, 91, 70])

# Key computational interference: irrelevant string processing
system_tag = "PERF-ANALYZER"
checksum = sum(ord(c) for c in system_tag if c in 'AEIOU') * 2  # Distractor

# Core logic with tuple unpacking and conditional adjustment
modifiers = (1.2, 0.9) if error_count < 3 else (0.8, 1.1)
scale_factor = modifiers[0] if productivity > 10 else modifiers[1]

interim_result = productivity * scale_factor + checksum * 0.01

# Final scoring with logical combination and boolean masking
is_stable = error_count <= 2
has_high_yield = productivity >= 12

bonus_applied = False
if is_stable and has_high_yield:
    interim_result *= 1.15
    bonus_applied = True

final_score = int(interim_result + risk_factor * 100)

# Print final result as required
print(f"Result: {final_score}")