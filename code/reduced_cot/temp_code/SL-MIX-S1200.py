pie_prices = [12.50, 15.75, 10.00, 18.25]
add_tax = lambda price: round(price * 1.07, 2)

def calculate_revenue(sales, index=0):
    if index >= len(sales):
        return 0.0
    return add_tax(sales[index]) + calculate_revenue(sales, index + 1)

pie_sales_count = [2, 1, 3, 1]  # Number of each pie type sold
flattened_sales = []
for i, count in enumerate(pie_sales_count):
    flattened_sales.extend([pie_prices[i]] * count)

total_revenue = calculate_revenue(flattened_sales)
print(f"Result: {total_revenue}")