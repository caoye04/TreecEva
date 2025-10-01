import math

def process_nested_data(data):
    transformed = []
    for i, sublist in enumerate(data):
        temp = []
        for j, val in enumerate(sublist):
            if isinstance(val, int):
                temp.append(val ** 2 if j % 2 == 0 else math.sqrt(val))
            elif isinstance(val, str):
                temp.append(len(val) * (i + 1))
        transformed.append(temp)
    return transformed

def aggregate_transformed(data):
    total = 0
    for sublist in data:
        for val in sublist:
            if isinstance(val, (int, float)):
                total += val
    return total

def apply_bitwise_operations(value):
    # Apply a sequence of bitwise operations
    value = (value & 0xFF) | 0x10
    value = value ^ 0x0F
    value = value << 2
    return value

def main():
    # Initial nested data structure
    nested_data = [
        [4, 9, 'hello', 16],
        ['world', 25, 36, 'test'],
        [49, 'example', 64, 81]
    ]
    
    # Step 1: Process nested data
    processed = process_nested_data(nested_data)
    
    # Step 2: Aggregate transformed values
    aggregated = aggregate_transformed(processed)
    
    # Step 3: Apply mathematical operations
    aggregated = math.floor(aggregated / 3.0) * 2
    
    # Step 4: Apply bitwise operations
    bitwise_result = apply_bitwise_operations(aggregated)
    
    # Step 5: Final calculation step
    result = (bitwise_result % 1000) + sum([ord(c) for c in 'SLMIX'])
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()