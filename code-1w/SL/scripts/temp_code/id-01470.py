def analyze_text_patterns(text_data):
    char_frequency = {}
    for char in text_data:
        if char.isalpha():
            char_frequency[char.lower()] = char_frequency.get(char.lower(), 0) + 1
    
    vowel_count = sum(count for letter, count in char_frequency.items() if letter in 'aeiou')
    consonant_count = sum(count for letter, count in char_frequency.items() if letter not in 'aeiou')
    diversity_score = len(char_frequency)

    # Distractor: irrelevant transformation
    temp_encoded = ''.join([chr((ord(c) - 97 + 3) % 26 + 97) if c.isalpha() else c for c in text_data.lower()])
    
    return vowel_count, consonant_count, diversity_score


def validate_integrity(check_sequence):
    cumulative = 0
    for i, val in enumerate(check_sequence):
        cumulative += (i + 1) * val  # weighted accumulation
    checksum = cumulative % 101
    return checksum == 42

# Simulated system log with embedded patterns
text_corpus = "Dynamic Analysis of Neural Patterns in Cognitive Systems"
numeric_sequence = [5, 8, 4, 9, 7, 6]

# Extract linguistic features
vowels, consonants, variety = analyze_text_patterns(text_corpus)

# Irrelevant intermediate computation (dead-end path)
entropy_approx = variety * 0.7071  # Not used later

# State tracking variables
status_flags = set()
system_health = True

# Evaluate multiple conditions
if vowels > 5 and variety >= 10:
    status_flags.add('LINGUISTIC_COMPLEXITY_OK')

if validate_integrity(numeric_sequence):
    status_flags.add('INTEGRITY_VERIFIED')
else:
    status_flags.discard('INTEGRITY_VERIFIED') if 'INTEGRITY_VERIFIED' in status_flags else None

# Core logic chain
baseline = vowels * 2 + consonants // 3
adjustment_factor = len(text_corpus.split())  # word count contribution

# Secondary distraction: unused statistical moment
moment_2 = sum((x - sum(numeric_sequence)/len(numeric_sequence))**2 for x in numeric_sequence) / len(numeric_sequence)

passing_threshold = 45
achievement_bonus = 0

if baseline >= passing_threshold - 10:
    achievement_bonus = 8
    secondary_adjust = variety // 4
    if secondary_adjust > 2:
        achievement_bonus += 3

# Misleading control flow with redundant check
if 'LINGUISTIC_COMPLEXITY_OK' in status_flags:
    temp_score = baseline + achievement_bonus
    if temp_score < passing_threshold:
        achievement_bonus += 2  # minor correction

# Final performance evaluation
def evaluate_performance(log, threshold):
    base = vowels * 2 + consonants // 3 + achievement_bonus
    penalty = 0
    
    words = text_corpus.strip().split()
    long_words = [w for w in words if len(w) > 5]  # list comprehension
    
    if len(long_words) < 4:
        penalty += 5
    
    unique_chars = set(text_corpus.lower())  # set operation
    if 'z' not in unique_chars and 'x' not in unique_chars:
        penalty -= 2  # leniency
    
    final_value = base - penalty
    return final_value

final_score = evaluate_performance(text_corpus, passing_threshold)
print(f"Result: {final_score}")