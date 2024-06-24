import pandas as pd
import numpy  as np
import matplotlib.pyplot as plt

def histo_col(df,colonne):
    plt.figure()
    plt.hist(df[colonne], bins=int(df[colonne].nunique()/4), alpha=0.7, color='blue', edgecolor='black')
    plt.title(f"Histogramme de la colonne '{colonne}'")
    plt.xlabel(colonne)
    plt.ylabel("Fréquence")
    plt.grid(True)
    plt.show()

def plotBoxWhisker(df):
    df.plot(kind='box', subplots=True, sharex=False, sharey=False)
    plt.show()
