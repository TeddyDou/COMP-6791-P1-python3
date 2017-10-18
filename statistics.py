"""This file calculates the statistics of the corpus Reuter-21578"""
import pickle
import os

unfiltered_terms_dir = 'unfiltered terms'
unfiltered_spimi_dir = 'unfiltered inverted index'

nonumber_terms_dir = 'no numbers terms'
nonumber_spimi_dir = 'no numbers inverted index'

casef_terms_dir = 'case folding terms'
casef_spimi_dir = 'case folding inverted index'

stopword30_terms_dir = '30 stopwords terms'
stopword30_spimi_dir = '30 stopwords inverted index'

stopword150_term_dir = '150 stopwords terms'
stopword150_spimi_dir = '150 stopwords inverted index'

stemming_terms_dir = 'stemming terms'
stemming_spimi_dir = 'stemming inverted index'


def calculate(tdir, sdir):

    with open(sdir+'/FinalSpimi.txt', 'rb') as f:
        mylist = pickle.load(f)
        mydict = pickle.load(f)
        f.close

    non_pos = 0
    for key in mylist:
        non_pos += len(mydict[key])

    pos = 0
    for doc in os.listdir(tdir):
        if os.path.splitext(doc)[1] == '.txt':
            ft = open(os.path.join(tdir, doc), "rb")
            termlist = pickle.load(ft)
            ft.close()
            pos += len(termlist)

    print ('For ' + sdir)
    print ('The word type (terms) size is:    ' + str(len(mylist)))
    print ('The non-positional index	size is: ' + str(non_pos))
    print ('The positional index	size is:     ' + str(pos))


if __name__ == '__main__':
    # calculate(unfiltered_terms_dir, unfiltered_spimi_dir)
    # calculate(nonumber_terms_dir, nonumber_spimi_dir)
    # calculate(casef_terms_dir, casef_spimi_dir)
    # calculate(stopword30_terms_dir, stopword30_spimi_dir)
    # calculate(stopword150_term_dir, stopword150_spimi_dir)
    calculate(stemming_terms_dir, stemming_spimi_dir)


##############################################
# Results for the statistics
# For unfiltered inverted index
# The word type (terms) size is:    129070
# The non-positional index	size is: 2918161
# The positional index	size is:     3091405
#
# For no numbers inverted index
# The word type (terms) size is:    69704
# The non-positional index	size is: 1621327
# The positional index	size is:     2625084
#
# For case folding inverted index
# The word type (terms) size is:    52819
# The non-positional index	size is: 1503153
# The positional index	size is:     2625084
#
# For 30 stopwords inverted index
# The word type (terms) size is:    52785
# The non-positional index	size is: 1261604
# The positional index	size is:     1890473
#
# For 150 stopwords inverted index
# The word type (terms) size is:    52680
# The non-positional index	size is: 1140436
# The positional index	size is:     1706555
#
# For stemming inverted index
# The word type (terms) size is:    41783
# The non-positional index	size is: 1081540
# The positional index	size is:     1706555
##############################################


