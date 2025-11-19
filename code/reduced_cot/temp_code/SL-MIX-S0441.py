from collections import defaultdict
import itertools

class TreeNode:
    def __init__(self, length):
        self.length = length
        self.words = []
        self.left = None
        self.right = None

def insert_word(root, word):
    word_len = len(word)
    if word_len < root.length:
        if root.left is None:
            root.left = TreeNode(word_len)
        insert_word(root.left, word)
    elif word_len > root.length:
        if root.right is None:
            root.right = TreeNode(word_len)
        insert_word(root.right, word)
    else:
        root.words.append(word)

def calculate_score(word_freq, threshold=2):
    return sum((freq * 3 if freq > threshold else freq) for freq in word_freq.values())

manuscript_words = ['ancient', 'text', 'symbol', 'ancient', 'glyph', 'text', 'mark', 'symbol', 'ancient', 'cipher']
word_frequency = defaultdict(int)

for word in manuscript_words:
    word_frequency[word] += 1

root = TreeNode(5)
for word in set(manuscript_words):
    insert_word(root, word)

# Calculate scores from different tree branches
left_branch_words = []
right_branch_words = []

if root.left:
    left_branch_words = list(itertools.chain.from_iterable(
        [[word] * word_frequency[word] for word in root.left.words]
    ))
if root.right:
    right_branch_words = list(itertools.chain.from_iterable(
        [[word] * word_frequency[word] for word in root.right.words]
    ))

left_freq = defaultdict(int)
right_freq = defaultdict(int)
for word in left_branch_words:
    left_freq[word] += 1
for word in right_branch_words:
    right_freq[word] += 1

branch_scores = []
branch_scores.append(calculate_score(left_freq))
branch_scores.append(calculate_score(right_freq))

final_score = sum(branch_scores) if branch_scores else 0
final_score = final_score + (10 if len(manuscript_words) > 5 else 0)

print(f"Result: {final_score}")