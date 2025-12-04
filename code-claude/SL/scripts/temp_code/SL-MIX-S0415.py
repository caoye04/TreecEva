import itertools

def calculate_word_value(word, multipliers=None):
    """Calculate value of a word based on character positions and optional multipliers."""
    # Distraction function that isn't used in main flow
    if not word:
        return 0
    
    base_value = sum(ord(c) - 96 for c in word.lower() if 'a' <= c.lower() <= 'z')
    
    if multipliers:
        return base_value * sum(multipliers)
    return base_value

def analyze_text_patterns(text):
    # Another distraction function
    if not text:
        return {}
        
    words = text.lower().split()
    patterns = {}
    for word in words:
        key = ''.join(sorted(set(word)))
        if key in patterns:
            patterns[key].append(word)
        else:
            patterns[key] = [word]
    return patterns

def calculate_final_score(words, priority_indices):
    # This is the function that will determine our answer
    base_points = 0
    bonus_points = 0
    penalty = 0
    
    # Misleading calculation
    irrelevant_sum = sum(ord(w[0]) for w in words if w)
    
    # Process words with their indices
    for i, word in enumerate(words):
        # Misleading calculation
        temp_value = len(word) * (i + 1)
        
        # Actual scoring logic
        if i in priority_indices:
            base_points += len(word) * 2
            # Important calculation for bonus
            if len(set(word)) == len(word):  # unique letters
                bonus_points += 15
        else:
            base_points += len(word)
            # Distractor calculation
            if word.startswith('z'):
                penalty += 50
    
    # More distracting calculations
    max_possible = sum(len(w) * 3 for w in words)
    efficiency_ratio = base_points / max_possible if max_possible else 0
    
    # Calculate letter frequency (distractor)
    all_letters = ''.join(words)
    freq = {}
    for letter in all_letters:
        freq[letter] = freq.get(letter, 0) + 1
    
    # Final score calculation
    score = base_points + bonus_points - penalty
    
    # Misleading return value preparation
    potential_scores = [score * 0.8, score * 1.2, score * 0.5]
    
    return score

# Main execution flow
text_sample = "the quick brown fox jumps over lazy dog"
all_words = text_sample.split()

# Distracting operations
word_patterns = analyze_text_patterns(text_sample)
unique_letters = set(text_sample.replace(" ", ""))

# Misleading variable
decoy_score = calculate_word_value("distraction", [1.5, 2])

# Slicing operation - relevant
selected_words = all_words[1:7:2]  # 'quick', 'fox', 'over'

# Zip and enumerate - creating distractions
word_lengths = [len(word) for word in all_words]
paired_data = list(zip(all_words, word_lengths))

# More distractions
for i, (word, length) in enumerate(paired_data):
    if length > 4:
        decoy_score += i

# Set operations - partly relevant
consonants = set("bcdfghjklmnpqrstvwxyz")
vowels = set("aeiou")

# Filter words - relevant for final calculation
filtered_words = []
for word in selected_words:
    consonant_count = len([c for c in word.lower() if c in consonants])
    vowel_count = len([c for c in word.lower() if c in vowels])
    
    # Condition that affects our answer
    if consonant_count > vowel_count:
        filtered_words.append(word)

# Create priority indices - relevant for final calculation
priority_indices = set()
for i, word in enumerate(filtered_words):
    # Condition that affects our answer
    if 'o' in word or 'e' in word:
        priority_indices.add(i)

# This is our target calculation
actual_score = calculate_final_score(filtered_words, priority_indices)

# More distractions after the target calculation
total_letters = sum(len(word) for word in filtered_words)
average_length = total_letters / len(filtered_words) if filtered_words else 0

# Misleading final calculations that don't affect our answer
if decoy_score > 100:
    adjusted_score = actual_score * 1.5
else:
    adjusted_score = actual_score * 0.9

print(f"Result: {actual_score}")