import math

# Simulated sensor grid diagnostics with interference logic
def generate_noise_sequence(length):
    return [((i ** 2 + 3 * i + 7) % 89) for i in range(length)]

def preprocess_signal(raw_signal):
    filtered = []
    for x in raw_signal:
        if x % 2 == 0:
            filtered.append(x // 3)
        else:
            filtered.append(x * 2)
    return [val for val in filtered if val > 0]

def compute_entropy(data):
    # Irrelevant entropy calculation (distractor)
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)

def evaluate_health_status(diag_matrix):
    # Dead code path - never actually used in final computation
    health_score = 0
    for row in diag_matrix:
        for val in row:
            health_score += (val % 7) ** 1.5
    return int(health_score % 100)

def decode_hidden_flag(metadata_log):
    # Decoy function: processes unrelated string transformations
    result = ''
    for entry in metadata_log:
        if len(entry) % 2 == 0:
            result += chr((ord(entry[0]) + 5) % 127)
        else:
            result += chr((ord(entry[-1]) - 3) % 127)
    return result.encode('utf-8').hex()

def shift_pattern(sequence, offset):
    # Bit manipulation red herring
    shifted = []
    for num in sequence:
        transformed = (num << 1) ^ offset
        transformed = transformed % 100
        shifted.append(transformed)
    return shifted

def build_logic_template(base_values):
    # Constructs a 5x5 grid using modular arithmetic and conditional fills
    grid = [[0]*5 for _ in range(5)]
    idx = 0
    for i in range(5):
        for j in range(5):
            if (i + j) % 3 == 0:
                grid[i][j] = (base_values[idx % len(base_values)] + i * j) % 47
                idx += 1
            elif i == j:
                grid[i][j] = (base_values[-(idx % len(base_values)) - 1] ** 2) % 53
            else:
                grid[i][j] = abs(i - j) * 3 + 2
    return grid

def activate_filters(grid, level):
    # Applies irrelevant transformation filters (not part of main logic)
    modified = [row[:] for row in grid]
    mask = [[(i * j + level) % 5 for j in range(5)] for i in range(5)]
    for i in range(5):
        for j in range(5):
            modified[i][j] ^= mask[i][j]
    return modified

def count_activations(grid, threshold):
    # Counts how many elements exceed threshold (used in final step)
    count = 0
    total = 0
    for row in grid:
        for val in row:
            total += val
            if val > threshold:
                count += 1
    return count, total

def analyze_pattern(grid, limit):
    # Core logic: counts activations above limit, uses dictionary to map results
    activation_count, sum_total = count_activations(grid, limit)
    
    # Real mapping logic with distractors
    decision_map = {
        'baseline': 42,
        'peak': None,
        'adjustment': 0,
        'scale_factor': -1,
        'version': 'diagnostic_v3'
    }
    
    # Meaningful branching based on activation count
    if activation_count > 10:
        decision_map['adjustment'] = 7
    elif activation_count > 5:
        decision_map['adjustment'] = 3
    else:
        decision_map['adjustment'] = 1
    
    # Final computation path
    reference_key = 'adjustment'
    adjustment_value = decision_map[reference_key]
    
    # Apply combinatorial correction
    correction = 0
    for i in range(1, min(activation_count, 8)):
        if i % 2 == 0:
            correction += i * adjustment_value
        else:
            correction -= (adjustment_value + i) // 2
    
    intermediate_result = sum_total + correction
    
    # Final answer depends only on this line
    final_diagnostic = (intermediate_result * adjustment_value) % 99997
    
    # Unused variables - red herrings
    diagnostic_token = decode_hidden_flag(['error', 'retry', 'sync'])
    noise_profile = generate_noise_sequence(10)
    entropy_metric = compute_entropy(noise_profile)
    shifted_data = shift_pattern(noise_profile, 7)
    health_status = evaluate_health_status([[1,2],[3,4]])
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    signal_input = [13, 17, 23, 31, 37, 41]
    processed_signal = preprocess_signal(signal_input)
    logic_grid = build_logic_template(processed_signal)
    activation_threshold = 25
    modified_grid = activate_filters(logic_grid, 4)  # Result not used
    final_diagnostic = analyze_pattern(logic_grid, activation_threshold)
    print(f"Result: {final_diagnostic}")