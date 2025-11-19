class TransactionNode:
    def __init__(self, tx_hash, next_node=None):
        self.tx_hash = tx_hash
        self.next = next_node

def string_to_hash_code(s):
    return sum(ord(c) * (i + 1) for i, c in enumerate(s))

# Transaction hash chain
head = TransactionNode('A1B2C3')
head.next = TransactionNode('D4E5F6')
head.next.next = TransactionNode('G7H8I9')

# Verification map
verification_map = {
    'A1B2C3': 15,
    'D4E5F6': 25,
    'G7H8I9': 35
}

# Hash modifier function
hash_modifier = lambda x: ''.join(chr((ord(c) - ord('A') + 3) % 26 + ord('A')) if 'A' <= c <= 'Z' else c for c in x)

# Process transactions
node = head
validation_scores = []
while node:
    modified_hash = hash_modifier(node.tx_hash)
    score = verification_map.get(node.tx_hash, 0) + string_to_hash_code(modified_hash)
    validation_scores.append(score)
    node = node.next

# Apply functional transformation
weighted_scores = list(map(lambda x: x * 2 if x > 50 else x // 2, validation_scores))

# Final calculation using ternary logic
final_validation_score = sum(weighted_scores) if len(weighted_scores) > 2 else 0

print(f'Result: {final_validation_score}')