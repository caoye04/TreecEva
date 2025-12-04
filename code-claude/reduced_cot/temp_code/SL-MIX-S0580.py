import itertools

# Inventory management for a clothing store
def analyze_inventory():
    # Available colors and sizes
    all_colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
    all_sizes = ['S', 'M', 'L', 'XL', 'XXL']
    
    # Filter out colors and sizes not currently in stock
    unavailable_colors = ['yellow', 'white']
    unavailable_sizes = ['XXL']
    
    filtered_colors = [color for color in all_colors if color not in unavailable_colors]
    filtered_sizes = [size for size in all_sizes if size not in unavailable_sizes]
    
    # Calculate total possible product combinations available
    product_count = len(list(itertools.product(filtered_colors, filtered_sizes)))
    
    # For comparison - count before filtering (not used in final calculation)
    original_count = len(all_colors) * len(all_sizes)
    
    # Calculate average products per color
    avg_per_color = product_count / len(filtered_colors)
    
    print(f"Result: {product_count}")
    return product_count

result = analyze_inventory()