def count_unique_categories(func):
    unique_categories = set()
    
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (set, frozenset)):
            unique_categories.update(result)
        return len(unique_categories)
    return wrapper

@count_unique_categories
def process_recipe_1():
    return frozenset({'protein', 'vegetable', 'spice'})

@count_unique_categories
def process_recipe_2():
    return frozenset({'dairy', 'grain', 'spice'})

@count_unique_categories
def process_recipe_3():
    return frozenset({'protein', 'dairy', 'fruit'})

process_recipe_1()
process_recipe_2()
total_categories = process_recipe_3()
print(f'Result: {total_categories}')