def process_text_data(text_input):
    temp_buffer = []
    for char in text_input:
        if char.isalpha():
            processed_char = char.lower() if ord(char) % 2 == 0 else char.upper()
            temp_buffer.append(processed_char)
    return ''.join(temp_buffer)

def compute_score(text, config):
    base_score = len(text) * 2
    multiplier = config.get('factor', 1)
    bonus = 5 if 'e' in text.lower() else 0
    offset = config.get('offset', 0)
    
    dummy_calc = base_score * multiplier + offset
    irrelevant_var = dummy_calc // 3
    
    return base_score * multiplier + bonus

def compute_final_score(data, settings):
    processed_text = process_text_data(data)
    intermediate_score = compute_score(processed_text, settings)
    
    adjustment_map = {'a': 3, 'b': 7, 'c': 2, 'd': 5}
    adjustment = 0
    for char in processed_text[:3]:
        adjustment += adjustment_map.get(char, 0)
    
    unused_calc = intermediate_score + adjustment * 2
    temp_result = intermediate_score - adjustment
    
    final_result = temp_result + settings.get('base', 10)
    print(f"Result: {final_result}")
    return final_result

text_input = "ProgrammingEvaluation2024"
config_map = {'factor': 3, 'offset': 2, 'base': 15}
processed_data = process_text_data(text_input)
final_result = compute_final_score(processed_data, config_map)