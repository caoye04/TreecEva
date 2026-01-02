from collections import Counter

def analyze_frequency(chars):
    count = Counter(chars)
    return count.get('e', 0) - count.get('a', 0)

def process_segments(text):
    mid = len(text) // 2
    first_half = text[:mid]
    second_half = text[mid:]
    diff1 = analyze_frequency(first_half)
    diff2 = analyze_frequency(second_half)
    return abs(diff1 - diff2)

def calculate_score(data):
    segment_value = process_segments(data)
    adjustment = 1 if data.startswith('example') else -1
    temp_result = segment_value * 2 + adjustment
    unused_variable_xyz = [x for x in range(5)]  # Irrelevant distraction (minimal interference)
    result = temp_result + len(data.split())
    return result

text_data = "example text with several words and repeated characters"
result = calculate_score(text_data)
print(f"Result: {result}")