"""Parse the raw data file and generate terms list files using Sgmllib module"""

import sgmllib
import os
import TokenNormalizer
import time
import pickle


# newdir = "Terms file by Sgmllib"
# newdir = "unfiltered terms"
# newdir = "no numbers terms"
# newdir = "case folding terms"
# newdir = "30 stopwords terms"
# newdir = "150 stopwords terms"
newdir = "stemming terms"


class SgmParser(sgmllib.SGMLParser):
    """A class to parse text from Reuters SGML files."""

    def parse(self, s):
        """Parse the given string 's', which is an SGML encoded file."""

        self.feed(s)
        self.close()

    def __init__(self, verbose=0):
        """Initialize an object, passing 'verbose' to the superclass."""

        sgmllib.SGMLParser.__init__(self, verbose)
        self.in_title = 0
        """Flag indicating whether or not we're parsing the title."""

        self.in_dateline = 0
        """Flag indicating whether or not we're parsing the dateline"""

        self.in_body = 0
        """Flag indicating whether or not we're parsing the body"""

        self.in_text = 0
        """Flag indicating whether or not we're parsing the text"""

        self.title = ""
        """Title of the document"""

        self.doc_id = 0
        """Document ID"""

        self.dateline = ""
        """Date line for the document"""

        self.body = ""
        """Body of the document"""

        self.text = ""
        """Text of the document"""

    def handle_data(self, data):
        """"Print out data in TEXT portions of the document."""

        # Ignaore the characters in data that ascii can not decode
        # data = unicode(data, errors='replace')

        if self.in_body:
            self.body += data
        elif self.in_title:
            self.title += data
        elif self.in_dateline:
            self.dateline += data
        elif self.in_text:
            self.text += data
    ####
    # Handle the Reuters tag
    ####
    def start_reuters(self, attributes):
        """Process Reuters tags, which bracket a document. Create a new file for each document encountered."""
        for name, value in attributes:
            if name == "newid":
                self.doc_id = value

    def end_reuters(self):
        """Write out the contents to a file and reset all variables."""

        article_string = ""
        if not self.body == "" and not self.title == "":
            article_string += self.title + "\n"
            article_string += self.body + "\n"
        elif self.body == "" and not self.title == "":
            article_string += self.title + "\n"
        elif self.title == "" and not self.body == "":
            article_string += self.body + "\n"
        else:
            article_string += self.text + "\n"

        terms = TokenNormalizer.generate_terms(article_string)
        if not os.path.isdir(newdir):
            os.mkdir(newdir)
        fname = newdir + "/" + str(self.doc_id) + ".txt"
        # change
        doc_file = open(fname, "w")
        for token in terms:
            doc_file.write(token + ', ')
        doc_file.close()
        # change
        # print "File number " + self.doc_id + " is processed"

        # Reset variables
        self.in_title = 0
        self.in_dateline = 0
        self.in_body = 0
        self.in_text = 0
        self.doc_id = 0
        self.title = ""
        self.body = ""
        self.dateline = ""
        self.text = ""

    ####
    # Handle TITLE tags
    ####
    def start_title(self, attributes):
        """Indicate that the parser is in the title portion of the document."""

        self.in_title = 1

    def end_title(self):
        """Indicate that the parser is no longer in the title portion of the document."""

        self.in_title = 0

    ####
    # Handle BODY tags
    ####
    def start_body(self, attributes):
        """Indicate that the parser is in the body portion of the document."""

        self.in_body = 1

    def end_body(self):
        """Indicate that the parser is no longer in the body portion of the document."""

        self.in_body = 0

    ####
    # Handle TEXT tags
    ####
    def start_text(self, attributes):
        """Indicate that the parser is in the title portion of the document."""

        self.in_text = 1

    def end_text(self):
        """Indicate that the parser is no longer in the title portion of the document."""

        self.in_text = 0


def begin_parse():

    # modify the directory of your reuter-21578 files
    rootdir = 'D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/'
    docname = 'D:/concordia study/Term 6 COMP 6791 Information Retrival/Lab/reuters/reut2-017.sgm'

    for doc in os.listdir(rootdir):
        if os.path.splitext(doc)[1] == '.sgm':
            ft = open(os.path.join(rootdir, doc), "rb")
            s = ft.read().decode('utf-8', errors='ignore')
            parser = SgmParser()
            parser.parse(s)
            ft.close()
            print("File number " + doc + " is processed")


if __name__ == "__main__":
    start = time.clock()
    begin_parse()

    print('Executed: %d s.' % int(time.clock()-start))

