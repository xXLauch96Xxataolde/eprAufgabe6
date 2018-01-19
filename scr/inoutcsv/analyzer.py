"""Module which includes the functions to analyze the statistic properties of a text"""

import json
import obj_writer

__author__ = "5241945: Elisabeth Zeyen, 6785468: Robert Anselm Dieter am Wege"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "lisa.zeyen@outlook.com, uni.goethe.horde@gmail.com"


# -----------------------------FUNCTIONS-----------------------------------------------------------
def analyzer(file_data, filepath):
    """function, which has as a parameter the whole text file as a string and returns the

    statistics of this text file as an JSON Object
    """
    word_list = file_data.split()   # splits the text file into words
    # print(word_list)   # for testing
    # print(len(word_list))
    stroke_count_n = stroke_count(file_data)  # counts the number of key strokes
    word_list = string_cleaner(word_list)     # removes the special characters of the word list
    word_count_n = word_count(word_list)      # calculates the number of words in the list
    word_stat = word_frequency_distribution(word_list)  # relative frequency of words
    char_stat = char_frequency_distribution(file_data)  # relative frequency of characters
    mean_word = mean_word_length(word_list)  # calculates mean length of a word
    char_n = char_count(file_data)   # calculates the number of characters
    # saves the data in an object
    statistic_obj = obj_writer.OutFileWriter(word_count_n, stroke_count_n, word_stat, mean_word,
                                             char_n, char_stat, filepath)
    """print("type word_count_n ", type(word_count_n))
    print("type i ", type(stroke_count_n))
    print("word_stat ", type(word_stat))
    print("mean_word ", type(mean_word))
    print("type i ", type(char_n))
    print("char_stat ", type(char_stat))
    print("filepath ", type(filepath))"""
    json_obj = json.dumps(statistic_obj.__dict__)   # turns the object to a JSON object
    return json_obj


def word_count(word_list):
    """function, which takes as a parameter a list and

    returns the number of elements of this list
    """
    word_count_n = len(word_list)    # number of elements
    # print(word_count_n)              # for testing
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


def char_count(file_data):
    """function, which counts the amount of characters in a given string without spaces"""
    num_chars = len(file_data)    # number of all characters in the text
    number_space = file_data.count(" ")  # number of spaces in the text
    number_space += file_data.count("\n")
    num_chars -= number_space   # number of characters without spaces
    return num_chars


def char_frequency_distribution(file_data):
    """functions, which takes as a parameter a text and returns a dictionnary with character:

    relative frequency
    """
    char_n = len(file_data)  # number of characters in the text
    char_n -= file_data.count("\n")
    char_stat_relativ = {}   # dictionary for relative frequency
    # dictionary with total frequency
    char_stat = {i: file_data.count(i) for i in file_data if i != "\n"}
    for key in char_stat:
        average = char_stat[key] * 100 / char_n
        char_stat_relativ.update({key: average})
    return char_stat_relativ


def word_frequency_distribution(word_list):
    """functions which takes as parameter a list of words and returns a dictionary with word:

    relative frequency
    """
    num_words = len(word_list)   # number of words in the text
    words_stat_relativ = {}      # dictionary for relative frequency
    words_stat = {i: word_list.count(i) for i in word_list}   # dictionary with total frequency
    for key in words_stat:
        average = words_stat[key] * 100 / num_words
        words_stat_relativ.update({key: average})
    return words_stat_relativ


def mean_word_length(word_list):
    """function which takes as a parameter the cleaned word list and

     returns the mean word length
    """
    num_words = len(word_list)  # number of words in the text
    num_char = 0     # number of characters
    char_list = []   # list of all characters
    for i in range(num_words):
        word = str(word_list[i])   # takes one word from the word list
        for j in range(len(word)):
            char_list.append(word[j])   # appends the letters of the word to the list
    num_char += len(char_list)   # lenght of the character list = total amount of characters
    mean_length = num_char/num_words
    # print(mean_length)
    return mean_length
    
    
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
    # print(word_list2)   # for testing
    return word_list2
