# Library inventory processing
book_categories = {'fiction': 12, 'science': 8, 'history': 15, 'art': 5}
base_value = 7

# Calculate total books using lambda and dictionary operations
total_books = sum(map(lambda x: book_categories[x], book_categories))

# Additional inventory check (distractor)
inventory_status = len(book_categories) > 3

# Final calculation
final_total = total_books * base_value

print(f"Result: {final_total}")