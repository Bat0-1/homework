# 1. დაწერეთ ფუნქცია, რომელიც ატრიბუტად მიიღებს რიცხვს, რა რიცხვსაც გადავცემთ, იმდენჯერ შეეკითხება მომხმარებელს
#    სახელს, გვარს და ასაკს. ანუ თუ გადავეცით 3, 3-ჯერ შეეკითხება მომხმარებელს აღნიშნულ ინფორმაციას, ინფუთის
#    საფუძველზე csv ფაილში ჩაწერეთ შესაბამისი ინფორმაცია შემდეგი სახით, მაგალითად:
#
#    ID,first_name,last_name,age
#    1,John,Doe,25
#    2,Alice,White,30
#
#    და ა.შ.
#
#    გამოიყენეთ try, ecxept იმისათვის რომ მომხმარებელმა ასაკის შემოყვანის დროს აუცილებლად ინტეჯერი შემოიყვანოს!
#    ფაილში ჩასაწერად აუცილებლად გამოიყენეთ csv მოდულიდან writer და DictWriter!

# from csv import DictWriter
# import sys
# def write_students_to_csv(num_students: int, filename: str = 'people.csv'):
#     with open(filename, mode='w', newline='') as file:
#         fieldnames = ['ID', 'first_name', 'last_name', 'age']
#         writer = DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#
#         for i in range(1, num_students + 1):
#             first_name = input(f"Enter first name for student {i}: ")
#             last_name = input(f"Enter last name for student {i}: ")
#             while True:
#                 try:
#                     age = int(input(f"Enter age for student {i}: "))
#                     break
#                 except ValueError:
#                     print("Please enter a valid integer for age.")
#
#             writer.writerow({'ID': i, 'first_name': first_name, 'last_name': last_name, 'age': age})
# if __name__ == "__main__":
#     try:
#         num_students = int(input("How many students do you want to enter? "))
#         if num_students <= 0:
#             raise ValueError("Number of students must be a positive integer.")
#     except ValueError as e:
#         print(f"Invalid input: {e}")
#         sys.exit(1)
#
#     write_students_to_csv(num_students)








# 2. მიმაგრებულ students.csv ფაილიდან წაიკითხეთ ინფორმაცია, გაფილტრეთ Grade-ის მიხედვით შემდეგნაირად:
#    ყველა სტუდენტი, რომელსაც 50-ზე ნაკლები ქულა აქვს შეინახეთ ახალ ფაილში(failed_students.csv)
#    ყველა სტუდენტი, რომელსაც 50-ზე მეტი ქულა აქვს შეინახეთ ახალ ფაილში(passed_students.csv)
#
#    ფაილებიდან ინფორმაციის წასაკითხად და ჩასაწერად აუცილებლად გამოიყენეთ DictReader და DictWriter!

# from csv import DictReader, DictWriter
# def filter_students_by_grade(input_file: str = 'students.csv'):
#     failed_students = []
#     passed_students = []
#
#     with open(input_file, mode='r', newline='') as file:
#         reader = DictReader(file)
#         for row in reader:
#             if 'Grade' in row:
#                 grade = float(row['Grade'])
#                 if grade < 50:
#                     failed_students.append(row)
#                 else:
#                     passed_students.append(row)
#
#     fieldnames = ['ID', 'First Name', 'Last Name', 'Grade']
#
#     with open('failed_students.csv', mode='w', newline='') as file:
#         writer = DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(failed_students)
#
#     with open('passed_students.csv', mode='w', newline='') as file:
#         writer = DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(passed_students)
#
#
# if __name__ == "__main__":
#     filter_students_by_grade('students.csv')
#     print("Students have been filtered and saved to 'failed_students.csv' and 'passed_students.csv'.")
