from collections import defaultdict
word_frequencies = defaultdict(int)
primary_lexicon = {'quantum', 'entanglement', 'superposition', 'wavefunction'}
secondary_lexicon = frozenset(['quantum', 'mechanics', 'schrodinger', 'equation'])
text_corpus = ['quantum', 'physics', 'quantum', 'mechanics', 'entanglement', 'quantum']
for term in text_corpus:
    word_frequencies[term] += 1
common_terms = primary_lexicon & secondary_lexicon
unique_primary = primary_lexicon - secondary_lexicon
hash_cache = {}
def get_hash(token_set):
    if id(token_set) not in hash_cache:
        hash_cache[id(token_set)] = hash(frozenset(token_set))
    return hash_cache[id(token_set)]
lexicon_hash_match = get_hash(primary_lexicon) == get_hash(secondary_lexicon)
semantic_distance = 0
if lexicon_hash_match or len(common_terms) > len(unique_primary):
    semantic_distance = sum(word_frequencies[word] for word in common_terms)
else:
    semantic_distance = sum(word_frequencies[word] for word in unique_primary)
print(f'Result: {semantic_distance}')