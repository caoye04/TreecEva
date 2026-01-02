def analyze_text(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    
    # Irrelevant transformation (dead path)
    temp_freq = {k: v / len(char_count) for k, v in char_count.items()}
    sorted_chars = sorted(char_count.keys())
    entropy = 0.0
    for count in char_count.values():
        prob = count / len(text)
        entropy -= prob * __import__('math').log2(prob) if prob > 0 else 0
    
    # Distractor variables
    avg_char_freq = sum(char_count.values()) / len(char_count) if char_count else 0
    unique_letters = set(sorted_chars)
    letter_rarity = {ch: 1/count for ch, count in char_count.items()}
    
    return char_count, entropy, avg_char_freq

# Unused helper function (red herring)
def compute_similarity(s1, s2):
    set1, set2 = set(s1), set(s2)
    return len(set1 & set2) / len(set1 | set2) if (set1 | set2) else 0

# Decoy data structures
document_corpus = [
    'The quick brown fox jumps over the lazy dog',
    'Pack my box with five dozen liquor jugs',
    'How vexingly quick daft zebras jump!',
]

# Simulated metrics (some irrelevant)
metrics_log = []
score_weights = {'length': 0.2, 'entropy': 0.5, 'uniqueness': 0.3}
baseline_shift = 42

# Real computation begins here
primary_text = "Hello world programming contest winner"
char_stats, text_entropy, _ = analyze_text(primary_text)

# Constructing multiple data structures with cross-references
token_set = set(primary_text.split())
letter_set = set(c.lower() for c in primary_text if c.isalpha())
common_letters = set('etaoinshrdluc')
frequent_in_text = set(ch for ch, cnt in char_stats.items() if cnt > 2)

metric_set = {
    'length_metric': len(primary_text),
    'vowel_ratio': len([c for c in primary_text if c.lower() in 'aeiou']) / len(primary_text),
    'rare_coverage': len(letter_set - common_letters),
    'token_diversity': len(token_set) / len(primary_text.split()),
    'entropy_norm': text_entropy / 4.0,
    'overlap_with_common': len(letter_set & common_letters),
    'freq_intersection': len(frequent_in_text & common_letters)
}

# Redundant and misleading calculations
phantom_score = 0
for i, token in enumerate(token_set):
    phantom_score += hash(token) % (i + 1)
adjustment_factor = __import__('math').sin(len(token_set))

# Dead code path (never called)
def calculate_dimensionality(text_set):
    return len(set(''.join(text_set))), sum(len(t) for t in text_set)

# Core recursive scoring logic (simple recursion)
def score_component(val, depth=3):
    if depth == 0 or val < 0.1:
        return val
    return val + score_component(val * 0.3, depth - 1)

# Complex data transformation with distractors
decoy_array = [sum(char_stats[c] for c in primary_text.lower()[:i]) for i in range(1, 10)]
offset_map = {i: __import__('math').log(i + 2) for i in range(len(decoy_array))}

# Final evaluation using only specific keys from metric_set
def evaluate_performance(metrics):
    # Only these components matter
    raw_length = score_component(metrics['length_metric'] * 0.1)
    entropy_bonus = score_component(metrics['entropy_norm'] * 10)
    diversity_penalty = metrics['token_diversity'] < 0.7
    
    # Set operations used meaningfully
    coverage_score = len(letter_set & frequent_in_text) * 2
    uniqueness_boost = len(letter_set - common_letters) * 1.5
    
    # Actual formula
    base = raw_length + entropy_bonus + coverage_score + uniqueness_boost
    if diversity_penalty:
        base *= 0.9
    
    # Irrelevant conditional (misleading)
    if len(token_set) > 100:
        base += adjustment_factor * 10
    
    return int(round(base))

# Key execution point
final_score = evaluate_performance(metric_set)
print(f"Target result: {final_score}")