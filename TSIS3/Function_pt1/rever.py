def reverse_sentence(sentence):
    words = sentence.split()
    #sequence[start:stop:step]
    #         конец:начало
    #sequence[5:1:-1]
    reversed_words = words[::-1]
    # Объединяем слова в предложение
    #"разделитель".join(последовательность)
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(sentence)
print( reversed_sentence)