from collections import defaultdict

def sales_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@sales_counter
def bake_batch():
    return 24

@sales_counter
def sell_batch():
    return 24

# Bakery operations
total_batches_made = 5
batches_sold = 3
giveaway_cookies = 17

cookies_baked = total_batches_made * bake_batch()
cookies_sold = batches_sold * sell_batch()
remaining_cookies = cookies_baked - cookies_sold - giveaway_cookies

print(f"Result: {remaining_cookies}")