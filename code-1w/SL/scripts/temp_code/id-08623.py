def convert_temperature(raw_input):
    celsius_offset = 273.15
    kelvin_offset = int(celsius_offset)
    
    raw_str = str(raw_input)
    digit_sum = sum(int(d) for d in raw_str if d.isdigit())
    
    if len(raw_str) > 3:
        truncated = int(raw_str[:3])
    else:
        truncated = int(raw_str)
    
    processed = truncated * 2 - digit_sum
    
    if processed < 0:
        processed = abs(processed)
    
    adjusted_value = processed // 3
    final_temperature = adjusted_value + kelvin_offset
    return final_temperature

result = convert_temperature(1428)
print(f"Result: {result}")