from collections import defaultdict
import math

# Simulated material testing framework with decoy computations

def analyze_failure_modes(data, threshold=0.75):
    # Irrelevant function: analyzes failure modes but not used in final calculation
    critical_modes = []
    for entry in data:
        if entry['stress'] > threshold and entry['temp'] > 300:
            critical_modes.append(entry['mode'])
    return len(critical_modes)  # Dead end


def compute_resilience_index(values):
    # Misleading function: computes resilience but never called
    base = sum([v**0.5 for v in values if v > 0])
    penalty = len([v for v in values if v < -1]) * 0.5
    return round(base - penalty, 3)


def evaluate_stress_sequence(sequence):
    # Distractor: processes sequences but unused
    total_shift = 0
    for i in range(len(sequence)):
        if i % 2 == 0:
            total_shift ^= int(sequence[i] * 10)  # Bitwise red herring
    return total_shift


def calculate_strain_response(inputs, params):
    # Core logic buried in distractions
    strain_map = defaultdict(float)
    temp_offset = params.get('temp_comp', 0.0)
    non_linear_factor = params['factor'] ** 2 + 0.1

    # Decoy initialization
    debug_log = []
    _ = [debug_log.append(f"Step {i}") for i in range(2)]  # Useless list comp

    intermediate_results = []
    for idx, reading in enumerate(inputs):
        # Real computation mixed with noise
        base_strain = reading * non_linear_factor

        # Conditional expression (required feature)
        adjustment = 0.3 if idx in [1, 3] else (0.15 if base_strain > 4.0 else 0.05)

        # Real logic step
        adjusted = base_strain + adjustment + temp_offset

        # Store in map (dictionary operation)
        strain_map[f'strain_{idx}'] = round(adjusted, 4)

        # Only every second valid reading contributes to result
        if idx % 2 == 0:
            intermediate_results.append(adjusted * 0.9)

    # Final transformation
    raw_sum = sum(intermediate_results)
    penalty_factor = math.log(strain_map['strain_0'] + 1)  # Depends on first element
    final_value = raw_sum - penalty_factor

    # One last adjustment based on map size (relevant!)
    if len(strain_map) > 3:
        final_value += 0.25

    return round(final_value, 6)

# Main execution with red herrings
if __name__ == "__main__":
    # Input data - realistic sensor readings
    stress_levels = [1.8, 2.4, 3.1, 4.0, 2.2]

    # Configuration with misleading keys
    config = {
        'factor': 1.7,
        'temp_comp': -0.05,
        'max_iter': 10,
        'debug_mode': True,
        'threshold': 0.8
    }

    # Unused variables (distractors)
    material_samples = [("A7X", 1.8), ("B9Y", 2.4), ("C3Z", 3.1)]
    sample_counter = defaultdict(int)
    for code, val in material_samples:
        sample_counter[code] += 1  # Never used

    # Fake preprocessing
    normalized = [x / max(stress_levels) for x in stress_levels]
    _ = [x for x in normalized if x > 0.5]  # Discarded

    # Critical statement
    final_yield = calculate_strain_response(stress_levels, config)

    # Print required output
    print(f"Result: {final_yield}")