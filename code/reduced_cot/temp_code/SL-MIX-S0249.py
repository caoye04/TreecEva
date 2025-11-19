catalog = {'Python Basics': 3, 'Advanced Java': 0, 'C++ Guide': 2}
check_order = ['Python Basics', 'Web Development', 'Advanced Java', 'C++ Guide']

available_count = 0
for title in check_order:
    if title in catalog and catalog[title] > 0:
        available_count += 1

print(f"Result: {available_count}")