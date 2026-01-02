def analyze_signal(data_stream):
    # Irrelevant preprocessing (distractor)
    filtered = [x for x in data_stream if x > 0]
    normalized = [x / max(filtered) for x in filtered]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]

    # Decoy transformation chain (dead path)
    transformed = []
    for val in data_stream:
        if val % 7 == 0:
            transformed.append(val ** 0.5)
        elif val % 3 == 0:
            transformed.append(val // 2)
        else:
            transformed.append(val)

    # Real computation begins: signal decomposition
    base_frequency = len(data_stream) % 13
    phase_shift = sum(data_stream[i] * i for i in range(len(data_stream))) % 11

    # Generate harmonic envelope (partially relevant)
    envelope = []
    for i in range(len(data_stream)):
        sample = data_stream[i]
        modulated = sample * ((i + 1) % base_frequency + 1)
        envelope.append(modulated)

    # Slice-based pattern extraction (key operation)
    segment_a = envelope[2:9:2]  # indices 2,4,6,8
    segment_b = envelope[-1:-6:-1]  # last 5 in reverse
    pivot = (sum(segment_a) // len(segment_a)) % 100

    # Red herring: FFT-like dummy (irrelevant)
    fft_approx = []
    for k in range(8):
        real = sum(envelope[n] * (n % (k + 1) + 1) for n in range(0, min(len(envelope), 10)))
        fft_approx.append(real % 1000)

    # Core logic: derive sequences and positions
    temp_seq = [pivot]
    for _ in range(6):
        next_val = (temp_seq[-1] * 7 + 13) % 97
        temp_seq.append(next_val)

    final_sequence = temp_seq[1:6]  # actual sequence used

    # Determine access pattern
    positions = [
        (phase_shift * 2) % 5,
        (phase_shift + pivot) % 5,
        (base_frequency * pivot) % 5  # index into final_sequence
    ]

    # Distractor: unused alternate checksums
    alt_checksum_1 = sum(final_sequence[i] for i in range(0, len(final_sequence), 2))
    alt_checksum_2 = final_sequence[0] ^ final_sequence[-1]
    temp_result = alt_checksum_1 * alt_checksum_2 % 41

    # Critical parameters (only one used)
    correction_factor = base_frequency - 3
    offset = (phase_shift * 2) - 10
    dummy_offset = sum(smoothed) * 100  # never used
    scaling_matrix = [[i + j for j in range(3)] for i in range(3)]  # decoy

    # Key statement
    checksum = final_sequence[positions[2]] * correction_factor + offset

    # Output only the target result
    print(f"Result: {checksum}")

# Input data (deterministic)
signal_data = [12, 7, 3, 8, 15, 6, 2, 9, 4, 11, 5]
analyze_signal(signal_data)