def int_func():
    my_text = input("Введите слово из маленьких латинских букв: ")
    my_words = my_text.split(" ")
    my_cap_text = []
    my_word = str
    for i in range(len(my_words)):
        my_word = my_words[i].capitalize()
        my_cap_text.append(my_word)
    return my_cap_text


print(int_func())
