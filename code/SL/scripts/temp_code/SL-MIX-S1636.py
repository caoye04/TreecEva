from dataclasses import dataclass
from typing import List

data_file_content = '''\nname,popularity,cost\nThe Art of Coding,30,20\nPython Tricks,25,15\nData Science Handbook,40,30\nMachine Learning Basics,35,25\nWeb Development Guide,20,10\n'''

def calculate_popularity_score(budget: int, books: List[tuple]) -> int:
    # Calculate popularity-to-cost ratios and sort in descending order
    books_with_ratios = [(pop/cost, pop, cost) for _, pop, cost in books]
    books_with_ratios.sort(reverse=True)
    
    total_popularity = 0
    remaining_budget = budget
    
    # Greedy selection
    for ratio, pop, cost in books_with_ratios:
        if remaining_budget >= cost:
            total_popularity += pop
            remaining_budget -= cost
    
    return total_popularity

selected_books = []
lines = data_file_content.strip().split('\n')[1:]  # Skip header
for line in lines:
    parts = line.split(',')
    name, popularity, cost = parts[0], int(parts[1]), int(parts[2])
    selected_books.append((name, popularity, cost))

budget_limit = 100
final_score = calculate_popularity_score(budget_limit, selected_books)
print(f"Result: {final_score}")