from collections import Counter

def calculate_score(data: str, limit: int) -> int:
    char_count = Counter(data)
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_sum = sum(count for char, count in char_count.items() if char.lower() in vowels)
    consonant_sum = sum(count for char, count in char_count.items() if char.isalpha() and char.lower() not in vowels)
    
    # Apply logic: if vowel frequency is high enough, boost score
    base_score = consonant_sum - vowel_sum
    if vowel_sum >= limit:
        base_score += 5
    
    temp_flag = True  # Irrelevant flag (minimal distraction)
    return base_score

text_data = "educationally"
threshold = 3
result = calculate_score(text_data, threshold)
print(f"Result: {result}")