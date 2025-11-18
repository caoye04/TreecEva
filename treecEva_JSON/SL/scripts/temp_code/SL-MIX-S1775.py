sales = [15, 25, 10, 30, 12]
adjusted_sales = sales[:]

for i in range(len(sales) - 1):
    if sales[i] > 20:
        adjusted_sales[i + 1] = min(50, sales[i + 1] * 2)

adjusted_total = sum(adjusted_sales)
print(f"Result: {adjusted_total}")