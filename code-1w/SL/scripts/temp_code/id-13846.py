def process_packet(header, payload):
    checksum = sum(ord(c) for c in header) % 100
    size_metric = len(payload) * 2 if 'urgent' in payload else len(payload)
    normalized = (size_metric + checksum) / 2.5
    return int(normalized)


def validate_sequence(sequence):
    valid_count = 0
    for item in sequence:
        if isinstance(item, str) and item.isalpha():
            valid_count += 1
    return valid_count > len(sequence) // 2

# Simulate sensor data processing with validation and scoring
data_stream = ['A7', 'B9', 'CZ', 'D2', 'E1']
convergence = [3, 7, 9, 12, 15]

# Irrelevant transformation chain (distractor)
temp_labels = [f"Node_{i}" for i in range(len(data_stream))]
label_hash = sum(len(label) for label in temp_labels) % 50
offset_correction = label_hash * 0.3

# Misleading intermediate calculation (dead-end)
apparent_trend = 0
for i in range(1, len(convergence)):
    apparent_trend += convergence[i] - convergence[i-1]
apparent_trend = apparent_trend / (len(convergence) - 1) if len(convergence) > 1 else 0

# Core logic disguised among distractions
baseline = 10
adjustment_factor = 0
for val in convergence:
    if val % 2 == 0:
        adjustment_factor += 1
    else:
        adjustment_factor -= 1

# Secondary distractor: unused statistical measure
mean_val = sum(convergence) / len(convergence)
variance_proxy = sum((x - mean_val) ** 2 for x in convergence) / len(convergence)

# Conditional expression usage (required feature)
signal_strength = 'high' if mean_val > 8 else 'low'
boost_enabled = True if signal_strength == 'high' and len(data_stream) > 4 else False

# String method integration (required feature)
formatted_headers = [h.lower().replace('7', 'X') for h in data_stream]

# Real computation hidden in helper function
packet_values = [process_packet(h, ['normal']) for h in formatted_headers]

# Another red herring: complex but unused logic
status_flags = {}
for i, p in enumerate(packet_values):
    status_flags[f"flag_{i}"] = (p % 4 == 0) or (i % 3 == 0)
dropped_flags = sum(1 for v in status_flags.values() if not v)

# Actual rating logic
convergence_stable = all(convergence[i] <= convergence[i+1] for i in range(len(convergence)-1))
validation_passed = validate_sequence(data_stream)

base_rating = sum(packet_values) / len(packet_values)

# Final conditional logic with nesting
if convergence_stable:
    if validation_passed:
        if boost_enabled:
            final_score = int(base_rating * 2.5)
        else:
            final_score = int(base_rating * 1.8)
    else:
        final_score = int(base_rating * 1.2)
else:
    final_score = int(base_rating * 0.7)

# This line executes the key statement
calculate_rating = lambda x, y: final_score  # Mock, since final_score already computed above
final_score = calculate_rating(convergence, data_stream)

print(f"Result: {final_score}")