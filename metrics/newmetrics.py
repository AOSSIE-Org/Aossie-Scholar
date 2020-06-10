from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
import datetime
import pandas as pd
from .SCI import get_df
import statistics

now = datetime.datetime.now()
df= get_df()



class ScholarRawData():

    def rawauthorscounterurl(self,author_mixed_list):

        self.counter_urls=[]

        for i, j in enumerate(author_mixed_list):
            if '...' in j:
                self.counter_urls.append(i)
        return self.counter_urls

    def seleniumScraper(self,N_author_url,counter_urls):

        self.coAuths=[]

        if len(counter_urls) != 0:
            options = Options()
            options.headless = True
            driver= webdriver.Firefox(options=options)
            driver.implicitly_wait(2)
            for url in counter_urls:
                driver.get(N_author_url[url])
                time.sleep(2)
                title= driver.find_elements_by_xpath('//div[@class="gsc_vcd_value"]')
                page_element = title[0].text
                self.coAuths.append(len(page_element.split(',')))
            driver.quit()
        else:
            return
        return self.coAuths
    
    def coAuthors(self,author_raw_list,coAuths):

        acounter= 0

        for pos,name in enumerate(author_raw_list):
            if ('...' in name):
                author_raw_list[pos]=coAuths[acounter]
                acounter+=1
            else:
                author_raw_list[pos]=len(name.split(','))
        self.Authors=author_raw_list

        return (self.Authors)


    def getNpapersNcitationsTcitations(self,Citations, coAuthors):

        self.n_papers=int(sum(list(map(lambda x: 1/x, coAuthors))))
       
        self.n_citations=[int(i/j) for i, j in zip(Citations,coAuthors)]
        
       
class Simple_Metrics():
    def __init__(self):
        self.CPDu= df.loc[df["Country"]=="United States"]["Citations per document"].iloc[0]

    def h_index(self, Citations):
        Citations.sort(reverse= True)
        for i, j in enumerate(Citations):
            if i+1>=j:
                h_index=i+1
                break
        return (h_index)

    def g_index(self, Citations):
        Citations.sort(reverse= True)
        addupC= 0
        for i, citation in enumerate(Citations):
            addupC+= citation
            if pow(i+1,2)<=addupC:
                g_index=i+1
            else:
                break
        return(g_index)

    def m_index(self, h_index, ist_pub_year):
        now = datetime.datetime.now()
        cur_year= now.year
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

    def o_index(self, h_index, maxCitation):
        product= (h_index*maxCitation)
        oindex= round(pow(product,(1/2)))
        return oindex

    def h_median(self, h_index, newCitations):
        h_core= [i for i in newCitations if (i>h_index)]
        hmedian= statistics.median(h_core)
        return hmedian
        
    def e_index(self, h_index, Citations):
        eindex= round((sum(Citations)-(h_index**2))**(1/2),2)
        return eindex