import datetime
import pandas as pd
from .SCI import get_df


now = datetime.datetime.now()
df= get_df()




class Simple_Metrics():
    def __init__(self):
        self.CPDu= df.loc[df["Country"]=="United States"]["Citations per document"].iloc[0]

    def h_index(self, newCitations):
        newCitations.sort(reverse= True)
        counter= 0
        for i in (newCitations):
            counter+= 1
            if (counter >= i):  
                h_index= counter
                break
        return (h_index)

    def g_index(self, newCitations):
        newCitations.sort(reverse= True)
        counter= 0
        addupC= 0
        for i in newCitations:
            counter+= 1
            addupC+= i
            if (addupC >= counter**2):
                g_index= counter
                continue
            else:
                break
        return(g_index)

    def m_index(self, h_index, ist_pub_year):
        now = datetime.datetime.now()
        cur_year= now.year
        print (cur_year, ist_pub_year)
        time_gap= cur_year-int(ist_pub_year)+1
        mindex= float(h_index/time_gap)
        m_index= round(mindex, 2)
        return (m_index)

    def TNCc(self, TNC, country):
        pf= df.loc[df["Country"]==country]
        a= pf['Citations per document']
        CPDc= a.iloc[0]
        tnc= round(TNC*(self.CPDu/CPDc), 3)
        return tnc








