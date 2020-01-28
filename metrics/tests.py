from django.test import TestCase
from .newmetrics import ScholarRawData, Simple_Metrics
from metrics.scrap import Scraper
# Create your tests here.
urls=['abcdskfb', 'sdkjcnvc ds','kjsdnckj','https://scholar.google.com/citations?user=zD0vtfwAAAAJ&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3DzD0vtfwAAAAJ%26citation_for_view%3DzD0vtfwAAAAJ%3Au5HHmVD_uO8C%26tzom%3D-330','dhaksc ',
'https://scholar.google.com/citations?user=zD0vtfwAAAAJ&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3DzD0vtfwAAAAJ%26citation_for_view%3DzD0vtfwAAAAJ%3Au-x6o8ySG0sC%26tzom%3D-330','ksdfn ',
'https://scholar.google.com/citations?user=zD0vtfwAAAAJ&hl=en#d=gs_md_cita-d&u=%2Fcitations%3Fview_op%3Dview_citation%26hl%3Den%26user%3DzD0vtfwAAAAJ%26citation_for_view%3DzD0vtfwAAAAJ%3A9yKSN-GCB0IC%26tzom%3D-330']

raw_list=["Edward", "Bruno Woltz", "Bruno,Asim,Edward", "Edward...","ks,djfn", "dancj...","skjd,vb", "skdjbc..."]


class TestScholar(TestCase):

	def test_ScholarRawData(self):
		obj=ScholarRawData()
		counter_urls=obj.rawauthorscounterurl(raw_list)
		self.assertEqual(counter_urls,[3,5,7])

	def test_counter_urls(self):
		obj=ScholarRawData()
		coAuths=obj.seleniumScraper(urls,[3,5,7])
		self.assertEqual(coAuths,[13,17,10])

	def test_coAuthors(self):
		obj=ScholarRawData()
		Authors_counts=obj.coAuthors(raw_list, [13,17,10])
		self.assertEqual(Authors_counts,[1,1,3,13,2,17,2,10])

class TestScraper(TestCase):

	def test_getData(self):
		obj=Scraper('https://scholar.google.com/citations?user=zD0vtfwAAAAJ&hl=en',400)
		obj.getScholarData()
		self.assertEqual(obj.total_citations, 3791)
		self.assertEqual(obj.first_pub_year, 1993)

		

		

	#def test_seleniumScraper(self):
	#	obj=ScholarRawData()
	#	coAuths=obj.seleniumScraper(urls,[3,5,7])
	#	self.assertEqual(coAuths,[13,17,10])

#	def test_CoAuthors(self):
#		authors=['a','a,b','a,sd,...']
#		obj=ScholarRawData()


	
		

#def test_getNpapersNcitationsTcitations():