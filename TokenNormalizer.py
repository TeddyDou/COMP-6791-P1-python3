from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_word_set_30 = set(["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it",
                        "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they",
                        "this", "to", "was", "will", "with", "reuter"])
stop_word_set_150 = set(['', 'a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are',
                         "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both',
                         'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't",
                         'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't",
                         'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here',
                         "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll",
                         "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's",
                         'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on',
                         'once', 'only', 'or', 'other', 'ought', 'our', 'ours\tourselves', 'out', 'over', 'own',
                         'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some',
                         'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then',
                         'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this',
                         'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd",
                         "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where',
                         "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would',
                         "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselves', 'reuter'])
def normalize(raw_data):
    """The function to normalize each token list"""

    term_list = []
    token_list = raw_data
    ps = PorterStemmer()
    wnl = WordNetLemmatizer()
    for string in token_list:
        if validate_string(string):
            new_string = string.lower()
            if new_string not in stop_word_set_150:
                term_list.append(ps.stem(new_string))
    return term_list


def validate_string(s):
    isvalid = False
    for char in s:
        if char.isdigit():
            isvalid = False
        elif char.isalpha():
            isvalid = True
    return isvalid


def generate_terms(string):
    tokens = word_tokenize(string)
    terms = normalize(tokens)
    return terms


#
# def preprocess_string(s):
#     new_s = ""
#     for char in s:
#         if char.isalpha():
#             new_s += char
#     return new_s.lower()


# mylist = ["U.S.A.", "CAn't", "policemen", "^^.", "already-weak", "games", "ab666", "Tony's", "daf", "fdfd"]
# print normalize(mylist)

