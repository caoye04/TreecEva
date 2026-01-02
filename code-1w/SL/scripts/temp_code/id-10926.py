from collections import defaultdict, Counter
import itertools

# Simulated bio-signal processing pipeline with decoy analysis paths
def analyze_rhythm(signal):
    if len(signal) < 5:
        return 0
    rhythm_score = 0
    for i in range(1, len(signal)):
        if signal[i] > signal[i-1]:
            rhythm_score += 2
        else:
            rhythm_score -= 1
    return rhythm_score

# Irrelevant auxiliary function – dead code path
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    normalized = [(x - mean_val) * 0.85 for x in data]
    return [round(x, 2) for x in normalized]

# Core transformation with embedded distractions
def generate_phase_vector(sequence):
    phase_map = defaultdict(int)
    temp_flags = [False] * len(sequence)
    
    # Real computation: counting transitions
    for idx, val in enumerate(sequence):
        phase_map[val] += 1
        if idx > 0 and sequence[idx] != sequence[idx-1]:
            temp_flags[idx] = True
    
    # Distractor: complex-looking but unused transformation
    shifted = [(sequence[i] + sequence[(i+1)%len(sequence)]) % 7 for i in range(len(sequence))]
    weighted = [shifted[j] * (j+1) for j in range(len(shifted))]
    aggregate = sum(weighted) // len(weighted) if weighted else 0

    # Another red herring: bitmask analysis (never used later)
    mask_analysis = 0
    for w in weighted:
        if w & 1:
            mask_analysis ^= w % 16

    return dict(phase_map), sum(temp_flags)

# Misleading diagnostic chain – appears important but feeds into decoy system
def assess_coherence(trace):
    counter = Counter(trace)
    entropy = 0
    total = len(trace)
    for count in counter.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Non-standard pseudo-entropy
    return round(entropy, 4)

# Unused recursive validator (dead path)
def validate_hierarchy(pattern, depth=0):
    if depth >= 3 or not pattern:
        return False
    if sum(pattern) % 2 == 0:
        return validate_hierarchy(pattern[1:], depth+1)
    return any(validate_hierarchy(pattern[:k]) for k in range(1, len(pattern)))

# Main metric processor – this is where the real logic resides
def process_metrics(signature, cycle_ref):
    base_offset = sum(cycle_ref) % 8
    adjusted = [abs(sig - base_offset) for sig in signature]
    
    # Real logic step 1: filter significant deviations
    deviations = [x for x in adjusted if x > 2]
    
    # Real logic step 2: compute weighted impulse
    impulse = 0
    for i, dev in enumerate(deviations):
        impulse += dev * (i + 1) * (3 if dev % 2 == 0 else -1)
    
    # Real logic step 3: apply correction based on pattern symmetry
    rev = list(reversed(deviations))
    symmetric_match = sum(1 for a, b in zip(deviations, rev) if a == b)
    
    # Real logic step 4: final computation
    if symmetric_match >= len(deviations) // 2:
        impulse = abs(impulse) // 2
    else:
        impulse = -abs(impulse)
    
    # Distractor: elaborate unused structure
    stats_bundle = {
        'raw_length': len(signature),
        'peak': max(signature, default=0),
        'transitions': sum(1 for i in range(1, len(signature)) if signature[i] != signature[i-1]),
        'phase_entropy': assess_coherence(signature),
        'aggregate_flag': (sum(signature) ^ len(signature)) & 7
    }
    
    # This looks like post-processing but is actually just noise
    phantom_correction = 0
    for key, value in stats_bundle.items():
        if isinstance(value, int) and value > 0:
            phantom_correction += (value * len(key)) % 5
    
    # Final result is only affected by earlier impulse logic
    return impulse + 17  # Final adjustment

# Primary data inputs
baseline_cycle = [3, 7, 2, 8, 1, 4]
health_signature = [5, 9, 1, 12, 3, 7, 2, 10]

# Decoy preprocessing steps (appear critical but are unused in final calculation)
data_stream = list(itertools.chain.from_iterable([health_signature[:3], baseline_cycle[:2]]))
normalized_phases = deprecated_normalization(baseline_cycle)
sync_flag = analyze_rhythm(baseline_cycle)

# Actual execution point of interest
phase_counts, transition_count = generate_phase_vector(health_signature)

# Red herring control flow
if transition_count > 5:
    health_signature.append(assess_coherence(health_signature))
elif sync_flag < 10:
    baseline_cycle.extend([sync_flag, sync_flag ^ 5])
else:
    # This branch runs
    temp_snapshot = [x * 2 for x in baseline_cycle if x % 2 == 0]
    temp_snapshot = [x for x in temp_snapshot if x > 5]

# Critical statement — answer derives from here
final_diagnostic = process_metrics(health_signature, baseline_cycle)

# Output required format
print(f"Result: {final_diagnostic}")