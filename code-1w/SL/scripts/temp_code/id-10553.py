from itertools import groupby

def analyze_text_patterns(input_str):
    char_frequency = {}
    uppercase_count = 0
    vowel_count = 0
    consecutive_pairs = 0
    
    vowels = set('aeiou')
    
    for i, char in enumerate(input_str):
        if char.isupper():
            uppercase_count += 1
        if char.lower() in vowels:
            vowel_count += 1
        if i > 0 and input_str[i-1] == char:
            consecutive_pairs += 1
            
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Misleading transformation - not used later
    transformed_freq = {k: v**2 for k, v in char_frequency.items() if k.isalpha()}
    
    # Dummy statistical computation (red herring)
    avg_frequency = sum(char_frequency.values()) / len(char_frequency) if char_frequency else 0
    variance_proxy = sum((v - avg_frequency) ** 2 for v in char_frequency.values()) / len(char_frequency) if char_frequency else 0

    # Actual relevant metric: length of grouped repeated characters
    sorted_chars = sorted(input_str)
    grouped = [list(group) for key, group in groupby(sorted_chars)]
    repeated_groups = [group for group in grouped if len(group) > 1]
    penalty_factor = sum(len(g) for g in repeated_groups)  # Used in final score

    return {
        'raw_length': len(input_str),
        'unique_chars': len(char_frequency),
        'penalty': penalty_factor,
        'ignored_variance': variance_proxy  # Not used
    }


def preprocess_entry(entry):
    # Simulate data cleaning with irrelevant steps
    cleaned = entry.strip().replace('\t', '').replace('\n', '')
    tokenized = cleaned.split(' ')
    filtered_tokens = [t for t in tokenized if len(t) > 0]
    
    # Extra processing that doesn't affect outcome
    word_lengths = [len(t) for t in filtered_tokens]
    max_len = max(word_lengths) if word_lengths else 0
    
    # But only the first token is actually processed
    primary_token = filtered_tokens[0].lower() if filtered_tokens else ''
    reversed_token = primary_token[::-1]
    
    # This call is what actually matters
    return analyze_text_patterns(reversed_token)


def calculate_final_score(data_list):
    base_total = 0
    adjustment = 0
    
    for item in data_list:
        raw = item['raw_length']
        unique = item['unique_chars']
        penalty = item['penalty']
        
        # Core logic: score based on uniqueness and penalize repetitions
        contribution = (unique * 7) - (penalty * 3)
        base_total += contribution
        
        # Dead code path - never executed due to logic
        if len(str(raw)) > 100:
            adjustment += raw  # unreachable
    
    # Additional distraction: unused helper calculation
    outlier_check = [d for d in data_list if d['raw_length'] == 0]
    null_ratio = len(outlier_check) / len(data_list)
    
    return base_total  # Final result unaffected by adjustment or null_ratio

# Main execution
if __name__ == '__main__':
    raw_entries = [
        'AABBCC',
        'Mississippi',
        'Bookkeeper',
        'Success',
        'Programming'
    ]

    # Irrelevant preprocessing step
    normalized_entries = [entry.upper() for entry in raw_entries]
    temp_analysis = [len(e) for e in normalized_entries if 'S' in e]
    avg_len_temp = sum(temp_analysis) / len(temp_analysis) if temp_analysis else 0

    processed_data = []
    for entry in raw_entries:
        result = preprocess_entry(entry)
        processed_data.append(result)
    
    final_score = calculate_final_score(processed_data)
    print(f"Target result: {final_score}")