from collections import Counter

def count_items(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return Counter(result)
    return wrapper

@count_items
def daily_sales():
    return ['BRD001', 'CRT002', 'BRD001', 'CRO003', 'CRT002', 'CRO003', 'CRO003']

sales_counter = daily_sales()
sales_counter['CRO003'] *= 2
final_croissant_count = sales_counter['CRO003']
print(f'Result: {final_croissant_count}')