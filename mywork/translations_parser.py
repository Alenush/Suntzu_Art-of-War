#!/usr/bin/python3
#  __author__ = 'alenush'

from lxml.html import parse
from collections import defaultdict

""" The Programm for parsing file of translations of sun tzu texts.
Parses and makes csv table from it"""

class DocTranslateParser:

    def __init__(self):
        self.subs = []
        self.csv_file = 'suntzu_translation.csv'
        self.current_sub = 0
        self.sub_left = defaultdict(lambda: defaultdict(list))
        self.sub_right = defaultdict(list)

    def begin_parsing_doc(self, filename):
            page = parse(filename)
            data2 = page.xpath('//td[1]//font')
            data3 = page.xpath('//td[2]//font')
            for d2 in data2:
                    try:
                        if d2.attrib['color'] == '#ff0000':
                            if d2.text != '計篇':
                                sub_chapter = d2.text.replace('1.','')
                                self.current_sub = sub_chapter
                                self.subs.append(sub_chapter)
                        elif d2.attrib['color'] == '#0000ff':
                            if self.current_sub != 0:
                                self.sub_left[self.current_sub]['blue'].append(d2.text)
                    except:
                        if self.current_sub != 0:
                            if d2.text != None:
                                self.sub_left[self.current_sub]['black'].append(d2.text)
                            for com in d2.xpath('span'):
                                if com.text != None:
                                    self.sub_left[self.current_sub]['black'].append(com.text)
            for d3 in data3:
                    try:
                            if d3.attrib['color'] == '#0000ff':
                                self.sub_right['blue'].append(d3.text)
                    except:
                                if d3.text != None:
                                    self.sub_right['black'].append(d3.text)
                                for com in d3.xpath('span'):
                                    if com.text != None:
                                        self.sub_right['black'].append(com.text)

    def collect_in_one_dict(self):
        """

        """
        with open('db_table_comments.csv', 'w', encoding='utf-8') as com_table:
            com_table.write('chapter,sub_ch,commentator,comment\n')
            for key in self.subs:
                for type, arr in self.sub_left[key].items():
                    length = len(self.sub_left[key][type])
                    right_array = self.sub_right[type]
                    new_right = right_array[:length]
                    for left, right in zip(self.sub_left[key][type], new_right):
                        right_array.remove(right)
                        com_table.write('1|'+key+'|'+left+'|'+right+'\n')


if __name__ == "__main__":
    document = DocTranslateParser()
    document.begin_parsing_doc('sun_tzu_translate.html') #kusok_table2.html
    document.collect_in_one_dict()