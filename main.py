def get_words(text):
    words = text.split()
    return (len(words))

def count_letters(text):
    characters = {}
    for letter in text:
        if letter.lower() in characters:
            characters[letter.lower()] += 1
        else:
            characters[letter.lower()] = 1
    return (characters)



with open('./books/frankenstein.txt') as f:
    text = f.read()
    words = get_words(text)
    characters_dict = count_letters(text)
    characters=list(characters_dict.items())
    characters = sorted(characters, key=lambda character: character[1],reverse=True)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print()

    for i in range(0,len(characters)):
        if characters[i][0].isalpha():
            print(f"The '{characters[i][0]}' character was found {characters[i][1]} times")
    
    print("--- End report ---")
        



