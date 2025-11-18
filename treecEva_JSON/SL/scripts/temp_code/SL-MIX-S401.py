from typing import NamedTuple

class Book(NamedTuple):
    title: str
    price: float

discount_calculator = lambda original_price, percent_off: original_price * (1 - percent_off / 100)

book_record = Book(title="The Python Guide", price=45.0)
discount_percent = 20
final_price = discount_calculator(book_record.price, discount_percent)

print(f"Result: {final_price}")