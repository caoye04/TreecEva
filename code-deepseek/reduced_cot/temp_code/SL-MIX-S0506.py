data = [22, 8, 35, 12, 19, 5, 27, 14]
temp_calc = len(data) * 3 - 5
result = sorted(filter(lambda x: x > 15, data))
target_result = result[1] if len(result) > 1 else -1
print(f"Target result: {target_result}")