from itertools import combinations

def calculate_product(nums):
    result = 1
    for num in nums:
        result *= num
    return result

def main():
    data_sequence = [2, 3, 5, 7, 11]
    
    # Extract all 3-element contiguous slices
    slices = [data_sequence[i:i+3] for i in range(len(data_sequence) - 2)]
    
    # Select the second slice: [3, 5, 7]
    subset = slices[1]
    
    # Compute product of selected subset
    subset_product = calculate_product(subset)
    
    # Irrelevant distraction: count pairs with sum > 10 (not used in answer)
    valid_pairs = 0
    for pair in combinations(data_sequence, 2):
        if sum(pair) > 10:
            valid_pairs += 1
    
    print(f"Result: {subset_product}")

if __name__ == "__main__":
    main()