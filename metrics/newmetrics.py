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

        self.author_raw_list=[j if '...' not in j else '#' for j in author_mixed_list]

        for i, j in enumerate(self.author_raw_list):
            if j=='#':
                self.counter_urls.append(i)

    def seleniumScraper(self,N_author_url):

        self.coAuths=[]

        if len(self.counter_urls) != 0:
            options = Options()
            options.headless = True
            driver= webdriver.Firefox(options=options)
            driver.implicitly_wait(2)
            for url in self.counter_urls:
                driver.get(N_author_url[url])
                time.sleep(2)
                title= driver.find_elements_by_xpath('//div[@class="gsc_vcd_value"]')
                page_element = title[0].text
                self.coAuths.append(len(page_element.split(',')))
            driver.quit()
        else:
            return
    
    def coAuthors(self):

        acounter= 0

        for pos,name in enumerate(self.author_raw_list):
            if (name=='#'):
                self.author_raw_list[pos]=self.coAuths[acounter]
                acounter+=1
            else:
                self.author_raw_list[pos]=len(name.split(','))

        return (self.author_raw_list)


    def getNpapersNcitationsTcitations(self,newCitations, size):

        self.n_papers=int(sum(list(map(lambda x: 1/x, self.author_raw_list))))
       
        self.n_citations=[int(i/j) for i, j in zip(newCitations,self.author_raw_list)]
        
        self.sum_citations= sum(newCitations)
        
       
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
            if pow(i+1,2)>addupC:
                g_index=i
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
