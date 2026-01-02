from collections import Counter

def tokenize_and_filter(text):
    words = text.lower().split()
    filtered = [word.strip('.,!?"') for word in words if len(word) > 2]
    return filtered

def calculate_final_score(word_count_dict, multiplier):
    base_score = sum(count for count in word_count_dict.values())
    unique_bonus = len(word_count_dict) * multiplier
    return base_score + unique_bonus

test_text = "The quick brown fox jumps over the lazy dog near the riverbank"
bonus_multiplier = 3

# Tokenize and filter the input text
tokens = tokenize_and_filter(test_text)

# Count frequency of relevant words
word_counts = Counter(tokens)

# Compute final score using word frequencies and bonus
final_score = calculate_final_score(word_counts, bonus_multiplier)

print(f"Result: {final_score}")