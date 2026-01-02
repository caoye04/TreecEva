def analyze_text_sequence(raw_input):
    # Preprocess and extract features from text
    cleaned = raw_input.strip().lower()
    char_count = len(cleaned)
    vowel_count = sum(1 for c in cleaned if c in 'aeiou')
    word_list = cleaned.split()
    word_count = len(word_list)
    
    # Simulate data processing stages with intermediate metrics
    stage_a = (char_count * 2) + vowel_count
    temp_offset = stage_a % 7  # Irrelevant offset, not used later
    processed_data = []
    
    for i, word in enumerate(word_list):
        # Apply transformation with embedded counting logic
        transformed = word[::-1]  # Reverse each word
        length_metric = len(transformed)
        vowel_in_word = sum(1 for c in transformed if c in 'aeiou')
        score = length_metric * 1.5 + vowel_in_word * 2.0
        
        # Store structured info - some fields are overengineered
        entry = {
            'index': i,
            'original': word,
            'transformed': transformed,
            'score': score,
            'redundant_checksum': (i ^ length_metric) % 13  # Dead computation
        }
        processed_data.append(entry)
    
    # Compute aggregate stats (some are distractions)
    total_score = sum(item['score'] for item in processed_data)
    avg_score = total_score / word_count if word_count > 0 else 0
    max_entry = max(processed_data, key=lambda x: x['score'])
    peak_index = max_entry['index']
    
    # Overhead simulation: includes irrelevant calculations
    base_overhead = char_count // 3
    dynamic_penalty = 0
    for i in range(min(word_count, 5)):
        if i % 2 == 0:
            dynamic_penalty += i * 1.1
        else:
            dynamic_penalty -= i * 0.5  # Net effect small, misleading
    
    overhead = base_overhead + dynamic_penalty + vowel_count // 2
    
    # Key computation: efficiency depends only on real signal
    def compute_efficiency(data, overhead):
        raw_sum = sum(len(item['transformed']) for item in data)
        penalty_factor = 0.9 if len(data) > 3 else 1.0
        return (raw_sum - overhead) * penalty_factor
    
    efficiency_ratio = compute_efficiency(processed_data, overhead)
    
    # Print final result as required
    print(f"Result: {efficiency_ratio}")

# Execute with sample input
text_input = "Optimization algorithms improve performance dramatically"
analyze_text_sequence(text_input)