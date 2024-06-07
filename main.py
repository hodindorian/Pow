#!/usr/bin/env python3
import sys
sys.path.append('./src/back/')

import load_csv as l 

df = l.return_csv("./data.csv")
l.csv_value(df)

l.csv_value(df)

l.csv_stadadisation_Z(df,"Vehicle Year")
