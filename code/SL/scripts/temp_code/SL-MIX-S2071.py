import math

def audio_filter_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return math.log(result + 1, 10) if result > 0 else 0
    return wrapper

@audio_filter_decorator
def calculate_gain(input_level):
    base_gain = 2.5
    modulation_factor = 1.8
    return base_gain * (input_level ** modulation_factor)

gain_processor = lambda x, y: x * math.exp(y) if x > 1 else x + y

decibel_readings = [3.2, 1.9, 4.7, 2.1]
tokenized_levels = []

for reading in decibel_readings:
    tokens = str(reading).split('.')
    numeric_tokens = [int(t) for t in tokens if t.isdigit()]
    tokenized_levels.extend(numeric_tokens)

processed_signal_level = 0
valid_tokens = [t for t in tokenized_levels if t > 0]

if valid_tokens and len(valid_tokens) >= 3:
    first_cond = valid_tokens[0] > 1 and valid_tokens[1] < 5
    second_cond = valid_tokens[2] % 2 == 0 or valid_tokens[0] == 3
    
    if first_cond or second_cond:
        intermediate_value = gain_processor(valid_tokens[0], valid_tokens[1])
        if intermediate_value > 10 and not (valid_tokens[2] > 4):
            processed_signal_level = calculate_gain(intermediate_value)
        else:
            processed_signal_level = math.pow(intermediate_value, 1/3)
    else:
        processed_signal_level = sum(valid_tokens[:3])
else:
    processed_signal_level = len(tokenized_levels)

print(f"Result: {round(processed_signal_level, 6)}")