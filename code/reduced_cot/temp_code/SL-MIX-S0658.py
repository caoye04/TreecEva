from itertools import accumulate

def sugar_accumulator():
    initial_sugar = 100
    increments = [25 + i*15 for i in range(7)]
    total_sugar = initial_sugar + sum(increments)
    return total_sugar

final_sugar_amount = sugar_accumulator()
print(f"Result: {final_sugar_amount}")