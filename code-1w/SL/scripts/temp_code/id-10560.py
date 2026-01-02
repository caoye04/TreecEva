import math

# Simulated environmental sensor data processing with red herrings
def collect_readings(samples):
    raw_data = [s['value'] for s in samples]
    avg = sum(raw_data) / len(raw_data)
    deviation = [(x - avg)**2 for x in raw_data]
    variance = sum(deviation) / len(deviation)
    return {'average': avg, 'variance': variance}

# Irrelevant helper: atmospheric correction (not used in final logic)
def correct_atmosphere(data, factor=1.03):
    return [d * factor for d in data]

# Misleading transformation chain
def enhance_signal(signal_stream):
    amplified = [s * 1.5 for s in signal_stream]
    filtered = [f for f in amplified if f > 10]
    reshaped = [filtered[i:i+3] for i in range(0, len(filtered), 3)]
    transposed = [[row[i] for row in reshaped if i < len(row)] for i in range(3)]
    return transposed

# Decoy function: looks important but unused
def compute_entropy(seq):
    from collections import Counter
    counts = Counter(seq)
    total = len(seq)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return entropy

# Unused recursive structure to distract
def recursive_window(arr, size=3):
    if len(arr) <= size:
        return [arr]
    return [arr[:size]] + recursive_window(arr[1:], size)

# Core data purification logic
measurements = [
    {'value': 12, 'flag': True},
    {'value': 8, 'flag': False},
    {'value': 15, 'flag': True},
    {'value': 5, 'flag': False},
    {'value': 20, 'flag': True},
    {'value': 3, 'flag': False},
    {'value': 18, 'flag': True}
]

readings = collect_readings(measurements)
avg_val = readings['average']  # 10.142857...

# Simulated depth levels in water column (main data source)
levels = [0.91, 0.87, 0.45, 0.63, 0.77, 0.33, 0.81, 0.52, 0.74, 0.69]

# Auxiliary list comprehension - irrelevant
compressed = [x for x in levels if x > 0.6]

# Another decoy variable
baseline_shift = sum([int(avg_val)] * 2) / 2.5

# Key analysis function
def analyze_purity(data, threshold):
    # Apply threshold filtering using slicing and comprehension
    above_threshold = [x for x in data if x >= threshold]
    below_threshold = [x for x in data if x < threshold]
    
    # Compute weighted purity score
    high_contrib = sum(above_threshold) * 0.8
    low_contrib = sum(below_threshold) * 0.2
    score = (high_contrib + low_contrib) / len(data)
    
    # Additional distraction inside function
    temp_grid = [[i+j for j in range(3)] for i in range(3)]
    magic_factor = temp_grid[1][1]  # Always 2, but looks dynamic
    
    final_score = score * (magic_factor / 1.6)  # Normalize by fake complexity
    return final_score

# Secondary distraction: string-based encoding of numbers (unused)
data_tags = ['A','B','C','D','E']
encoded_seq = ''.join([t + str(i) for i, t in enumerate(data_tags)])

# Noise injection
buffer = [0] * 5
for i in range(len(buffer)):
    buffer[i] = i ** 2

# Critical execution point
filtration_score = analyze_purity(levels, threshold=0.75)

# Print required output
print(f"Result: {filtration_score}")