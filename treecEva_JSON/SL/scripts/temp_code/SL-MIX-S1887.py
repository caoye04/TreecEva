from collections import defaultdict

document_ids = [12, 27, 34, 49, 56, 63, 78, 81, 92, 105]
classified_docs = defaultdict(set)
prime_collection = frozenset([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])

for doc_id in document_ids:
    factors = {f for f in prime_collection if doc_id % f == 0}
    if factors:
        classified_docs[min(factors)].add(doc_id)
    else:
        classified_docs[0].add(doc_id)

historical_set = set()
for prime_key in sorted(classified_docs.keys()):
    subset = classified_docs[prime_key]
    if prime_key != 0 and len(subset) > 1:
        historical_set |= subset
    elif prime_key == 0:
        historical_set -= subset

lambda_filter = lambda x: x > 50 and bin(x).count('1') % 2 == 0
filtered_docs = set(filter(lambda_filter, historical_set))
thematic_count = len(filtered_docs)

print(f'Result: {thematic_count}')