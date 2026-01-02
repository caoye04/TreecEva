import math

def generate_wave_sequence(length, frequency, phase=0):
    # Irrelevant helper function – dead end for reasoning
    return [math.sin(2 * math.pi * frequency * (i / length) + phase) for i in range(length)]

def analyze_harmonic_profile(signal):
    # Distractor: looks important but unused in final result
    magnitude = sum(s**2 for s in signal)
    peak = max(signal)
    return {'magnitude': magnitude, 'peak': peak}

def shift_phase_components(phases, offset):
    # Red herring function: modifies list but not used in critical path
    for i in range(len(phases)):
        phases[i] = (phases[i] + offset) % (2 * math.pi)
    return None

def calculate_interference(seq1, seq2):
    # Core logic hidden among distractions
    weights = [0.5, 1.0, 0.75, 1.25, 0.9]
    accumulator = 0.0
    temp_buffer = []
    
    for i in range(min(len(seq1), len(seq2))):
        if i % 4 == 0:
            # Conditional weighting based on index
            factor = weights[i % len(weights)]
        elif i % 3 == 0:
            factor = 1.1
        else:
            factor = 0.8
            
        product = seq1[i] * seq2[i] * factor
        temp_buffer.append(product)
        
        # Accumulate only every second non-zero contribution
        if product > 0 and i % 2 == 1:
            accumulator += product * 1.5
        
        # Early termination red herring – never triggers due to data range
        if accumulator > 1e6:
            break
    
    # Real answer derived from sum with damping
    interference_score = sum(temp_buffer) * 0.65
    
    # Decoy transformation
    transformed = [math.cos(x) for x in temp_buffer if x > 0.5]
    dummy_sum = sum(transformed)
    
    return interference_score

# Main execution block
if __name__ == "__main__":
    # Generate two synthetic signal patterns using trigonometric sequences
    base_indices = list(range(1, 17))
    pattern_a = [math.tan(i * 0.2) if i % 5 != 0 else 0.1 for i in base_indices]
    pattern_b = [math.log(abs(math.cos(i * 0.3)) + 0.1) for i in base_indices]
    
    # Irrelevant pre-processing steps
    filtered_a = [x for x in pattern_a if x > -1.0]
    filtered_b = [x for x in pattern_b if x < 0.5]
    set_a = set(filtered_a)
    set_b = set(filtered_b)
    overlap_count = len(set_a.intersection(set_b))
    
    # Dummy phase tracking array
    phase_states = [0.1, 0.3, 0.7, 1.1, 1.5, 2.0]
    shift_phase_components(phase_states, 0.5)
    
    # Key computation
    net_phase_shift = calculate_interference(pattern_a, pattern_b)
    
    # Unused combinatorics distraction
    combo_total = 0
    for i in range(1, min(5, len(pattern_a))):
        combo_total += math.comb(len(pattern_a), i)
    
    # Output target result
    print(f"Result: {net_phase_shift}")