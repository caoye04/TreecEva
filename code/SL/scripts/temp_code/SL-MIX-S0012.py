bakery_inventory = [('muffins', 12), ('apple pies', 5), ('croissants', 20), ('orange cakes', 8), ('donuts', 15), ('egg tarts', 10)]
vowels = {'a', 'e', 'i', 'o', 'u'}
sorted_inventory = sorted(bakery_inventory)
vowel_item_total = sum(quantity for item, quantity in sorted_inventory if item[0].lower() in vowels)
print(f'Result: {vowel_item_total}')