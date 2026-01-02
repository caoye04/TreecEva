def analyze_frequency(pattern):
    # Irrelevant frequency analysis with decoy logic
    freq = {}
    for p in pattern:
        freq[p] = freq.get(p, 0) + 1
    normalized = [f / sum(freq.values()) for f in freq.values()]
    return sum(normalized[i] * i for i in range(len(normalized))) if normalized else 0

# Decoy data structures
token_map = {'A': 1, 'B': 2, 'C': 3, 'X': -999, 'Y': -888}
weights = [0.1, 0.2, 0.3, 0.4, 0.5]

# Unused transformation function
def transform_grid(grid):
    transposed = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]
    rotated = [row[::-1] for row in transposed]
    return rotated  # Dead code path

def compute_magnitude(vec):
    return sum(v ** 2 for v in vec) ** 0.5

# Real processing begins here
def extract_features(sequence, threshold=5):
    features = []
    for i, val in enumerate(sequence):
        if val > threshold:
            window = sequence[max(0, i-2):i+3]
            avg = sum(window) / len(window)
            features.append(avg * (i % 4 + 1))
    return features

def validate_checksum(data):
    # Complex checksum that looks important but is only used once
    total = 0
    for i, d in enumerate(data):
        total += d * (i + 1) * (-1)**i
    return abs(total) % 100 == 0

def process_segments(raw_data, settings):
    result = 0
    segment_size = settings['chunk']
    
    # Real logic: slicing and processing
    for i in range(0, len(raw_data), segment_size):
        segment = raw_data[i:i + segment_size]
        
        # Distractor: irrelevant conditional based on length
        if len(segment) == 4:
            temp = [x * 2 for x in segment if x < 0]
            _ = sum(temp) * 0.5  # Unused
        
        # Key computation
        indices = list(range(len(segment)))
        paired = zip(segment, indices)
        filtered = [val for val, idx in paired if val > idx - 1]
        
        # Accumulation step
        contribution = 0
        for j, item in enumerate(filtered):
            if j % 2 == 0:
                contribution += item * (j + 1)
            else:
                contribution -= item
        
        result += contribution
        
        # Early exit red herring
        if result > 1000:
            break  # Never actually triggered
    
    # Final adjustment using enumerate
    adjustments = [1, -2, 3, -1]
    for idx, adj in enumerate(adjustments):
        result += result * adj * 0.01  # Small cumulative effect
    
    return int(result)

# Main execution flow
data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3]
config = {
    'chunk': 4,
    'mode': 'fast',
    'debug': False
}

# Seemingly important pre-processing (partially irrelevant)
decoys = [compute_magnitude([3,4,5]), analyze_frequency('ABCCBA')]
filtered_data = [x for x in data if x != 1]  # Looks useful, not used

# Actual call
final_output = process_segments(data, config)

# Output result as required
print(f"Result: {final_output}")