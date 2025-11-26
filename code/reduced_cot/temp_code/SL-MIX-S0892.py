def compute_final(data):
    process_values = lambda x: x * 2 if x > 10 else x + 5
    intermediate = process_values(data)
    if intermediate > 25:
        return intermediate - 8
    return intermediate + 3

initial_value = 15
result_data = initial_value * 2
final_score = compute_final(result_data)
print(f"Target result: {final_score}")