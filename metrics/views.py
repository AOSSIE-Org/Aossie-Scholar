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

from .graphs import Graph

from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import scholarly



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
		o_index= scholar_object.Oindex
		e_index= scholar_object.Eindex
		h_median= scholar_object.Hmedian
		tncc= scholar_object.TNCc
		publications= scholar_object.publication_title
		scholar_name= scholar_object.author_name
		search_form= SearchForm

		table= NameTable.createtable(publications, scholar_object.normalized_citations, scholar_object.citations, scholar_object.coAuthors, Year)

		table.paginate(page=request.GET.get('page', 1), per_page=100)
#RequestConfig(request, paginate={'paginator_class': LazyPaginator}).configure(table)				table.paginate(page=request.GET.get('page', 1), per_page=25)

		chartObj= Graph.histFusionchart(scholar_object.citations)

		img_url="https://scholar.google.com.au/citations?view_op=view_photo&user="+scholar_url+"&citpid=2"
		user= "url 'metrics:results' scholar_url={}".format(scholar_url)

		return (render (request, self.template_name, {'Name': scholar_name, 'user': scholar_url,
		 'list': publications, 'searchform': search_form, 'img_url': img_url, 'table': table, 
		 'company': company, 'website':website, 'Country': country, 'publications': t_publications, 
		 'Tcitations': t_citations, 'g_index': g_index, 'e_index': e_index, 'h_index': h_index, 'h_median': h_median, 'm_index': m_index, 'o_index': o_index, 'TNCc': tncc, 'output': chartObj.render()}))
		



class SearchResultsView(ListView):
    template_name = 'metrics/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get("search")
        context['input'] = q
        return context

    def get_queryset(self): 
        query = self.request.GET.get('search')
        object_list = ScholarProfile.objects.filter(
            Q(author_name__icontains=query) #| Q(state__icontains=query)
        )
        return object_list



class InfoPageView(TemplateView):
	template_name= 'metrics/info.html'

	def get(self, request):
		return (render(request, self.template_name, {}))

def author_search(request):
  if request.method == 'POST':
    author_name = request.POST.get('authorname')
    numbers_list = range(1, 1000)
    page = request.GET.get('page', 1)
    paginator = Paginator(numbers_list, 10)
    try:
      search_query = next(scholarly.search_author(author_name), 1).fill()
      numbers = paginator.page(page)
      pub_title = [(search_query.publications[i].bib['title']) for i in range(20)]
      pub_url = list()
      pub_author = list()
      pub_abstract = list()
      #pub_journal = list()
      pub_publisher = list()
      pub_year = list()
      pub_source = list()
      for title in pub_title:
        publication_search_query = next(scholarly.search_pubs_query(title))
        pub_url.append(publication_search_query.bib['url'])
        pub_abstract.append(publication_search_query.bib['abstract'])
        pub_author.append(publication_search_query.bib['author'])
        pub_source.append(publication_search_query.source)
      final_url = zip(pub_title, pub_author, pub_abstract,pub_source, pub_url)
      mycontext = {
        'filled': search_query._filled,
        'affiliation': search_query.affiliation,
        'email': search_query.email,
        'id': search_query.id,
        'interests': search_query.interests,
        'citedby': search_query.citedby,
        'name': search_query.name,
        'url_picture': search_query.url_picture,
        'publications': search_query.publications,
        'total_publications': len(search_query.publications),
        'l' : [i for i in range(len(search_query.publications))],
        'final_url': final_url,
        'numbers' : numbers,
        'row':0
			}
      return render(request, 'metrics/author_search_result.html', mycontext)
    except PageNotAnInteger:
      numbers = paginator.page(1)
      return render(request, 'metrics/author_search_result.html', {'numbers': numbers})
    except EmptyPage:
      numbers = paginator.page(paginator.num_pages)
      return render(request, 'metrics/author_search_result.html', {'numbers': numbers})
  else:
    return render(request, 'metrics/index.html', {})
