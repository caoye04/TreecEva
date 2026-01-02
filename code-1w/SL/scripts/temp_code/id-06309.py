def main():
    raw_signals = [0.85, 1.23, -0.45, 0.99, 2.01, -1.33, 0.76]
    threshold = 0.75
    
    # Normalize signals using lambda and list comprehension
    normalized = list(map(lambda x: round(x * 0.9, 2), raw_signals))
    
    # Apply initial filter based on threshold
    filtered = [val for val in normalized if abs(val) > threshold]
    
    # Simulate signal inversion for negative values
    inverted = []
    for val in filtered:
        if val < 0:
            inverted.append(abs(val) + 0.1)
        else:
            inverted.append(val)
    
    # Further processing: remove duplicates using set operations
    unique_signals = list(set(inverted))
    sorted_signals = sorted(unique_signals, reverse=True)
    
    # Final aggregation function
    def final_filter(data):
        return int(sum(map(lambda x: x * 10, data)) // len(data))
    
    # Key computation point
    filtration_score = final_filter(sorted_signals)
    
    print(f"Result: {filtration_score}")

if __name__ == "__main__":
    main()