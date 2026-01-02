import math

# Simulated sensor grid processing with diagnostic metrics

def analyze_pattern(sequence, pivot):
    if len(sequence) < 2:
        return 0
    weighted_sum = sum(x * (i + 1) for i, x in enumerate(sequence))
    return weighted_sum % pivot


def generate_sequence(seed, length):
    seq = [seed]
    for i in range(1, length):
        next_val = (seq[-1] * 7 + 3) % 11
        seq.append(next_val)
    return seq

def compute_entropy(data):
    # Irrelevant entropy calculation - red herring
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 6)

def shift_window(grid, offset):
    # Misleading transformation - unused in final result
    shifted = []
    for row in grid:
        shifted.append([row[(i - offset) % len(row)] for i in range(len(row))])
    return shifted

def detect_anomalies(grid):
    # Dead code path - never called but looks important
    anomalies = []
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val > 7 and (i + j) % 3 == 0:
                anomalies.append((i, j, val))
    return anomalies

def filter_signals(signal_stream):
    # Unused signal filtering function - distractor
    filtered = [x for x in signal_stream if x % 2 == 1]
    return [x for x in filtered if x > 3]

def aggregate_metrics(buffer, threshold):
    # Core logic: combine multiple metrics across layers
    flat_data = [item for sublist in buffer for item in sublist]
    base_score = sum(flat_data) * threshold
    
    # Apply modular correction based on pattern analysis
    pattern_seq = generate_sequence(threshold, 5)
    pivot_correction = analyze_pattern(pattern_seq, 9)
    
    # Bit manipulation layer - relevant but masked by noise
    magic_factor = 0
    for idx, val in enumerate(pattern_seq):
        if val % 2 == 0:
            magic_factor ^= (val << 1) | (idx & 1)
    
    # Decoy computation with sets - looks important but not used directly
    unique_values = set(flat_data)
    expected_set = set(range(1, 8))
    missing_count = len(expected_set - unique_values)
    
    # Actual formula: base_score + pivot_correction - (magic_factor mod 5)
    intermediate = base_score + pivot_correction
    adjustment = magic_factor % 5
    final_score = intermediate - adjustment
    
    # Final thresholding gate
    return final_score if final_score > 0 else -1 * final_score

# Main execution flow
if __name__ == "__main__":
    # Initialize sensor grid (real data source)
    raw_input_grid = [
        [2, 3, 1, 4],
        [5, 2, 6, 3],
        [1, 4, 2, 5],
        [3, 1, 4, 2]
    ]
    
    # Activation parameters
    activation_threshold = 7
    calibration_offset = 3  # Unused parameter - red herring
    
    # Irrelevant preprocessing steps
    normalized_grid = [[round(cell / 2.5) for cell in row] for row in raw_input_grid]
    transposed_grid = list(zip(*raw_input_grid))  # Looks important, unused
    indexed_scan = list(enumerate([sum(row) for row in raw_input_grid]))
    
    # Buffer preparation - only this matters
    grid_buffer = raw_input_grid  # Critical assignment
    
    # Decoy operations with list comprehensions and zip
    spectral_analysis = [
        sum(col) * (i + 1) for i, col in enumerate(zip(*normalized_grid))
    ]
    correlation_matrix = [
        [a ^ b for a, b in zip(row, raw_input_grid[i])] 
        for i, row in enumerate(normalized_grid)
    ]
    
    # Key statement
    final_diagnostic = aggregate_metrics(grid_buffer, activation_threshold)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")