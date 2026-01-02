def process_sequence(seq):
    filtered = [s for s in seq if s.startswith('A')]
    transformed = [s[::-1].upper() for s in filtered]
    lengths = [len(s) for s in transformed]
    return sum(lengths) - len(transformed)

data = ['Apple', 'Ant', 'Banana', 'Avocado', 'Cherry', 'Aardvark']
result = process_sequence(data)
print(f"Target result: {result}")