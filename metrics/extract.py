from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options


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
        
       