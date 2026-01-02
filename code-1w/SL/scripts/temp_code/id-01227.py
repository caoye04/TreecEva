def process_item(x):
    return x * 2 + 1

# Irrelevant helper (mild distraction)
def unused_helper(y):
    return y ** 2

data_stream = [3, 5, 7]

# Lambda for transformation
mapper = lambda items: [process_item(x) for x in items]

# Filtering condition using comparison operations
temp_result = [val for val in mapper(data_stream) if val > 10]

# Processor function combining mapping and reduction
processor = lambda seq: sum(seq) // len(seq) if seq else 0

final_output = processor(temp_result)
print(f"Result: {final_output}")