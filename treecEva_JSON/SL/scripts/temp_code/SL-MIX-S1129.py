import math
from functools import reduce

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def key_validator(initial_key, constraints):
    temp_key = initial_key
    for i, (modulus, threshold) in enumerate(constraints):
        if temp_key > 0 and modulus > 1:
            temp_key = mod_exp(temp_key, i+1, modulus) 
            if temp_key >= threshold or (temp_key % 2 == 0 and i % 2 != 0):
                continue
            else:
                temp_key = temp_key // 2 if temp_key > 10 else temp_key * 2
        else:
            temp_key = temp_key + 1 if temp_key <= 0 else temp_key - 1
    return temp_key

constraints_set = [(17, 5), (19, 7), (23, 11)]
initial_candidate = 12
validated_key_strength = key_validator(initial_candidate, constraints_set)

# Apply logarithmic scaling only if the validated strength is non-zero
scaled_result = math.log(validated_key_strength) if validated_key_strength > 0 else 0
validated_key_strength = int(scaled_result) if scaled_result.is_integer() else round(scaled_result)

print(f"Result: {validated_key_strength}")