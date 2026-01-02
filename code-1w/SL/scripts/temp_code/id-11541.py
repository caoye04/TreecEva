def calculate_final_score(data):
    word_count = len(data.split())
    char_count = len(data.replace(' ', ''))
    unique_chars = len(set(char_count.lower() for char_count in data if char_count.isalpha()))

    stats = {
        'length': word_count,
        'chars_no_space': char_count,
        'unique_letters': unique_chars
    }

    # Irrelevant metric (mild distraction)
    ignored_metric = data.count('.') + data.count(',')

    score = (stats['length'] * 2) + (stats['chars_no_space'] // 5)
    bonus = 10 if stats['unique_letters'] > 10 else 5

    final_part = score + bonus
    return final_part

# Input text about climate patterns
text_data = "Climate variations affect ecosystems. Temperature shifts impact species distribution and seasonal behaviors."

final_score = calculate_final_score(text_data)
print(f'Result: {final_score}')