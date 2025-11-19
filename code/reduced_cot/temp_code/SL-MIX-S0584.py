from functools import reduce

def tokenize_and_process(document):
    tokens = document.split()
    processed = []
    for token in tokens:
        # Remove punctuation and convert to lowercase
        clean_token = ''.join(filter(str.isalpha, token)).lower()
        if len(clean_token) > 0:
            processed.append(clean_token)
    return processed

def compute_hash_score(word_list):
    return sum(hash(w) % 100 for w in word_list)

document_content = "Robust systems need stable architectures. Efficient designs prevent failures."
word_sequence = tokenize_and_process(document_content)
hash_accumulator = compute_hash_score(word_sequence)

lengths = list(map(len, word_sequence))
squared_values = list(map(lambda x: x**2 if x % 2 == 0 else x*3, lengths))
filtered_values = list(filter(lambda x: x > 5, squared_values))
aggregated_value = reduce(lambda a, b: a ^ b, filtered_values, 0) if filtered_values else 0

is_even_count = len(word_sequence) % 2 == 0
is_high_hash = hash_accumulator > 500
stability_flag = is_even_count and is_high_hash

sentiment_stability_index = (aggregated_value + 10) if stability_flag else (aggregated_value - 5)
print(f"Result: {sentiment_stability_index}")