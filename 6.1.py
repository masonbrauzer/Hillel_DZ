import string
letters = input("Введіть дві літери через дефіс: ")
letter_first, letter_end = letters.split('-')
index_first = string.ascii_letters.find(letter_first)
index_end = string.ascii_letters.find(letter_end)
result = string.ascii_letters[index_first:index_end + 1]
print(result)