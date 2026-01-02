def analyze_composition(atomic_sequence):
    unique_atoms = set(atomic_sequence)
    trace_impurities = {atom for atom in unique_atoms if atomic_sequence.count(atom) < 3}
    pure_elements = [atom for atom in atomic_sequence if atom not in trace_impurities]
    pure_elements = pure_elements[::2]  # Sample every other element to reduce noise
    filtration_score = len(pure_elements)
    return filtration_score

# Simulated spectroscopic data sequence
test_sequence = ['C', 'H', 'O', 'C', 'H', 'N', 'C', 'H', 'S', 'O', 'O']
result = analyze_composition(test_sequence)
print(f"Target result: {result}")