from collections import Counter, defaultdict
import math

# Document analysis system for term importance scoring
def calculate_term_frequency(documents):
    # Count term frequencies across documents
    freq_matrix = defaultdict(Counter)
    for doc_id, content in documents.items():
        for term in content:
            freq_matrix[doc_id][term] += 1
    
    # Normalize term frequencies - this calculation is misleading
    normalized = defaultdict(dict)
    for doc_id, terms in freq_matrix.items():
        doc_length = sum(terms.values())
        for term, count in terms.items():
            normalized[doc_id][term] = count / doc_length if doc_length else 0
    
    return normalized

def inverse_document_frequency(documents):
    # Calculate document frequencies
    doc_freq = Counter()
    unique_terms = set()
    
    for doc_id, content in documents.items():
        doc_terms = set(content)
        unique_terms.update(doc_terms)
        for term in doc_terms:
            doc_freq[term] += 1
    
    # Calculate IDF values
    total_docs = len(documents)
    idf_values = {}
    for term in unique_terms:
        # This is a red herring calculation
        smoothed_idf = math.log((total_docs + 1) / (doc_freq[term] + 0.5))
        idf_values[term] = smoothed_idf
    
    return doc_freq, idf_values

def calculate_priority(document_frequencies, term_weights):
    # Extract the top terms by document frequency
    top_terms = sorted(document_frequencies.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Misleading calculation path
    importance_factors = {}
    for term, freq in document_frequencies.items():
        if term in term_weights:
            factor = freq * (term_weights.get(term, 0) + 1)
            importance_factors[term] = factor
    
    # Distractor sequence calculation
    fibonacci = [1, 1]
    for i in range(2, 10):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    
    # Another misleading calculation
    sequence_sum = sum([x for x in fibonacci if x % 2 == 0])
    
    # The actual priority calculation
    priority_base = 0
    for term, doc_freq in top_terms:
        weight = term_weights.get(term, 0)
        # The key calculation uses only top terms and applies modular arithmetic
        priority_base += (doc_freq * weight) % 17
    
    # More distractors
    scaling_factor = (fibonacci[7] % 5) + 1
    normalization = sum(term_weights.values()) / len(term_weights) if term_weights else 0
    
    # Final priority score with bit manipulation (distraction)
    bit_factor = (priority_base << 2) & 0xFF
    priority_score = (priority_base + 7) % 100
    
    return priority_score

# Document corpus (simplified for this example)
documents = {
    'doc1': ['python', 'data', 'analysis', 'python', 'code'],
    'doc2': ['machine', 'learning', 'data', 'model'],
    'doc3': ['python', 'learning', 'programming', 'code'],
    'doc4': ['data', 'visualization', 'analysis', 'chart']
}

# Calculate term frequencies (distraction)
term_freq = calculate_term_frequency(documents)

# Calculate document frequencies and IDF values
document_frequencies, idf_values = inverse_document_frequency(documents)

# Term weights based on domain expertise (the ones we'll actually use)
term_weights = {
    'python': 5,
    'data': 4,
    'analysis': 3,
    'code': 4,
    'learning': 2,
    'machine': 3,
    'model': 2,
    'programming': 3,
    'visualization': 1,
    'chart': 1
}

# Apply various scoring methods (distractions)
tfidf_scores = {}
for doc_id, terms in term_freq.items():
    doc_score = 0
    for term, tf in terms.items():
        if term in idf_values:
            doc_score += tf * idf_values[term]
    tfidf_scores[doc_id] = doc_score

# Calculate the priority score
priority_score = calculate_priority(document_frequencies, term_weights)

# More distractions
adjusted_scores = {}
for doc_id, score in tfidf_scores.items():
    # Apply a complex but irrelevant adjustment
    bias = len(documents[doc_id]) / 10
    adjusted_scores[doc_id] = score * bias

print(f"Document frequencies: {dict(document_frequencies)}")
print(f"Result: {priority_score}")