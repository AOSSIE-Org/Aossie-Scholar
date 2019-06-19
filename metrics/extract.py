from selenium import webdriver
import time
import os
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


def rawauthorscounterurl(author_names_list):
    n_author_names_list=[]
    counter_urls=[]
    counter= 0
    for j in author_names_list:
        if '...' not in j:
            n_author_names_list.append(author_names_list[counter])
            counter+=1
            continue
        else:
            n_author_names_list.append('#')
            counter_urls.append(counter)
            counter+= 1
    return (n_author_names_list, counter_urls)

def seleniumScraper(url_to_counter, N_author_url):
    coAuths=[]
    if len(url_to_counter) != 0:
        options= webdriver.FirefoxOptions()
        options.add_argument('-headless')
       # gecko = os.path.normpath(os.path.join(os.path.dirname(__file__), 'geckodriver'))
        binary = FirefoxBinary(str(os.environ.get('FIREFOX_BIN')))
        driver= webdriver.Firefox(firefox_options=options, firefox_binary= binary, executable_path=str(os.environ.get('GECKODRIVER'))) #executable_path= "/usr/local/bin:/usr/bin:/bin:/metrics/vendor/")                                      # executable_path= "/tmp/build_f1b375df49e68e9d0628cfb83907ac6c/vendor/geckodriver/")
        driver.implicitly_wait(5)
        for url in url_to_counter:
            driver.get(N_author_url[url])
            driver.implicitly_wait(5)
            title= driver.find_elements_by_xpath('//div[@class="gsc_vcd_value"]')
            #print (N_author_url[url])
            page_element = title[0].text
            coAuths.append(len(page_element.split(',')))
        driver.quit()
    return (coAuths)    

def coAuthors(n_author_names_list, coAuths):
    number_of_coauths= []
    acounter= 0
    for name in n_author_names_list:
        if (name=='#'):
            number_of_coauths.append(coAuths[acounter])
            acounter+=1
        else:
            number_of_coauths.append(len(name.split(',')))
    return (number_of_coauths)

def getnewCitations(Citations):
    newCitations= []
    for entry in Citations:
        try:
            newCitations.append(int(entry[0]))
        except:
            newCitations.append(0)			# newCitations has all the citations as a list
    return (newCitations)

def getNpapersNcitationsTcitations(number_of_coauths, newCitations, size):
    n_citations= []
    n_papers= 0
    sum_citations= 0
    for element in range(size):
        n_papers +=1/number_of_coauths[element]
        n_citations.append(int(int(newCitations[element])/number_of_coauths[element]))
        
    for k in newCitations:
        sum_citations+= int(k)

    return (int(n_papers), n_citations, sum_citations)
