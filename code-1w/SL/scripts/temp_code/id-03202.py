def calculate_total(values, penalty):
    processed = list(map(lambda x: x ** 2 % 7, values))
    filtered = [val for val in processed if val > 3]
    base_sum = sum(filtered)
    penalty_deduction = len(values) * penalty
    return base_sum - penalty_deduction

base_values = [4, 6, 2, 8, 3]
penalty_factor = 2
temp_diagnostic = ''.join([str(x) for x in base_values])  # Irrelevant string operation
final_score = calculate_total(base_values, penalty_factor)
print(f"Target result: {final_score}")