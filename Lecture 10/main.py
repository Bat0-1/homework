# 1. გამოიყენეთ lambda ფუნქცია sorted() ფუნქციაში, იმისათვის რომ დაასორტიროს მოცემული ლისტი:
#    [(1, 3), (4, 2), (2, 5)] - მასში არსებული ელემენტების მეორე ელემენტის მიხედვით

# data = [(1, 3), (4, 2), (2, 5)]
# sorted_data = sorted(data, key=lambda x: x[1])
# print(sorted_data)




# 2. დაწერეთ ფუნქცია, რომელიც მომხმარებელს შეაყვანინებს ორ რიცხვს და პირველ რიცხვს გაყოფს მეორე რიცხვზე და დააბრუნებს შედეგს,
# დაიჭირეთ ორი ერორი: ის რომ მომხმარებელმა ინტეჯერები შეიყვანოს და ნულზე რომ არ შეიძლება გაყოფა, თითოეული ერორისთვის გამოუტანეთ
# შესაბამისი შეტყობინება. (ორივე ერორი უნდა იყოს შესაბამისი ერორებით დაჭერილი, არ გამოიყენოთ ზოგადი იქსეფშენი)

# def divide_numbers():
#     try:
#         num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
#         num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
#         result = num1 / num2
#         print(f"შედეგი: {result}")
#     except ValueError:
#         print("გთხოვთ, შეიყვანეთ მთელი რიცხვი.")
#     except ZeroDivisionError:
#         print("ნულზე გაყოფა შეუძლებელია.")
#
# divide_numbers()




# 3. მოცემულია პროდუქტების ლისტი:
#
#    products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]
#
# filter() ფუნქციის გამოყენებით გაფილტრეთ და გამოიტანეთ პროდუქტები, რომლის ფასი ნაკლებია 100-ზე;
# map() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის სახელი და ფასი
# sorted() ფუნქციის გამოყენებით დაასორტირეთ პროდუქტების სია ფასის მიხედვით
# reduce() ფუნქციის გამოყენებით გამოიტანეთ ყველა პროდუქტის ფასების ჯამი

# from functools import reduce
# from operator import itemgetter
# products = [
#     {"name": "Laptop", "price": 1200},
#     {"name": "Mouse", "price": 15},
#     {"name": "Keyboard", "price": 25},
#     {"name": "Monitor", "price": 150},
#     {"name": "Power", "price": 100},
#     {"name": "Pad", "price": 10},
# ]
#
# # filter ფუნქცია
# filtered_products = list(filter(lambda p: p['price'] < 100, products))
# print("Filtered products (price < 100):")
# for product in filtered_products:
#     print(product)
#
# # map ფუნქცია
# mapped_products = list(map(lambda p: f"{p['name']}: ${p['price']}", products))
# print("\nMapped products (name and price):")
# for product in mapped_products:
#     print(product)
#
# # sorted ფუნქცია
# sorted_products = sorted(products, key=itemgetter('price'))
# print("\nSorted products by price:")
# for product in sorted_products:
#     print(f"{product['name']}: ${product['price']}")
#
#
# # Reduce ფუნქცია
# total_price = reduce(lambda acc, p: acc + p['price'], products, 0)
# print(f"\nTotal price of all products: ${total_price}")
