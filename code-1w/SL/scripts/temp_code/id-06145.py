import itertools

# Simulated sensor data processing with embedded logic chain and distractions
def collect_telemetry():
    raw_samples = [i * 0.7 + ((i % 3) ** 1.5) for i in range(120)]
    return [x for x in raw_samples if x > 10][:50]


def filter_noise(data, threshold=15.0):
    # Real filtering used later
    filtered = [x for x in data if abs(x - 18.2) > 2.1]
    temp_correction = sum([i for i in range(len(filtered)) if i % 4 == 0]) / 2.0  # red herring
    return [x + 0.1 for x in filtered]


def compute_checksum(sequence):
    # Unused decoy function
    return sum(x * (i+1) for i, x in enumerate(sequence)) % 1000


def generate_reference_map():
    # Dead code path — never called
    ref_map = {}
    for k, v in enumerate(itertools.product('AB', repeat=3)):
        ref_map[k] = ''.join(v)
    return ref_map

# Global decoy state
system_flags = {"calibrated": False, "legacy_mode": True, "debug_lock": 773}
active_channels = [1, 1, 0, 1, 1, 0, 0, 1]

# Signal shaping with distractor operations
def shape_pulse_envelope(signal):
    envelope = []
    accumulator = 0.0
    for idx, val in enumerate(signal):
        if idx % 5 == 0 and idx > 0:
            accumulator += 0.5
        phase_shift = (idx % 7) // 3.5
        adjusted = val * 0.9 + phase_shift - accumulator
        envelope.append(round(adjusted, 3))
    
    # Irrelevant transformations
    mirror_image = [envelope[-i] for i in range(1, len(envelope), 3)][:15]
    _ = [x * 1.1 for x in mirror_image if x < 12]  # dead computation
    
    return envelope

# Core transformation pipeline
def process_frameset(frames):
    indexed = list(enumerate(frames))
    paired = list(zip([x[1] for x in indexed[::2]], [x[1] for x in indexed[1::2]]))
    
    # Real operation: differential encoding
    differentials = []
    for a, b in paired:
        diff = abs(a - b) * 0.5
        if diff > 1.0:
            differentials.append(diff)
    
    # Fake aggregation path
    dummy_agg = 0
    for i in range(len(paired)):
        dummy_agg += (i * paired[i][0]) % 4
    dummy_agg *= 0.0  # neutralize but looks important
    
    return differentials

# Critical analysis function
final_diagnostic = 0
baseline_offsets = []

for offset in range(3, 13, 3):
    baseline_offsets.append((offset ** 2) % 7)

# Main execution flow
sensor_data = collect_telemetry()
noise_filtered = filter_noise(sensor_data)
signal_envelope = shape_pulse_envelope(noise_filtered)
processed_frames = process_frameset(signal_envelope)

# This checksum is unused — distraction
_ = compute_checksum(processed_frames + [sum(processed_frames)])

# Real diagnostic logic buried among noise
def analyze_signal(seq):
    total_energy = sum(x ** 2 for x in seq)
    peak = max(seq) if seq else 0
    count_above = len([x for x in seq if x > 2.5])
    
    # Distractor: complex weight matrix (unused)
    weights = [[(i*j) % 4 for j in range(4)] for i in range(4)]
    penalty = 0
    for w_row in weights:
        for w in w_row:
            penalty += w * 0.01
    
    # Actual formula
    diagnostic_score = int((total_energy * 1.7) + (peak * 12) + (count_above * 5) - (penalty * 100))
    return diagnostic_score

final_diagnostic = analyze_signal(processed_frames)

# Output required format
print(f"Target result: {final_diagnostic}")