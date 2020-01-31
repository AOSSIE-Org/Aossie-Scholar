from .models import ScholarProfile
import urllib.request
from bs4 import BeautifulSoup as soup 
import re
from django.utils import timezone
from metrics.newmetrics import Simple_Metrics, ScholarRawData
from .graphs import Graph
from metrics.decorators import timedecorator


class Scraper():
	def __init__(self, url, maxP, country='United States'):
		self.url= url
		self.maxP= maxP
		self.country= country
	@timedecorator.my_timer
	def getScholarData(self):

		title_list = []
		Citations =[]
		N_author_url= []
		author_names_list= []
		YEARS=[]
		self.first_pub_year=float('Inf')
		for i in range(0, 1000, 100):
			if (self.maxP <=i):
				pageSize = i
				break        									

		# looping trough pages to get all the publications

		for j in range(0,pageSize, 100): 
			S_url=self.url + "&cstart=" + str(j) +"&pagesize=100"
			with urllib.request.urlopen(S_url) as my_url:
				page_html = my_url.read()			
			page_soup = soup(page_html, "html.parser")	

			# Informaiton to be scraped only from the first page (Scholar's Name, Picture, his/her website, Company)

			if (j == 0): 				
												
				NameElement= page_soup.find('div', {'id': 'gsc_prf_in'})			
				scholar_name= NameElement.text

				imageElement = page_soup.find('img', {'id': 'gsc_prf_pup-img'})
				img_url= imageElement["src"]

				WebsiteElement = page_soup.findAll('a', {'class': 'gsc_prf_ila'})
				website=WebsiteElement[-1]["href"]
			
				work_infoElement = page_soup.find('div', {'class': 'gsc_prf_il'})	
				company= work_infoElement.text	
				
				
			#publication titles, title_list has all the titles of publications

			TitleElement = page_soup.findAll('td', {'class': 'gsc_a_t'})	

			for title in TitleElement:
				Title = title.a.text
				x=Title.encode('utf-8')
				title_list.append(x.decode('utf-8', 'ignore'))	
							
			
			# loop to get all the pop up urls embeded in publication

			info_pageElement = page_soup.findAll('a', {'class' : 'gsc_a_at'})

			for auth in info_pageElement:										

				Author_names_link = auth["data-href"]

				temp= re.findall("user=.+?[&]", Author_names_link)

				user= temp[0][5:-1]

				n_input=Author_names_link[-12:]

				n_author_url="https://scholar.google.com.au/citations?user="+user+"&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3D"+user+"%26citation_for_view%3D"+user+"%3A"+n_input+"%26tzom%3D-330"

				N_author_url.append(n_author_url)

			# Scraping author names from the page only

			authors_soupElement= page_soup.findAll('div', {'class': 'gs_gray'})

			for i in range(0, len(authors_soupElement), 2):
				author_names_list.append(authors_soupElement[i].text)

			# Scraping and cleaning Citations data

			Citations_soupElement = page_soup.findAll('td', {'class': 'gsc_a_c'})
			
			for c in Citations_soupElement:

				p= c.text.encode('utf-8')
				r=p.decode('utf-8', 'ignore')	
				try:
					Citations.append(int(r))
				except:
					try:
						Citations.append(int(r[:-1:]))
					except:
						Citations.append(0)
						
			# Scraping published Year data and making it usable

			YearsElement = page_soup.findAll('td', {'class': 'gsc_a_y'})

			for year in YearsElement:
				Yea=year.text
				YEARS.append(Yea)
				try:
					if int(Yea)<self.first_pub_year:
						self.first_pub_year=int(Yea)
				except:
					continue
				
		#ScholarRawData class 

		scholarData=ScholarRawData()
		urls_to_counter=scholarData.rawauthorscounterurl(author_names_list) 
		large_coAuths=scholarData.seleniumScraper(N_author_url,urls_to_counter)
		number_of_coauths=scholarData.coAuthors(author_names_list,large_coAuths)
		scholarData.getNpapersNcitationsTcitations(Citations,number_of_coauths)
		total_normalized_papers= scholarData.n_papers
		normalized_citations= scholarData.n_citations
		self.total_citations= sum(Citations)

		for i,j in enumerate(sorted(normalized_citations[:total_normalized_papers],reverse=True)):
			if(i+1 > j):
				normalized_h_index= i
				break

		Simple_Metrics_object= Simple_Metrics()
		h_index= Simple_Metrics_object.h_index(Citations)
		g_index= Simple_Metrics_object.g_index(Citations)
		m_index= Simple_Metrics_object.m_index(h_index, self.first_pub_year)
		o_index= Simple_Metrics_object.o_index(h_index,max(Citations))
		h_median= Simple_Metrics_object.h_median(h_index,Citations)
		TNCc= Simple_Metrics_object.TNCc(sum(normalized_citations), self.country)

		q= ScholarProfile(author_name= scholar_name, Company= company, Website= website, normalized_citations= normalized_citations, profile_url= user, publication_title= title_list, citations=Citations,
			coAuthors=number_of_coauths, country=self.country, Hmedian=h_median, Oindex= o_index, TNCc= TNCc, publications= len(title_list),Tcitations= self.total_citations, Year= YEARS, Gindex= g_index, Hindex= h_index, Mindex= m_index, created_at= timezone.now())
		q.save()

		return (user)
