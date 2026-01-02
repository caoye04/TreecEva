import math

# Simulated sensor data processing with interference
def analyze_sensor_stream(raw_data, threshold=0.7):
    # Irrelevant helper function (dead code path)
    def normalize(v):
        mag = sum(x ** 2 for x in v) ** 0.5
        return [x / mag for x in v] if mag else v

    # Real preprocessing
    cleaned = [x for x in raw_data if isinstance(x, (int, float)) and not math.isnan(x)]
    
    # Bit manipulation red herring
    bit_analysis = 0
    for i in range(len(cleaned)):
        if i % 2 == 0:
            bit_analysis ^= int(cleaned[i]) & 0xF
    
    # Actual signal transformation
    transformed = [math.sin(x * math.pi / 4) for x in cleaned]
    envelope = [abs(x) ** 1.5 for x in transformed]  # Signal power estimation

    # Decoy statistical analysis
    mean_val = sum(envelope) / len(envelope) if envelope else 0
    variance = sum((x - mean_val) ** 2 for x in envelope) / len(envelope) if envelope else 0
    entropy_proxy = -sum(x * math.log(abs(x) + 1e-8) for x in envelope)

    # Real logic: find dominant phase
    phases = [(math.cos(x * math.pi / 2), math.sin(x * math.pi / 2)) for x in cleaned]
    phase_angles = [math.atan2(sin_val, cos_val) for cos_val, sin_val in phases]
    quantized_phases = [int((angle + math.pi) / (math.pi / 2)) % 4 for angle in phase_angles]

    # Distractor: unused frequency analysis
    fft_magnitude = []
    for k in range(4):
        real_part = sum(transformed[n] * math.cos(2 * math.pi * k * n / len(transformed)) for n in range(len(transformed)))
        imag_part = sum(-transformed[n] * math.sin(2 * math.pi * k * n / len(transformed)) for n in range(len(transformed)))
        fft_magnitude.append((real_part ** 2 + imag_part ** 2) ** 0.5)

    # Critical path: filter based on power threshold
    strong_signals = [i for i, e in enumerate(envelope) if e > threshold]
    if not strong_signals:
        strong_signals = [envelope.index(max(envelope))]  # fallback

    # Red herring: complex number conversion (unused)
    analytic_signal = []
    for x in transformed:
        hilbert_imag = sum(transformed[j] * math.sin(math.pi * (i - j)) 
                           for i, j in enumerate(range(len(transformed))))
        analytic_signal.append(complex(x, hilbert_imag / len(transformed) if transformed else 0))

    # Real operation: construct sequence using slicing and modular arithmetic
    base_sequence = (quantized_phases * 3)[len(cleaned): len(cleaned) * 2]
    rotated_seq = base_sequence[2:] + base_sequence[:2]
    downsampled = rotated_seq[::2]

    # Final decision logic with slicing and conditionals
    valid_indices = [i for i in strong_signals if 0 <= i < len(downsampled)]
    final_sequence = [downsampled[i] if i < len(downsampled) else 0 for i in range(max(valid_indices) + 1)]
    
    # Decoy state machine
    state_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
    current_state = 'A'
    for val in cleaned:
        if val > 5:
            current_state = 'B'
        elif val < 0:
            current_state = 'C'

    # Critical execution point
    phase_flag = (len(strong_signals) * 7) % 4 > 1  # boolean control
    filtered_phase = final_sequence[valid_indices][phase_flag]

    # Output required result
    print(f"Result: {filtered_phase}")

    # Irrelevant cleanup
    del raw_data, cleaned, transformed
    return None

# Input data with mixed types and NaNs (simulated sensor noise)
sensor_input = [2.1, 3.8, 'error', float('nan'), 5.2, -1.3, 4.0, 6.7]
analyze_sensor_stream(sensor_input)