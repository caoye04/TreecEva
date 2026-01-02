def generate_sequence(n):
    seq = [1, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq

# Simulate wave interference patterns with weighted phase contributions
def calculate_interference(phases, weights):
    weighted_sum = 0
    normalization_factor = sum(weights)
    temp_results = []
    
    for i, phase in enumerate(phases):
        if i % 2 == 0:
            adjusted_phase = (phase * 1.5) % 360
        else:
            adjusted_phase = (phase * 0.8) % 360
        
        # Irrelevant transformation (distractor)
        mirrored = 360 - adjusted_phase
        temp_results.append(mirrored)
        
        contribution = adjusted_phase * weights[i]
        weighted_sum += contribution

    # Dead code path (distractor)
    if len(temp_results) > 100:
        cleanup_buffer(temp_results)
    
    final_shift = weighted_sum / normalization_factor
    return int(final_shift)  # Discrete phase shift in degrees

# Unused helper (distractor)
def cleanup_buffer(data):
    data.clear()
    return

def main():
    # Generate Fibonacci-based frequency sequence
    freq_seq = generate_sequence(8)
    
    # Extract phase angles from frequencies (simplified physics model)
    raw_phases = [f * 7.5 for f in freq_seq]
    
    # Apply modulo to simulate cyclic phase behavior
    phases = [p % 180 for p in raw_phases]
    
    # Compute corresponding weights based on index position
    weights = []
    for idx in range(len(phases)):
        if idx < 3:
            weight = 1.0
        elif idx < 6:
            weight = 1.8
        else:
            weight = 2.5
        weights.append(weight)
    
    # Track cumulative statistics (semi-relevant but not used in final answer)
    total_power = sum(w ** 2 for w in weights)
    efficiency_ratio = total_power / (len(weights) * 2.5)
    
    # Set of unique phase values (set operation - required feature)
    unique_phases = set(int(p) for p in phases)
    filtered_phases = [p for p in phases if int(p) in unique_phases and p > 40]
    
    # Recalculate weights to match filtered length (maintains consistency)
    filtered_weights = [weights[i] for i in range(len(filtered_phases))]
    
    # Introduce recursive correction factor (simple recursion)
    def correction(depth):
        if depth <= 0:
            return 1
        return 0.95 * correction(depth - 1)
    
    corr_factor = correction(2)
    filtered_weights = [w * corr_factor for w in filtered_weights]
    
    # Final computation point
    net_phase_shift = calculate_interference(filtered_phases, filtered_weights)
    
    # Print result as required
    print(f"Result: {net_phase_shift}")

if __name__ == "__main__":
    main()