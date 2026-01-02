from itertools import compress

def calculate_modular_sum(sequence, modulus):
    # Filter even-indexed elements using a boolean selector
    selector = [(i % 3 == 0) for i in range(len(sequence))]
    filtered = list(compress(sequence, selector))
    
    # Compute sum of filtered elements and apply modular arithmetic
    total = sum(filtered)
    result = total % modulus
    
    # Irrelevant auxiliary variable (minimal distraction)
    temp_debug = [x for x in sequence if x > 5]  
    
    return result

# Main execution
sequence = [12, 7, 3, 9, 4, 6, 8, 11, 5]
modulus = 17
result = calculate_modular_sum(sequence, modulus)
print(f"Result: {result}")