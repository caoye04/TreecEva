def analyze_text(text):
    words = text.split()
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    upper_count = sum(1 for char in text if char.isupper())
    digit_count = sum(1 for char in text if char.isdigit())
    reversed_words = [word[::-1].lower() for word in words]
    palindrome_count = sum(1 for word in words if word.lower() == word.lower()[::-1])

    # Distractor: irrelevant transformation chain
    temp_transform = ''.join(reversed_words)
    shifted = temp_transform.translate(str.maketrans('aeiou', '12345'))
    dummy_score = len(shifted) * 1.5 - digit_count

    return {
        'avg_word_length': avg_length,
        'palindrome_count': palindrome_count,
        'uppercase_chars': upper_count,
        'valid_words': len([w for w in words if w.isalpha()])
    }


def preprocess_entry(entry_str):
    cleaned = entry_str.strip().replace('"', '').replace("'", "")
    parts = cleaned.split(',')
    name = parts[0].strip().title()
    age_str = parts[1].strip() if len(parts) > 1 else '0'
    
    # Distractor: parsing but not using all fields
    status = parts[2].strip().lower() if len(parts) > 2 else 'unknown'
    category_code = ord(status[0]) if status != 'unknown' else 0

    age = int(age_str) if age_str.isdigit() else 0
    
    return name, age, status


def calculate_final_score(data):
    base = data['avg_word_length'] * 10
    bonus = data['palindrome_count'] * 15
    penalty = 0
    
    if data['uppercase_chars'] > 5:
        penalty += 20
    if data['valid_words'] < 3:
        penalty += 10
    
    intermediate = (base + bonus - penalty) * 1.1
    
    # Key adjustment based on logic
    adjustment = 5 if data['valid_words'] >= 4 and data['avg_word_length'] > 4.0 else -8
    
    final_value = intermediate + adjustment
    
    # Dead code: calculated but unused
    outlier_check = abs(final_value - base) > 50
    consistency_flag = 'stable' if not outlier_check else 'review_needed'
    
    return int(round(final_value))

# Main execution flow
raw_input = "Level, 42, Active"
name, age, status = preprocess_entry(raw_input)

text_corpus = "Madam Radar Stats Python 3.9 LevelUp"
features = analyze_text(text_corpus)

# Insert age-based modification to features (state mutation)
if age > 30:
    features['avg_word_length'] += 0.5

# Introduce auxiliary computation with string methods (distractor)
status_padded = status.upper().ljust(10, '*')
encoded_tag = hash(status_padded) % 1000  # Not used later

final_score = calculate_final_score(features)
print(f"Result: {final_score}")