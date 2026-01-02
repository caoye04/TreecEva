from collections import defaultdict, Counter

# Simulated bioinformatics pathway analysis with decoy computations

def preprocess_sequence(raw_seq):
    base_map = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    return [base_map.get(base, 0) for base in raw_seq]

def generate_checksum(signal):
    # Irrelevant checksum used in dead code path
    return sum(x * (i + 1) for i, x in enumerate(signal)) % 1000

def encrypt_segment(data):
    # Unused encryption function — red herring
    return [((x << 2) ^ 0xFE) & 0xFF for x in data]

def compute_thermal_stability(seq):
    # Misleading intermediate calculation (not used in final result)
    stability = 0
    for i in range(len(seq) - 1):
        stability += abs(seq[i] - seq[i+1])
    return round(stability / len(seq), 3) if seq else 0

def filter_anomalies(records):
    # Dead code path — never invoked
    valid = []
    for r in records:
        if r['score'] > 5 and r['flag'] != -1:
            valid.append(r)
    return valid

def decode_segments(segments):
    # Distractor transformation — looks important but unused
    result = []
    for s in segments:
        transformed = [x ^ (len(s) % 7) for x in s]
        result.append([t * 2 for t in transformed])
    return result

def accumulate_metrics(values):
    # Decoy accumulation logic
    stats = defaultdict(int)
    for v in values:
        stats['total'] += v
        stats['count'] += 1
        stats['max'] = max(stats['max'], v) if stats['count'] > 1 else v
    return dict(stats)

def validate_pathway(path):
    # Looks critical but only returns boolean not used in final flow
    if not path:
        return False
    cumulative = 0
    for idx, val in enumerate(path):
        if idx % 2 == 0:
            cumulative += val * 3
        else:
            cumulative -= val * 2
    return cumulative % 5 == 0

def analyze_pathway(encoded):
    # Core relevant logic buried among distractions
    flat = [item for sublist in encoded for item in sublist]
    
    # Extract every third element starting from index 1 (key signal trace)
    signal_trace = flat[1::3]
    
    # Apply bitwise masking to isolate diagnostic bits
    masked = [(x & 0b1111) ^ 0b1010 for x in signal_trace]  # XOR mask pattern
    
    # Compute weighted score using modular arithmetic
    weights = [i + 1 for i in range(len(masked))]
    weighted_sum = sum(w * v for w, v in zip(weights, masked))
    
    # Final transformation: mod 97 then scaled by 1.5
    raw_score = weighted_sum % 97
    final_score = raw_score * 1.5
    
    return round(final_score, 6)

# Real input data
raw_genetic_sequence = "ATGCATGCGCGCATTA"

# Step 1: Preprocess sequence into numerical form
numerical_sequence = preprocess_sequence(raw_genetic_sequence)

# Generate irrelevant stability metric (distraction)
stability_index = compute_thermal_stability(numerical_sequence)

# Segment into chunks of 4 (relevant)
segments = [numerical_sequence[i:i+4] for i in range(0, len(numerical_sequence), 4)]

# Encrypt segments — looks important but unused (red herring)
encrypted_segments = [encrypt_segment(seg) for seg in segments]

# Validate each segment pathway — computes but doesn't affect main logic
validation_flags = [validate_pathway(seg) for seg in segments]

# Accumulate meaningless metrics on segment sums (distractor)
sums = [sum(seg) for seg in segments]
metrics_summary = accumulate_metrics(sums)

# Create encoded_segments — this IS the real input to analyze_pathway
encoded_segments = []
for i, seg in enumerate(segments):
    shifted = [(x << 1) | (i % 2) for x in seg]  # Left shift + parity bit
    encoded_segments.append(shifted)

# DEAD CODE PATH: filtering anomalies (never called)
# anomaly_filtered = filter_anomalies([...])

# CORE EXECUTION POINT — this determines the answer
final_diagnostic = analyze_pathway(encoded_segments)

# Print result as required
print(f"Target result: {final_diagnostic}")