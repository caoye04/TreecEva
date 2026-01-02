from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

def analyze_text_pattern(text):
    char_count = Counter(text)
    rare_chars = [ch for ch, cnt in char_count.items() if cnt < 2]
    sorted_chars = sorted(char_count.keys())
    frequency_map = {ch: cnt for ch, cnt in char_count.items() if ch in sorted_chars[:len(sorted_chars)//2]}
    
    # Irrelevant intermediate variable (low interference)
    temp_normalization = sum(frequency_map.values()) / len(text)
    
    total_entropy = calculate_entropy(frequency_map)
    return total_entropy

# Main execution
input_text = "abacabadabacaba"
result = analyze_text_pattern(input_text)
print(f"Result: {result}")