def preprocess_signal(raw_samples):
    filtered = [x for x in raw_samples if abs(x) > 0.1]
    normalized = [x / max(filtered) for x in filtered]
    return normalized


def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq


def encrypt_chunk(data, key):
    # Irrelevant encryption function (dead path)
    return [d ^ key for d in data]


def analyze_pattern(signal, limit):
    truncated = signal[:limit]
    weighted_sum = 0
    for i, val in enumerate(truncated):
        weight = (i + 1) / len(truncated)
        weighted_sum += val * weight
    
    # Misleading intermediate calculation
    dummy_metric = sum([abs(signal[j] - signal[j-1]) for j in range(1, len(signal))]) * 0.05
    
    adjustment_factor = 1.0
    if len(signal) % 2 == 0:
        adjustment_factor *= 0.9
    if abs(weighted_sum) > 0.5:
        adjustment_factor *= 1.1
    
    return int(weighted_sum * 1000 * adjustment_factor)

# Main execution
raw_input = [-2.1, 0.05, 1.8, -0.03, 0.95, 1.4, -1.1, 0.01]
decoy_data = [0.1, 0.2, 0.3]
scaling_factor = 1.5

# Real processing path
processed = preprocess_signal(raw_input)
expanded = processed + [p * 0.5 for p in processed][:4]
sorted_expanded = sorted(expanded, reverse=True)

# Slice manipulation with meaningful use
segment_a = sorted_expanded[::2]  # Every other element
segment_b = sorted_expanded[1::2]  # Offset slice

# Combine using alternating pattern (irrelevant to final result but looks important)
interleaved = []
for i in range(max(len(segment_a), len(segment_b))):
    if i < len(segment_b):
        interleaved.append(segment_b[i])
    if i < len(segment_a):
        interleaved.append(segment_a[i])

# Transform via string-based mapping (red herring)
str_values = [f'{x:.3f}' for x in interleaved]
case_toggled = []
for s in str_values:
    toggled = ''.join([ch.lower() if ch.isupper() else ch.upper() for ch in s])
    case_toggled.append(toggled)

# Convert back — looks critical but unused
reverted_numeric = [float(s.lower()) for s in case_toggled]

# Actual relevant transformation
transformed_data = [x * 100 for x in processed]  # Amplify for analysis

# Decoy recursive function (never called)
def calculate_depth(n):
    if n <= 1:
        return 1
    return calculate_depth(n-1) + calculate_depth(n-2)

# Another decoy sort operation
sorted_decoy = sorted(generate_sequence(6), reverse=True)

threshold = 7
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Print required output
print(f"Result: {final_diagnostic}")