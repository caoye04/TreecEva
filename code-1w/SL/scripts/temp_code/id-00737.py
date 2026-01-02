def preprocess_signal(data, threshold=0.5):
    """Irrelevant preprocessing function for signal smoothing (dead code path)."""
    return [x for x in data if abs(x) > threshold]


def compute_entropy(sequence):
    """Misleading entropy computation (decoy function)."""
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return round(entropy, 6)

# Irrelevant sensor simulation constants (distractor variables)
CALIBRATION_OFFSETS = [0.12, -0.05, 0.33, 0.08, -0.21]
MAX_BUFFER_SIZE = 256
SENSOR_NOISE_FLOOR = 0.007

# Core data structures with mixed relevance
grid_buffer = [
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0],
    [1, 1, 1, 0]
]

activation_chain = [True, False, True, True]

# Misleading intermediate metrics (red herring variables)
baseline_correction = sum(sum(row) for row in grid_buffer) / len(grid_buffer)**2
normalization_factor = len(activation_chain) * 0.75
auxiliary_score = 0
for i, row in enumerate(grid_buffer):
    for j, val in enumerate(row):
        auxiliary_score += (i + j) * val  # Distraction: unused later

# Simulated timestamp processing (irrelevant loop)
current_timestamps = []
for t in range(13):
    if t % 4 == 0:
        current_timestamps.append(t * 17 + 3)

# Decoy transformation using string methods (distractor logic)
status_codes = ['OK', 'ERR', 'OK', 'PEND', 'OK']
status_flags = [1 if s == 'OK' else 0 for s in status_codes]
padded_flags = ''.join(map(str, status_flags)).zfill(16)

# Real computation begins here — counting active zones with neighbor influence
def count_active_with_neighbors(matrix):
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                neighbors = 0
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and matrix[ni][nj] == 1:
                        neighbors += 1
                if neighbors >= 2:
                    count += 1
    return count

# Secondary logic: determine effective chain length based on activation pattern
def get_effective_chain_length(chain):
    if not any(chain):
        return 0
    first = chain.index(True)
    last = len(chain) - 1 - chain[::-1].index(True)
    return last - first + 1

# Main aggregation function — this is where the answer comes from
def aggregate_metrics(buffer, activations):
    raw_count = count_active_with_neighbors(buffer)
    chain_length = get_effective_chain_length(activations)
    
    # Complex interaction: modulation via activation span and grid density
    density = sum(sum(row) for row in buffer) / (len(buffer) * len(buffer[0]))
    
    # Integer division and modular arithmetic to obscure logic
    modulated_score = (raw_count * chain_length) // max(1, int(density * 10))
    adjustment = (modulated_score % 7) - 3
    
    # Final transformation using enumerate and zip (required Python features)
    temporal_weights = [0.8, 1.1, 0.9, 1.2]
    weighted_sum = 0
    for idx, (act, weight) in enumerate(zip(activations, temporal_weights)):
        if act:
            weighted_sum += (idx + 1) * weight
    
    # Key formula combining multiple concepts
    result = int(modulated_score + adjustment + weighted_sum)
    return result

# Dead code branch — never executed (misdirection)
if __name__ == "__fake_main__":
    debug_trace = preprocess_signal([-0.2, 0.0, 0.7, -1.0])
    print("Debug mode inactive")

# Execution point of interest
final_diagnostic = aggregate_metrics(grid_buffer, activation_chain)

# Print required output
print(f"Result: {final_diagnostic}")