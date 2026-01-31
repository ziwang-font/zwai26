# -*- coding: utf-8 -*-




import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
#

#matplotlib.rc('image', cmap='Greys')
#mpl.rc('image', cmap='Greys')
    
#--------------------------
#mpl.use('Qt5Agg') 
#

#df = pd.read_csv('APPL2014.csv',index_col=0,parse_dates=[0],encoding='gbk') 
df = pd.read_csv('002046.csv',index_col=0)
d30=df[:30];
#dr_xtyp(d30);

d30[['open','close']].plot()
plt.show()

print(df)
