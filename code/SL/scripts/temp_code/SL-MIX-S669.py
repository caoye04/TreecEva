from math import floor

def get_optimal_position(scores):
    n = len(scores)
    if n == 0:
        return 0
    target_score = 75
    low, high = 0, n - 1
    while low <= high:
        mid = floor((low + high) / 2)
        match (scores[mid] - target_score):
            case x if x < 0:
                low = mid + 1
            case x if x > 0:
                high = mid - 1
            case _:
                return mid
    return low

spice_popularity_scores = [20, 40, 60, 80, 100]
optimal_position = get_optimal_position(spice_popularity_scores)
print(f'Result: {optimal_position}')