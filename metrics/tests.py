from django.test import TestCase
from .newmetrics import ScholarRawData, Simple_Metrics
# Create your tests here.

class TestScholar(TestCase):
	def test_rawauthorscounterurl(self):
		raw_list=["abcdsds", "rewncjd", "ksdfhbc", "ksdjfcn...","ksdjfn", "dancj..."]
		obj=ScholarRawData()
		print ('sdfjv')
		counter_urls=obj.rawauthorscounterurl(raw_list)
		self.assertEqual(counter_urls,[3,5])

	#def test_seleniumScraper():

	#def test_getNpapersNcitationsTcitations():
	#def test_CoAuthors():
