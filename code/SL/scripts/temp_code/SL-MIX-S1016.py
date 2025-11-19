def count_sold_out(original_set, remaining_frozenset):
    if not original_set:
        return 0
    item = original_set.pop()
    if item in remaining_frozenset:
        return count_sold_out(original_set, remaining_frozenset)
    else:
        return 1 + count_sold_out(original_set, remaining_frozenset)

desserts_monday = {'croissant', 'muffin', 'donut', 'bagel'}
end_of_day_inventory = frozenset(['muffin', 'bagel'])
sold_out_count = count_sold_out(desserts_monday, end_of_day_inventory)
print(f'Result: {sold_out_count}')