# TODO здесь писать код

def cipher_word(text_list, shift, new_text):
    for text in text_list:
        encryption = ""
        for word in text.upper():
            if word.isupper():
                word_index = ord(word) - ord("A")
                new_index = (word_index + shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                encryption = encryption + new_character
        new_text.write(encryption.capitalize())
        new_text.write('\n')
        shift += 1
        print(encryption.capitalize())


old_file = open('text.txt', 'r')
new_text = open('cipher_text.txt', 'w')
text_list = [i_text for i_text in old_file]


shift = 1
cipher_word(text_list, shift, new_text)
old_file.close()
new_text.close()
