from collections import deque

# Initialize return queue with book IDs and their condition ratings
book_returns = deque([(101, 8), (102, 5), (103, 9), (104, 6), (105, 7)])
special_processing_stack = []

# Lambda to calculate priority: double the rating minus 5
priority_calc = lambda rating: rating * 2 - 5
threshold = 10

while book_returns:
    book_id, rating = book_returns.popleft()
    priority = priority_calc(rating)
    if priority > threshold:
        special_processing_stack.append(book_id)

final_count = len(special_processing_stack)
print(f"Result: {final_count}")