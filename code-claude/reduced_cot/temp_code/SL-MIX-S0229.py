from collections import Counter

# Analysis of books read by two book clubs
club_a_books = {'Dune', 'Foundation', 'Neuromancer', 'Snow Crash', '1984'}
club_b_books = {'Foundation', 'Hyperion', '1984', 'Brave New World'}

# Books read in the last month by all members
recent_readings = ['Dune', 'Foundation', 'Hyperion', '1984', 'Snow Crash', 
                  'Foundation', '1984', 'Brave New World', 'Neuromancer']

# Find the frequency of recently read books
reading_frequency = Counter(recent_readings)

# Books read by both clubs
common_books = club_a_books.intersection(club_b_books)

# Books that appear in both clubs and were read at least twice recently
common_items = {book for book in common_books if reading_frequency[book] >= 2}

# Count of unique elements that meet our criteria
unique_elements = len(common_items)

print(f"Result: {unique_elements}")