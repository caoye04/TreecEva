from collections import defaultdict, Counter
import math

# Irrelevant helper function (decoy)
def analyze_sentiment(text):
    return sum(1 for c in text if c in 'aeiou') % 3

def generate_metrics(raw_values):
    # Distractor: complex-looking but unused computation
    temp_log = [math.log(abs(x) + 1) for x in raw_values if x != 0]
    squared_norm = [x ** 2 for x in raw_values]
    filtered_peaks = [x for x in raw_values if x > sum(raw_values) / len(raw_values)]

    # Actual relevant transformation
    histogram = defaultdict(int)
    for v in raw_values:
        bin_key = v // 10 * 10
        histogram[bin_key] += 1

    return dict(histogram)

def compute_entropy(data):
    total = sum(data.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in data.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

# Unused recursive decoy
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Misleading intermediate processing
def adjust_weights(signal, factor=1.5):
    weighted = [s * factor for s in signal]
    normalized = [w / max(weighted) for w in weighted]
    return normalized

# Core logic disguised among distractions
def evaluate_performance(metrics, threshold):
    keys = sorted([k for k in metrics.keys() if k >= threshold])
    if not keys:
        return -1
    
    # Real computation path
    values = [metrics[k] for k in keys]
    aggregate = sum(v ** 2 for v in values)
    adjustment = math.sqrt(len(values)) if values else 0
    
    # Dead code branch (never executed due to logic above)
    fallback = None
    if threshold < 0:
        fallback = sum(values) * adjustment  # unreachable
    
    result = int(aggregate / (adjustment + 1e-6))
    
    # Conditional expression red herring
    status = 'valid' if result > 100 else ('borderline' if result > 50 else 'low')
    
    # Final decision
    scale_factor = 2 if status == 'valid' else (1.5 if status == 'borderline' else 1)
    return int(result * scale_factor)

# --- MAIN EXECUTION ---
raw_input_data = [12, 15, 23, 25, 27, 34, 36, 38, 41, 42, 45, 47, 50, 53, 55]

# Irrelevant string processing distraction
text_corpus = "Performance evaluation metrics analysis"
syllable_count = sum(1 for c in text_corpus.lower() if c in 'aeiou')
sentiment_score = analyze_sentiment(text_corpus)

# Unused combinatorics distraction
combinations = [(a, b) for a in raw_input_data for b in raw_input_data if a < b and (a + b) % 10 == 0]

# Signal processing decoy
signal_strength = [x % 7 for x in raw_input_data]
adjusted_signal = adjust_weights(signal_strength)

# Actual pipeline begins here
metric_data = generate_metrics(raw_input_data)
entropy_value = compute_entropy(metric_data)  # Used only for red herring

# Distractor: conditional that looks important but isn't
if entropy_value > 2.0:
    base_threshold = 20
else:
    base_threshold = 20  # Same either way

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

# Output result as required
print(f"Target result: {final_score}")