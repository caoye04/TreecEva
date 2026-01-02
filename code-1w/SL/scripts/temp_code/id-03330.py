def analyze_text_patterns(input_str):
    char_freq = {}
    for c in input_str:
        char_freq[c] = char_freq.get(c, 0) + 1
    
    vowels = set('aeiou')
    vowel_count = sum(char_freq.get(v, 0) for v in vowels)
    consonant_count = len(input_str) - vowel_count
    
    # Distractor: unused transformation
    reversed_freq = {k: v for k, v in reversed(list(char_freq.items()))}
    
    return vowel_count, consonant_count, char_freq


def compute_entropy(values):
    from math import log2
    total = sum(values)
    if total == 0:
        return 0.0
    entropy = 0.0
    for v in values:
        if v > 0:
            p = v / total
            entropy -= p * log2(p)
    return round(entropy, 6)

# Misleading data structure
user_preferences = {
    'theme': 'dark',
    'font_size': 14,
    'auto_save': True,
    'recent_files': ['doc1.txt', 'doc2.py', 'doc3.json']
}

# Unused recursive function (red herring)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Simulated system metrics with decoy calculations
cpu_load_history = [0.45, 0.67, 0.52, 0.71, 0.58]
memory_usage_peak = 85.3
bandwidth_simulated = sum([i * 0.1 for i in range(10)])  # Dead computation

# Core logic disguised among distractions
def process_metrics(raw_data):
    processed = []
    for item in raw_data:
        if isinstance(item, str):
            # Extract digit count as proxy metric
            digit_count = len([c for c in item if c.isdigit()])
            processed.append(digit_count)
        elif isinstance(item, (int, float)):
            processed.append(abs(int(item * 10)) % 7)
    return processed

# Main evaluation chain
def evaluate_performance(metrics):
    # Relevant slicing operation
    recent_metrics = sorted(metrics)[-5:]
    
    # Set difference as filtering mechanism
    baseline = {0, 1, 2}
    deviant_indices = {i for i, val in enumerate(recent_metrics) if val not in baseline}
    
    # Primary scoring logic
    raw_score = sum(recent_metrics)
    penalty = len(deviant_indices) * 2
    adjustment = compute_entropy(recent_metrics)
    
    # Final calculation
    final_score = int(raw_score - penalty + adjustment)
    
    # Critical print statement
    print(f"Target result: {final_score}")
    return final_score

# Orchestration with irrelevant setup
text_sample = "The quick brown fox jumps over 13 lazy dogs near river Mississippi 987."

# Extract patterns (only vowel/consonant used later in non-critical way)
vowel_cnt, cons_cnt, freq_map = analyze_text_patterns(text_sample)

# Generate feature vector from text digits
feature_vector = [int(c) for c in text_sample if c.isdigit()]

# Process through pipeline
processed_features = process_metrics(feature_vector)

# Add meaningless augmentation
augmented_data = processed_features + [processed_features[-1] ^ 3, (processed_features[0] + 4) % 7]

# Define evaluation input (core data)
metric_set = [3, 1, 4, 1, 5, 9, 2, 6]

# Spurious sorting operation (distractor)
sorted_distractor = metric_set.copy()
sorted_distractor.sort(reverse=True)

# Actual execution point
final_score = evaluate_performance(metric_set)