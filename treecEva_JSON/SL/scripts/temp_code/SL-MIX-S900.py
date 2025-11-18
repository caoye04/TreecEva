from collections import defaultdict
from contextlib import contextmanager

daily_sales = [
    frozenset(['apple', 'cherry', 'blueberry']),
    frozenset(['apple', 'pumpkin', 'pecan']),
    frozenset(['cherry', 'apple', 'key_lime']),
    frozenset(['apple', 'chocolate_cream', 'cherry']),
    frozenset(['apple', 'pecan', 'blueberry'])
]

@contextmanager
def sales_file(day_data):
    try:
        yield day_data
    finally:
        pass

cumulative_count = defaultdict(int)
common_pies = None

for day_index in range(len(daily_sales)):
    with sales_file(daily_sales[day_index]) as sales:
        for pie in sales:
            cumulative_count[pie] += 1
        if common_pies is None:
            common_pies = set(sales)
        else:
            common_pies &= set(sales)

unique_pie_count = len(common_pies)
print(f'Result: {unique_pie_count}')