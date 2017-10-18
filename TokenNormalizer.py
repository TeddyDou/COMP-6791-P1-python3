from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

stop_word_set_30 = set(["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it",
                        "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they",
                        "this", "to", "was", "will", "with", "reuter"])
stop_word_set_150 = set(stopwords.words('english'))|{'reuter'}


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

