from collections import defaultdict

# Simulate text analysis for linguistic pattern scoring
def analyze_text_patterns(text_blocks):
    word_freq = defaultdict(int)
    for block in text_blocks:
        words = block.lower().split()
        for word in words:
            cleaned = ''.join(filter(str.isalpha, word))
            if len(cleaned) > 1:
                word_freq[cleaned] += 1
    return word_freq

text_blocks = [
    "The matrix transforms vectors via linear operations",
    "Eigenvalues reveal dynamic system behaviors",
    "Linear algebra underpins modern computation models"
]

word_freq = analyze_text_patterns(text_blocks)

# Define adjustment rules based on word length patterns
adjustment_map = {}
for word in word_freq:
    base_adj = len(word) % 3
    adjustment_map[word] = base_adj

# Calculate final composite score
def calculate_final_score(freq_dict, adj_map):
    raw_total = sum(freq_dict.values())
    adjustment_sum = sum(adj_map[w] * freq_dict[w] for w in freq_dict)
    return raw_total + adjustment_sum

final_score = calculate_final_score(word_freq, adjustment_map)
print(f"Target result: {final_score}")