from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time
h5data={}
B=[]
A=[]
category_list=[]
options = Options()
options.headless = True
driver= webdriver.Firefox(options= options)
wait= WebDriverWait(driver, 10)
data_url= "https://scholar.google.com.au/citations?view_op=top_venues&hl=en"
driver.get(data_url)
element= wait.until(EC.element_to_be_clickable((By.ID, "gsc_mtv_ac-b")))
#categories_button= driver.find_element_by_xpath("//button[@id='gsc_mtv_ac-b']")
element.click()
counter=0
categories_list= driver.find_elements_by_xpath('//a[@class="gs_md_li"]')
category_links=[]
for link in categories_list:
    if (counter<8):
        category_links.append(link.get_attribute("href"))
        category_list.append(link.text)
        counter+=1
    else:
        break

for category in category_links:
    driver.get(category)
    element2= wait.until(EC.element_to_be_clickable((By.ID, "gsc_mcn_sb")))
    element2.click()
    subCat_list= driver.find_elements_by_xpath('//a[@class="gs_md_li"]')
    sub_category_links=[]
    subcategory_list=[]
    for slink in subCat_list:
        sub_link= slink.get_attribute("href")
        sub_category_links.append(sub_link)
        subcategory_list.append(slink.text)
    A.append(sub_category_links)
    B.append(subcategory_list)
T_list=[]
for lastlink in A:
    for linklast in lastlink:
        T= []
        driver.get(linklast)
        h5index= driver.find_elements_by_xpath('//a[@class="gs_ibl gsc_mp_anchor"]')
        h5median= driver.find_elements_by_xpath('//span[@class="gs_ibl gsc_mp_anchor"]')
        l1 =[]
        l2=[]
        for i in h5index:
            l1.append(i.text)
        for j in h5median:    
            l2.append(j.text)
        temp_list= [l1,l2]    
        T.append(temp_list)   
    T_list.append(T)

print (category_list, B, T_list)
print (len(category_list), len(B), len(A))