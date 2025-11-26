even_numbers = [i for i in range(1, 21) if i % 2 == 0]
filtered_numbers = list(filter(lambda x: x % 3 == 0, even_numbers))
final_result = len(filtered_numbers)
print(f"Result: {final_result}")