def filter_criteria(book):
    # Books are eligible if published after 2000 and either have rating >= 4.0 or are non-fiction
    return book['year'] > 2000 and (book['rating'] >= 4.0 or book['genre'] == 'non-fiction')

def calculate_library_metrics(books):
    total_pages = sum(book['pages'] for book in books)
    avg_rating = sum(book['rating'] for book in books) / len(books) if books else 0
    oldest = min(book['year'] for book in books) if books else 0
    return total_pages, avg_rating, oldest

# Library catalog with book information
library = [
    {'title': 'Data Science Handbook', 'year': 2018, 'rating': 4.5, 'genre': 'non-fiction', 'pages': 350},
    {'title': 'The Great Novel', 'year': 1998, 'rating': 4.7, 'genre': 'fiction', 'pages': 420},
    {'title': 'Modern Programming', 'year': 2021, 'rating': 3.8, 'genre': 'non-fiction', 'pages': 280},
    {'title': 'Fantasy World', 'year': 2005, 'rating': 4.2, 'genre': 'fiction', 'pages': 500},
    {'title': 'Historical Events', 'year': 2015, 'rating': 3.9, 'genre': 'non-fiction', 'pages': 310},
    {'title': 'Mystery Tales', 'year': 2010, 'rating': 4.0, 'genre': 'fiction', 'pages': 275}
]

# Calculate some metrics for reporting (not directly related to eligibility)
pages_threshold = 300
recent_books = [book for book in library if book['year'] >= 2010]
long_books = len([book for book in library if book['pages'] > pages_threshold])

# Temporary analysis variables
popular_fiction = [book for book in library if book['genre'] == 'fiction' and book['rating'] > 4.0]
oldest_nonfiction = min([book['year'] for book in library if book['genre'] == 'non-fiction'], default=0)

# Apply filtering criteria to find eligible books
eligible_books = len([book for book in library if filter_criteria(book)])

# Calculate metrics for eligible books only
eligible_book_objects = [book for book in library if filter_criteria(book)]
total_eligible_pages, avg_eligible_rating, _ = calculate_library_metrics(eligible_book_objects)

# Final count adjustment (doesn't affect eligible_books)
adjusted_count = eligible_books + (1 if long_books > 3 else 0) - (1 if oldest_nonfiction < 2000 else 0)

print(f"Result: {eligible_books}")