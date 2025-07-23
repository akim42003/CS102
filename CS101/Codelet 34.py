def op(word: str) -> str:
    result = ""

    for letter in word:
        if letter in ['A', 'E', 'I', 'O', 'U', "a", "e", "i", "o", "u"] and word.index(letter)!=(len(word)-1):
            result += letter + "-"
        elif letter in ['A', 'E', 'I', 'O', 'U', "a", "e", "i", "o", "u"] and word.index(letter)==(len(word)-1):
            result += letter
        else:
            result += letter + "op-"

    return result

word = input("Enter a word: ")

print(op(word))
