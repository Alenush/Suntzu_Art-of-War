#!/usr/bin/python3
#  __author__ = 'alenush'

from collections import defaultdict

class SunTzuData:

    def __init__(self, book, translations):
        self.chapters = 0
        self.sub_chapter = 0
        self.commentators = {'曹操曰∶':'Цао Цао:','李筌曰∶':'Ли Цюань:','杜牧曰∶':'Ду My:',
                             '陳皞注∶':'','孟氏曰∶':'Господин Мэн:','賈林曰∶':'Цзя Линь:',
                             '梅堯臣曰∶':'Мэй Яочэнь:','王皙曰∶':'Ван Си:',
                             '何延錫曰∶':'','張預曰∶':'Чжан Юй:', '陳皞曰∶':'', '何氏曰∶':''}
        self.my_book = defaultdict(lambda: defaultdict(str))
        self.content = defaultdict(lambda: defaultdict(str))
        self.translation_data = translations
        self.com_array = []

        for line in book.split('\n'):
            if len(line.split(',')) == 1:
                if 'sunzi' in line:
                    self.chapters += 1
                    self.sub_chapter = 0
                elif line.split(',')[0]!='':
                    self.sub_chapter +=1
                    self.content[str(self.chapters)][str(self.sub_chapter)] = line.split(',')[0]
            else:
                commentator = line.split(',')[0][1:-1]
                comment = line.split(',')[1]
                if self.chapters == 1:
                    self.comments(commentator, comment)
                else:
                    my_string = '|'.join([str(self.chapters),
                         str(self.sub_chapter), commentator, comment])
                    self.com_array.append(my_string)

    def comments(self, commentator, comment):
            for line in self.translation_data:
                com_ar = line.split('|')
                punkt, translator, translate = com_ar[1], com_ar[2], com_ar[3]
                if str(punkt) == str(self.sub_chapter):
                    if self.commentators[commentator] == translator:
                        element = '|'.join([str(self.chapters), str(self.sub_chapter), commentator,
                                comment, translator,translate])
                        self.com_array.append(element)
                        self.current_element = element
                    else:
                        my_string = '|'.join([str(self.chapters),
                                    str(self.sub_chapter), commentator, comment])
                        if my_string not in self.com_array:
                            if my_string != self.current_element[:len(my_string)]:
                                self.com_array.append(my_string)

    def write_db_chapter_table(self):
        """
        Function writes the initial db table. "chapters_table.csv"
        Format: 'chapter, sub_chapter, name_of_subchapter'
        """
        with open('chapter_table.csv', 'w', encoding='utf-8') as first_dbtable:
            for key, value in self.content.items():
                for sub in self.content[key]:
                    first_dbtable.write(key+','+sub+','+self.content[key][sub]+'\n')

sub_chapters = []

def pull_out_comments(translations):
    """Separate translation of comments and content
    :param translations: io_object. is 'translation_all.csv' file
    :return: if content -- collects in array. if comments return generator
    """
    for line in translations.readlines():
        if '-' not in line.split('|')[1]:
            yield line[:-1]
        else:
            sub_chapters.append(line[:-1])

def open_csv_book():
    with open('suntzu_data_valid.csv') as book:
        return book.read()

def write_content():
    """Write translation for content sub-chapters"""
    with open('translation_chapters.csv', 'w', encoding='utf-8') as comments:
        for line in sub_chapters:
            comments.write(line+'\n')

def write_comments(com_array):
    """Write translation for comments"""
    with open('db_translation_comments.csv', 'w', encoding='utf-8') as db_table:
        for line in com_array:
            db_table.write(line+'\n')

def open_csv_trans_comments():
    """Open all translation, divide on content and comments and add extra comment translations!
    :return array of all comments lines. Line = '1|1|Цао Цао:|«То, что именуется...\n' """
    with open('translations_all.csv') as trans_comments, \
    open('kusok.csv') as kusok_comments:
        comments_ar = pull_out_comments(trans_comments)
        extra_comments = [line for line in kusok_comments.read().split('\n')]
        return list(comments_ar) + extra_comments

if __name__ == "__main__":
    book = open_csv_book()
    trans_comments = open_csv_trans_comments()
    sun_tzu = SunTzuData(book, trans_comments)
    write_content() #write translation for sub_chapters
    write_comments(sun_tzu.com_array)

