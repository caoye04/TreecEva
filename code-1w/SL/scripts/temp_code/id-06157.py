def analyze_signal_strength(signal_sequence):
    total_power = 0
    power_log = []
    for i, signal in enumerate(signal_sequence):
        adjusted_power = signal * (i + 1)
        if adjusted_power > 50:
            clipped = 50
        else:
            clipped = adjusted_power
        total_power += clipped
        power_log.append(clipped)
    
    # Irrelevant normalization (distractor)
    normalized_powers = [p / max(power_log) for p in power_log if p > 0]
    avg_normalized = sum(normalized_powers) / len(normalized_powers) if normalized_powers else 0

    return total_power


def calculate_interference_phase(phases, impact_weights):
    base_phase = 0
    temp_storage = {}
    shift_accumulator = 0
    
    for idx, (phase, weight) in enumerate(zip(phases, impact_weights)):
        # Real contribution to result
        weighted_delta = phase * weight
        shift_accumulator += weighted_delta
        
        # Dead code: stored but never used
        temp_storage[f'entry_{idx}'] = {
            'raw': phase,
            'weighted': weighted_delta,
            'index_sq': idx * idx
        }
        
        # Simulated interference reflection (no effect)
        reflection_factor = (idx % 3) ** 0.5 if idx % 3 != 0 else 0
        dummy_reflection = phase * reflection_factor
        _ = dummy_reflection  # Unused

    # Actual answer computation
    net_phase_shift = int(shift_accumulator % 1000)
    
    # Additional red herring variables
    theoretical_max = sum(impact_weights) * max(phases)
    efficiency_ratio = shift_accumulator / theoretical_max if theoretical_max else 0
    
    return net_phase_shift

# Main execution
if __name__ == '__main__':
    raw_signals = [12, 15, 22, 8, 43, 19]
    frequency_shifts = [3.5, -2.1, 7.8, 1.3, -5.6, 4.2]
    influence_weights = [0.8, 1.3, 0.9, 2.1, 1.7, 0.6]
    
    # Irrelevant preprocessing (distractor)
    scaled_signals = [sig * 1.5 for sig in raw_signals]
    filtered_signals = [s for s in scaled_signals if s > 20]
    
    # Real data used in logic
    processed_shifts = [round(s * 2) / 2 for s in frequency_shifts]  # Snap to 0.5 intervals
    
    # Meaningless aggregation
    cumulative_product = 1
    for val in influence_weights[:3]:
        cumulative_product *= int(val)
    
    # Key call that produces the answer
    net_phase_shift = calculate_interference_phase(processed_shifts, influence_weights)
    
    # Final output
    print(f"Result: {net_phase_shift}")