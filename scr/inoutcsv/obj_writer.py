"""module which contains the class OutFileWriter, which saves all the statistic data in one object"""
import json
import os
import codecs
from idlelib.iomenu import encoding


class OutFileWriter():

    def __init__(self, word_count, stroke_count, word_stat_relativ, mean_word, char_n, char_stat, filepath):
        self.word_count = word_count
        self.stroke_count = stroke_count
        self.word_stat_relativ = word_stat_relativ
        self.mean_word = mean_word
        self.char_n = char_n
        self.char_stat = char_stat
        self.save_to_file(filepath)

    def save_to_file(self, filepath):
        """Save_to_file
        
        This func takes a filepath as argument, splits it at ".", concatenates the
        analyzed txt file name with "_statitics.", adds the file ending "txt" and
        gives this string as the location for the statistics file to save
        """
        temp_var = filepath.split(".")
        temp_var = temp_var[0]+"_statistics."+temp_var[1]
        with open(temp_var, "w", encoding="UTF-8") as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=4)
        file.close()
        print("Statistics File saved to:", temp_var)