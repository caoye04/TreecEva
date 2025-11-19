from statistics import mean

daily_sales = {
    'croissant': [10, 20, 15],
    'muffin': [25, 30, 20],
    'danish': [5, 10, 8],
    'scone': [18, 22, 17]
}

def compute_popular_items(sales_data, threshold):
    averages = {pastry: mean(counts) for pastry, counts in sales_data.items()}
    popular_items = frozenset(pastry for pastry, avg in averages.items() if avg > threshold)
    return popular_items

popular_pastry_set = compute_popular_items(daily_sales, 15)
result_size = len(popular_pastry_set)
print(f"Result: {result_size}")