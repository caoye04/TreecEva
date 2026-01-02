def analyze_pattern(sequence):
    if not sequence:
        return 0
    transformed = list(map(lambda x: (x ** 2 + 1) % 10, sequence))
    count_map = {}
    for num in transformed:
        count_map[num] = count_map.get(num, 0) + 1
    
    # Irrelevant string processing - distraction
    status_log = "Processing complete."
    flagged = status_log.upper().replace(" ", "_")
    temp_checksum = sum([ord(c) for c in flagged]) % 50
    
    # Real logic continues
    peaks = 0
    for i in range(1, len(transformed) - 1):
        if transformed[i] > transformed[i-1] and transformed[i] > transformed[i+1]:
            peaks += 1
    
    # Secondary transformation
    adjusted_peaks = max(peaks, len(transformed) // 3)
    return adjusted_peaks * 2


def validate_input(raw_data):
    # Dead code path - never actually used
    if isinstance(raw_data, str) and raw_data.isdigit():
        return int(raw_data)
    elif isinstance(raw_data, list):
        cleaned = [x for x in raw_data if isinstance(x, int) and x >= 0]
        return len(cleaned) > 0
    return False

# Main execution block
data = [3, 7, 2, 8, 4, 6, 1]
weights = [0.1, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1]

# Misleading intermediate calculations
aggregate = sum([a * w for a, w in zip(data, weights)])
dummy_shift = ''.join([str((d * 2) % 9) for d in data])
shadow_value = int(dummy_shift[:3]) if len(dummy_shift) >= 3 else 0

# Core processing with nested logic
primary_metric = analyze_pattern(data)
secondary_metric = sum([d for d in data if d % 2 == 0])

# Conditional weight adjustment (only looks complex, result is deterministic)
effective_weight = 0.8 if primary_metric > 5 else 0.6
bonus_factor = len(data) - len(set(data))  # duplicate penalty

intermediate_score = primary_metric * 10 + secondary_metric * effective_weight

# Final computation chain
penalty = 0
for d in data:
    if d < 5:
        penalty += 3

final_score = int(intermediate_score - penalty + bonus_factor)

# Output required format
print(f"Result: {final_score}")