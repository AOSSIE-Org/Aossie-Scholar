import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import csv
import json

categories=[]
sub_categories=[]
tup_list=[]

def load_dict_from_file():
    f = open('h5data.txt','r')
    data=f.read()
    f.close()
    return (eval(data))

Data= load_dict_from_file()

for key, value in Data.items():
    categories.append(key)
    sub_cat_categories=[]
    sub_tup_list=[]
    for i in value:
        for j, k in i.items():
            sub_cat_categories.append(j)
            sub_tup_list.append(k)
            
    sub_categories.append(sub_cat_categories)
    tup_list.append(sub_tup_list)
        




def estimate_coef(x, y): 
    # number of observations/points 
    x=np.array(x)
    y=np.array(y)
    n = np.size(x) 
  
    # mean of x and y vector 
    m_x, m_y = np.mean(x), np.mean(y) 
  
    # calculating cross-deviation and deviation about x 
    SS_xy = np.sum(y*x) - n*m_y*m_x 
    SS_xx = np.sum(x*x) - n*m_x*m_x 
  
    # calculating regression coefficients 
    b_1 = SS_xy / SS_xx 
    b_0 = m_y - b_1*m_x 
  
    return(b_0, b_1) 



def main(): 
    observations=[]     
    for i in tup_list:
        coeff_list=[]
        for j in i:
            tup=()
            x= list(map(int, j[0]))
            y= list(map(int, j[1]))
            coeff=estimate_coef(x, y)
            tup=(coeff[0], coeff[1])
            coeff_list.append(tup)
        observations.append(coeff_list)


    print(observations)





main() 
  



































#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt   #Data visualisation libraries 
#print(h5data.head())
#print(h5data.info())
#print(h5data.describe())
#print(h5data.columns)