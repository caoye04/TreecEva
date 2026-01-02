def analyze_sentiment(pattern):
    sentiment_value = 0
    for i, ch in enumerate(pattern):
        if ch == '+':
            sentiment_value += (i + 1) * 1.5
        elif ch == '-':
            sentiment_value -= (i + 1) * 0.7
    return sentiment_value

# Irrelevant helper function (dead code path)
def compute_entropy(data):
    import math
    freq = {}
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0
    total = len(data)
    for count in freq.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused transformation map
token_map = {k: v for k, v in zip('abcdefghij', range(10))}

# Decoy variables with misleading names
event_log = [12, 15, 23, 45, 67, 89, 90]
baseline_offset = sum(event_log) // len(event_log)

# Real processing begins here
def extract_signals(readings):
    signals = []
    for idx, val in enumerate(readings):
        if idx % 2 == 0 and val > 30:
            signals.append(val * 0.1)
        elif idx % 3 == 0:
            signals.append(-val * 0.05)
    return signals

# Another irrelevant computation
redundant_stats = {
    'max_val': max(event_log),
    'min_val': min(event_log),
    'range': max(event_log) - min(event_log),
    'median_approx': sorted(event_log)[len(event_log)//2]
}

# Core logic disguised among distractions
def evaluate_response_time(base, delay):
    if delay < 0.1:
        return base * 1.2
    elif delay < 0.5:
        return base * 0.9
    else:
        return base * 0.6

# Weight adjustment using dictionary operations
adjustment_table = {i: w * 0.8 for i, w in enumerate([1.0, 1.2, 0.9, 1.1, 1.3])}
adjusted_weights = list(adjustment_table.values())

# Simulated feedback sequence with meaning
feedback_sequence = ['+', '-', '+', '+', '-']

# Misleading accumulation
phantom_sum = 0
for x in range(len(feedback_sequence)):
    phantom_sum += x * 17

# Actual weight vector used
weights = [1.0, 0.8, 1.2, 0.9, 1.1]

# Red herring function that is never called
def normalize_sequence(seq):
    total = sum(seq)
    return [s / total for s in seq] if total else seq

# Real aggregation function
def aggregate_performance(seq, w):
    score = 0.0
    # Use enumerate and zip together as required
    for i, (fb, weight) in enumerate(zip(seq, w)):
        if fb == '+':
            contribution = (i + 1) * weight * 10
        else:
            contribution = -(i + 1) * weight * 4
        score += contribution
    # Apply non-linear bonus based on pattern length
    if len(seq) >= 5:
        bonus = 12.5
    else:
        bonus = 5.0
    score += bonus
    
    # Extra obfuscation: use dictionary to modify result by index parity
    modifier_map = {0: 1.05, 1: 0.95}
    final_mod = 1.0
    for k, v in modifier_map.items():
        if len(seq) % 2 == k:
            final_mod *= v
    
    return round(score * final_mod, 6)

# Unused signal extraction
dummy_readings = [40, 10, 60, 20, 80]
signals_out = extract_signals(dummy_readings)

# Key execution point
temp_analysis = analyze_sentiment(feedback_sequence)
final_score = aggregate_performance(feedback_sequence, weights)

# Output result as required
print(f"Target result: {final_score}")