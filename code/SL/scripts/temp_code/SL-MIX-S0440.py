subnet_options = {0b11111111, 0b11111110, 0b11111100, 0b11111000}
magic_number = 0b11111111
user_input = 0b11111100

is_valid_mask = (user_input & magic_number) in subnet_options
validation_flag = int(is_valid_mask) << 2

print(f'Result: {validation_flag}')