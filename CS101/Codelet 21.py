from random import choice

def create_word():
    alphabet = ["A", "C", "G", "T", "Z"]
    word = choice(alphabet[:-1])
    letter = choice(alphabet)
    while (letter != "Z"):
        word = word + letter
        letter = choice(alphabet)
    return word

def main():
    num_words = int(input("Enter a number of words: "))
    
    ###
#     words = []
#     for index in range(num_words):
#         words.append(create_word())
    ###
    
    # your answer goes here
    words = [create_word() for index in range(num_words)]
    
    print(f"words: {words}")

main()