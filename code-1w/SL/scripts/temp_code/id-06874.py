import math

# Irrelevant helper function (dead code path)
def unused_diagnostic(x):
    return [i ** 2 for i in range(x) if i % 3 == 0]

# Misleading transformation chain
def transform_signal(data):
    processed = []
    for val in data:
        temp = val * 1.5 + 2
        if temp > 10:
            temp = math.log(temp, 2)
        processed.append(round(temp, 3))
    return processed

# Decoy accumulator with misleading intermediate results
def accumulate_noise(seq):
    accumulator = 0
    for i in seq:
        accumulator += i * (i % 7)
    return accumulator * 0.1  # Red herring result

# Core logic disguised among distractions
def analyze_pattern(sequence):
    count = 0
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1] and sequence[i] % 2 == 0:
            count += 1
    return count

# Bit manipulation red herring
class BitAnalyzer:
    def __init__(self, value):
        self.value = value
        self.flipped = ~value
        
    def shift_check(self):
        return (self.value << 2) ^ (self.value >> 1)

# Unused but complex data structure
class DataBuffer:
    def __init__(self):
        self.buffer = [0]*100
        self.index = 0
        
    def fill_random(self, seed=42):
        for i in range(len(self.buffer)):
            self.buffer[i] = (seed * i) % 19

# Distractor: linear search with no real impact
def find_peak(arr):
    peak_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[peak_idx]:
            peak_idx = i
    return peak_idx

# Real computation buried in noise
def calculate_entropy(values):
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        p = v / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Lambda-based filtering (actual use)
adaptive_filter = lambda x, threshold: list(filter(lambda y: y >= threshold * 0.75, x))

# Main processing function with hidden signal
def evaluate_performance(metrics):
    # Step 1: Filter relevant metrics
    filtered = adaptive_filter(metrics, 8)
    
    # Step 2: Analyze growth pattern
    trend_strength = analyze_pattern(filtered)
    
    # Step 3: Calculate information entropy
    diversity = calculate_entropy(filtered)
    
    # Step 4: Apply weighted scoring
    base_score = sum(filtered) / len(filtered) if filtered else 0
    adjustment = trend_strength * 1.75
    penalty = int(diversity) * 0.5
    
    # Hidden critical calculation
    raw_value = base_score + adjustment - penalty
    
    # Irrelevant bit analysis (distraction)
    analyzer = BitAnalyzer(int(raw_value))
    _ = analyzer.shift_check()  # Unused result
    
    # Final nonlinear scaling
    final_score = int((raw_value ** 1.5) // 1) if raw_value > 0 else 0
    
    # Dead code: complex buffer with no effect
    buffer = DataBuffer()
    buffer.fill_random(13)
    
    return final_score

# Input data with subtle pattern
metric_data = [3, 5, 8, 9, 10, 12, 14, 15]

# Key execution point
final_score = evaluate_performance(metric_data)

# Output result
print(f"Result: {final_score}")