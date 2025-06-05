# 1. დაწერეთ ტრანზაქციის ფუნქცია, რომელსაც გადაეცემა ატრიბუტად ბალანსი და გადასახდელი თანხა, დაუწერეთ დეკორატორი,
# რომელიც საკომისიოს ჩამოაჭრის 1 ლარს და თუ საკმარისი თანხა არ იქნება ანგარიშზე დაუბრუნეთ შეცდომის ტექსტი


# def transaction(func):
#     def wrapper(balance, amount):
#         fee = 1
#         if balance < amount + fee:
#             return "Insufficient funds"
#         return func(balance - amount - fee)
#     return wrapper
#
# @transaction
# def process_transaction(balance):
#     return f"Transaction successful, new balance: {balance} GEL"
#
# print(process_transaction(10, 5))

# 2. შექმენით მეტაკლასი, რომელიც სხვა კლასზე გამოყენების შემთხვევაში შეამოწმებს ამ კლასის მეთოდის სახელებს,
#    შემდეგი სახით: თუ მეთოდი იწყება _ ეს მეთოდი ვალიდური იქნება, თუ არ იწყება _, მაშინ აღზევდეს
#    ValueError. მაგ: _test() - ეს მეთოდი იქნება ვალიდური, test() - ეს მეთოდი არ იქნება ვალიდური
#    და გამოიწვევს ValueError-ს. გაითვალისწინეთ რომ მეტაკლასმა უნდა შეამოწმოს მხოლოდ მეთოდები და არა ატრიბუტები!


# class MethodNameMeta(type):
#     def __new__(cls, name, bases, attrs):
#         for attr_name, attr_value in attrs.items():
#             if callable(attr_value) and not attr_name.startswith('_'):
#                 raise ValueError(f"Method '{attr_name}' is not valid. It must start with an underscore.")
#         return super().__new__(cls, name, bases, attrs)
#
# class MyClass(metaclass=MethodNameMeta):
#     def _valid_method(self):
#         return "This is a valid method."
#
#     def invalid_method(self):
#         return "This method will raise an error because it does not start with an underscore."