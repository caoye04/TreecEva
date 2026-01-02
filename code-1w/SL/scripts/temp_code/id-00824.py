from collections import defaultdict
import math

# Irrelevant helper (dead function - red herring)
def compute_entropy(data):
    total = sum(data.values())
    return sum(-v/total * math.log2(v/total) for v in data.values() if v > 0)

# Unused transformation matrix (distractor)
transform_matrix = [
    [1.1, -0.3, 0.7],
    [0.4, 2.2, -0.8],
    [-0.6, 0.5, 1.3]
]

# Misleading intermediate variables
temp_cache = {}
redundant_sum = 0
offset_key = 17

# Real logic begins: signal processing simulation
def preprocess_grid(raw_grid):
    processed = []
    for row in raw_grid:
        new_row = []
        for val in row:
            # Apply non-linear scaling (relevant)
            scaled = int(math.sqrt(val ** 2 + 1)) % 100
            new_row.append(scaled)
        processed.append(new_row)
    return processed

# Bit manipulation decoy (looks important but unused)
def obfuscate_key(n):
    n = ((n << 3) & 0xFF) | (n >> 5)
    n ^= 0b10101010
    n = (n * 0x45D9F31) & 0xFFFFFFFF
    return n

# Another red herring: statistical outlier detection (unused)
def detect_outliers(arr):
    mean = sum(arr) / len(arr)
    variance = sum((x - mean) ** 2 for x in arr) / len(arr)
    std_dev = math.sqrt(variance)
    return [i for i, x in enumerate(arr) if abs(x - mean) > 2 * std_dev]

# Core transformation logic (key path)
def apply_phase_shift(grid, shift):
    shifted = []
    for i, row in enumerate(grid):
        shifted_row = []
        for j, val in enumerate(row):
            # Conditional phase application based on position
            if (i + j) % 2 == 0:
                shifted_row.append(val ^ shift)  # XOR with shift
            else:
                shifted_row.append(val)
        shifted.append(shifted_row)
    return shifted

# Aggregation with lambda and slicing (critical)
def aggregate_diagonals(grid):
    size = len(grid)
    diag_sum = 0
    # Extract main diagonal and anti-diagonal using slicing
    for i in range(size):
        diag_sum += grid[i][i] + grid[i][size - 1 - i]
    # Remove center element counted twice (if odd-sized)
    if size % 2 == 1:
        center = size // 2
        diag_sum -= grid[center][center]
    return diag_sum

# Main transformation pipeline
threshold_map = [0, 1, 1, 0, 1]
grid_data = [
    [48, 12, 87, 33, 65],
    [29, 54, 18, 72, 38],
    [91, 14, 67, 25, 83],
    [44, 76, 39, 58, 21],
    [63, 89, 52, 17, 74]
]

# Preprocessing stage (relevant)
normalized_grid = preprocess_grid(grid_data)

# Decoy assignment (misleading)
entropy_profile = defaultdict(int)
for idx, row in enumerate(normalized_grid):
    entropy_profile[idx] = round(sum(math.log(v + 1) for v in row if v > 0), 3)

# Real transformation chain
shift_value = 0
for t in threshold_map:
    shift_value += t * 3

# Apply actual phase shift
modulated_grid = apply_phase_shift(normalized_grid, shift_value)

# Critical aggregation function
aggregate_transform = lambda g, t_map: (
    aggregate_diagonals(g) + 
    len([x for row in g for x in row if x % 4 == 3]) - 
    sum(t_map) * 2
)

# Key execution point
final_flux = aggregate_transform(modulated_grid, threshold_map)

# Print result as required
print(f"Target result: {final_flux}")