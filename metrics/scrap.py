from .models import ScholarProfile
import urllib.request
from urllib.request import Request, urlopen
#from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as soup 
import re
from django.utils import timezone
from .extract import rawauthorscounterurl, seleniumScraper, coAuthors, getnewCitations, getNpapersNcitationsTcitations
from metrics.newmetrics import Simple_Metrics
import requests
import random



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

	def f(self):
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

	
		for j in range(0,pageSize, 100):		#{ looping trough pages to get all the publications
			S_url=self.url + "&cstart=" + str(j) +"&pagesize=100"
			#opener = AppURLopener()
			#response = opener.open(S_url)
			#print (response)
			#with urllib.request.urlopen(S_url, headers=headers) as response:
			headers= {'User-Agent': random.choice(Uagents) ,
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
			'Accept-Encoding': 'gzip, deflate, br',
			'cookie': 'NID=186=af-CVNC8GNzt8rJ07GDHalL_UUDdkX2KjTTNM61dG10jjPp2cCPdl-Spob7J9B84281Du-VmKr65GvXvQWgnTVfTrpl7r9H_Bkdnwgbvc9xAWhDXRj-2FjSV_fAzueAwE8PhCgEzRTvWm7PFqZ4I0fEmQ0fdXsNaTfbV6V-L5aI6rBkkgslTYqsZWJfrZfGEdInOTT_VKCcOSgpwnqDThGw1Csszv6sCg7UNfNwNq6Mj; SID=cwcEQIJPThIyE2505P_0U3sFu7cjBdH8pxIkUcgZA5sDvDQxzfX0Y7b2bWLEgAjmJekvvQ.; HSID=AazwSocT1Hhvv2MSm; SSID=AQm3kmHTvfwSSQQnh; APISID=2922JlQjqOog42XH/AqxPpbuzeqtt4Ky1M; SAPISID=ioDH3BBSO7wXdAH6/Ag3swezHRw17luS_g; CONSENT=YES+IN.en+',
			'Host': 'scholar.google.com/au',
			'Accept-Language': 'en-US,en;q=0.8',
			'Connection': 'keep-alive'}
			req= Request(url=S_url, headers=headers)
			response= urlopen(req).read()
			#response= web_byte.decode('utf-8')
			#response= requests.get(S_url)
			#	page_html = response.read()	


			#response.close()	

			page_soup = soup(response, "html.parser")		

			if (j == 0):
				Name= page_soup.find('div', {'id': 'gsc_prf_in'})			# extracting the author's name
				scholar_name= Name.text
				print (scholar_name)
			Years = page_soup.findAll('td', {'class': 'gsc_a_y'})
			print ('5')
			for year in Years:
				try:
					years.append(int(year.text))
				except:
					years.append(None)
			print (years)

			Titles = page_soup.findAll('td', {'class': 'gsc_a_t'})			# publication titles

			for title in Titles:
				Title = title.a.text
				x=Title.encode('utf-8')
				title_list.append(x.decode('utf-8', 'ignore'))				#title_list has all the titles
			print (title_list)
			info_page = page_soup.findAll('a', {'class' : 'gsc_a_at'})

			for author in info_page:	
				
				print (author)									# loop to get all the pop up urls and then collect number of co-authors from there

				Author_names_link = author["data-href"]

				user=Author_names_link[44:56]
				print (user)

				n_input=Author_names_link[-12:]

				n_author_url="https://scholar.google.com.au/citations?user="+user+"&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3D"+user+"%26citation_for_view%3D"+user+"%3A"+n_input+"%26tzom%3D-330"

				N_author_url.append(n_author_url)

			authors_soup= page_soup.findAll('div', {'class': 'gs_gray'})

			less_authors_name=[]

			for a in authors_soup:
				less_authors_name.append(a.text)

			for i in range(0, len(less_authors_name), 2):
				author_names_list.append(less_authors_name[i])

			Citations_soup = page_soup.findAll('td', {'class': 'gsc_a_c'})
			
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

		coAuths= seleniumScraper(url_to_counter, N_author_url)
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
		#normalized_h_index= int(sum(n_citations)/len(title_list))

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
		


