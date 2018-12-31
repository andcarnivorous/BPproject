import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

randmatrix = np.random.rand(9,100)
x_axis = range(len(randmatrix[0,]))

num_rows, num_columns = randmatrix.shape

"""

# bar plot

for row in range(0, num_rows):
    plt.subplot(3,3,row + 1)
    plt.bar(x_axis, randmatrix[row,], width = 0.2, color="blue")
    plt.title("plot number %d" % (row + 1))
    plt.xlabel("words")
    plt.ylabel("Frequencies")

plt.show()

"""

def graphics (randmatrix):

    import random

    num_rows, num_columns = randmatrix.shape

    cols = ["r", "w", "blue", "g", "m", "c"]
    sns.set_style("darkgrid", {"axes.facecolor": ".1", "grid.color": ".8"})
    sns.set_context("poster")

    print(num_rows)
    sns.distplot(randmatrix[0,], hist=False, color=random.choice(cols))
    plt.title("Frequency of Words")
    plt.xlabel("Words")
    plt.ylabel("Frequencies")

