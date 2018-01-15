from collections import Counter
import json
from inoutcsv import obj_writer

def analyzer(file_data):
    """analyses the text file"""
    split_list = file_data.split()
    print(split_list)
    print(len(split_list))
    stroke_count_n = stroke_count(split_list)
    split_list = string_cleaner(split_list)
    word_count_n = word_count(split_list)
    statistic_obj = obj_writer.AS(word_count_n, stroke_count_n)
    json_obj = json.dumps(statistic_obj.__dict__)
    return(json_obj)
    
def word_count(split_list):
    word_count_n = len(split_list)
    print(word_count_n)
    return(word_count_n)

def stroke_count(split_list):
    temp_string = ""
    for entry in split_list:
        temp_string += entry

    stroke_count_n = Counter(temp_string)
    return(stroke_count_n)

def char_count():
    pass

def char_frequency_distribution():
    pass

def word_frequency_distribution():
    pass

def mean_word_length():
    pass
    
    
def string_cleaner(split_list):
    for i in range(len(split_list)):
        if split_list[i].endswith("!"):
            split_list[i] = split_list[i].replace("!","")
        if split_list[i].endswith("."):
            split_list[i] = split_list[i].replace(".","")
        if split_list[i].endswith(","):
            split_list[i] = split_list[i].replace(",","")
    print(split_list)
    return(split_list)