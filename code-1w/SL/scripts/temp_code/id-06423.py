def evaluate_performance(entries, threshold):
    # Preprocess: extract names and normalize case
    names = [entry['name'].lower() for entry in entries]
    scores = [entry['score'] for entry in entries]

    # Distractor: character counting in names (not used later)
    char_count_map = {name: len(name) for name in names}
    total_chars = sum(char_count_map.values())

    # Compute frequency of unique characters per name (semi-relevant)
    unique_char_count = [len(set(name)) for name in names]

    # Normalize scores using min-max scaling (modular arithmetic twist)
    min_score, max_score = min(scores), max(scores)
    if max_score == min_score:
        normalized = [0.5 for _ in scores]
    else:
        normalized = [(s - min_score) / (max_score - min_score) for s in scores]

    # Apply threshold-based filtering
    passed = [n for n, norm in zip(names, normalized) if norm >= threshold]
    bonus_factor = len(passed) % 7  # modular arithmetic use

    # Use set operations to find high performers with diverse names
    top_names_set = set(passed)
    all_letters = set(''.join(top_names_set))
    vowel_set = {'a', 'e', 'i', 'o', 'u'}
    vowels_in_top = all_letters.intersection(vowel_set)
    distinct_vowels = len(vowels_in_top)

    # Final scoring logic
    base_value = sum(normalized) * 100
    adjustment = distinct_vowels * bonus_factor * 10
    final_score = int(base_value + adjustment)

    # Dead code path - misleading recursion
    def recursive_discount(n):
        if n <= 1:
            return n
        return n + recursive_discount(n - 2)  # never called

    # Irrelevant sorting
    sorted_names = sorted(names, key=lambda x: (-len(x), x))

    return final_score

# Input data
rankings = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 90},
    {'name': 'Charlie', 'score': 78},
    {'name': 'Diana', 'score': 95},
    {'name': 'Eve', 'score': 92}
]
base_threshold = 0.6

final_score = evaluate_performance(rankings, base_threshold)
print(f"Result: {final_score}")