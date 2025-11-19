from statistics import mean

def calculate_conditional_average(sales):
    bread, cakes, cookies = sales
    # Short-circuit evaluation: only compute mean if both cakes and cookies > 10
    final_average = mean(sales) if cakes > 10 and cookies > 10 else 0
    return final_average

# Sales data: [bread, cakes, cookies]
sales_data = [20, 15, 8]
final_average = calculate_conditional_average(sales_data)
print(f'Result: {final_average}')