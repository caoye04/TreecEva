import itertools

def process_numbers(values):
    # Filter even numbers and apply transformation
    filtered_data = list(filter(lambda x: x % 2 == 0, values))
    
    # Generate pairs and calculate products
    pairs = itertools.combinations(filtered_data, 2)
    products = list(map(lambda pair: pair[0] * pair[1], pairs))
    
    # Return the maximum product found
    if products:
        return max(products)
    return 0

data_points = [3, 8, 5, 12, 7, 4]
final_result = process_numbers(data_points)
print(f"Result: {final_result}")