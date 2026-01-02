def final_computation():
    base = 7
    exponent = 4
    mod_factor = 13

    # Compute power under modulo using built-in pow for efficiency
    intermediate = pow(base, exponent, mod_factor)

    # Define a lambda to check if number is even and scale by 3 if true
    scale_if_even = lambda x: x * 3 if x % 2 == 0 else x + 5

    adjusted = scale_if_even(intermediate)

    # Apply modular adjustment to keep within bounds
    result = (adjusted + 9) % 17
    
    return result

# Execute and print result
target_result = final_computation()
print(f"Result: {target_result}")