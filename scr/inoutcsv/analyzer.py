"""Module which includes the functions to analyze the statistic properties of a text"""

import json
import obj_writer


# -----------------------------FUNCTIONS-----------------------------------------------------------
def analyzer(file_data):
    """function, which has as a parameter the whole text file as a string and returns the
    statistics of this text file as an JSON Object"""
    word_list = file_data.split()   # splits the text file into words
    print(word_list)   # for testing
    print(len(word_list))
    stroke_count_n = stroke_count(file_data)  # counts the number of key strokes
    word_list = string_cleaner(word_list)     # removes the special characters of the word list
    word_count_n = word_count(word_list)      # calculates the number of words in the list
    word_stat = word_frequency_distribution(word_list)
    statistic_obj = obj_writer.AS(word_count_n, stroke_count_n, word_stat)  # saves the data in an object
    json_obj = json.dumps(statistic_obj.__dict__)   # turns the object to a JSON object
    return json_obj


def word_count(word_list):
    """function, which takes as a parameter a list and returns the number of elements of this
    list"""
    word_count_n = len(word_list)    # number of elements
    print(word_count_n)              # for testing
    return word_count_n


def stroke_count(file_data):
    """function, which counts the key strokes of a given string"""
    stroke_count_n = 0
    for c in file_data:
        if c.islower() or c == '.' or c == ',' or c == ' ':
            stroke_count_n += 1
        else:
            stroke_count_n += 2
    return stroke_count_n


def char_count():
    pass


def char_frequency_distribution():
    pass


def word_frequency_distribution(word_list):
    num_words = len(word_list)   # number of words in the text
    words_stat_relativ = {}      # dictionary for relative frequency
    words_stat = {i: word_list.count(i) for i in word_list}   # dictionary with total frequency
    for key in words_stat:
        average = words_stat[key] * 100 / num_words
        words_stat_relativ.update({key: average})
    print(words_stat_relativ)
    return words_stat_relativ


def mean_word_length():
    pass
    
    
def string_cleaner(word_list):
    """function, which takes as a parameter a list and removes '!', '.', ',', '-' """
    word_list2 = []
    for i in range(len(word_list)):
        if word_list[i].endswith("!"):
            word_list[i] = word_list[i].replace("!", "")
        elif word_list[i].endswith("."):
            word_list[i] = word_list[i].replace(".", "")
        elif word_list[i].endswith(","):
            word_list[i] = word_list[i].replace(",", "")
    for i in range(len(word_list)):   # to remove '-' from the word list
        if word_list[i] != "–":
            word_list2.append(word_list[i])
    print(word_list2)   # for testing
    return word_list2
