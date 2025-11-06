class Address:
    def __init__(self, city, street, zipcode):
        self.city = city
        self.street = street
        self.zipcode = zipcode

class Company:
    def __init__(self, name, address, employee_count):
        self.name = name
        self.address = address
        self.employee_count = employee_count

class Person:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company
        self.hobby = "reading"  # 这个不会被用到

# 创建深层嵌套的对象
addr = Address("Beijing", "Chaoyang Road", "100000")
company = Company("TechCorp", addr, 500)
person = Person("Bob", 30, company)

# 只访问深层的city属性
city_name = person.company.address.city
print(f"City: {city_name}")

# 计算
result = len(city_name) + person.age