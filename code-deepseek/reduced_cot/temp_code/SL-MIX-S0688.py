data_points = [12, 7, 15, 22, 9, 25, 18, 31, 10, 42]
processing_count = len([x for x in data_points if x % 3 == 0 or x % 5 == 0])
print(f"Result: {processing_count}")