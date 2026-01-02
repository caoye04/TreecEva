from collections import Counter

def analyze_frequency(text):
    # Count character frequencies
    freq = Counter(text.lower())
    vowels = 'aeiou'
    vowel_count = sum(freq[char] for char in vowels if char in freq)
    consonant_count = len(text) - vowel_count - text.count(' ')
    
    # Distractor: irrelevant calculation
    temp_avg = (vowel_count + consonant_count) / max(len(freq), 1)
    adjustment = int(temp_avg) % 3
    
    return vowel_count, consonant_count, adjustment

def normalize_string(s):
    # Case conversion and cleaning
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    reversed_clean = cleaned[::-1]
    
    # Irrelevant transformation
    encoded = ''.join(chr((ord(c) - 96) % 26 + 97) for c in reversed_clean)
    
    return cleaned, len(encoded)  # second return value not used

def compute_final_score(raw_data):
    processed = []
    total_length = 0
    
    for item in raw_data:
        clean_text, _ = normalize_string(item)
        v_count, c_count, adj = analyze_frequency(clean_text)
        
        # Core logic: weighted score based on vowel/consonant ratio
        if c_count != 0:
            ratio = round(v_count / c_count, 4)
        else:
            ratio = 0.0
        
        # Distractor: intermediate variables that don't affect final result
        temp_product = v_count * c_count * (adj + 1)
        dummy_shift = temp_product >> 2
        
        score_component = int(100 * ratio) + len(clean_text)
        processed.append(score_component)
        total_length += len(item)
    
    # Secondary distractor: unused aggregate
    average_length = total_length / len(raw_data)
    length_bonus = int(average_length) if average_length > 5 else 0
    
    # Final computation
    base_sum = sum(processed)
    penalty = len([p for p in processed if p < 20]) * 5
    final_score = base_sum - penalty + length_bonus  # length_bonus is predictable but slightly misleading
    
    return final_score

data = ["Hello World", "Python Code", "LLM Reasoning Test", "Benchmark Evaluation"]
final_score = compute_final_score(data)
print(f"Result: {final_score}")