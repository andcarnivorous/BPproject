from scipy import stats
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import pickle
import os
import random
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC, LinearSVC
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import EnglishStemmer

import graphs

def stemmed_words(doc):
    #stems words (it gets only the "root" of a word, deleting suffixes). Improves accuracy and speed.
    return (stemmer.stem(w) for w in analyzer(doc))

# Make the directory Graphs if it is not there.
if "Graphs" not in os.listdir():
    os.mkdir("Graphs")

# Define what stemmer will be used and which function will turn words into numbers.

stemmer = EnglishStemmer()
analyzer = CountVectorizer().build_analyzer()

# Make the directory Women if it is not there.
if "Women" not in os.listdir():
    os.mkdir("Women")

women_list = []
os.chdir("Women")

# open all the books in the directory and save the content in the proper list.
for _file in os.listdir():
    try:
        with open(_file, "r") as read_file:
            women_list.append(read_file.read())
    except:
        continue

# Give the category tag to each book
women_list = [("W", x) for x in women_list]
# Take only the first 250 books.
women_list = women_list[:250]

os.chdir("..")


men_list = []

# Make the directory Men if it is not there.
if "Men" not in os.listdir():
    os.mkdir("Men")

os.chdir("Men")

# open all the books in the directory and save the content in the proper list.
for _file in os.listdir():
    try:
        with open(_file, "r") as read_file:
            men_list.append(read_file.read())
    except:
        continue


os.chdir("..")

# Give a category tag to each book in this list
men_list = [("M", x) for x in men_list]
# Take only the first 250 books
men_list = men_list[:250]

# Put together the 250 books by men and the 250 books by women.
both_list = women_list + men_list

# make a word count to vector object which takes single words, bigrams, trigrams and 4-grams,
# deletes stopwords and stems the remaining
cv = CountVectorizer(ngram_range = (1,4),
                     stop_words = "english",
                     analyzer = stemmed_words)

######
#
# PLOTTING OF DISTRIBUTIONS HERE
# This takes time.
"""

dist_number = 0
for book in both_list:
    if len(book[1]) > 1000:
        try:
            f=plt.figure(figsize=(14,14))
            book_vec = cv.fit_transform([book[1]])
            book_vec = book_vec.toarray()
            print(book_vec.shape)
            graphs.graphics(book_vec)
            plt.savefig("./Graphs/distribution-%s.png" % dist_number)
            plt.close()
            dist_number += 1
        except:
            continue

"""
#######

# The scores of each time you execute the experiment will be stored here.
scoresLinear = []

for testing in range(10):

    # make the selection random.
    random.shuffle(both_list)

    # get the books contents, not their category
    texts = [book[1] for book in both_list]
    print("Number of Books:", len(both_list))
    
    # get the cateogries for each book (either "Man" or "Woman")
    categories = [x[0] for x in both_list]
    print("Categories: ", set(categories))
    
    # choose the training set size
    texts_train = texts[:350]
    categories_train = categories[:350]

    # choose the testing set size
    texts_test = texts[350:]
    categories_test = categories[350:]

    print("Fitting the Data...\n")
    # fit the training set set.
    cv_fit=  cv.fit_transform(texts_train)
    cv_trans = cv.transform(texts_train)

    # get the names of the features.
    names = cv.get_feature_names()

    # convert the data into a matrix (np array)
    arr = cv_fit.toarray()

    # apparently in bag-of-word methodology this algorithm is often applied
    # Term-Frequency-Inverse-Document-Frequency.
    transformer = TfidfTransformer().fit(cv_fit)

    # Turn the huge sparse matrix to a dense one to save resources.
    x_train_tf = transformer.transform(cv_fit).todense()

    print("Training the algorithm...\n")
    # Feed the matrix to the LinearSVC algorithm.
    linear = LinearSVC().fit(x_train_tf, categories_train)

    # Transform the testing set as well now
    X_new_counts = cv.transform(texts_test)
    X_new_tfidf = transformer.transform(X_new_counts)

    # Use the LinearSVC trained algorithm on the testing set
    predicted = linear.predict(X_new_tfidf)

    # get the average of accuracy and append it to the list of scores.
    print("linear: ", np.mean(predicted == categories_test))
    scoresLinear.append(np.mean(predicted == categories_test))

# print the scores, save them in a pickle file.
print(scoresLinear)
pickle.dump(scoresLinear, open( "scoresLinear.p", "wb" ))
