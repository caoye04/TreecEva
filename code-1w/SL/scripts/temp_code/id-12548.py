def process_segments(segs):
    # Irrelevant transformation: case conversion and slicing
    names = ['Alpha', 'Beta', 'Gamma', 'Delta']
    coded_names = [name.lower()[::-1] for name in names]  # distraction: not used later

    # Semi-relevant preprocessing
    lengths = list(map(lambda x: len(x), segs))
    total_length = sum(lengths)
    avg_length = total_length / len(lengths) if lengths else 0

    # Key accumulation with filtering
    filtered_segs = [seg for seg in segs if len(seg) > avg_length]
    weighted_values = []
    
    for i, seg in enumerate(filtered_segs):
        # Some complex but partially irrelevant computation
        shift = (i + 1) * 2
        shifted_chars = [chr((ord(c) - ord('a') + shift) % 26 + ord('a')) for c in seg]
        numeric_vals = [ord(c) - ord('a') + 1 for c in shifted_chars]
        segment_sum = sum(numeric_vals) * (i + 1)
        weighted_values.append(segment_sum)

    # Dead code path - never executed due to data
    if any(len(v) < 0 for v in weighted_values):  # always false
        cleanup(weighted_values)

    # Actual result computation
    base_score = sum(weighted_values)
    penalty = 0
    for seg in segs:
        if seg.startswith('x') or seg.startswith('z'):
            penalty += len(seg)

    final_score = base_score - penalty
    return final_score

# Helper function defined but not called
def cleanup(data):
    data.clear()

# Input data
segments = ['abc', 'defg', 'xyz', 'mnop']

# Execution
final_score = process_segments(segments)
print(f"Result: {final_score}")