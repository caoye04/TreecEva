import math

def analyze_pattern(seq):
    # Irrelevant function: analyzes frequency but not used in final result
    freq = {x: seq.count(x) for x in set(seq)}
    return sum(k * v for k, v in freq.items()) if seq else 0

def decoy_transformation(data):
    # Dead path: complex-looking but unused transformation
    shifted = [(x >> 2) ^ 3 for x in data]
    return [math.sin(x) for x in shifted if x % 2 == 1]

def compute_entropy(values):
    # Unused entropy calculation (red herring)
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def shift_sequence(arr, key):
    # Misleading shift operation with no impact on answer
    rotated = arr[-key:] + arr[:-key]
    return [x + 1 if i % 2 else x for i, x in enumerate(rotated)]

def evaluate_stability(index, value):
    # Decoy logic with plausible-sounding name
    if index < 0:
        return value ** 2
    elif index % 3 == 0:
        return int(math.sqrt(abs(value)))
    return abs(value) - index

def extract_core_features(dataset):
    # Irrelevant feature extraction (not connected to output)
    features = []
    for i, val in enumerate(dataset):
        if val % 4 == 0:
            features.append(i * 2 + (val & 7))
    return features

def process_state(state_vector):
    # Core logic embedded within distractions
    
    # Distractor variables
    temp_buffer = [x * 2 + 1 for x in state_vector if x < 5]  # Unused
    checksum = sum(x ^ (i + 1) for i, x in enumerate(state_vector)) * 0.5  # Misleading intermediate
    
    # Key computation chain begins
    filtered = [x for x in state_vector if x >= 3]  # Step 1: filter values >= 3
    scaled = [x * 1.5 for x in filtered]  # Step 2: scale by 1.5
    
    # Conditional transformation
    adjusted = []
    for i, val in enumerate(scaled):
        if i % 2 == 0:
            adjusted.append(val + 2.5)  # Even indices: add 2.5
        else:
            adjusted.append(val - 1.75)  # Odd indices: subtract 1.75
    
    # Tuple unpacking and arithmetic
    a, b, c = adjusted[0], adjusted[1], adjusted[2]  # Assume at least 3 elements
    derived = (a + b) * c  # Step 3: combine via (a+b)*c
    
    # Bit manipulation red herring
    mask = 0b1101
    decoy_result = derived ^ mask | (mask << 2)  # Looks important, unused
    
    # Final core logic
    exponent_part = math.log(abs(derived) + 1)  # Step 4: log transform
    thermodynamic_potential = round(exponent_part * 1000, 4)  # Step 5: scale and round
    
    # Unused control flow
    if thermodynamic_potential > 1000:
        thermodynamic_potential /= 2
    elif len(str(thermodynamic_potential)) > 6:
        thermodynamic_potential += 50

    # Distractor data structure
    diagnostics = {
        'raw_length': len(state_vector),
        'peak_value': max(state_vector),
        'stability_metric': evaluate_stability(-1, len(state_vector)),
        'pattern_score': analyze_pattern(state_vector)
    }
    
    return thermodynamic_potential  # Only this matters

# Main execution
state_vector = [2, 3, 4, 5]
baseline_offset = 17.5  # Unused global
reference_table = {'a': 1, 'b': 2, 'c': 3}  # Dead data structure

# Trigger key computation
final_output = process_state(state_vector)

# Print required result
print(f"Result: {final_output}")