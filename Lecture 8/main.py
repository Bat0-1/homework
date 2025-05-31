# 1. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს მომხმარებლის მიერ შეყვანილ ტექსტს და ამ ტექსტში დათვლის რამდენი სიმბოლო იყო მაღალ რეგისტრში
#    შეყვანილი და ასევე ამ ტექსტს გადააქცევს uppercase-ად ანუ მაღალ რეგისტრში დააბრუნებს, მაგალითად, მომხმარებელმა თუ შეიყვანა ტექსტი
#    Hello woRld, ფუნქციამ უნდა დააბრუნოს რომ 2 დიდი ამ ტექსტში და ეს ტექსტი აქციოს HELLO WORLD-ად.

def count_uppercase_and_convert(text):
    uppercase_count = sum(1 for char in text if char.isupper())
    converted_text = text.upper()
    return uppercase_count, converted_text

print(count_uppercase_and_convert("Hello woRld"))


# 2. დაწერეთ ფუნქცია, რომელიც პარამეტრად მიიღებს ე.წ. camel case ცვლადებს და დააბრუნებს snake case სახით, ანუ თუ გადავცემთ ცვლადს
#    firstName დააბრუნებს first_name, name დააბრუნებს ისევ name, preferredFirstName დააბრუნებს preferred_first_name, lastName დააბრუნებს
#    last_name და ასე შემდეგ.

def camel_to_snake(camel_case):
    snake_case = ''
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

print(camel_to_snake("preferredFirstname"))