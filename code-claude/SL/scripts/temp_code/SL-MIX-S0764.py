def analyze_text_features(text1, text2):
    # Convert texts to lowercase for consistent analysis
    text1 = text1.lower()
    text2 = text2.lower()
    
    # Calculate various text metrics
    word_count1 = len(text1.split())
    word_count2 = len(text2.split())
    
    # Extract unique characters
    set_a = set(text1.replace(" ", ""))
    set_b = set(text2.replace(" ", ""))
    
    # Calculate bitwise lengths for distraction
    bit_length1 = sum(ord(c) & 0x3F for c in text1)
    bit_length2 = sum(ord(c) | 0x20 for c in text2)
    
    # Find common characters between texts
    common_chars = len(set_a & set_b)
    
    # Calculate character frequency distribution (not used in final result)
    char_freq = {}
    for c in (text1 + text2):
        if c.isalpha():
            char_freq[c] = char_freq.get(c, 0) + 1
    
    # Find most common character (distraction)
    most_common = max(char_freq.items(), key=lambda x: x[1]) if char_freq else ('', 0)
    
    # Calculate symmetric difference (not used in final result)
    sym_diff = len(set_a ^ set_b)
    
    # Apply a complex formula that doesn't affect the final result
    complexity_score = word_count1 * 0.4 + word_count2 * 0.6 + sym_diff - sym_diff
    
    return common_chars

text_a = "Python programming is fun"
text_b = "Data processing with Python"

result = analyze_text_features(text_a, text_b)
print(f"Result: {result}")