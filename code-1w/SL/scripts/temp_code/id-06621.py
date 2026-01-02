from math import comb

def calculate_combinatorial_product(arr, r):
    # Select first r elements for combination count
    n = len(arr)
    if r > n:
        return 0
    combinations_count = comb(n, r)
    selected_elements = arr[:r]  # Use slicing to get first r elements
    product_of_selection = 1
    for val in selected_elements:
        product_of_selection *= val
    return combinations_count * product_of_selection

# Problem setup
elements = [4, 7, 2, 9]
k = 3

# Irrelevant distraction: unused variable (minimal interference)
dummy_flag = True

subset_product = calculate_combinatorial_product(elements, k)

print(f"Result: {subset_product}")