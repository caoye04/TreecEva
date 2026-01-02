def analyze_text_patterns(input_text):
    # Irrelevant preprocessing: reverse and pad text
    padded_text = input_text[::-1] + 'xyz'
    shifted_chars = [chr((ord(c) - ord('a') + 3) % 26 + ord('a')) for c in padded_text if c.isalpha()]
    
    # Semi-relevant character frequency analysis (not used later)
    freq_map = {}
    for char in input_text:
        if char.isalpha():
            lower_char = char.lower()
            freq_map[lower_char] = freq_map.get(lower_char, 0) + 1
    
    # Key computation: count vowels at even indices
    even_index_vowels = sum(1 for i, c in enumerate(input_text) if i % 2 == 0 and c.lower() in 'aeiou')
    
    # Misleading complexity: simulate unused word scoring
    words = input_text.split()
    word_scores = []
    for w in words:
        score = 0
        for ch in w:
            if ch.isupper():
                score += 2
            elif ch in 'aeiou':
                score += 1
        word_scores.append(score)  # Never used
    
    # Distractor: nested loop with no side effects
    total_pairs = 0
    for i in range(len(shifted_chars)):
        for j in range(i+1, len(shifted_chars)):
            if shifted_chars[i] == shifted_chars[j]:
                total_pairs += 1  # Computed but irrelevant
    
    return even_index_vowels


def calculate_final_score(text_data, multiplier=3, offset=5):
    # Early return condition (not triggered in this case)
    if len(text_data) == 0:
        return 0
    
    # Extract metadata that slightly modifies logic
    line_count = text_data.count('\n') + 1
    clean_lines = [line.strip() for line in text_data.split('\n') if line.strip()]
    
    # Core logic hidden among distractions
    total_weight = 0
    for idx, line in enumerate(clean_lines):
        analysis_result = analyze_text_patterns(line)
        weight = analysis_result * (idx + 1)
        total_weight += weight
        
        # Dead code path: only applies to very long lines
        if len(line) > 100:
            backup = weight ** 0.5
            total_weight -= weight  # Would undo, but never reached
    
    # Real answer computation
    adjustment = len([c for c in text_data if c in '.,!?'])
    final_score = (total_weight * multiplier) - adjustment + offset
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Main execution
log_entry = '''\nUser login attempt failed. Invalid credentials.\nRetrying with alternate method...\nConnection timeout detected on port 8080.\n'''  
final_score = calculate_final_score(log_entry)