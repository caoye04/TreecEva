def main():
    threshold = 7
    scale_factor = 3
    offset = 2
    
    # Irrelevant distraction variable (minimal interference)
    dummy_counter = 0
    
    transform = lambda x: (x ** 2) % threshold
    
    def processor(values):
        accumulated = 0
        for val in values:
            if val > threshold:
                processed = transform(val) + offset
            else:
                processed = val * scale_factor
            accumulated += processed
        return accumulated

    data = [1, 5, 8, 10, 3]
    result = processor(data)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()