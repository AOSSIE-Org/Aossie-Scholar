from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic.list import ListView

from metrics.forms import IndexForm, SearchForm

from .scrap import Scraper

from django.http import HttpResponseRedirect

from django.urls import reverse

from .models import ScholarProfile


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
			p_url= z.f()
			key= p_url[-18:]

			return HttpResponseRedirect(reverse('metrics:results', args= (key,)))

class ResultView(ListView):
	model = ScholarProfile
	template_name= 'metrics/profile.html'
	paginate_by= 100
	
	def get(self, request, scholar_url):
		scholar_object= ScholarProfile.objects.get(profile_url= scholar_url)
		publications= scholar_object.publication_title
		scholar_name= scholar_object.author_name
		print ('b')
		return (render (request, self.template_name, {'Name': scholar_name, 'list': publications}))
		


		#searchform = SearchForm(request.POST)
		#if searchform.is_valid():


