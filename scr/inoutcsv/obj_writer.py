"""OutFileWriter

module which contains the class OutFileWriter, which saves all the statistic data in one object.
Because json and python get along so well, it is a nice trick to save the statistics to a 
object and then lets the built in function .__dict__ compile the obj to a json dumpable file
"""

import json
import os


__author__ = "5241945: Elisabeth Zeyen, 6785468: Robert Anselm Dieter am Wege"
__copyright__ = "Copyright 2017/2018 – EPR-Goethe-Uni"
__email__ = "lisa.zeyen@outlook.com, uni.goethe.horde@gmail.com"


class OutFileWriter:

    def __init__(self, word_count, stroke_count, word_stat, mean_word, char_n, char_stat,
                 filepath):
        """constructor, called when the instance is created"""
        rounded_char_stat = self.dict_entry_float_rounder(char_stat)
        rounded_word_stat = self.dict_entry_float_rounder(word_stat)
        self.word_count = word_count
        self.stroke_count = stroke_count
        self.word_stat_relativ = rounded_word_stat
        self.mean_word = round(mean_word, 3)
        self.char_n = char_n
        self.char_stat = rounded_char_stat
        self.save_to_file(filepath)

    def dict_entry_float_rounder(self, float_dict):
        """dict_entry_float_rounder

        What a handy function. This func takes a dict full of keys and values 
        which are floats and rounds the vals to 3 digits after the deciaml point.
        """
        for k in float_dict:
            float_dict[k] = round(float_dict[k], 3)
        return float_dict

    def check_remove_stat_file(self, filepath):
        """function, which deletes a file"""
        try:
            os.remove(filepath)
        except FileNotFoundError:
            pass

    def write_intro_file(self, filename):
        with open("definitions.txt", "r", errors="surrogateescape") as def_txt:
            def_obj = def_txt.read()
        def_txt.close()
        with open(filename, "a") as file:
            file.write(def_obj)
        file.close()

    def save_to_file(self, filepath):
        """Save_to_file

        This func takes a filepath as argument, splits it at ".", concatenates the
        analyzed txt file name with "_statitics.", adds the file ending "txt" and
        gives this string as the location for the statistics file to save
        """
        temp_var = filepath.split(".")
        temp_var = temp_var[0] + "_statistics." + temp_var[1]

        # deletes possible old stat files.
        self.check_remove_stat_file(temp_var)

        # writes an intro to the stat file
        self.write_intro_file(temp_var)

        with open(temp_var, "a", encoding="UTF-8") as file:
            json.dump(self.__dict__, file, ensure_ascii=False, indent=4)
        file.close()
        print("Statistics File saved to:", temp_var)
