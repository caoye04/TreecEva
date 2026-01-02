def compute_string_score(input_str):
    char_points = {chr(i): i - 96 for i in range(97, 123)}
    extra_bonus = 10
    total_score = 0
    
    for index, char in enumerate(input_str.lower()):
        if char.isalpha():
            total_score += char_points[char]
            if index % 2 == 0:
                total_score += 2
    
    return total_score

result = compute_string_score('Logic')
print(f'Result: {result}')