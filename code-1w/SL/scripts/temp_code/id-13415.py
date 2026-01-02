def is_even_and_positive(x):
    return x > 0 and x % 2 == 0

numbers = [-5, -2, 0, 3, 4, 7, 8, 11, 12]

doubled = [n * 2 for n in numbers]  # Irrelevant transformation

even_checker = lambda x: x % 2 == 0

filtered_sum = sum(filter(is_even_and_positive, numbers))

Result: filtered_sum