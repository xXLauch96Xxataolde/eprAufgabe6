"""module which contains the class AS, which saves all the statistic data in one object"""

class AS():

    def __init__(self, word_count, stroke_count, word_stat_relativ):
        self.word_count = word_count
        self.stroke_count = stroke_count
        self.word_stat_relativ = word_stat_relativ
