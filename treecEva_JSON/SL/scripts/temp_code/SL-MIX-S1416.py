import hashlib

def tokenize(sentence):
    return [word.strip(',.!?') for word in sentence.lower().split()]

def hash_word(word):
    return int(hashlib.md5(word.encode()).hexdigest()[:8], 16)

def compute_similarity(tokens1, tokens2):
    hashes1 = {hash_word(token) for token in tokens1}
    hashes2 = {hash_word(token) for token in tokens2}
    
    intersection = hashes1 & hashes2
    union = hashes1 | hashes2
    
    if not union:
        return 0
    
    return len(intersection) / len(union)

def recursive_combination_score(hashes_list, index=0, current_set=set()):
    if index == len(hashes_list):
        if len(current_set) >= 2:
            product = 1
            for h in current_set:
                product *= (h % 100)
            return product
        return 0
    
    # Include current element
    score_with = recursive_combination_score(hashes_list, index + 1, current_set | {hashes_list[index]})
    # Exclude current element
    score_without = recursive_combination_score(hashes_list, index + 1, current_set)
    
    return score_with + score_without

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A fast auburn fox leaps above a sleepy canine.",
    "Pack my box with five dozen liquor jugs."
]

tokenized_sentences = [tokenize(s) for s in sentences]
all_hashes = []
for tokens in tokenized_sentences:
    for token in tokens:
        all_hashes.append(hash_word(token))

pairwise_scores = []
for i in range(len(tokenized_sentences)):
    for j in range(i+1, len(tokenized_sentences)):
        sim = compute_similarity(tokenized_sentences[i], tokenized_sentences[j])
        pairwise_scores.append(sim)

avg_similarity = sum(pairwise_scores) / len(pairwise_scores) if pairwise_scores else 0

combination_score = recursive_combination_score(all_hashes[:5])

final_score = int(avg_similarity * combination_score)
print(f"Result: {final_score}")