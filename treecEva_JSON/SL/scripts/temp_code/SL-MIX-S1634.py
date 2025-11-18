from collections import defaultdict

def compute_book_score(title):
    return hash(title) % 100

def calculate_shelf_scores(books):
    dp = [0] * (len(books) + 1)
    for i in range(1, len(books) + 1):
        book_score = compute_book_score(books[i-1])
        dp[i] = max(dp[i-1], dp[i-1] + book_score)
    return dp[len(books)]

book_titles = ['TheGreatGatsby', 'ToKillAMockingbird', '1984', 'PrideAndPrejudice', 'TheCatcherInTheRye']
final_score = calculate_shelf_scores(book_titles)
print(f'Result: {final_score}')