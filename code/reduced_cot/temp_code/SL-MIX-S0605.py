data_stream = [12, 8, 15, 6, 20, 3]
enumerated_values = [(idx, val * 2 if idx % 2 == 0 else val + 5) for idx, val in enumerate(data_stream)]
final_result = max(enumerated_values)
print(f"Result: {final_result}")