numbers = [12, 7, 18, 23, 9, 31, 15, 4, 27]
# Initial processing step
filtered_result = list(filter(lambda x: x % 3 == 0, numbers))
# Calculate final count
final_count = len(filtered_result)
print(f"Result: {final_count}")