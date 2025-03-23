# 1. დაწერეთ პროგრამა, რომელიც შექმნის დიქტს, რომელშიც key-ები იქნება 1-დან 10-ის ცათვლით რიცხვები, ხოლო value-ები key-ს შესაბამისი
#    კვადრატები, ანუ {1: 1, 2: 4, 3: 9...}, არ დაწეროთ ხელით, გამოიყენეთ ციკლი(ბონუსი: გამოიყენეთ dictionary comprehension )

# num_dict = {i: i ** 2 for i in range(1, 11)}
# print(num_dict)







# 2. მოცემულია პროდუქტების ლისტი:
#    products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]
#
# ა. დაბეჭდეთ ყველა პროდუქტის დასახელება
# ბ. გამოითვალეთ ყველა პროდუქტის ღირებულების ჯამი(ანუ პროდუქტის ფასი უნდა გაამრავლოთ რაოდენობაზე და დააჯამოთ)
#
# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ხილის სახელს, მანამ სანამ, მომხმარებელი არ შეიყვანს სიტყვას stop,
#    ამის შემდეგ გამოიტანეთ დიქტის სახით ხილის დასახელება და ველიუ იქნება რამდენჯერაც შეიყვანა ეს ხილი, მაგალითად:
#
#    Enter your favorite fruit: banana
#    Enter your favorite fruit: apple
#    Enter your favorite fruit: banana
#    Enter your favorite fruit: stop

# შედეგი:

# {'banana': 2, 'apple': 1}


# products = [
#     {"cola": {
#         "price": 1.5,
#         "quantity": 10
#     }},
#     {"fanta": {
#         "price": 2.5,
#         "quantity": 5
#     }},
#     {"snickers": {
#         "price": 3.5,
#         "quantity": 12
#     }},
#     {"water": {
#         "price": 4.5,
#         "quantity": 8
#     }},
#     {"beer": {
#         "price": 6.5,
#         "quantity": 5
#     }}
# ]
#
# print("Product names:")
# for product in products:
#     for name in product.keys():
#         print(name)
#
# total_price = sum([list(product.values())[0]["price"] * list(product.values())[0]["quantity"] for product in products])
# print("Total price of products:", total_price)
#
# fruits = {}
# while True:
#     fruit = input("\nEnter your favorite fruit: ").strip().lower()
#     if fruit == "stop":
#         break
#     fruits[fruit] = fruits.get(fruit, 0) + 1
#
# print("\nFruit Count:", fruits)