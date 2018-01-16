"""module which contains the class AS, which saves all the statistic data in one object"""

class AS():

    def __init__(self, word_count, stroke_count, word_stat_relativ, mean_word, char_n, char_stat):
        self.word_count = word_count
        self.stroke_count = stroke_count
        self.word_stat_relativ = word_stat_relativ
        self.mean_word = mean_word
        self.char_n = char_n
        self.char_stat = char_stat