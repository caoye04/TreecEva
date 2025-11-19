import math

def calculate_token_weight(token):
    vowels = set('aeiouAEIOU')
    vowel_count = sum(1 for char in token if char in vowels)
    consonant_count = len(token) - vowel_count
    return vowel_count * 3 - consonant_count if consonant_count > 0 else 0

def process_document(doc_text):
    sentences = doc_text.split('.')
    sentence_scores = []
    
    for sentence in sentences:
        tokens = [token.strip().lower() for token in sentence.split() if token.isalpha()]
        valid_tokens = [t for t in tokens if len(t) > 2 and 'a' in t]
        
        if not valid_tokens:
            continue
            
        weights = [calculate_token_weight(token) for token in valid_tokens]
        avg_weight = sum(weights) / len(weights) if weights else 0
        
        if avg_weight > 5:
            modifier = 2
        elif avg_weight < 0:
            modifier = -1
        else:
            modifier = 1
            
        sentence_score = math.ceil(avg_weight) * modifier
        sentence_scores.append(sentence_score)
        
        if len(sentence_scores) >= 3 and sum(sentence_scores[-3:]) > 15:
            break
    
    return sum(sentence_scores) if sentence_scores else 0

technical_corpus = [
    "Advanced algorithms require mathematical optimization techniques.",
    "Data structures facilitate efficient information retrieval systems.",
    "Machine learning models utilize statistical pattern recognition methods.",
    "Cryptographic protocols ensure secure communication channels.",
    "Database normalization eliminates redundant data storage issues."
]

processed_scores = [process_document(doc) for doc in technical_corpus]
valid_scores = [score for score in processed_scores if score != 0]

if len(valid_scores) >= 2:
    pairwise_products = [valid_scores[i] * valid_scores[i+1] for i in range(len(valid_scores)-1)]
    max_product = max(pairwise_products)
    final_complexity_index = max_product // 2 + len(set(str(max_product)))
else:
    final_complexity_index = sum(valid_scores) * 3

print(f"Result: {final_complexity_index}")