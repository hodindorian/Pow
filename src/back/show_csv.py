import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

def histo_col(df, col):
    plt.figure()
    plt.hist(df[col], bins=4, alpha=0.7, color='blue', edgecolor='black')
    plt.title(f"Histogramme de la colonne '{col}'")
    plt.xlabel(col)
    plt.ylabel("Fréquence")
    plt.grid(True)
    return plt.gcf()

def plotBoxWhisker(df, col):
    df[col].plot(kind='box', subplots=True, sharex=False, sharey=False)
    return plt.gcf()
