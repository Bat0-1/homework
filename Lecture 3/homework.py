# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება რიცხვს და გამოითვლის არ რიცხვის ფაქტორიალს, შეგახსენებთ რომ ფაქტორიალი
# არის ამ რიცხვის ნამრავლი ყველა მთელ რიცხვზე 1-მდე, ანუ 5-ის ფაქტორიალი არის 5 X 4 X 3 X 2 X 1 (დაწერეთ for ლუპის გამოყენებით)

# from math import factorial
#
# number = int(input('Input number: '))
#
# if number < 0:
#     print("Negatives don't have factorials")
# elif number == 0:
#     print("0's factorial is 1")
# else:
#     print(factorial(number))





# 2. დაწერეთ გამრავლების ტაბულა, მაგალითად ასეთი სახით:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# .........
# 9 * 7 = 63
# 9 * 8 = 72
# 9 * 9 = 81

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i * j}")


# 3. ჩავთვალოთ რომ გვაქვს აპარატი, რომელშიც უნდა გადავიხადოთ რაღაც სერვისის გადასახადი, რომლის ღირებულებაც არის 50 ლარი,
# ხოლო აპარატი იღებს მხოლოდ 5, 10 და 20 ლარიან კუპიურებს და გვიბრუნებს ასევე ხურდას.

# payment = 50
# paid_amount = 0
#
# bills = (5, 10, 20)
#
# while paid_amount < payment:
#     pay = int(input('insert payment: '))
#     if pay in bills:
#         paid_amount += pay
#         print(f'Total: ₾{paid_amount}')
#     else:
#         print('Invalid bill')
#
# change = paid_amount - payment
# if change > 0:
#     print(f'payment done. your change is ₾{change}.')
# else:
#     print('payment done. no change.')



# 4. დაწერეთ პროგრამა, რომელიც ბეჭდავს გადასახადი თანხის ოდენობას, შემდეგ მომხმარებელს სთხოვს მოათავსოს კუპიურა, თუ კუპიურა არ არის ვალიდური,
# დაბეჭდოს რომ შეიტანოს ვალიდური კუპიურა. თუ კუპიურა ვალიდურია, დაბეჭდოს რაც დარჩა გადასახდელი თანხა და კვლავ სთხოვოს მომხმარებელს კუპიურის
# მოთავსება, მანამ სანამ, გადასახდელი თანხა არ განულდება. ბოლოს კი დაუწეროს რამდენი ეკუთვნის ხურდა. ანუ ბოლო იტერაციაზე თუ დარჩენილია
# მაგალითად გადასახდელი თანხა 10 ლარი და მომხმარებელი შეიტანს 20 ლარიანს, დაუწეროს რომ ეკუთვნის 10 ლარი ხურდა.

# import random
#
# valid_bill = (5, 10, 20, 50, 100)
# payment = random.randint(1, 100)
# paid_amount = 0
# print(payment)
#
#
# while paid_amount < payment:
#     pay = int(input('insert payment: '))
#     if pay in valid_bill:
#         paid_amount += pay
#         print(f'Total: ₾{paid_amount}')
#     else:
#         print('Invalid bill')
#
# change = paid_amount - payment
# if change > 0:
#     print(f'payment done. your change is ₾{change}.')
# else:
#     print('payment done. no change.')