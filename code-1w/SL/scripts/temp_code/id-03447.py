from collections import Counter

def calculate_letter_frequency_score(word):
    freq = Counter(word.lower())
    top_two = sorted(freq.values(), reverse=True)[:2]
    return sum(top_two) if len(top_two) >= 2 else top_two[0] if top_two else 0

def calculate_final_score(words):
    scores = [calculate_letter_frequency_score(word) for word in words]
    filtered_scores = [s for s in scores if s > 2]
    return sum(filtered_scores) // len(filtered_scores) if filtered_scores else 0

text = "The quick brown fox jumps over the lazy dog"
word_list = text.split()

# Irrelevant distraction: unused variable
unused_var = {len(w) for w in word_list if 'o' in w}

final_score = calculate_final_score(word_list)
print(f"Target result: {final_score}")