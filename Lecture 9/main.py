# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს რიცხვს, თუ რამდენჯერ უნდა ჰკითხოს მომხმარებელს რიცხვი და საბოლოოდ დააჯამებს
#    ყველა შეყვანილ რიცხვს, თუ არგუმენტად არ გადაეცა არანაირი რიცხვი, მაშინ ფუნქციამ 5-ჯერ ჰკითხოს მომხმარებელს რიცხვის
#    შეყვანა და დააჯამოს ეს 5 რიცხვი. დააბრუნეთ საბოლოო ჯამი


# def sum_numbers(times=5):
#     total = 0
#     for _ in range(times):
#         while True:
#             try:
#                 number = int(input("შეიყვანეთ რიცხვი: "))
#                 total += number
#                 break
#             except ValueError:
#                 print("გთხოვთ, შეიყვანოთ მთელი რიცხვი.")
#     return total
#
# print("საბოლოო ჯამი:", sum_numbers())


# 2. დაწერეთ ფუნქცია რომელიც მიიღებს არგუმენტების განუსაზღვრელ რაოდენობას მთელი რიცხვების სახით და დააბრუნებს
#    ორ ლისტს, ერთ ლისტში იქნება გადაცმული არგუმენტებიდან კენტი რიცხვები ხოლო მეორე ლისტში ლუწი რიცხვები

# def separate_even_odd(*args):
#     even_numbers = []
#     odd_numbers = []
#
#     for number in args:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             odd_numbers.append(number)
#
#     return even_numbers, odd_numbers
#
# print("კენტი რიცხვები:", separate_even_odd(1, 2, 3, 4, 5)[1])
# print("ლუწი რიცხვები:", separate_even_odd(1, 2, 3, 4, 5)[0])

# 3. დაწერეთ ფუნქცია, რომელსაც პარამეტრად გადაეცემა მომხმარებლის მიერ შეყვანილი წინადადება და ამ წინადადებაში დაითვლის სიტყვებს
#    და დიქტის სახით დააბრუნებს თუ რომელი სიტყვა რამდენჯერ არის, მაგ: "This is a test. This test is fun." --> დააბრუნებს დიქტის
#    შემდეგი სახით: {'this': 2, 'is': 2, 'a': 1, 'test': 2, 'fun': 1} უნდა იყოს case insensitive (ანუ დიდ და პატარა ასოებს არ უნდა
#    ჰქონდეს მნიშვნელობა!)

# def count_words(sentence):
#     words = sentence.lower().split()
#     word_count = {}
#
#     for word in words:
#         word = word.strip('.,!?;:"\'')  # წაშლის პუნქტუაციის ნიშნებს
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
#     return word_count
#
# print("სიტყვების ოდენობა:", count_words("This is a test. This test is fun."))



# 4. დაწერეთ რეკურსიული ფუნქცია, რომელსაც პარამეტრად გადაეცემა რიცხვი და დააბრუნებს 1-დან ამ რიცხვის ჩათვლით ყველა რიცხვის ჯამს

# def recursive_sum(n):
#     if n <= 1:
#         return n
#     else:
#         return n + recursive_sum(n - 1)
# print("რეკურსიული ჯამი:", recursive_sum(5))