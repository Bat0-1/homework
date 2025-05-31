# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს უსასრულოდ შეეკითხება ჯერ სახელს,
# შემდეგ გვარს და რაიმე ფაილში ჩაწერს სახელს და გვარს ერთ ხაზზე თავისი ნუმერაციით,
# ყველა ასეთი სახეული უნდა იყოს ახალ ხაზზე ჩაწერილი, მაგალითად:
#
#    Enter your first name: Otar
#    Enter your last name: Tumanishvili
#    Enter your first name: Nika
#    Enter your last name: Papaskiri
#    Enter your first name: stop

# ფაილში უნდა ჩაიწეროს შემდეგი სახით:
# 1. Otar Tumanishvili
# 2. Nika Papaskiri
#
# პროგრამა ჩერდება იმ შემთხვევაში, თუ მომხმარებელმა სახელის ადგილა შეიყვანა სიტყვა "stop"

# def main():
#     filename = "names.txt"
#     with open(filename, "w") as file:
#         count = 1
#         while True:
#             first_name = input("Enter your first name: ")
#             if first_name.lower() == "stop":
#                 break
#             last_name = input("Enter your last name: ")
#             file.write(f"{count}. {first_name} {last_name}\n")
#             count += 1
# if __name__ == "__main__":
#     main()







# 2. თანდართულ ფაილში "persons.txt" მოცემულია ადამიანების სია შემდეგი ფორმატით:სახელი და გვარი, ასაკი, ქალაქი
#
#   Evelyn Cook, 75, Nixonland
#   Dr. Briana Davidson, 22, South Hunterside
#    ...
#    ...
#
# თქვენი დავალებაა არსებული ფაილიდან წაიკითხოთ ინფორმაცია, შექმნათ ორი ახალი ტექსტური ფაილი (.txt გაფართოებით), ერთ ფაილში
# ჩაწერეთ ყველა პიროვნება რომლის ასაკი ნაკლებია 50-ზე, ხოლო მეორე ფაილში ჩაწერეთ ყველა პიროვნება, რომლის ასაკი მეტია 50-ზე,
# ფორმატი დაცული უნდა იყოს ისეთი სახით, როგორიც არის ორიგინალ "persons.txt" ფაილში ანუ თითო პიროვნება თითო ხაზზე!

# def main():
#     input_filename = "persons.txt"
#     young_filename = "young_persons.txt"
#     old_filename = "old_persons.txt"
#
#     with open(input_filename, "r") as infile, \
#          open(young_filename, "w") as young_file, \
#          open(old_filename, "w") as old_file:
#
#         for line in infile:
#             name, age, city = line.strip().rsplit(',', 2)
#             age = int(age.strip())
#             if age < 50:
#                 young_file.write(f"{name.strip()}, {age}, {city.strip()}\n")
#             else:
#                 old_file.write(f"{name.strip()}, {age}, {city.strip()}\n")
# if __name__ == "__main__":
#     main()