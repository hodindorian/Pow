#!/usr/bin/env python3

import sys
sys.path.append('./src/back/')

import load_csv as l 
import show_csv as s 
import clustering_csv as c

df = l.return_csv("./data.csv")
l.csv_value(df)

l.csv_value(df)

# l.csv_standardisation_Z(df,"Vehicle Year")

# l.csv_robust_normalize(df,"Speed Limit")

# s.histo_col(df,"Speed Limit")

# s.plotBoxWhisker(df)

c.launch_cluster(df,['Speed Limit','Vehicle Year'])
