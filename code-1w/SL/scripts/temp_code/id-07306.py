from collections import defaultdict, Counter
import math

def analyze_trend(values):
    # Irrelevant function: analyzes trend but not used in final computation
    if len(values) < 2:
        return 0
    slope = sum(values[i+1] - values[i] for i in range(len(values)-1)) / (len(values) - 1)
    return slope if slope > 0 else 0

def preprocess_input(raw):
    # Dead code path — looks useful but unused
    cleaned = [x for x in raw if x > 0]
    normalized = [x / max(cleaned) for x in cleaned]
    return normalized

def simulate_load(factor):
    # Distractor: simulates system load with bit manipulation red herring
    state = 1023
    for _ in range(factor % 5):
        state = (state << 1) | (state >> 9)
        state &= 0xFFFF
    return bin(state).count('1')

def calculate_entropy(data):
    # Unused advanced math — misleading complexity
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count/total) * math.log2(count/total) for count in counts.values())
    return round(entropy, 4)

def evaluate_performance(metrics, base):
    # Core logic embedded in distractions
    temp_results = defaultdict(float)
    adjustments = [0.85, 1.1, 0.95, 1.05]
    
    # Real computation begins
    primary = metrics['throughput'] * adjustments[metrics['tier'] - 1]
    penalty = 0
    
    # Conditional expression red herring
    penalty += 10 if metrics['errors'] > base['max_errors'] else 0
    penalty += 5 if metrics['latency'] > base['threshold'] else 0
    
    # Real adjustment
    if metrics['consistency'] >= 3:
        primary += 15  # Hidden bonus
    
    temp_results['adjusted'] = primary - penalty
    
    # Decoy transformation
    transformed = [math.sin(x) for x in range(1, 6)]
    dummy_sum = sum(transformed)
    
    # Critical statement: combines arithmetic and conditional logic
    multiplier = 1.2 if temp_results['adjusted'] >= 90 else 0.85
    final_raw = temp_results['adjusted'] * multiplier
    
    # Final threshold clamp
    final_raw = min(final_raw, 120)
    
    # This line is key — determines answer
    final_score = int(round(final_raw))
    
    # Unused variables to mislead
    debug_info = {'processed': True, 'version': '2.1', 'flags': 0b1010}
    overflow_check = (final_score << 3) >> 2
    
    return final_score

# Simulated input data
metric_data = {
    'throughput': 78,
    'tier': 2,            # affects adjustment factor
    'errors': 12,
    'latency': 480,
    'consistency': 4      # triggers +15 bonus
}

baseline = {
    'max_errors': 10,
    'threshold': 450
}

# Unused data structures for distraction
historical_logs = [
    {'t': 1, 'val': 88}, {'t': 2, 'val': 85}, {'t': 3, 'val': 90}
]

feature_mask = 0b11011011

# Key execution point
final_score = evaluate_performance(metric_data, baseline)

# Print result as required
print(f"Result: {final_score}")