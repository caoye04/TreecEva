import re

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_linked_list(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for item in items[1:]:
        current.next = ListNode(item)
        current = current.next
    return head

dairy_ingredients = frozenset(['milk', 'cheese', 'butter', 'cream', 'yogurt'])
recipe_lists = [
    ['flour', 'sugar', 'butter'],
    ['eggs', 'flour', 'milk'],
    ['tomato', 'basil', 'olive oil'],
    ['cheese', 'bread', 'ham'],
    ['chicken', 'rice', 'broth']
]

# Convert each recipe to a linked list
recipe_linked_lists = list(map(build_linked_list, recipe_lists))

# Extract ingredients from linked lists
extracted_recipes = []
for head in recipe_linked_lists:
    ingredients = []
    current = head
    while current:
        ingredients.append(current.data)
        current = current.next
    extracted_recipes.append(ingredients)

# Count dairy-free recipes using set operations
contains_dairy = lambda recipe: bool(frozenset(recipe) & dairy_ingredients)
dairy_free_count = len(list(filter(lambda recipe: not contains_dairy(recipe), extracted_recipes)))

print(f"Result: {dairy_free_count}")