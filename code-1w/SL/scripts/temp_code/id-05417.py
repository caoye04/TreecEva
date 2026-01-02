def analyze_frequency(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            lower_char = char.lower()
            char_count[lower_char] = char_count.get(lower_char, 0) + 1
    return char_count

# Irrelevant helper function (dead code path)
def unused_helper(arr):
    return [x ** 2 for x in arr if x % 2 == 0]

# Misleading computation with no impact
temp_multiplier = 3.14159
dummy_offset = sum([i * 2 for i in range(5)]) - 10  # evaluates to 10

# Main processing chain
data = 'ProgrammingLanguagesAreFunToWorkWith'
char_freq = analyze_frequency(data)

vowel_count = 0
consonant_sum = 0
vowels = 'aeiou'

for char, freq in char_freq.items():
    if char in vowels:
        vowel_count += freq
    else:
        consonant_sum += ord(char) - ord('a')  # position in alphabet

# Intermediate distraction: compute average ASCII (not used later)
avg_ascii = sum(ord(c) for c in char_freq.keys()) / len(char_freq) if char_freq else 0

# Conditional expression with lambda filtering
is_significant = lambda f: f > 1
significant_vowel_contrib = sum(char_freq[c] for c in vowels if c in char_freq and is_significant(char_freq[c]))

# Complex list comprehension with filter
rare_chars = [c for c, f in char_freq.items() if f == 1 and c not in vowels]
penalty = len(rare_chars) * 2

# Distractor state tracking
state_log = []
state_log.append(('init', vowel_count))
state_log.append(('mid', consonant_sum))

# Real calculation buried among distractions
def calculate_final_score(input_data):
    local_freq = analyze_frequency(input_data)
    score = 0
    for ch, cnt in local_freq.items():
        if ch in 'aeiou':
            score += cnt * 3
        elif cnt >= 2:
            score += (ord(ch) - ord('a')) // 2
        else:
            score -= 1  # rare consonants reduce score
    bonus = 5 if len(local_freq) > 10 else 0
    return score + bonus - penalty

final_score = calculate_final_score(data)
print(f"Result: {final_score}")