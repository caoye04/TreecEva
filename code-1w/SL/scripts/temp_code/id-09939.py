from collections import defaultdict, Counter

def analyze_text_patterns(input_text):
    # Irrelevant preprocessing: reverse and pad text
    padded_text = input_text[::-1] + 'xyz'
    char_frequency = Counter(padded_text)
    
    # Misleading vowel tracking (not used in final result)
    vowels = 'aeiou'
    vowel_count = sum(1 for c in padded_text.lower() if c in vowels)
    
    # Real work: count consonant clusters
    cleaned = ''.join(c.lower() for c in input_text if c.isalpha())
    cluster_lengths = []
    current_cluster = 0
    
    for c in cleaned:
        if c not in vowels:
            current_cluster += 1
        else:
            if current_cluster > 0:
                cluster_lengths.append(current_cluster)
                current_cluster = 0
    if current_cluster > 0:
        cluster_lengths.append(current_cluster)
    
    # Distractor: unused syllable estimation
    estimated_syllables = len(cleaned) // 3 + 1
    
    # Compute weighted pattern score
    pattern_score = 0
    for i, length in enumerate(cluster_lengths):
        pattern_score += length * (i + 1)  # Weight by position
    
    return pattern_score, len(cluster_lengths)

def validate_structure(text):
    # Use of string methods - partially relevant
    lines = text.strip().split('\n')
    line_length_variability = sum(len(line) ** 0.5 for line in lines) / len(lines) if lines else 0
    
    # Dead code path - never affects output
    if len(lines) > 100:
        return False  # Impossible in our use case
    
    # Actual validation: check alphanumeric ratio
    alpha_chars = sum(1 for c in text if c.isalpha())
    total_chars = len(text)
    alpha_ratio = alpha_chars / total_chars if total_chars else 0
    
    return alpha_ratio > 0.6

def calculate_final_score(doc, threshold=0.75):
    # Initialize various metrics
    stats = defaultdict(int)
    stats['init_flag'] = 1
    
    # Primary analysis
    pattern_score, cluster_count = analyze_text_patterns(doc)
    
    # Secondary checks
    is_valid = validate_structure(doc)
    stats['valid_doc'] = int(is_valid)
    
    # Red herring computation: word entropy (unused)
    words = doc.split()
    word_freq = Counter(words)
    entropy = 0
    total_words = len(words)
    if total_words > 1:
        for count in word_freq.values():
            p = count / total_words
            entropy -= p * (p ** 0.5)  # Not real entropy, but looks plausible
    
    # Another distraction: simulate version check
    config_version = '2.1.8'
    version_parts = config_version.split('.')
    version_score = sum(int(x) * (10 ** (2-i)) for i, x in enumerate(version_parts[:3]))

    # Core logic hidden among noise
    base_score = pattern_score * 3
    penalty = 0
    if cluster_count < 2:
        penalty += 15
    if not is_valid:
        penalty += 25
    
    # Final computation
    intermediate = base_score - penalty
    adjustment = len(words) % 7
    final_score = intermediate + adjustment
    
    # Critical debugging print (mimics importance)
    debug_state = {
        'pattern': pattern_score,
        'intermediate': intermediate,
        'adjustment': adjustment,
        'final': final_score
    }
    
    return final_score

# Main execution
document = "The quick brown fox jumps over the lazy dog near the swift river.\nStreams flow gently under ancient stone bridges."
result = calculate_final_score(document)
print(f"Target result: {result}")