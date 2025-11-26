students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
scores = [85, 92, 78, 96, 88]
attendance = [True, True, False, True, True]

# Calculate difference between even and odd indexed scores
even_scores = [score for i, score in enumerate(scores) if i % 2 == 0]
odd_scores = [score for i, score in enumerate(scores) if i % 2 == 1]

final_score = sum(scores[::2]) - sum(scores[1::2])
print(f"Result: {final_score}")