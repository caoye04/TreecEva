from collections import Counter

def analyze_frequency(chars):
    count = Counter(chars)
    return count['a'] + count.get('e', 0)

def transform_string(s):
    reversed_s = s[::-1]
    upper_s = reversed_s.upper()
    return upper_s.lower()

def calculate_score(data):
    cleaned = ''.join([c for c in data if c.isalpha()])
    freq_value = analyze_frequency(cleaned)
    length_factor = len(cleaned) // 2
    score = freq_value * length_factor
    if 'xyz' in data:
        score -= 10
    return score

text_data = "exaggerated anxiety causes real trouble"
interim = transform_string(text_data)
result = calculate_score(text_data)
print(f"Result: {result}")