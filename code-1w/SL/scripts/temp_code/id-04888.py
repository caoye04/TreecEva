def generate_pattern(length):
    return [i ** 2 for i in range(length)]


def validate_sequence(seq):
    return all(x % 2 == 0 for x in seq)


def calculate_final_score(sequences):
    scores = []
    for idx, seq in enumerate(sequences):
        if len(seq) > 3:
            adjusted = [x + idx for x in seq]
            filtered = [x for x in adjusted if x > 10]
            scores.append(sum(filtered))
        else:
            scores.append(0)
    total = sum(scores)
    penalty = 5 if any(validate_sequence(seq) for seq in sequences) else 0
    return total - penalty

# Generate input sequences
base = generate_pattern(5)
sequences = [
    base[:3],
    base,
    [x * 2 for x in base[:4]]
]

# Irrelevant utility function (minor interference)
def unused_helper(data):
    return ''.join([str(len(str(x))) for x in data])

result = calculate_final_score(sequences)
print(f"Result: {result}")