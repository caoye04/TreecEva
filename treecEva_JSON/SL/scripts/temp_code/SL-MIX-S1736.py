from collections import defaultdict

book_inventory = defaultdict(lambda: True)
book_inventory['The Great Gatsby'] = False
book_inventory['To Kill a Mockingbird'] = True
book_inventory['1984'] = True
book_inventory['Pride and Prejudice'] = False

available_count = 0
for title, is_available in book_inventory.items():
    if is_available and not title.startswith('The'):
        available_count += 1

print(f'Result: {available_count}')