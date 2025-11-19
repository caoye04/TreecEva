cookie_increment = lambda prev: 2 * prev + 5

def total_cookies(day):
    if day == 1:
        return 10
    else:
        return cookie_increment(total_cookies(day - 1))

final_count = total_cookies(4)
print(f"Result: {final_count}")