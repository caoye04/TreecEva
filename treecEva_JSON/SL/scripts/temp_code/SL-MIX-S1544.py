from functools import reduce

doc_metadata = [
    ('a1b2', 5),
    ('c3d4', 3),
    ('e5f6', 7),
    ('0x789', 4),
    ('dead', 2)
]

# Process document metadata using functional programming
revision_weights = list(map(lambda doc: doc[1] * (3 if bin(int(doc[0], 16)).count('1') % 2 == 0 else 2), doc_metadata))

# Calculate cumulative score with a reduction operation
raw_score = reduce(lambda acc, weight: acc + weight, revision_weights, 0)

# Apply final transformation using ternary operator
final_score = raw_score - 50 if raw_score > 100 else raw_score + 25

print(f"Result: {final_score}")