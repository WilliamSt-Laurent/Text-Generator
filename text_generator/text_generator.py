# Write your code here
from nltk import WhitespaceTokenizer
from collections import Counter
import random
import re

end_program = False
white_spaces_tkn = WhitespaceTokenizer()

# Get user input here
user_input = input()
file = open(user_input, "r", encoding="utf-8")

# Work on the file here
tokens_list = white_spaces_tkn.tokenize(file.read())
tokens_set = set(tokens_list)
dictionary = {}
# random_word = random.choice(tokens_list)


# FROM PREVIOUS STAGE
# print("Corpus statistics")
# print(f"All tokens: {len(tokens_list)}")
# print(f"Unique tokens: {len(tokens_set)}")
# print()

trigram_collection = []
for i in range(len(tokens_list) - 2):
    trigram = [f"{tokens_list[i]} {tokens_list[i + 1]}", tokens_list[i + 2]]
    trigram_collection.append(trigram)

for trigram in trigram_collection:
    dictionary.setdefault(trigram[0], []).append(trigram[1])

tail_count_dict = {key: Counter(value).most_common() for (key, value) in dictionary.items()}

# FROM PREVIOUS STAGE(2)
# print(f"Number of bigrams: {len(bigram_collection)}")


def find_first_word():
    global tokens_list
    template_first = r"^[A-Z]{1}[^\.\!\?]*?$"
    head_to_return = ""
    is_valid_head = False
    while not is_valid_head:
        head = random.choice(trigram_collection)
        if re.match(template_first, head[0]) and re.match(template_first, head[1]) is not None:
            is_valid_head = True
            head_to_return = head[0]
    return head_to_return


first_words = find_first_word().split(" ")
text = [first_words[0], first_words[1]]


def predict_text():
    global tail_count_dict
    global text
    template_last = '\\w+[?.!]'
    sentence_number = 0

    while sentence_number < 10:
        word_population = []
        weights = []
        last_two_words = f"{text[len(text) - 2]} {text[len(text) - 1]}"
        word_counts = tail_count_dict[last_two_words]

        for word in word_counts:
            word_population.append(word[0])
            weights.append(word[1])
        next_word = random.choices(word_population, weights)[0]
        if re.match(template_last, next_word) is not None and len(text) > 5:
            text.append(next_word)
            print(*text, sep=" ")
            text.clear()
            next_sentence_first = find_first_word().split(" ")
            text = [next_sentence_first[0], next_sentence_first[1]]
            sentence_number += 1
        elif re.match(template_last, next_word) is None:
            text.append(next_word)
        else:
            text.clear()
            next_sentence_first = find_first_word().split(" ")
            text = [next_sentence_first[0], next_sentence_first[1]]


# FROM PREVIOUS STAGE
# def print_text():
#     global text
#     sentence = []
#     for index in range(100):
#         if (index + 1) % 10 == 0:
#             sentence.append(text[index])
#             print(*sentence, sep=" ")
#             sentence.clear()
#         else:
#             sentence.append(text[index])

# def display_index():
#     global end_program
#     word_input = input()

#     if word_input == "exit":
#         end_program = True
#     else:
#         print(f"Head: {word_input}")
#         try:
            # FROM PREVIOUS STAGE (1)
            # print(tokens_list[int(index_input)])

            # FROM PREVIOUS STAGE (2)
            # print(f"Head: {bigram_collection[int(index_input)][0]}    \
        #     Tail: {bigram_collection[int(index_input)][1]} ")

        #     tails = tail_count_dict[word_input]

        #     for frequency in tails:
        #         print(f"Tail: {frequency[0]}    Count: {frequency[1]}")
        #     print()
        # except IndexError:
        #     print("Index Error. Please input a value that is not greater than the number of all bigrams.\n")
        # except TypeError:
        #     print("Type Error. Please input an integer.\n")
        # except ValueError:
        #     print("ValueError. Please input an integer\n")
        # except KeyError:
        #     print("Key Error. The requested word is not in the model. Please input another word.\n")

# while not end_program:
#    display_index()


predict_text()
