import itertools

# System diagnostics and quantum register analysis simulation
def initialize_quantum_routine():
    base_frequency = 42.0
    harmonic_series = [base_frequency * (i + 1) for i in range(7)]
    phase_shifts = [round(h * 0.23, 3) for h in harmonic_series]

    # Irrelevant signal processing (distractor)
    noise_floor = sum([abs(p - 9.66) for p in phase_shifts if p > 10])
    dummy_filter = list(map(lambda x: (x + 1j*x) ** 0.5, harmonic_series))

    quantum_registers = [
        [1, 0, 1, 1],
        [0, 1, 1, 0],
        [1, 1, 0, 0]
    ]

    # Decoy data structure
    legacy_buffers = [[0]*4 for _ in range(3)]
    for i in range(len(legacy_buffers)):
        for j in range(len(legacy_buffers[i])):
            legacy_buffers[i][j] = (i * j + 2) % 3

    # Real calibration sequence
    calibration_sequence = []
    for idx in range(len(quantum_registers[0])):
        bit_sum = sum(reg[idx] for reg in quantum_registers)
        parity_bit = bit_sum % 2
        calibration_sequence.append(parity_bit)

    # Spurious transformation (dead path)
    def obsolete_transform(vec):
        return [v ^ 1 for v in vec][::-1]

    # Another red herring: frequency mixing
    mixed_signals = []
    for a, b in itertools.combinations(harmonic_series[:5], 2):
        mix = round(abs(a - 2*b) / 3.0, 2)
        if mix > 15.0:
            mixed_signals.append(mix)

    # Actual analysis function
    def analyze_register_pair(reg_a, reg_b):
        xor_score = 0
        for i in range(len(reg_a)):
            if reg_a[i] ^ reg_b[i]:
                xor_score += 2**i
        return xor_score

    # Distractor: unused recursive function
    def calculate_entropy(depth, acc=0):
        if depth <= 0:
            return acc
        return calculate_entropy(depth - 1, acc + (depth * 0.33))

    # Key diagnostic logic
    def analyze_system_state(qregs, calib):
        # Step 1: Compute inter-register XOR fingerprints
        fingerprint = 0
        for i in range(len(qregs)):
            for j in range(i+1, len(qregs)):
                score = analyze_register_pair(qregs[i], qregs[j])
                fingerprint ^= score

        # Step 2: Apply calibration mask
        masked_fingerprint = fingerprint
        for k, bit in enumerate(calib):
            if bit == 1:
                mask = 1 << k
                masked_fingerprint |= mask  # Set bit if calibration says so

        # Step 3: Slice-based transformation
        bin_str = bin(masked_fingerprint)[2:]
        if len(bin_str) > 6:
            sliced = bin_str[-6:]  # Take last 6 bits
        else:
            sliced = bin_str.rjust(6, '0')

        # Step 4: Convert back and perturb with fixed offset
        temp_value = int(sliced, 2)
        final_value = temp_value * 17 - 55

        # Irrelevant floating point distraction
        coherence_ratio = sum(phase_shifts) / (base_frequency * 7)
        normalization_factor = round(coherence_ratio * 100, 4)

        return final_value

    # Execute main analysis
    final_diagnostic = analyze_system_state(quantum_registers, calibration_sequence)
    
    # Print result for extraction
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Run simulation
initialize_quantum_routine()