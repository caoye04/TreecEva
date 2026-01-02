from collections import Counter

def analyze_text_complexity(text):
    words = text.lower().split()
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths)
    
    # Count frequency of each word length
    length_counter = Counter(word_lengths)
    mode_length = length_counter.most_common(1)[0][0]
    
    # Irrelevant distraction: unused variable (minimal interference)
    ignored_value = sum([i**2 for i in range(3)])
    
    return avg_length, mode_length

def calculate_final_score(data):
    avg_len, mode_len = data
    score = (avg_len * 10) + mode_len
    bonus = 5 if avg_len < mode_len else 0
    score += bonus
    return int(score)

# Main execution
input_text = "the quick brown fox jumps over the lazy dog repeatedly"
word_data = analyze_text_complexity(input_text)
final_score = calculate_final_score(word_data)
print(f"Result: {final_score}")