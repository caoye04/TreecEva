from collections import namedtuple

token_data = namedtuple('TokenData', ['value', 'priority'])
encoded_tokens = [token_data(15, 3), token_data(28, 1), token_data(9, 2), token_data(42, 0)]
processed_values = {}
running_total = 0
modulus_base = 17
early_exit_flag = False

for idx, token in enumerate(encoded_tokens):
    if token.priority == 0:
        processed_values[token.value] = (token.value * 3) % modulus_base
        early_exit_flag = True
        break
    elif token.priority > 1 and not early_exit_flag:
        temp_calc = (token.value + idx * 2) % modulus_base
        processed_values[token.value] = temp_calc
        running_total += temp_calc
    else:
        continue

checksum_components = {k: v for k, v in processed_values.items() if k % 2 == 1}
interim_result = sum(checksum_components.values())
final_checksum = (interim_result * 2 + (1 if early_exit_flag else 0)) % modulus_base
print(f"Result: {final_checksum}")