def analyze_pattern(sequence):
    count_vowels = sum(1 for c in sequence if c.lower() in 'aeiou')
    count_consonants = sum(1 for c in sequence if c.isalpha() and c.lower() not in 'aeiou')
    length = len(sequence)
    ratio = count_vowels / length if length > 0 else 0
    
    # Irrelevant distraction: entropy-like computation (not used later)
    import math
    entropy = 0
    for p in [count_vowels/length, count_consonants/length]:
        if p > 0:
            entropy -= p * math.log2(p)
    
    # Semi-relevant transformation
    normalized_score = (count_vowels * 2 + count_consonants) / (length or 1)
    return normalized_score


def process_entries(entries):
    temp_results = []
    total_chars = 0
    
    for entry in entries:
        if not isinstance(entry, str):
            continue
        if 'error' in entry.lower():
            continue
        
        score = analyze_pattern(entry)
        temp_results.append(score)
        total_chars += len(entry)
    
    # Dead code path: never executed due to filter above
    fallback_value = -1
    if any(isinstance(e, int) for e in entries):
        fallback_value = sum(e for e in entries if isinstance(e, int))
    
    average_score = sum(temp_results) / len(temp_results) if temp_results else 0
    return average_score, total_chars

def calculate_final_score(raw_data):
    # Preprocessing step with string operations
    cleaned = [item.strip().upper() for item in raw_data if isinstance(item, str)]
    filtered = [s for s in cleaned if len(s) >= 3]
    
    # Auxiliary computation: character frequency analysis (partially distracting)
    char_freq = {}
    for s in filtered:
        for c in s:
            char_freq[c] = char_freq.get(c, 0) + 1
    top_char = max(char_freq, key=char_freq.get) if char_freq else 'A'
    top_count = char_freq.get(top_char, 0)
    
    # Core logic embedded within noise
    base_score, _ = process_entries(filtered)
    bonus = 5 if top_char in 'AEIOU' else 2
    
    # Conditional expression usage (required Python feature)
    adjustment = 1.5 if len(filtered) > 4 else (0.8 if top_count > 6 else 1.1)
    
    # Multiple concepts: string processing, conditionals, loops, data aggregation
    intermediate_result = base_score * 100 * adjustment + bonus
    
    # Distracting floating-point accumulation (not affecting final outcome directly)
    phantom_sum = 0.0
    for i in range(len(filtered)):
        for j in range(i+1, len(filtered)):
            if filtered[i][0] == filtered[j][0]:
                phantom_sum += 0.1
    
    final_score = int(intermediate_result + 0.5)  # Round to nearest integer
    return final_score

# Main execution
raw_input_data = [
    "hello world", "Error: invalid input", "algorithm", "data structure",
    "dynamic programming", "AI reasoning test", "short", "LLM evaluation"
]

result = calculate_final_score(raw_input_data)
print(f"Result: {result}")