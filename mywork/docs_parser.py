#!/usr/bin/python3
#  __author__ = 'alenush'

from lxml.html import parse
import re

""" The Programm for parsing file of whole 13 chapter Sun Tzu's Art of war with comments.
Parses and makes csv table from it"""

class DocParser:

    def __init__(self):
        self.json_dict = {}
        self.csv_file = 'suntzu_data.csv'
        self.document_data = []
        self.for_csv_data = []
        self.string_compare = re.compile("(\\*)?[a-z]+\\.[0-9]+")

    def begin_parsing_doc(self, filename):
        page = parse(filename)
        rows = page.xpath("body/p//font")
        for row in rows:
            if (row.text!=None) and (row.text!=''):
                self.document_data.append(('text', row.text)) #todo: check if the color blue
            else:
                inside_row = row.xpath(".//font//span")
                for r in inside_row:
                    if r.text != None:
                        self.document_data.append(('remarks', r.text))
                comments = row.xpath('.//font//font/b')
                if len(comments) > 0 and comments[0].text != None:
                    self.document_data.append(('commentator',comments[0].text))

    def preprocess_data(self):
        """Preprocees data from tree. Make comments complete. Write in new array """
        remember = []
        for data in self.document_data:
            if data[0] != 'text':
                    self.for_csv_data.append(('text',' '.join(remember)))
                    self.for_csv_data.append(data)
                    remember.clear()
            else:
                #if self.string_compare.match(data[1]):
                #    self.for_csv_data.append(('remarks', data[1]))
                #else:
                remember.append(data[1])

    def write_in_csv(self):
        """
        Function write the data (self.document_data) in csv file
        """
        self.preprocess_data()
        with open(self.csv_file, 'w', encoding='utf-8') as csv_file:
            for data in self.for_csv_data:
                if data[0]=='remarks':
                    csv_file.write(data[1]+'\n')
                elif data[0] == 'commentator':
                    csv_file.write(data[1]+',')
                else:
                    csv_file.write(data[1]+'\n')

if __name__ == "__main__":
    document = DocParser()
    document.begin_parsing_doc('sun_tzu_book_comments.html')
    document.write_in_csv()