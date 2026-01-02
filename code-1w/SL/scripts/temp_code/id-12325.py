import math

# Simulated sensor data processing with diagnostic analysis
def acquire_signal():
    raw_samples = [i * 0.5 for i in range(20)]
    offset = 7.2
    return [math.sin(x) + 0.3 * math.cos(3 * x) + offset for x in raw_samples]

def filter_noise(signal, cutoff=0.5):
    filtered = []
    for val in signal:
        if abs(val - 7.2) > cutoff:  # arbitrary noise threshold
            filtered.append(val)
    return filtered

def compute_envelope(signal):
    envelope = []
    for val in signal:
        envelope.append(abs(val))
    return envelope

def shift_phase(data, steps=1):
    # Irrelevant transformation - not used in final path
    shifted = data[-steps:] + data[:-steps]
    return shifted

def compress_data(sequence):
    # Dead code path - never called
    return [x for i, x in enumerate(sequence) if i % 2 == 0]

def detect_spikes(envelope, spike_threshold=1.0):
    spikes = []
    for i, val in enumerate(envelope):
        if val > spike_threshold:
            spikes.append(i)
    return spikes

def accumulate_diagnostics(spikes, base_score=10):
    score = base_score
    multiplier = 1
    for idx in spikes:
        if idx % 2 == 0:
            score += idx * 0.5
        else:
            score -= idx * 0.1
        multiplier *= (1 + 0.05 * (idx % 7))
    return int(score * multiplier)

def transform_sequence(raw):
    # Complex but partially irrelevant transformation chain
    temp_a = [x * 1.1 for x in raw]
    temp_b = [y - 7.2 for y in temp_a]  # center around zero
    temp_c = [z ** 2 for z in temp_b]   # square to emphasize magnitude
    smoothed = [sum(temp_c[i:i+3]) / 3 if i+3 <= len(temp_c) else temp_c[i] for i in range(len(temp_c))]
    normalized = [w / max(smoothed) * 10 for w in smoothed] if max(smoothed) > 0 else temp_c
    return normalized

def analyze_pattern(processed, limit):
    total = 0
    contribution = 0
    for val in processed:
        if val > limit:
            total += val * 1.5
            contribution += 1
    if contribution > 0:
        total /= contribution
    return round(total, 6)

# --- Main Execution with Distractors ---
base_data = acquire_signal()

# Irrelevant intermediate variables (red herrings)
decoy_signal = [math.cos(x * 0.7) for x in range(15)]
phase_shifted = shift_phase(decoy_signal, 3)
spurious_sum = sum(phase_shifted) * 0.01  # unused beyond this point

filtered_data = filter_noise(base_data)
envelope_data = compute_envelope(filtered_data)
spike_indices = detect_spikes(envelope_data, 1.5)

# Unused diagnostic branch
if len(spike_indices) > 5:
    preliminary_score = accumulate_diagnostics(spike_indices)
else:
    preliminary_score = 0  # never used

transformed_data = transform_sequence(filtered_data)

# Key threshold derived from constant logic
threshold = len(envelope_data) / 12.0  # evaluates to 1.5

# Critical execution point
final_diagnostic = analyze_pattern(transformed_data, threshold)

# Output result as required
print(f"Target result: {final_diagnostic}")