from collections import Counter
import math

def calculate_semantic_density(sentence, stop_words):
    tokens = [word.strip('.,!?;').lower() for word in sentence.split()]
    filtered_tokens = [token for token in tokens if token not in stop_words]
    freq_map = Counter(filtered_tokens)
    total_weight = sum(math.log(freq + 1) * len(word) for word, freq in freq_map.items())
    return round(total_weight / len(filtered_tokens), 2) if filtered_tokens else 0

sentence = "The quick brown fox jumps over the lazy dog efficiently and swiftly"
stop_words = {'the', 'over', 'and'}
semantic_density_score = calculate_semantic_density(sentence, stop_words)
print(f"Result: {semantic_density_score}")