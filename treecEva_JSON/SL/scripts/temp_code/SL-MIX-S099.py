def process_recipes():
    appetizer_ingredients = {'bread', 'cheese', 'olives', 'tomato'}
    main_course_ingredients = {'rice', 'chicken', 'broccoli', 'carrot'}
    dessert_ingredients = {'sugar', 'flour', 'butter', 'eggs', 'milk'}
    
    # Some ingredients overlap between recipes
    shared_dessert_appetizer = {'bread'}
    shared_dessert_main = {'eggs'}
    
    # Remove shared items from dessert set
    exclusive_dessert = dessert_ingredients - shared_dessert_appetizer - shared_dessert_main
    
    return len(exclusive_dessert)

# Using a dictionary comprehension to simulate a switch-case pattern
recipe_operations = {
    'appetizer': lambda: None,
    'main_course': lambda: None,
    'dessert': process_recipes
}

selected_recipe = 'dessert'
final_count = recipe_operations.get(selected_recipe, lambda: 0)()
print(f'Result: {final_count}')