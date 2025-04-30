# 1. მოცემულია სია:
#
# (სახელი, გვარი, ასაკი)
#
# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
# დაწერეთ უსასრულო ციკლი, რომელშიც მომხმარებელს ჰკითხავთ სახელს, თუ სახელი იქნება მოცემულ სიაში, შემდეგ ჰკითხეთ გვარი და გვარიც თუ იქნება,
# დაბეჭდეთ მისი ასაკი, ხოლო თუ არ იქნება სახელი დაბეჭდეთ რომ არ არის მოცემული სახელი, შესაბამისად გვარი აღარ ჰკითხოთ, ანალოგიურად
# მოიქეცით გვარის კითხვის შემთხვევაშიც. ციკლი უნდა გაჩერდეს იმ შემთხვევაში თუ მომხმარებელი შემოიყვანს სიტყვას "stop".

# persons = [
#     ('Kelly', 'Simpson', 26),
#     ('Erika', 'Stephens', 24),
#     ('Cheryl', 'Dunn', 30),
#     ('Amy', 'Larsen', 49),
#     ('Christine', 'Gordon', 23),
#     ('Monica', 'Huff', 38),
#     ('David', 'Nixon', 36),
#     ('Cindy', 'Escobar', 41),
#     ('Cindy', 'White', 33),
#     ('Joel', 'Hall', 43),
#     ('Steven', 'Winters', 28),
#     ('Alex', 'Cole', 68),
#     ('Alex', 'Smith', 32),
#     ('Brittany', 'Thompson', 18),
#     ('Ernest', 'Young', 43),
#     ('Traci', 'Wells', 38),
#     ('Andrew', 'Flores', 61),
#     ('Christopher', 'Lewis', 29),
#     ('Kevin', 'Willis', 57),
#     ('Kayla', 'Lucas', 28),
#     ('Michelle', 'Rush', 43),
#     ('Thomas', 'Mason', 37)
# ]
#
# while True:
#     first_name = input("Enter first name (or type 'stop' to exit): ").strip()
#     if first_name.lower() == 'stop':
#         break
#
#     matches = [person for person in persons if person[0] == first_name]
#
#     if not matches:
#         print("No such first name found.")
#         continue
#
#     last_name = input("Enter last name: ").strip()
#     full_match = [person for person in matches if person[1] == last_name]
#
#     if not full_match:
#         print("No such last name found.")
#         continue
#
#     print(f"Age: {full_match[0][2]}")



# 2. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს ჯერ პირველ და მერე მეორე სიტყვას.
#    იპოვეთ ამ სიტყვებში საერთო სიმბოლოები, განსხვავებული სიმბოლოები, და გაერთიანებული სიმბოლოები(ანუ ორივეში ერთად რომელიცაა ყველა ერთად)
#    დაბეჭდეთ ყველა ზემოთჩამოთვლილი(გამოიყენეთ set)

# first_word = input("Enter first word: ")
# second_word = input("Enter second word: ")
#
# first_set = set(first_word)
# second_set = set(second_word)
#
# print("Common symbols:", first_set.intersection(second_set))
# print("Different symbols:", first_set.symmetric_difference(second_set))
# print("All symbols:", first_set.union(second_set))