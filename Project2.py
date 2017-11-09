"""The file to make queries"""

import pickle
import TokenNormalizer
import time
import math

#All the queries
query1 = "Democrats' welfare and healthcare reform policies"
query2 = "Drug company bankruptcies"
query3 = "George Bush"


# logic para should be 'and' or 'or', if the keyword is single word, logic can be any word
def makequery(keywords):
    result = []
    nor_keylist = TokenNormalizer.generate_terms(keywords)
    with open('stemming inverted index/FinalSpimi.txt', 'rb') as fp:
        termlist = pickle.load(fp)
        termdict = pickle.load(fp)
        doclength = pickle.load(fp)
        fp.close

    if len(nor_keylist) == 0:
        print ('Invalid input keywords, please try again')
        return
        # print ('The keywords you queried is not in the dictionary.')
        # return
    else:
        postings = []
        for keyword in nor_keylist:
            postings.append([t[0] for t in termdict[keyword]])
        if len(postings) == 0:
            print ('The keywords you queried is not in the dictionary.')
            return
        else:
            result = union(postings)

    if result:
        total_len = 0
        for number in doclength:
            total_len += number
        len_ave = round(total_len / len(doclength))
        ranked_result = rank(result, nor_keylist, termlist, termdict, doclength, len_ave)
        print (keywords)
        print (ranked_result)
        print ('The lenght of result is: ' + str(len(ranked_result)))
    else:
        print ('The keywords you queried has no valid result')


def rank(input, query, termlist, termdict, doclength, len_ave):
    N = 21578
    k = 1.6
    b = 0.75
    input_weight = []
    for doc_id in input:
        score = 0
        for term in query:
            tf_idf = 0
            if term in termlist:
                postings = termdict[term]
                tf_t_d = 0
                for element in postings:
                    if element[0] == doc_id:
                        tf_t_d = len(element[1])
                d_ft = len(postings)
                idf = math.log(N/d_ft)
                tf = ((k+1)*tf_t_d)/(k*((1-b)+ (b*(doclength[doc_id-1]/len_ave)))+tf_t_d)
                tf_idf = idf * tf
            score += tf_idf
        input_weight.append([doc_id, score])
    # print(input_weight)
    output = sorted(input_weight, key= lambda x:x[1], reverse=True)
    output = [x[0] for x in output]
    return output


def union(lists):
    result = set().union(*lists)
    return result


def multi_intersection(lists):
    # lists.sort(lambda x, y: cmp(len(x), len(y)))
    lists.sort(key = lambda s: len(s))
    # sorted(dictionary, key=lambda postings: postings[0])
    result = lists[0]
    for posting in lists[1:]:
        result = intersection(result, posting)
    return result


def intersection(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while not p1 == len(list1) and not p2 == len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p1 += 1
            p2 += 1
        elif list1[p1] < list2[p2]:
            p1 += 1
        else:
            p2 += 1
    return result


if __name__ == "__main__":

    start = time.clock()
    print("=============================================")
    makequery(query1)
    print("=============================================")
    makequery(query2)
    print("=============================================")
    makequery(query3)
    print("=============================================")
    print('Executed: %d s.' % int(time.clock() - start))
