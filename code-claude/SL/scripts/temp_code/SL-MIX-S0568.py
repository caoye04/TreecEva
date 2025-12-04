from collections import Counter

# Book collections of three friends
alice_books = ['Dune', 'Foundation', 'Neuromancer', '1984', 'Hyperion']
bob_books = ['Snow Crash', 'Neuromancer', 'Foundation', 'Ender\'s Game']
charlie_books = ['Dune', 'The Martian', 'Foundation']
david_books = ['Neuromancer', 'Snow Crash', 'Ready Player One']

# Calculate reading statistics
total_books = len(set(alice_books + bob_books + charlie_books + david_books))
book_counts = Counter(alice_books + bob_books + charlie_books + david_books)
most_common = book_counts.most_common(1)[0][0]

# Find books that Alice and Bob both have, but Charlie doesn't
common_books = set(alice_books).intersection(bob_books) - set(charlie_books)

# Count books owned by at least two people
shared_books_count = sum(1 for book, count in book_counts.items() if count >= 2)

print(f"Result: {len(common_books)}")