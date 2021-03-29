import pandas as pd
import random

from analyzer_lib import *
from common_lib import *

import numpy as np
from tqdm import tqdm


dfst = pd.read_csv (r'stock_price/AAAA_stock_price.csv')
df = dfst.iloc[-7:]
df.to_csv(r'stock_price/AAAA.csv', index = False)
df = pd.read_csv (r'stock_price/AAAA.csv')

Open = df ['Open']
Close = df ['Close']
High = df ['High']
Low = df ['Low']
Volume=df ['Volume']
#### previous price#####
df1=df.loc[0, :]
mean1 = (df1["Open"] + df1["Close"])/2
V1=df1["Volume"]
Vd1= V1/1.1
df2=df.loc[1, :]
mean2 = (df2["Open"] + df2["Close"])/2
V2=df2["Volume"]
Vd2= V2/1.1
df3=df.loc[2, :]
mean3 = (df3["Open"] + df3["Close"])/2
V3=df3["Volume"]
Vd3= V3/1.1
df4=df.loc[3, :]
mean4 = (df4["Open"] + df4["Close"])/2
V4=df4["Volume"]
Vd4= V4/1.1
df5=df.loc[4, :]
mean5 = (df5["Open"] + df5["Close"])/2
V5=df5["Volume"]
Vpre = (V1 + V2 + V3 + V4 + V5)/5
MAX = max(V1, V2, V3, V4, V5)
Vd5= V5/1.1
#########Star day###############
df6=df.loc[5, :]

dif1 = df6["Close"] - df6["Open"]   
dif2 = df6["High"] - df6["Close"]
dif3 = df6["Open"] - df6["Low"]

mean6 = (df6["Open"] + df6["Close"])/2
V6= (df6["Volume"])/1.1
per = dif1 / mean6
Vd6 = (df6["Volume"])/1.1
#########next day###############
df7=df.loc[6, :]
dif4 = df7["Close"] - df7["Open"]
mean7 = (df7["Open"] + df7["Close"])/2
per7 =dif4 / mean7
V7= (df7["Volume"])/1.2
Vd7 = df7["Volume"]

file1 = open("buy.list","a")
file2 = open("waiting.list","a")
if ((dif1 >= 0) and (per < 0.01) and (dif3 >= dif2) and (dif4 >= 0) and (mean1 >= mean2 >= mean3 >=  mean4 >= mean5 >= mean6) and (mean7 >= mean6) and (V7  >= 500000 >= V6 > Vpre)):
   file1.write("AAAA_sz_star \n")
elif ((dif1 >= 0) and (per < 0.05) and ((dif4 >= 0) and (per7 < 0.05) )and (mean7 >= mean6) and (V7 >= 500000 > V6 > MAX >= Vpre)):
   file1.write("AAAA_fl_up \n")
elif ((mean3 > mean4 > mean5 > mean6 > mean7 ) and ( Vd3 > Vd4 > Vd5 > Vd6 > Vd7) and (((mean3/mean4) >= 1.03) and ((mean4/mean5) >= 1.03) and ((mean5/mean6) >= 1.03) and ((mean6/mean7) >= 1.03))) :
   file1.write("AAAA_sl_down \n")  
elif ((mean3 < mean4 < mean5 < mean6 < mean7 ) and ( Vd3 > Vd4 > Vd5 > Vd6 > Vd7) and ((mean4/mean3) >= 1.03 ) and ((mean5/mean4) >= 1.03 ) and ((mean6/mean5) >= 1.03 ) and ((mean7/mean6) >= 1.03 )) :
   file1.write("AAAA_sl_up \n")
else:
    file2.write("AAAA_waiting_time \n")
file1.close()
file2.close()

