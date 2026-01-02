def analyze_system_health(reading_sequence, config_profile):
    base_offset = 17
    temp_cache = [r % 13 for r in reading_sequence if r > 50]
    adjusted_values = []
    for i, val in enumerate(temp_cache):
        shift = i % 4
        if shift == 0:
            adjusted_values.append(val * 1.05)
        elif shift == 1:
            adjusted_values.append(val * 0.98)
        elif shift == 2:
            adjusted_values.append(val * 1.02)
        else:
            adjusted_values.append(val * 0.95)

    # Irrelevant signal smoothing (distractor)
    smoothed = []
    for j in range(len(adjusted_values)):
        window = adjusted_values[max(0, j-1):min(j+2, len(adjusted_values))]
        smoothed.append(sum(window) / len(window))

    # Decoy diagnostic path (dead code)
    if len(smoothed) > 100:
        return sum(smoothed) // len(smoothed)

    # Unused transformation chain
    inverted_map = list(map(lambda x: int(100 - x), temp_cache))
    string_data = [str(base_offset + x) for x in inverted_map]
    joined_block = ''.join(string_data)
    checksum_distractor = sum(int(c) for c in joined_block if c in '369')

    # Actual relevant logic begins here
    critical_flags = [1 for v in reading_sequence if v % 11 == 0 and v > 60]
    flag_sum = sum(critical_flags)

    # Simulated log compression via zip and enumerate (mixed relevance)
    indexed_logs = list(enumerate(reading_sequence))
    compressed_size = len(indexed_logs) // 3 + 1
    size_factor = compressed_size * (flag_sum or 1)

    # Conditional expression with modular arithmetic
    mode_select = 'aggressive' if len(temp_cache) > 5 else 'conservative'
    multiplier = 3.2 if mode_select == 'aggressive' else 1.8

    # Real computation path
    raw_score = 0
    for idx, entry in indexed_logs:
        if entry > 75:
            raw_score += (entry // 10) * (idx % 7 + 1)

    # Secondary modulator using string method distraction
    tag_string = 'SYS|MONITOR|ACTIVE|LEVEL4'
    tags = tag_string.split('|')
    active_levels = [t for t in tags if t.lower().startswith('level')]
    level_val = int(active_levels[0][-1]) if active_levels else 1

    intermediate_diagnostic = int(raw_score * multiplier) + (base_offset * level_val)

    # Final red herring: unused complex function
    def deep_evaluate(x):
        return (x ** 0.5 + (x % 19)) if x > 100 else x * 2.1

    final_diagnostic = intermediate_diagnostic - (checksum_distractor % 29)
    return final_diagnostic


def process_metrics(entries, thresholds):
    # Simulate preprocessing steps with distractors
    filtered = [e for e in entries if e in thresholds]
    paired_data = list(zip(entries[::2], entries[1::2]))
    sum_product = sum(a * b for a, b in paired_data)

    # Fake entropy calculation (irrelevant)
    bit_entropy = 0
    for p in paired_data:
        for val in p:
            bit_entropy += bin(val).count('1')

    # Meaningful but indirect path
    scaled_total = sum(entries) // len(thresholds)
    trigger_count = sum(1 for e in entries if e > 88)

    # Core logic hidden among distractions
    status_code = 4 if any(t % 5 == 0 for t in thresholds) else 2
    adjustment = sum_product % 17 if status_code == 4 else 0

    return scaled_total + adjustment + (trigger_count * 10)

# Main execution flow
log_entries = [65, 70, 82, 91, 44, 77, 88, 95, 61, 73]
system_thresholds = [60, 70, 80, 85, 90]

# Dead assignment chain (distractor)
dummy_buffer = [0] * 5
for k in range(len(dummy_buffer)):
    dummy_buffer[k] = (k * 13 + 17) % 255

# Key call that computes the target variable
final_diagnostic = process_metrics(log_entries, system_thresholds)

# Output requirement
print(f"Target result: {final_diagnostic}")