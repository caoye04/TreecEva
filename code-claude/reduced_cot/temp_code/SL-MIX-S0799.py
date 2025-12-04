from collections import Counter, defaultdict

def tokenize(text):
    # Tokenize text by splitting on spaces and removing punctuation
    cleaned = "".join(c.lower() if c.isalnum() else " " for c in text)
    return [token for token in cleaned.split() if token]

def compute_similarity(vec1, vec2):
    # Compute cosine similarity between two vectors (not actually used)
    norm1 = sum(v*v for v in vec1.values()) ** 0.5
    norm2 = sum(v*v for v in vec2.values()) ** 0.5
    dot_product = sum(vec1.get(k, 0) * vec2.get(k, 0) for k in set(vec1) | set(vec2))
    return dot_product / (norm1 * norm2) if norm1 > 0 and norm2 > 0 else 0

def calculate_token_weight(token, position, is_priority=False):
    # Calculate weight based on token position and priority
    base_weight = 1.0
    if position < 10:
        base_weight *= 1.5
    elif position > 50:
        base_weight *= 0.7
    
    # Apply bitwise operations for priority tokens
    if is_priority:
        # Convert first char to ASCII and perform bit operations
        ascii_val = ord(token[0]) if token else 0
        bit_factor = ((ascii_val & 0x0F) | 0x10) / 16.0
        return base_weight * bit_factor * 2
    return base_weight

def process_negations(tokens):
    # Process negations in text (not actually used in final calculation)
    negation_words = {"not", "no", "never"}
    negated_indices = set()
    for i, token in enumerate(tokens):
        if token in negation_words and i + 1 < len(tokens):
            negated_indices.add(i + 1)
    return negated_indices

def recursive_token_count(tokens, depth=0, max_depth=3):
    # A recursive function that isn't actually used in the final calculation
    if depth >= max_depth or not tokens:
        return 0
    return len(tokens) + recursive_token_count(tokens[len(tokens)//2:], depth+1)

def calculate_final_score(text, priority_tokens):
    tokens = tokenize(text)
    token_counts = Counter(tokens)
    
    # Initialize variables for tracking
    total_score = 0
    priority_matches = 0
    neg_indices = process_negations(tokens)  # Not used in calculation
    
    # Calculate vector representations (not used in final calculation)
    vector_rep = defaultdict(float)
    for i, token in enumerate(tokens):
        vector_rep[token] += 1.0 / (i + 1)  # Position-weighted
    
    # This is where the actual calculation happens
    for i, token in enumerate(tokens):
        is_priority = token in priority_tokens
        if is_priority:
            priority_matches += 1
        
        weight = calculate_token_weight(token, i, is_priority)
        token_score = weight * (token_counts[token] ** 0.5)  # Square root of frequency
        total_score += token_score
    
    # Apply bitwise operations to priority match count
    priority_factor = 1.0
    if priority_matches > 0:
        # Get binary representation of priority_matches, count 1 bits
        binary = bin(priority_matches)[2:]  # Remove '0b' prefix
        ones_count = binary.count('1')
        zeros_count = binary.count('0')
        priority_factor = 1.0 + (ones_count * 0.1) - (zeros_count * 0.05)
    
    # Calculate unused metrics (distractors)
    unique_ratio = len(token_counts) / len(tokens) if tokens else 0
    avg_token_length = sum(len(t) for t in tokens) / len(tokens) if tokens else 0
    entropy_factor = sum((1/len(tokens)) * (token_counts[t]/len(tokens)) for t in tokens) if tokens else 0
    
    # Final calculation - what actually matters
    document_score = (total_score * priority_factor) / max(1, len(tokens) ** 0.3)
    
    return round(document_score, 2)

# Main code execution
text_content = "The quick brown fox jumps over the lazy dog. The fox was quick and brown."
priority_tokens = {"fox", "quick", "jumps"}

# Some distractor calculations
token_diversity = len(set(tokenize(text_content)))
max_possible_score = len(text_content) * 2.5  # Not actually used
minimum_threshold = token_diversity * 0.4  # Not actually used

# Calculate recursive metrics (not used)
all_tokens = tokenize(text_content)
recursive_metric = recursive_token_count(all_tokens)  # Not used

# The key calculation
document_score = calculate_final_score(text_content, priority_tokens)

# More distractor calculations after the result is already determined
quality_index = document_score / len(all_tokens) if all_tokens else 0
normalized_score = (document_score / max_possible_score) * 100 if max_possible_score else 0

print(f"Result: {document_score}")