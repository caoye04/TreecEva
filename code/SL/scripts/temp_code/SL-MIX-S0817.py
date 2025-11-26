def analyze_text_statistics(text_data):
    # Process character metrics with some unnecessary intermediate steps
    char_counts = {}
    temp_analysis = []
    
    for i, char in enumerate(text_data):
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
        temp_analysis.append((i, char, ord(char)))
    
    # Distractor: process that doesn't affect final result
    redundant_chars = [c for c in text_data if c in 'aeiou']
    vowel_count = len(redundant_chars)
    
    # Calculate meaningful metrics
    unique_chars = len(char_counts)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    # More intermediate calculations (partially relevant)
    ascii_sum = sum(ord(c) for c in text_data)
    avg_ascii = ascii_sum / len(text_data) if text_data else 0
    
    # Key computation with slicing and enumerate
    text_length = len(text_data)
    positional_values = []
    
    for idx, char in enumerate(text_data):
        if idx % 2 == 0:
            positional_values.append(ord(char) * (idx + 1))
        else:
            positional_values.append(ord(char) // (idx + 1))
    
    # Final metrics calculation
    unique_metrics = [
        unique_chars,
        len(sorted_chars[0][0]) if sorted_chars else 0,
        sum(positional_values[:3]),
        positional_values[-1] if positional_values else 0
    ]
    
    # Distractor: unused computation
    unused_calculation = vowel_count * avg_ascii
    
    final_result = unique_metrics[-1]
    print(f"Target result: {final_result}")

# Execute the analysis
sample_text = "python3"
analyze_text_statistics(sample_text)