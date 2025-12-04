items = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
filter_criteria = lambda x: len(x) >= 5 and 'a' in x
filtered_items = list(filter(filter_criteria, items))
final_count = len(filtered_items)
print(f"Result: {final_count}")