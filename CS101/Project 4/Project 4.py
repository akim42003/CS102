import random
import string
import unidecode
import nltk

def read_words_from_file(filename):
    # Opens the given file using the UTF-8 encoding
    with open(filename, encoding = "utf-8") as file:
        
        # Reads the file into a string
        text_utf8 = file.read()
        
        # Replaces all special characters (like É and slanted quotes) with
        # standard (ASCII) equivalents, which will make them easier for NLTK
        # to handle.
        text = unidecode.unidecode(text_utf8)
        
    # What does this do?
    words = nltk.word_tokenize(text)
    return words

def put_words_in_dictionary(WORDS):
    file_names = ["JJ.txt", "NN.txt", "DET.txt", "VBZ.txt", "PRP.txt"]
    keys = list(WORDS.keys())
    for data in WORDS:
        WORDS[data] = read_words_from_file(file_names[keys.index(data)])
    return WORDS


def define_structure(S):
    S = read_words_from_file("Structures.txt")
    return S


# WORDS = {"JJ": ["quiet", "grim", "cozy"],
#          "NN": ["coward", "exam", "pub"],
#          "DT": ["the", "a"],
#          "VBZ": ["hugs", "soaks", "loafs"],
#          "PRP": ["in", "on", "up"]
#          }
# Words from level 1
WORDS = {"JJ": [],
         "NN": [],
         "DT": [],
         "VBZ": [],
         "PRP": [],
         }

S = []

alphabet = list(string.ascii_lowercase)

   
def find_pangrams(WORDS, structure, all_pangrams):
    pan_gram = []
    for entry in structure:
#         print(entry)
        word_list = WORDS[entry]
#         print(len(word_list))
        for word in word_list:
            if word not in pan_gram:
                apply_word = word_list[random.randint(0, len(word_list)-1)]
#                 print(word_list)
            else:
                apply_word = word_list[0]
#         if len(word_list) > 1:
#             word_list.remove(apply_word)
        pan_gram.append(apply_word)
        if pan_gram in all_pangrams:
            all_pangrams.pop()
            
    return pan_gram, all_pangrams

def highest_count(pan_gram):
    pangram_letters = []
    if pan_gram != None:
        for word in pan_gram:
            for letter in word:
                pangram_letters.append(letter)
    length = len(pangram_letters)
#     print(pangram_letters)
    final_count = 0
    for letter in alphabet:
        if letter in str(pangram_letters):
            final_count += 1       
    return final_count, length

def highest_count_indexes(last_count, all_counts, all_pangrams):
    best_lengths = []
    for index in range(0, len(all_counts)-1):
        if all_counts[index] == last_count:
            temp_length = "".join(all_pangrams[index])
            best_lengths.append(len(temp_length))
    return best_lengths

def best_index(all_counts, all_lengths, last_count, last_length):
    pangram_index = 0
    for data in range(0, len(all_counts) - 1):
        if all_counts[data] == last_count and all_lengths[data] == last_length:
#             print(all_counts[data])
#             print(all_lengths[data])
            pangram_index = data
    return pangram_index
    
def main():
    all_pangrams = []
    all_counts = []
    all_lengths = []
    put_words_in_dictionary(WORDS)
    structure = define_structure(S)
    pan_gram = find_pangrams(WORDS, structure, all_pangrams)
    last_count = 0
    last_length = 0
    while True:
        structure = define_structure(S)
        put_words_in_dictionary(WORDS)
        pan_gram, all_pangrams = find_pangrams(WORDS, structure, all_pangrams)
        final_count, length = highest_count(pan_gram)
        if pan_gram in all_pangrams:
#             print(all_pangrams)
            break
        if pan_gram not in all_pangrams:
            all_pangrams.append(pan_gram)
            all_counts.append(final_count)
            all_lengths.append(length)
                
    last_count = max(all_counts)
    best_lengths = highest_count_indexes(last_count, all_counts, all_pangrams)
    last_length = min(best_lengths)
    pangram_index = best_index(all_counts, all_lengths, last_count, last_length)
    final_pan_gram = all_pangrams[pangram_index]
    print("Structure: " + " ".join(structure))
    print("Sentence: " + " ".join(final_pan_gram))
    print("Score: " + str(last_count))
    print("Length: " + str(last_length))
    
main()