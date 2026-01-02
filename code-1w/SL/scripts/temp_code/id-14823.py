import math

# Irrelevant utility function (decoy)
def normalize_vector(v):
    norm = sum(x ** 2 for x in v) ** 0.5
    return [x / norm for x in v] if norm else v

# Misleading data processing chain
def preprocess_metrics(raw):
    adjusted = {}
    for k, v in raw.items():
        if k.startswith('temp_'):
            adjusted[k.replace('temp_', '')] = v * 1.1
        elif k.startswith('cache_'):
            adjusted[k.replace('cache_', '')] = max(v, 0.5)
    return adjusted

# Unused transformation (dead code path)
def legacy_transform(data):
    return {k: (v ** 2 + 1) / (v + 0.1) for k, v in data.items()}

# Core logic disguised among distractions
def calculate_efficiency(x, y, z):
    base = (x * 0.7) + (y * 0.2)
    penalty = 0.1 * z if z > 80 else 0
    return base - penalty

# Bit manipulation red herring
def obfuscate_key(n):
    n ^= 0xABCD
    n = (n << 3) & 0xFFFF
    n ^= (n >> 4)
    n &= 0x7FFF
    return n  # Never actually used in final calculation

# Distractor: complex but irrelevant data structure
class PerformanceBuffer:
    def __init__(self, size=5):
        self.data = [{} for _ in range(size)]
        self.index = 0
    
    def add_entry(self, entry):
        self.data[self.index] = entry
        self.index = (self.index + 1) % len(self.data)
    
    def get_recent(self):
        return self.data[(self.index - 1) % len(self.data)]

# Real business logic buried in noise
def compute_stability_factor(metrics):
    if not metrics:
        return 0.0
    
    # Extract relevant values with default fallbacks
    response_time = metrics.get('response_time', 100)
    error_rate = metrics.get('error_rate', 5)
    throughput = metrics.get('throughput', 200)
    uptime = metrics.get('uptime', 99.5)
    
    # Actual stability formula
    stability = (throughput / response_time) * (uptime / 100)
    stability -= error_rate * 1.5
    
    return round(stability, 4)

# Main evaluation with conditional logic and comprehensions
def evaluate_performance(data, weight_map):
    # Preprocess only specific keys
    filtered = {k: v for k, v in data.items() if k in ['response_time', 'error_rate', 'throughput', 'uptime']}
    
    # Compute derived metrics
    efficiency = calculate_efficiency(
        filtered.get('response_time', 0),
        filtered.get('throughput', 0),
        filtered.get('uptime', 0)
    )
    
    stability = compute_stability_factor(filtered)
    
    # Apply weights using dictionary operation
    weighted_efficiency = efficiency * weight_map.get('efficiency', 0.6)
    weighted_stability = stability * weight_map.get('stability', 0.4)
    
    # Conditional adjustment based on threshold
    bonus = 5.0 if stability > 10 and efficiency > 50 else 2.5
    
    # Final score computation (this is the real answer)
    final_raw = weighted_efficiency + weighted_stability + bonus
    
    # Additional distraction: list comprehension with unused result
    adjustment_history = [
        final_raw * (0.95 ** i) for i in range(1, 4) if final_raw > 30
    ]
    
    return int(round(final_raw))

# Simulated input data with misleading entries
raw_input = {
    'temp_response_time': 120,
    'cache_error_rate': 4.2,
    'response_time': 95,
    'error_rate': 3.8,
    'throughput': 240,
    'uptime': 98.7,
    'debug_flag': True,
    'version': '2.1.5',
    'timestamp': 1712345678
}

# Weight configuration (some keys irrelevant)
weights = {
    'efficiency': 0.65,
    'stability': 0.35,
    'legacy_factor': 0.1,  # Unused weight
    'dummy': 0.0          # Dead weight
}

# Execute preprocessing (irrelevant to final result)
preprocessed = preprocess_metrics(raw_input)

# Initialize buffer with decoy data
buffer = PerformanceBuffer()
buffer.add_entry({'simulated': 'data'})

# Key execution point
final_score = evaluate_performance(raw_input, weights)

# Print target result
print(f"Target result: {final_score}")