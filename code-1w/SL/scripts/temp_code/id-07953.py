def analyze_signal_pattern(sequence):
    magnitude = sum(abs(x) for x in sequence)
    normalized = [x / (magnitude + 1e-9) for x in sequence]
    return normalized

pattern_a = [3, -4, 5, -2]
pattern_b = [-1, 6, -3, 4]

# Irrelevant transformation - distractor
temp_scaled = [val * 1.5 for val in pattern_a]
offset_correction = sum(temp_scaled[:2]) - temp_scaled[3]

# Signal analysis with side computation
def calculate_coherence(seq1, seq2):
    coherence_score = 0
    phase_angles = []
    for i, (a, b) in enumerate(zip(seq1, seq2)):
        product = a * b
        adjusted_product = product + (i % 2) * 0.1  # minor perturbation
        coherence_score += adjusted_product
        angle = abs(a + b) if product > 0 else -abs(a - b)
        phase_angles.append(angle)
    
    # Dead code path - misleading
    if len(phase_angles) > 10:
        return sum(phase_angles) / len(phase_angles)
    
    average_angle = sum(phase_angles) / len(phase_angles)
    return average_angle

# Real computation chain
processed_a = analyze_signal_pattern(pattern_a)
processed_b = analyze_signal_pattern(pattern_b)

coherence = calculate_coherence(processed_a, processed_b)

# Secondary irrelevant metric
divergence_index = sum((a - b)**2 for a, b in zip(pattern_a, pattern_b)) / len(pattern_a)
baseline_shift = divergence_index * 0.3

# Core logic: compute net phase shift using conditional logic and enumeration
phase_contributions = []
for idx, (pa, pb) in enumerate(zip(processed_a, processed_b)):
    contribution = pa * pb * (idx + 1)
    is_significant = abs(contribution) > 0.1
    scaled_contribution = contribution * 2 if is_significant else contribution
n    phase_contributions.append(scaled_contribution)

# Conditional expression usage
peak_magnitude = max(phase_contributions) if len(phase_contributions) > 0 else 0
inverted_weights = [1 / (abs(c) + 0.1) for c in phase_contributions]

# Final function with tuple unpacking and intermediate red herring
def calculate_interference_phase(sig1, sig2):
    total_shift = 0.0
    aux_factor = 0.0
    for i, (x, y) in enumerate(zip(sig1, sig2), start=1):
        raw_shift = x * y * i
        correction = 0.05 if x < 0 else -0.05
        adjusted_shift = raw_shift + correction
        total_shift += adjusted_shift
        aux_factor += abs(raw_shift)  # unused auxiliary accumulation
    
    # Distractor: complex but irrelevant formula
    hypothetical_bound = (aux_factor + 1) ** 0.5 if aux_factor > 1 else 1.0
    
    # Actual answer depends only on total_shift
    return total_shift

net_phase_shift = calculate_interference_phase(pattern_a, pattern_b)
print(f"Result: {net_phase_shift}")