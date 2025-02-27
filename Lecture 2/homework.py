# 1. დაწერეთ პროგრამა რომელიც მომხმარებელს ჰკითხავს წონას(კგ) და სიმაღლეს(მ), შეყვანილი მონაცემების
# საფუძველზე გამოითვლის BMI-ს(Body Mass Index). ფორმულა: წონა გაყოფილი სიმაღლის კვადრატზე
# თუ BMI ნაკლებია 19-ზე, გამოიტანეთ ინფო რომ ის არის underweight
# თუ BMI არის 19 და 25 შორის, გამოიტანეთ ინფო რომ ის არის normalweight
# თუ BMI მეტია 25-ზე, გამოიტანეთ ინფო რომ ის არის overweight


# weight_kg = float(input('input your weight (kg): '))
# height_m = float(input('input your height(m) : '))
# BMI = weight_kg / (height_m ** 2)
#
# if BMI < 19:
#     print('you are underweight')
# elif 19 <= BMI <= 25:
#     print('you are normalweight')
# elif BMI > 25:
#     print('you are overweight')
#
# print(f'your BMI is: {BMI}')



# 2. დაწერეთ კალკულატორის პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ რიცხვს და არითმეტიკულ ოპერატორს,
# შესაბამისი ოპერატორის საფუძველზე გამოითვლის ამ ორი რიცხვის შედეგს.(გამოიყენეთ Match-Case მეთოდი)


# number1 = float(input('input first number: '))
# number2 = float(input('input second number: '))
# arithmetic_operator = input('input arithemtic operator: ')
#
# match arithmetic_operator:
#     case "+":
#         print(number1 + number2)
#     case "-":
#         print(number1 - number2)
#     case "*":
#         print(number1 * number2)
#     case "/":
#         print(number1 / number2)
#     case "**":
#         print(number1 ** number2)
#     case "%":
#         print(number1 % number2)



# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება 3 რიცხვს, ჯერ შეამოწმეთ ეს რიცხვები არ უდრიდეს ერთმანეთს,
# თუ რომელიმე ორი ერთმანეთს უდრის, დაპრინტეთ რომ შეიყვანოს განსხვავებული რიცხვები. თუ რიცხვები განსხვავებულია,
# იპოვეთ ყველაზე დიდი რიცხვი

# number1 = input('input first number: ')
# number2 = input('input second number: ')
# number3 = input('input third number: ')
#
# if number1 == number2:
#     print('please input a different number')
# elif number1 == number3:
#     print('please input a different number')
# elif number2 == number3:
#     print('please input a different number')
# elif number2 < number1 > number3:
#     print(f'{number1} is the biggest number')
# elif number1 < number2 > number3:
#     print(f'{number2} is the biggest number')
# elif number2 < number3 > number1:
#     print(f'{number3} is the biggest number')