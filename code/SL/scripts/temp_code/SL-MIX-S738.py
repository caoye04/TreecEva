import math
from collections import defaultdict

def process_cosmic_signal(frequency):
    if frequency <= 0:
        return 0
    # Apply modular exponentiation with prime modulus
    mod_exp_result = pow(frequency, 17, 31)
    # Apply logarithmic transformation
    log_scaled = int(math.log(mod_exp_result + 1) * 10)
    return log_scaled % 23

cosmic_ray_frequencies = [42, 18, 73, 29, 55, 36, 91]
signal_categories = defaultdict(int)

for idx, freq in enumerate(cosmic_ray_frequencies):
    processed_value = process_cosmic_signal(freq)
    category = processed_value % 5
    
    match category:
        case 0:
            signal_categories['alpha'] += processed_value
        case 1 | 2:
            signal_categories['beta'] += processed_value * 2
        case 3:
            signal_categories['gamma'] += processed_value // 2
        case 4:
            signal_categories['delta'] += processed_value ** 2
        case _:
            signal_categories['unknown'] += 1

# Calculate final stellar classification index
stellar_classification_index = (
    (signal_categories['alpha'] * 3) ^ 
    (signal_categories['beta'] // 4) ^ 
    (signal_categories['gamma'] + signal_categories['delta'])
) % 100

print(f"Result: {stellar_classification_index}")