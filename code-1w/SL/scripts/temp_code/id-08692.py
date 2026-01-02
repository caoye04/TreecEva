def analyze_text_quality(text):
    if not text:
        return 0
    
    # Irrelevant statistics (distractors)
    vowel_count = sum(1 for c in text.lower() if c in 'aeiou')
    consonant_ratio = (len(text) - vowel_count - text.count(' ')) / len(text) if len(text) > 0 else 0
    upper_case_only = text.upper()
    reversed_text = text[::-1]

    # Semi-relevant preprocessing
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    unique_chars = len(set(cleaned))
    
    # Red herring: palindrome check (not used directly)
    is_palindrome = cleaned == cleaned[::-1]
    palindrome_bonus = 10 if is_palindrome else 0

    return unique_chars


def compute_entropy_signal(length, diversity):
    # Fake entropy approximation (only loosely related)
    if length == 0:
        return 0.0
    import math
    max_entropy = math.log2(length) if length > 1 else 1
    return round(diversity * max_entropy / 5, 4)


def evaluate_consistency(text):
    words = text.split()
    if len(words) == 0:
        return 0
    
    # Distractor: word length variance
    avg_len = sum(len(w) for w in words) / len(words)
    variances = sum((len(w) - avg_len) ** 2 for w in words)
    variance_penalty = variances / len(words) if words else 0

    # Another red herring: repeated word detection
    seen = set()
    duplicates = 0
    for word in words:
        if word in seen:
            duplicates += 1
        seen.add(word)
    
    # Fake consistency score (semi-relevant)
    return len(set(words))


def calculate_final_score(data):
    # Main logic chain begins
    raw_input = data.strip()
    size = len(raw_input)
    
    # Step 1: Extract core quality metric
    base_metric = analyze_text_quality(raw_input)
    
    # Step 2: Compute auxiliary signal
    entropy_signal = compute_entropy_signal(size, base_metric)
    
    # Step 3: Evaluate structural consistency
    consistency_score = evaluate_consistency(raw_input)
    
    # Step 4: Apply weighting and offset (key transformation)
    weighted_sum = base_metric * 3 + consistency_score * 2
    
    # Step 5: Conditional adjustment based on length threshold
    adjustment = 5 if size > 10 else -2
    
    # Step 6: Final composition with decimal component
    final_score = weighted_sum + adjustment + entropy_signal
    
    # Step 7: Truncate to reasonable precision
    final_score = round(final_score, 4)
    
    # Output result as required
    print(f"Target result: {final_score}")
    return final_score

# Execution entry point
input_data = "Hello world this is a test message xyz"
data = input_data.replace("xyz", "abc")  # Minor mutation
final_score = calculate_final_score(data)