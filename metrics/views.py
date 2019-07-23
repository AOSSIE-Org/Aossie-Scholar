from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic.list import ListView

from metrics.forms import IndexForm, SearchForm

from .scrap import Scraper

from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import ScholarProfile

from .metrictables import NameTable

from django_tables2 import RequestConfig
from django_tables2.paginators import LazyPaginator
from .fusioncharts import FusionCharts


class HomeView(TemplateView):
	template_name = 'metrics/home.html'

	def get(self, request):
		index_form = IndexForm
		search_form = SearchForm
		return render(request, self.template_name, {'indexform': index_form, 'searchform': search_form})

	def post(self, request):
		indexform = IndexForm(request.POST)
		if indexform.is_valid():
			text1 = indexform.cleaned_data['scholar_url']
			text2 = indexform.cleaned_data['max_approx_publications']
			text3 = indexform.cleaned_data['country']
			print(text1, text2, text3)
			z= Scraper(text1, text2, text3)
			key= z.getScholarData()

			return HttpResponseRedirect(reverse('metrics:results', args= (key,)))

class ResultView(ListView):
	model = ScholarProfile
	template_name= 'metrics/profile.html'
	paginate_by= 100
	
	def get(self, request, scholar_url):
		scholar_object= ScholarProfile.objects.get(profile_url= scholar_url)
		country= scholar_object.country
		company= scholar_object.Company
		website=scholar_object.Website
		t_publications= scholar_object.publications
		t_citations= scholar_object.Tcitations
		Year= scholar_object.Year
		g_index= scholar_object.Gindex
		h_index= scholar_object.Hindex
		m_index= scholar_object.Mindex
		publications= scholar_object.publication_title
		scholar_name= scholar_object.author_name
		search_form= SearchForm
		dlist=[]


		chartObj = FusionCharts( 'column2d', 'ex1', '600', '400', 'chart-1', 'json', """{
			  "chart": {
			    "caption": "Countries With Most Oil Reserves [2017-18]",
			    "subcaption": "In MMbbl = One Million barrels",
			    "xaxisname": "Country",
			    "yaxisname": "Reserves (MMbbl)",
			    "numbersuffix": "K",
			    "theme": "fusion"
				  },
				  "data": [
				    {
				      "label": "Venezuela",
				      "value": "290"
				    },
				    {
				      "label": "Saudi",
				      "value": "260"
				    },
				    {
				      "label": "Canada",
				      "value": "180"
				    },
				    {
				      "label": "Iran",
				      "value": "140"
				    },
				    {
				      "label": "Russia",
				      "value": "115"
				    },
				    {
				      "label": "UAE",
				      "value": "100"
				    },
				    {
				      "label": "US",
				      "value": "30"
				    },
				    {
				      "label": "China",
				      "value": "30"
				    }
				  ]
				}""")

		for i, j, k, l, m in zip(publications, scholar_object.normalized_citations, scholar_object.citations, scholar_object.coAuthors, Year):
			d={}
			d["Title"]= i
			d["Ncitations"]= j
			d["Citations"]= k
			d["CoAuthors"]= l
			d["Year"]= m
			dlist.append(d)

		table= NameTable(dlist)

		RequestConfig(request, paginate={'paginator_class': LazyPaginator}).configure(table)

		#table.paginate(page=request.GET.get('page', 1), per_page=25)

		img_url="https://scholar.google.com.au/citations?view_op=view_photo&user="+scholar_url+"&citpid=2"

		gpath= '/static/metrics/images/'+scholar_url+'.png'

		return (render (request, self.template_name, {'Name': scholar_name, 'user': gpath,
		 'list': publications, 'searchform': search_form, 'img_url': img_url, 'table': table, 
		 'company': company, 'website':website, 'Country': country, 'publications': t_publications, 
		 'Tcitations': t_citations, 'g_index': g_index, 'h_index': h_index, 'm_index': m_index, 'output': chartObj.render()}))
		
