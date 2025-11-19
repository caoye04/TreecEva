import math
from functools import reduce

def modular_power(base, exp, mod):
    return pow(base, exp, mod)

def validate_checksum(value, threshold):
    if value <= 1:
        return value
    elif value < threshold:
        return validate_checksum(value + 7, threshold)
    else:
        return value

crypto_keys = [3, 5, 7, 9, 11]
threshold_limit = 50
modulus_base = 13

transformed_values = [
    modular_power(key, int(math.log(key) * 2), modulus_base) 
    for key in crypto_keys 
    if key > 4
]

validated_results = [
    validate_checksum(val * 3, threshold_limit)
    for val in transformed_values
]

final_validated_sum = reduce(lambda x, y: x + y, validated_results, 0)

print(f"Result: {final_validated_sum}")