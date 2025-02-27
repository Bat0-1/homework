# 1. დაწერეთ პროგრამა, რომელიც მომხმარებელს შემოაყვანინებს წინადადებას, პირველ სიტყვას და მეორე სიტყვას და შემოყვანილ წინადადებაში
# პირველ სიტყვას ჩაანაცვლებს მეორე სიტყვით



# text = input("Enter text: ")
# text = text.split()
# if len(text) >= 2:
#     text[0], text[1] = text[1], text[0]
# print(' '.join(text))



# 2. დაწერეთ პროგრამა, რომელიც მომხმარებლის მიერ შემოყვანილ წინადადებაში იპოვის ყველაზე გრძელ სიტყვას და დაბეჭდავს მას

# def find_longest_word(sentence):
#     words = sentence.split()
#     longest_word = max(words, key=len)
#     return longest_word
#
# sentence = input('Enter a sentence: ')
# longest_word = find_longest_word(sentence)
#
# print('The longest word is:', longest_word)




# 3. დაწერეთ პროგრამა, რომელიც მომხმარებელს შეეკითხება ორ სიტყვას შეამოწმებს არის თუ არა ერთმანეთის ანაგრამა
# ანაგრამა არის ერთ სიტყვაში ასოების გადაადგილებით მიღებული მეორე სიტყვა, მაგალითად ("listen", "silent" ), ("Triangle", "Integral")
# და ა.შ. უნდა იყოს case-insensitive, ანუ მომხმარებელი დიდი ასოებით შემოიყვანს თუ არა ტექსტს, არ უნდა ჰქონდეს მნიშვნელობა.
# არ გამოიყენოთ sorted() ფუნქცია.

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")
# def is_anagram(word1, word2):
#     word1 = word1.lower()
#     word2 = word2.lower()
#     return sorted(word1) == sorted(word2)
#
# if is_anagram(word1, word2):
#     print("These words are anagrams")
# else:
#     print("These words are not anagrams")