from collections import defaultdict

# Simulate character frequency counting in a text processing pipeline
def analyze_text_patterns(text_blocks):
    counts = defaultdict(int)
    for block in text_blocks:
        cleaned = block.strip().lower()
        for char in cleaned:
            if char.isalpha():
                counts[char] += 1

    # Irrelevant helper (minimal distraction)
    unused_freqs = {k: v for k, v in counts.items() if v > 2}

    return counts

def calculate_final_score(freq_dict, weight_map):
    score = 0.0
    for char, count in freq_dict.items():
        weight = weight_map.get(char, 0.5)
        score += count * weight
    return int(score)

# Input data
documents = [
    "Data analysis requires precision.",
    "Machine learning models improve over time.",
    "Code reasoning benchmarks are essential."
]

# Weight map for scoring
weights = {chr(i): (i - 96) * 0.1 for i in range(97, 123)}  # a=0.1, b=0.2, ..., z=2.6

# Main execution flow
character_counts = analyze_text_patterns(documents)
total_score = calculate_final_score(character_counts, weights)

# Output result
print(f"Result: {total_score}")