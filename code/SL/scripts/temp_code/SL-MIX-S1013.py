import math
from collections import namedtuple

# Define a configuration structure
def create_encryption_config():
    Config = namedtuple('Config', ['base_modulus', 'key_strength', 'log_base'])
    return Config(17, 23, 2)

# Lambda for modular exponentiation
mod_exp = lambda base, exp, mod: pow(base, exp, mod)

# Security computation function
compute_security = lambda x, y: (x & y) | (x ^ y)

# Main computation
config = create_encryption_config()
intermediate_result = mod_exp(config.base_modulus, config.key_strength, 100)
log_component = int(math.log(intermediate_result, config.log_base))

# Boolean logic chain
condition_a = (intermediate_result % 5) == (log_component % 5)
condition_b = not ((intermediate_result > 50) and (log_component < 20))
condition_c = (intermediate_result != log_component) or (intermediate_result >= log_component)

final_mask = 0
if condition_a and condition_b:
    final_mask = intermediate_result >> 2
elif condition_b or condition_c:
    final_mask = log_component << 1
else:
    final_mask = intermediate_result ^ log_component

security_index = compute_security(intermediate_result, final_mask) % 37
print(f"Result: {security_index}")