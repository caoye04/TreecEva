def process_character_mapping():
    text_segments = ['data', 'PROCESS', 'input', 'OUTPUT']
    offset_calc = 0
    temp_buffer = []
    
    for segment in text_segments:
        processed_segment = segment.lower() if len(segment) % 2 == 0 else segment.upper()
        temp_buffer.append(processed_segment)
        
    for i, item in enumerate(temp_buffer):
        char_sum = sum(ord(c) for c in item)
        offset_calc += char_sum
        
    intermediate_offset = offset_calc * 3
    dummy_operation = intermediate_offset // 10
    processed_value = offset_calc - 256
    final_offset = processed_value % 17
    
    print(f"Target result: {final_offset}")

process_character_mapping()