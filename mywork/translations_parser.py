#!/usr/bin/python3
#  __author__ = 'alenush'

from lxml.html import parse
from collections import defaultdict
import re

""" The Programm for parsing file of translations of sun tzu texts.
Parses and makes csv table from it"""

class DocTranslateParser:

    def __init__(self):
        self.json_dict = {}
        self.csv_file = 'suntzu_translation.csv'
        self.current_sub = 0
        self.all_trans = defaultdict(lambda: defaultdict(str))
        self.sub_left = defaultdict(list)
        self.sub_right = defaultdict(list)

    def begin_parsing_doc(self, filename):
            page = parse(filename)
            data2 = page.xpath('//td[1]//font')
            data3 = page.xpath('//td[2]//font')
            print(len(data2), len(data3))
            for d2, d3 in zip(data2, data3):
                    try:
                        if d2.attrib['color'] == '#ff0000':
                            if d2.text != '計篇':
                                self.current_sub = d2.text
                        elif d2.attrib['color'] == '#0000ff':
                            if self.current_sub != 0:
                                self.sub_left['blue'].append(d2.text)
                    except:
                        if self.current_sub != 0:
                            if d2.text != None:
                                self.sub_left['black'].append(d2.text)
                            for com in d2.xpath('span'):
                                if com.text != None:
                                    self.sub_left['black'].append(com.text)
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

        :return:
        """
        for dict1, dict2 in zip(self.sub_left, self.sub_right):
            print(dict1)
            left_array = self.sub_left[dict1]
            right_array = self.sub_right[dict2]
            print('!', dict1)
            for persn, comm in zip(left_array, right_array):
                print(persn, comm)


    def write_in_csv(self):
        """
        Function write the data (self.document_data) in csv file
        """
        pass

if __name__ == "__main__":
    document = DocTranslateParser()
    document.begin_parsing_doc('sun_tzu_translate.html')
    document.collect_in_one_dict()
    #document.write_in_csv()