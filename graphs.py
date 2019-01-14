import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


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

