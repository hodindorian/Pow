#!/usr/bin/env python3
import sys
sys.path.append('./src/back/')

import load_csv as l 
import show_csv as s 

df = l.return_csv("./data.csv")
l.csv_value(df)

l.csv_value(df)

# l.csv_stadardisation_Z(df,"Vehicle Year")

s.histo_col(df,"Speed Limit")

s.plotBoxWhisker(df)
