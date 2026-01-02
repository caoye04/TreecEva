import itertools

# Simulated sensor array diagnostics with embedded signal processing
def run_diagnostics():
    base_frequency = 57.3
    harmonic_series = [base_frequency * (i + 1) for i in range(7)]
    filtered_bands = list(filter(lambda x: x > 100 and x < 300, harmonic_series))

    # Irrelevant transformation chain (distractor)
    temp_correction = sum([abs(x - base_frequency) for x in harmonic_series])
    normalized_power = [pow(f / max(harmonic_series), 2) for f in harmonic_series]
    weighted_sum = sum(normalized_power[:3]) * 1.75

    # Core data generation (relevant)
    phase_shifts = [int(f % 10) for f in filtered_bands]
    modulation_index = len(filtered_bands) * 2 + phase_shifts[0]

    # Red herring: unused complex structure
    class SignalNode:
        def __init__(self, val):
            self.val = val
        def get_value(self):
            return self.val * 0.95

    node_chain = [SignalNode(x) for x in phase_shifts]

    # Distractor: elaborate but unused calculation
    spectral_entropy = 0.0
    for i in range(1, len(normalized_power)):
        if normalized_power[i] > 0.1:
            spectral_entropy -= normalized_power[i] * __import__('math').log(normalized_power[i])

    # Real processing path (obscured by noise)
    windowed_data = [modulation_index // p if p != 0 else 0 for p in phase_shifts]
    rolling_averages = []
    for i in range(len(windowed_data) - 1):
        avg = (windowed_data[i] + windowed_data[i+1]) / 2
        rolling_averages.append(round(avg))

    # Decoy assignment
    transient_state = (rolling_averages[0] ^ rolling_averages[-1]) & 15

    # Key intermediate values
    system_gain = len(rolling_averages) + 3
    phase_offset = abs(phase_shifts[-1] - phase_shifts[0])

    # Generate multi-stage metric sequence
    metrics = []
    for idx, val in enumerate(rolling_averages):
        if idx % 2 == 0:
            metrics.append(val * 2 + system_gain)
        else:
            metrics.append(val + phase_offset)

    # Use itertools to extend sequence (critical path)
    extended_cycle = itertools.cycle(metrics)
    aggregate_metrics = [next(extended_cycle) for _ in range(system_gain)]

    # Unused permutation branch (dead code path)
    if False:
        permuted = list(itertools.permutations(metrics[:3]))
        perm_sum = sum([p[0] for p in permuted])

    # Final computation — this is the target statement
    final_diagnostic = aggregate_metrics[-1] + phase_offset * system_gain

    # Print result for execution verification
    print(f"Result: {final_diagnostic}")

    return final_diagnostic

# Execute and capture result
diag_result = run_diagnostics()