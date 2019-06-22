import os
from .models import ScholarProfile
import urllib.request
from urllib.request import Request, urlopen
#from urllib.request import Request, urlopen
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as soup 
import re
from django.utils import timezone
from .extract import rawauthorscounterurl, coAuthors, getnewCitations, getNpapersNcitationsTcitations
from .newmetrics import Simple_Metrics
import requests
import random
import time



class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

Uagents= ['Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) ' 
                      'Chrome/23.0.1271.64 Safari/537.11', 'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
					  'Googlebot/2.1 (+http://www.google.com/bot.html)' ]

class Scraper():
	def __init__(self, url, maxP, country):
		self.url= url
		self.maxP= maxP
		self.country= country

	def getScholarData(self):	 
		for i in range(0, 1000, 100):
			if (self.maxP <=i):
				pageSize = i
				break
                   									
		ncounter= 0
		bcounter= 0																					          
		Citations =[]  												# to count total numbers citations an author recieved. 
		title_list= []
		N_author_url= []
		author_names_list= []
		years= []
		
		options= Options()
		options.binary_location= os.environ.get('GOOGLE_CHROME_BIN')
		options.add_argument('--headless')
		options.add_argument('--disable-gpu')
		options.add_argument('--no-sandbox')
		options.add_argument('--remote-debugging-port=9222')

		driver= webdriver.Chrome(desired_capabilities=options.to_capabilities(), executable_path=str(os.environ.get('CHROMEDRIVER_PATH')))
		
		for j in range(0,pageSize, 100):		#{ looping trough pages to get all the publications
			S_url=self.url + "&cstart=" + str(j) +"&pagesize=100"
			driver.implicitly_wait(5)
			driver.get(S_url)
			if (j == 0):
				time.sleep(3)
				Name= driver.find_element_by_xpath('//div[@id="gsc_prf_in"]')
				scholar_name= Name.text
				print (scholar_name)
			else:
				time.sleep(3)

			Years= driver.find_elements_by_xpath('//td[@class="gsc_a_y"]')
			for year in Years:
				try:
					years.append(int(year.text))
				except:
					years.append(None)
			print (years)

			Titles= driver.find_elements_by_xpath('//a[@class="gsc_a_at"]')	# publication titles
			for title in Titles:
				Title = title.text
				title_list.append(str(Title))
			print (title_list)
			
			for author in Titles:							# loop to get all the pop up urls and then collect number of co-authors from there
				Author_names_link = author.get_attribute("data-href")
				temp= re.findall("user=.+?[&]", Author_names_link)
				user= temp[0][5:-1]
				print (user)
				n_input=Author_names_link[-12:]

				n_author_url="https://scholar.google.com.au/citations?user="+user+"&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3D"+user+"%26citation_for_view%3D"+user+"%3A"+n_input+"%26tzom%3D-330"

				N_author_url.append(n_author_url)

			authors_soup= driver.find_elements_by_xpath('//div[@class= "gs_gray"]')
			less_authors_name=[]
			for a in authors_soup:
				less_authors_name.append(a.text)

			for i in range(0, len(less_authors_name), 2):
				author_names_list.append(less_authors_name[i])

			Citations_soup = driver.find_elements_by_xpath('//td[@class= "gsc_a_c"]')
			for c in Citations_soup:
				p= c.text.encode('utf-8')
				r=p.decode('utf-8', 'ignore')
				q= re.findall('[0-9]+',r)
				Citations.append(q)
		
		CoauthsAndUrls= rawauthorscounterurl(author_names_list)

		url_to_counter= CoauthsAndUrls[1]

		n_author_names_list= CoauthsAndUrls[0]
		print ("d")
		print (len(N_author_url), url_to_counter, len(n_author_names_list))
		coAuths=[]
		if len(url_to_counter) != 0:
			for url in url_to_counter:
				driver.implicitly_wait(5)
				driver.get(N_author_url[url])
				try:
					time.sleep(2)
					title= driver.find_elements_by_xpath('//div[@class="gsc_vcd_value"]')
				except:
					time.sleep(5)
					title= driver.find_elements_by_xpath('//div[@class="gsc_vcd_value"]')
				try:
					page_element= title[0].text
				except:
					print(title.text)

				coAuths.append(len(page_element.split(',')))

			driver.quit()

		#coAuths= seleniumScraper(url_to_counter, N_author_url)
		print ('c')
		print (len(title_list), len(coAuths))

		number_of_coauths= coAuthors(n_author_names_list, coAuths)

		newCitations= getnewCitations(Citations)

		myvar= getNpapersNcitationsTcitations(number_of_coauths, newCitations, len(title_list))

		total_normalized_papers= myvar[0]

		normalized_citations= myvar[1]

		total_citations= myvar[2]

		q= ScholarProfile(author_name= Name.text, profile_url= self.url[-18:], publication_title= title_list,
		created_at= timezone.now())
		q.save()

		total_normalized_citations= int(sum(normalized_citations))

		nn_citations= normalized_citations[0:total_normalized_papers]
		nn_citations.sort(reverse= True)

		for i in nn_citations:
			ncounter+= 1
			print (ncounter, i)
			if(ncounter> i):
				normalized_h_index= ncounter-1
				break

		h_index= Simple_Metrics.h_index(newCitations)
		print (h_index)
		return (self.url)
		


