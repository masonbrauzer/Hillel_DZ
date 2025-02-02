import string
text = input('Введіть текст: ')
t_text = text.title()
trash = string.punctuation + string.whitespace
text_for_result = ''
for i in t_text:
    if i not in trash:
        text_for_result += i
print('#' + (text_for_result[:139]))

