"""This file is to generate inverted index using spimi according to terms list files,
it records the positional index as well as the length of each document in the collection.
"""

import sys
import os
import pickle
import time


termfiledir = "stemming terms"
targetdir = "stemming inverted index"


def spimi_invert():
    """The spimi algorithm and it records the inverted index positions and doc lengths"""
    spimiFileNumber = 0
    DocID = 0
    endInput = False
    input_stream = []

    dictionary = {}
    doc_lengths = []
    while not endInput:
        if input_stream ==[]:
            DocID += 1
            filename = termfiledir + '/' + str(DocID) + '.txt'
            position = 0
            if os.path.isfile(filename):
                with open(filename, 'r') as termfile:
                    input_stream = read_from_dist(termfile)
                    doc_lengths.append(len(input_stream))
                termfile.close()
            else:
                endInput = True
                break
            termfile.close()
        else:
            term = input_stream.pop(0)
            position += 1
            if term not in dictionary:
                postings_list = add_to_dictionary(dictionary, term)
            else:
                postings_list = get_postings_list(dictionary, term)
            add_to_postings_list(postings_list, DocID, position)
    sorted_terms = sort_terms(dictionary)
    # sorted_terms = sorted(dictionary, key=lambda postings: postings[0])
    spimiFileNumber += 1
    spimi_file = open(targetdir + '/FinalSpimi.txt', 'wb')
    pickle.dump(sorted_terms, spimi_file)
    pickle.dump(dictionary, spimi_file)
    pickle.dump(doc_lengths, spimi_file)
    print ('Created file: ' + str(spimi_file))
    print ('Files processed: ' + str(DocID-1))
    spimi_file.close()


def add_to_dictionary(dictionary, term):
    dictionary[term] = []
    return dictionary[term]


def get_postings_list(dictionary, term):
    return dictionary[term]


def add_to_postings_list(postings_list, doc_id, position):
    for element in postings_list:
        if doc_id == element[0]:
            element[1].append(position)
            return
    postings_list.append([doc_id, [position]])


def write_to_disk(sorted_terms, dictionary, spimi_file):
    pickle.dump(sorted_terms, spimi_file)
    pickle.dump(dictionary, spimi_file)


def read_from_dist(terms_file):
    temp = terms_file.read()
    termlist = [x for x in temp.split(', ') if x is not '']
    return termlist


def sort_terms(dict):
    sorted_terms = []
    for k in sorted(dict):
        sorted_terms.append(k)
    return sorted_terms


def begin_spimi():
    if not os.path.isdir(targetdir):
        os.mkdir(targetdir)
    spimi_invert()


def create_readable_spimi_dictionary():
    fp = open(targetdir + '/FinalSpimi.txt', 'r')
    mylist = read_from_dist(fp)
    mydic = read_from_dist(fp)
    fp.close()
    with open('readable_dict.txt', 'w') as fw:
        for item in mylist:
            fw.write(item+': ' + str(mydic[item])+'\n')
            # print item + ': ' + str(mydic[item])
        fw.close


if __name__ == "__main__":
    start = time.clock()
    begin_spimi()

    print('Executed: %d s.' % int(time.clock()-start))
