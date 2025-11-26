data_sequence = [42, 18, 73, 29, 56, 91, 14, 67, 33, 88]
processing_flag = True
processed_data = data_sequence[2:8]
if processing_flag:
    processed_data = [x + 5 for x in processed_data]
final_result = processed_data[len(processed_data)//2]
print(f"Result: {final_result}")