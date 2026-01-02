def process_data(data, limit):
    filtered = [x for x in data if x > limit]
    indexed = list(enumerate(filtered))
    transformed = [i ^ val for i, val in indexed]
    return sum(transformed) // len(transformed) if transformed else 0

values = [12, 3, 8, 15, 27, 6, 11]
thresh = 7
result = process_data(values, thresh)
print(f"Target result: {result}")