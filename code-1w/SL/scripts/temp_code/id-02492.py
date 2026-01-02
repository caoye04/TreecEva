from itertools import accumulate

def main():
    data_stream = [3, 1, 4, 1, 5, 9, 2, 6]
    offset = 2
    adjusted = [x + offset for x in data_stream]
    
    # Filter values above threshold
    threshold = 5
    filtered = list(filter(lambda x: x > threshold, adjusted))
    
    # Apply cumulative operation
    processed = list(accumulate(filtered, lambda a, b: a + b % 3))
    
    # Irrelevant distraction: unused variable
    metadata_checksum = sum(data_stream) % 7
    
    key_func = lambda x: x * 2 if x % 2 == 0 else x + 1
    result = transform_data(processed, key_func)
    print(f"Result: {result}")

# External function to break inline flow slightly
def transform_data(seq, func):
    return sum(func(x) for x in seq)

if __name__ == "__main__":
    main()