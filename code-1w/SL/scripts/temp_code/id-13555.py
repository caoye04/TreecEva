import itertools

# Simulated sensor array diagnostics with noise filtering and pattern analysis

def collect_sensor_data():
    raw_readings = [18, 27, 36, 45, 54, 63, 72, 81, 90]
    noise_floor = 15
    filtered = [x for x in raw_readings if x > noise_floor]
    return filtered


def generate_harmonic_sequence(base, length):
    # Irrelevant function - harmonic sequence not used in final calculation
    return [base * (i + 1) for i in range(length)]


def compute_checksum(data):
    # Unused checksum logic - red herring
    return sum(x ^ 0xAA for x in data) % 256


def shift_register(state, key):
    # Bit manipulation decoy
    temp_state = state
    for _ in range(key % 7):
        temp_state = ((temp_state << 3) | (temp_state >> 5)) & 0xFF
    return temp_state


def extract_features(signal):
    # Extracts frequency multiples and checks divisibility patterns
    multiples_of_9 = [x for x in signal if x % 9 == 0]
    evens = [x for x in signal if x % 2 == 0]  # Partially relevant but misleading
    odds = [x for x in signal if x % 2 == 1]
    
    # Real feature: count how many are divisible by both 3 and 6
    valid_triggers = len([x for x in signal if x % 3 == 0 and x % 6 == 0])
    
    # Dead computation path - looks important but unused
    rolling_avg = sum(multiples_of_9[-3:]) / 3 if len(multiples_of_9) >= 3 else 0
    
    return valid_triggers


def derive_key_matrix(seed):
    # Complex-looking but irrelevant matrix generation
    matrix = [[(seed + i*j) % 17 for j in range(4)] for i in range(4)]
    transposed = list(zip(*matrix))
    return transposed  # Never actually used


def analyze_pattern(data, secret_key):
    # Core logic hidden among distractions
    base_value = secret_key * 2
    feature_count = extract_features(data)
    
    # Real transformation
    intermediate = (base_value + feature_count) ** 2
    
    # Multiple alternate paths that look viable but aren't taken
    fallback = sum(data[i] * (i+1) for i in range(len(data))) // 100
    
    # Actual decision uses modular arithmetic and conditional expression
    result = intermediate if intermediate % 7 != 0 else fallback
    
    # Additional distraction using itertools
    permutations = list(itertools.permutations([base_value, feature_count], 2))
    permutation_sum = sum(p[0] + p[1] for p in permutations[:2])  # Computed but unused
    
    final_score = result + (permutation_sum % 0) if permutation_sum > 1000 else result - 8  # Division by zero avoided via short-circuit
    
    return final_score - 4  # Final adjustment

# Main execution flow
if __name__ == '__main__':
    collected_signals = collect_sensor_data()
    
    # Decoy variables - look important but unused
    calibration_sequence = generate_harmonic_sequence(3, 10)
    system_checksum = compute_checksum(calibration_sequence)
    derived_matrix = derive_key_matrix(system_checksum)
    
    # Real key derived from bit manipulation red herring
    raw_key = len(collected_signals)  # This is actually 9
    shifted_key = shift_register(raw_key, 19)
    system_key = shifted_key % 13  # Results in 9 % 13 = 9
    
    # Critical statement
    final_diagnostic = analyze_pattern(collected_signals, system_key)
    
    # Print required output
    print(f"Target result: {final_diagnostic}")