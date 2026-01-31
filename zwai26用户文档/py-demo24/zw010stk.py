# -*- coding: utf-8 -*-




import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

def dr_xtyp(_dat):
    
    plt.plot(_dat['Open'])
    plt.plot(_dat['Close'])
    plt.plot(_dat['High'])
    plt.plot(_dat['Low'])
    #fss="tmp/stk010.png";plt.savefig(fss);
    plt.show()
    
#--------------------------
#mpl.use('Qt5Agg') 
#

df = pd.read_csv('APPL2014.csv',index_col=0,parse_dates=[0],encoding='gbk') 
d30=df[:30];
dr_xtyp(d30);

print(df)
