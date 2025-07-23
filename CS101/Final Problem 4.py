import random
alphabet = ["A", "C", "G", "T"]

def closest(words, target):
    closest = 0
    differences = 0
    lowest_diff = 10
    s = ""
    for data in range(5):
        for letter in words[data]:
            if target[words[data].index(letter)] != letter:
                differences += 1
        if differences < lowest_diff:
            lowest_diff = differences
            s = words[data]
    return s, lowest_diff
    

def main():
    words = []
    entry = ""
    length = int(input("Enter the length of all words"))
    target = str(input("Enter a word of the length:" + str(length)))
    for i in range(5):
        for word in range(length):
            entry += alphabet[random.randint(0, 3)]
        words.append(entry)
        entry = ""
    s, lowest_diff = closest(words, target)
    print("Random words of the length " + str(length) + " are: " , words)
    print("The closest word is " + s +" with " + str(lowest_diff) + " differences.")
    
    
main()