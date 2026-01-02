def process_string_data(data):
    char_count = len(data)
    vowel_count = sum(1 for c in data.lower() if c in 'aeiou')
    upper_count = sum(1 for c in data if c.isupper())
    score = char_count * 2 - vowel_count + (upper_count * 3)
    normalized = score / 2.5
    result = int(normalized)
    return result

# Irrelevant auxiliary variable
auxiliary_flag = True

text_input = "DynamicAnalysisTool"
result = process_string_data(text_input)
print(f"Target result: {result}")