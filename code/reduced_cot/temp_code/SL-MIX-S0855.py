from functools import reduce

documents_corpus = [
    "the quick brown fox jumps over the lazy dog",
    "a quick brown dog outpaces a lazy fox",
    "the dog and the fox are quick and lazy"
]

# Process each document into a set of unique words
lexical_sets = list(map(lambda doc: set(doc.split()), documents_corpus))

# Create signatures by hashing frozensets of words
signatures = list(map(lambda word_set: hash(frozenset(word_set)), lexical_sets))

# Build hash table mapping signatures to their word sets
signature_table = dict(zip(signatures, lexical_sets))

# Find common vocabulary across all documents
common_vocabulary = reduce(lambda acc, word_set: acc & word_set, lexical_sets)

# Calculate signature hashes for the common vocabulary
common_signature = hash(frozenset(common_vocabulary))

# Determine how many original signatures match subsets of the common vocabulary
intersection_cardinality = len(list(filter(lambda sig: signature_table[sig] <= common_vocabulary, signature_table)))

print(f"Result: {intersection_cardinality}")