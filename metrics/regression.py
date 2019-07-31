import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import csv
import json

categories=[]
sub_categories=[]

def load_dict_from_file():
    f = open('h5data.txt','r')
    data=f.read()
    f.close()
    return (eval(data))

Data= load_dict_from_file()

for key, value in Data.items():
    categories.append(key)
    for i in value:
        for j, k in i.items():
            sub_categories.append(j)
            print (k)
            break
        break
    break







def estimate_coef(x, y): 
    # number of observations/points 
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
    # observations 
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) 
    y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12]) 
  
    # estimating coefficients 
    b = estimate_coef(x, y) 
    print("Estimated coefficients:\nb_0 = {}  \\nb_1 = {}".format(b[0], b[1]))

main() 
  



































#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt   #Data visualisation libraries 
#print(h5data.head())
#print(h5data.info())
#print(h5data.describe())
#print(h5data.columns)