def simulate_neural_pathway(signal_strength, noise_threshold=0.15):
    import math
    
    # Irrelevant signal preprocessing (distractor)
    raw_spectrum = [math.sin(x * 0.1) + signal_strength for x in range(10)]
    filtered_spectrum = [x for x in raw_spectrum if abs(x) > noise_threshold]
    spectral_entropy = sum([abs(x) for x in filtered_spectrum]) / (len(filtered_spectrum) + 1)

    # Core activation logic
    neuron_states = []
    for i in range(8):
        phase_shift = math.cos(i * 0.5)
        activated = (signal_strength * phase_shift) > (noise_threshold * 2)
        neuron_states.append(activated)
    
    # Decoy neural cluster (dead path)
    decoy_activations = []
    for j in range(5):
        dummy_val = (j ** 2) % 7
        decoy_activations.append(dummy_val > 2)
    
    # Real pathway analysis
    critical_nodes = {i for i, active in enumerate(neuron_states) if active}
    backup_nodes = {x for x in range(10) if x % 3 == 0}
    
    # Misleading intermediate score
    shadow_metric = len(decoy_activations) + sum([1 for x in decoy_activations if x])
    
    # Key set operations and control flow
    if len(critical_nodes) > 3:
        expanded_coverage = critical_nodes.union(backup_nodes)
        pruned_coverage = expanded_coverage.difference({0, 1})
        high_activity = {n for n in pruned_coverage if n % 2 == 1}
        
        # Simulated temporal gating
        gated_sequence = []
        for step in range(6):
            if step % 2 == 0:
                gated_sequence.append(step in high_activity)
            else:
                gated_sequence.append(False)
        
        # Conditional efficiency factor (looks complex but deterministic)
        if all(gated_sequence[::2]):
            efficiency_factor = 13
        elif any(gated_sequence[::2]):
            efficiency_factor = 7
        else:
            efficiency_factor = 3
        
        # Distractor: unused transformation chain
        temp_grid = [[i + j for j in range(3)] for i in range(3)]
        flattened = [item for row in temp_grid for item in row]
        normalized = [x / max(flattened) for x in flattened]
        
        # Critical execution point
        activated_paths = high_activity.intersection({1, 3, 5, 7, 9})
        filtration_score = len(activated_paths) * efficiency_factor // 2
        
        # Unused derived metrics (red herrings)
        coherence_index = len(normalized) * efficiency_factor / (len(activated_paths) + 1)
        dispersion_ratio = len(pruned_coverage) / (len(critical_nodes) + 0.5)
        
        return filtration_score
    else:
        # Fallback that won't trigger
        fallback_score = int(math.log(len(critical_nodes) + 1) * 100)
        return fallback_score - 50

# Trigger execution with specific input
result = simulate_neural_pathway(0.85)
print(f"Result: {result}")