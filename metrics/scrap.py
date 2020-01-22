from .models import ScholarProfile
import urllib.request
from bs4 import BeautifulSoup as soup 
import re
from django.utils import timezone
from .extract import rawauthorscounterurl, seleniumScraper, coAuthors, getnewCitations, getNpapersNcitationsTcitations
from .newmetrics import Simple_Metrics
from .graphs import Graph

title_list = []
Citations =[]
N_author_url= []
author_names_list= []


class Scraper():
	def __init__(self, url, maxP, country):
		self.url= url
		self.maxP= maxP
		self.country= country

	def getScholarData(self):
		for i in range(0, 1000, 100):
			if (self.maxP <=i):
				pageSize = i
				break        									# to count normalized papers.
		title_list = []
		Citations =[]
		N_author_url= []
		author_names_list= []
		YEARS=[]
		year_list=[]
		ncounter = 0
		bcounter= 0            												# to count total numbers citations an author recieved. 

	#{ looping trough pages to get all the publications
		for j in range(0,pageSize, 100):

			S_url=self.url + "&cstart=" + str(j) +"&pagesize=100"

			with urllib.request.urlopen(S_url) as my_url:

				page_html = my_url.read()			

			page_soup = soup(page_html, "html.parser")		

			if (j == 0):
				Name= page_soup.find('div', {'id': 'gsc_prf_in'})			# extracting the author's name
				scholar_name= Name.text
				img = page_soup.find('img', {'id': 'gsc_prf_pup-img'})
				img_url= img["src"]
				Website = page_soup.findAll('a', {'class': 'gsc_prf_ila'})
				work_info = page_soup.find('div', {'class': 'gsc_prf_il'})	
				company= work_info.text	
				counter=0
				for site in Website:
					if(len(Website)==2):
						if(counter==0):
							counter+=1
							continue
					website = site["href"]

			Titles = page_soup.findAll('td', {'class': 'gsc_a_t'})			# publication titles

			for title in Titles:
				Title = title.a.text
				x=Title.encode('utf-8')
				title_list.append(x.decode('utf-8', 'ignore'))				#title_list has all the titles

			info_page = page_soup.findAll('a', {'class' : 'gsc_a_at'})

			for author in info_page:										# loop to get all the pop up urls and then collect number of co-authors from there

				Author_names_link = author["data-href"]

				temp= re.findall("user=.+?[&]", Author_names_link)
				user= temp[0][5:-1]

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
		
			Years = page_soup.findAll('td', {'class': 'gsc_a_y'})
			for year in Years:
				YEARS.append(year.text)

			for year in Years:
				try:
					y= int(year.text)
					year_list.append(y)
				except:
					continue 
				

		CoauthsAndUrls= rawauthorscounterurl(author_names_list)

		url_to_counter= CoauthsAndUrls[1]

		n_author_names_list= CoauthsAndUrls[0]

		coAuths= seleniumScraper(url_to_counter, N_author_url)

		number_of_coauths= coAuthors(n_author_names_list, coAuths)

		newCitations= getnewCitations(Citations)

		myvar= getNpapersNcitationsTcitations(number_of_coauths, newCitations, len(title_list))

		total_normalized_papers= myvar[0]

		normalized_citations= myvar[1]

		total_citations= myvar[2]

		total_normalized_citations= int(sum(normalized_citations))
		#normalized_h_index= int(sum(n_citations)/len(title_list))

		nn_citations= normalized_citations[0:total_normalized_papers]
		nn_citations.sort(reverse= True)

		for i in nn_citations:
			ncounter+= 1
			if(ncounter> i):
				normalized_h_index= ncounter-1
				break

		Simple_Metrics_object= Simple_Metrics()
		h_index= Simple_Metrics_object.h_index(newCitations)
		g_index= Simple_Metrics_object.g_index(newCitations)
		m_index= Simple_Metrics_object.m_index(h_index, min(year_list))
		o_index= Simple_Metrics_object.o_index(h_index,max(newCitations))
		h_median= Simple_Metrics_object.h_median(h_index,newCitations)
		TNCc= Simple_Metrics_object.TNCc(total_normalized_citations, self.country)
		print (TNCc)

		q= ScholarProfile(author_name= scholar_name, Company= company, Website= website, normalized_citations= normalized_citations, profile_url= user, publication_title= title_list, citations=newCitations,
			coAuthors=number_of_coauths, country=self.country, Hmedian=h_median, Oindex= o_index, TNCc= TNCc, publications= len(title_list),Tcitations= total_citations, Year= YEARS, Gindex= g_index, Hindex= h_index, Mindex= m_index, created_at= timezone.now())
		q.save()

		return (user)
