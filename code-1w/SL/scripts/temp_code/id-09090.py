def analyze_pattern(seq, config):
    if not seq:
        return 0
    
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(seq) for x in seq if x > 0]
    smoothed = [normalized[i] for i in range(len(normalized)) if i % 2 == 0]
    
    # Core logic disguised among noise
    magnitude = sum(abs(x) for x in seq)
    peaks = [i for i, x in enumerate(seq) if x > 0 and (i == 0 or seq[i-1] < x)]
    
    # Decoy transformation
    inverted = [1.0 / (1 + x) for x in normalized]
    entropy_proxy = len(inverted) * 0.3
    
    return magnitude + len(peaks)

# Misleading data structures
signal_cache = {}

def generate_thresholds(base_value):
    # Dead code path - never actually used in main logic
    levels = []
    temp = base_value
    for _ in range(5):
        temp = (temp * 1.618) % 100
        levels.append(round(temp, 2))
    return levels

class DiagnosticEngine:
    def __init__(self, mode="standard"):
        self.mode = mode
        self.correction_factor = 0.85 if mode == "strict" else 1.0
    
    def adjust(self, x):
        return x * self.correction_factor

# Unused recursive red herring
def fibonacci_limit(n, limit=10):
    if n <= 1 or limit <= 0:
        return n
    return fibonacci_limit(n-1, limit-1) + fibonacci_limit(n-2, limit-1)

# Real computation buried in distractions
def compute_entropy_signal(data):
    total = 0
    for i, val in enumerate(data):
        if i % 3 == 0:
            total += val ** 2
    return total

# Primary processing function
def process_metrics(sequence, thresholds):
    # Distractor: unused zip operation
    paired = list(zip(sequence[::2], sequence[1::2]))
    transforms = [a ^ b for a, b in paired]  # Bitwise red herring
    
    # Slicing distraction
    subset_a = sequence[:len(sequence)//2]
    subset_b = sequence[len(sequence)//2:]
    
    # Conditional expression decoy
    proxy_score = sum(subset_a) if len(subset_a) > 3 else sum(subset_b) * 2
    
    # Key intermediate values
    base_metric = analyze_pattern(sequence, {})
    adjustment = len([x for x in sequence if x & 1])  # Count odd numbers
    
    # Real signal extraction via enumerate
    weighted_sum = 0
    for idx, val in enumerate(sequence):
        if val > thresholds.get(idx % 4, 0):
            weighted_sum += val * (idx + 1)
    
    # Final calculation - only this matters
    secondary_component = compute_entropy_signal(sequence)
    engine = DiagnosticEngine(mode="relaxed")
    adjusted_weight = engine.adjust(weighted_sum)
    
    final_diagnostic = (base_metric + adjustment) * 3 - secondary_component + adjusted_weight
    return final_diagnostic

# Setup inputs with meaningful names
health_sequence = [12, -7, 9, 14, 0, 22, -3, 8]
threshold_map = {0: 5, 1: 8, 2: 3, 3: 10}

# Execute
final_diagnostic = process_metrics(health_sequence, threshold_map)
print(f"Result: {final_diagnostic}")