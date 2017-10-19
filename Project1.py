"""The file to make queries"""

import pickle
import TokenNormalizer

#different lists of queries
givenquaries = ["Jimmy Carter", "Green Party", "Innovations in telecommunication"]
myquaries = ["Ted", "Potomac customers", "concession obstructing"]
exchquaries1 = ["Realtors", "Chinese Trade Report", "Agriculture Citicorp Germany"]
exchquaries2 = ["able", "able interesting", "able interesting"]
labquaries = ["Reagan", "Brown-Forman Inc", "Hyundai Motors"]


# logic para should be 'and' or 'or', if the keyword is single word, logic can be any word
def makequery(keywords, logic):
    result = []
    nor_keylist = TokenNormalizer.generate_terms(keywords)
    with open('stemming inverted index/FinalSpimi.txt', 'rb') as fp:
        termlist = pickle.load(fp)
        termdict = pickle.load(fp)
        fp.close
    if len(nor_keylist) == 0:
        print ('Invalid input keywords, please try again')
        return
    elif len(nor_keylist) == 1:
        logic = 'N/A'
        if nor_keylist[0] in termlist:
            result = termdict[nor_keylist[0]]
        else:
            print ('The keywords you queried is not in the dictionary.')
            return
    else:
        postings = []
        for keyword in nor_keylist:
            postings.append(termdict[keyword])
        if logic.lower() == 'or':
            result = union(postings)
        elif logic.lower() == 'and':
            result = multi_intersection(postings)
        else:
            print ('Can not recognise the logic operation of your query')

    if result:
        print (keywords + ' : '+logic.upper())
        print (sorted(result))
        print ('The lenght of result is: ' + str(len(result)))
    else:
        print ('The keywords you queried has no valid result')


def union(lists):
    result = lists[0]
    for posting in lists[1:]:
        result.extend(posting)
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

    for query in givenquaries:
        makequery(query, "and")
        makequery(query, "or")
        print("=============================================")
    makequery(myquaries[0], "and")
    makequery(myquaries[1], "and")
    makequery(myquaries[2], "or")
    print("=============================================")
    makequery(exchquaries1[0], "and")
    makequery(exchquaries1[1], "and")
    makequery(exchquaries1[2], "or")
    print("=============================================")
    makequery(exchquaries2[0], "and")
    makequery(exchquaries2[1], "and")
    makequery(exchquaries2[2], "or")
    print("=============================================")
    makequery(labquaries[0], "N/A")
    makequery(labquaries[1], "and")
    makequery(labquaries[2], "or")
    print("=============================================")
    
