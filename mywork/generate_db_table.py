#!/usr/bin/python3
#  __author__ = 'alenush'

import re
from collections import defaultdict

class SunTzuData:

    def __init__(self, book):
        self.chapters = 0
        self.sub_chapter = 0
        self.commentators = []
        self.my_book = defaultdict(lambda: defaultdict(str))
        self.content = defaultdict(lambda: defaultdict(str))

        for line in book.split('\n'):
            if len(line.split(',')) == 1:
                if 'sunzi' in line:
                    self.chapters += 1
                    self.sub_chapter = 0
                elif line.split(',')[0]!='':
                    self.sub_chapter +=1
                    self.content[str(self.chapters)][str(self.sub_chapter)]=line.split(',')[0]
            else:
                commentator = line.split(',')[0]
                comment = line.split(',')[1]

    def write_db_chapter_table(self):
        """
        Function writes the initial db table. "chapters_table.csv"
        Format: 'chapter, sub_chapter, name_of_subchapter'
        """
        with open('chapter_table.csv', 'w', encoding='utf-8') as first_dbtable:
            first_dbtable.write('chapter,sub_ch,sub_ch_name\n')
            for key, value in self.content.items():
                for sub in self.content[key]:
                    first_dbtable.write(key+','+sub+','+self.content[key][sub]+'\n')

def open_csv():
    with open('suntzu_data_valid.csv') as book:
        return book.read()

if __name__ == "__main__":
    book = open_csv()
    sun_tzu = SunTzuData(book)
    sun_tzu.write_db_chapter_table()
