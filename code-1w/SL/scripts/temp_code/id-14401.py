from collections import defaultdict
import math

def analyze_pattern_sequence(raw_data):
    # Preprocess: filter and normalize signal strengths
    normalized = [x / max(raw_data) for x in raw_data]
    threshold = 0.3
    significant = [i for i, val in enumerate(normalized) if val > threshold]

    # Misleading computation: frequency analysis (not used later)
    freq_map = defaultdict(int)
    for val in raw_data:
        freq_map[val] += 1
    avg_freq_magnitude = sum(freq_map.values()) / len(freq_map) if freq_map else 0

    # Generate two phase-modulated patterns based on position
    pattern_a = []
    pattern_b = []
    for idx in significant:
        angle = math.sin(idx * 0.5) * math.pi
        if idx % 2 == 0:
            pattern_a.append(math.cos(angle))
        else:
            pattern_b.append(math.sin(angle))

    # Dead code path: entropy calculation (irrelevant to final result)
    entropy = 0
    for p in freq_map.values():
        prob = p / len(raw_data)
        if prob > 0:
            entropy -= prob * math.log2(prob)

    # Truncate to equal length for interference analysis
    min_len = min(len(pattern_a), len(pattern_b))
    pattern_a = pattern_a[:min_len]
    pattern_b = pattern_b[:min_len]

    return pattern_a, pattern_b

def calculate_interference(seq1, seq2):
    # Compute element-wise phase difference
    phase_diffs = []
    for a, b in zip(seq1, seq2):
        diff = abs(a - b)
        phase_diffs.append(diff)
    
    # Accumulate net effect with damping factor
    damping = 0.95
    cumulative = 0
    for i, diff in enumerate(phase_diffs):
        weighted = diff * (damping ** i)  # Exponential decay weighting
        cumulative += weighted

    # Secondary metric: coherence score (unused distractor)
    coherence = sum(1 for d in phase_diffs if d < 0.5) / len(phase_diffs) if phase_diffs else 0

    return cumulative

# Main execution
signal_data = [12, 45, 23, 67, 89, 34, 56, 78, 91, 11, 8, 65]

# Process the signal into interference-ready patterns
processed_a, processed_b = analyze_pattern_sequence(signal_data)

# Introduce redundant transformation (irrelevant slicing)
reversed_a = processed_a[::-1]
shifted_b = [x * 0.9 for x in processed_b][1:] + [0]  # misalign intentionally

# Core calculation: compute net phase shift from original sequences
net_phase_shift = calculate_interference(processed_a, processed_b)

# Additional red herring: combinatorics on indices (no impact)
index_pairs = [(i, j) for i in range(3) for j in range(3) if i != j]
permutation_count = len(index_pairs) ** 2

# Final output
Result: {net_phase_shift}