from django import forms
from .SCI import get_df

class IndexForm(forms.Form):
	scholar_url = forms.URLField(widget=forms.URLInput(
		attrs={
				'class': 'form-control',
		}
	))
	max_approx_publications = forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
		}
	))

	df=get_df()
	Country_list= [tuple([x,x]) for x in df["Country"]]
	Country_list.sort()
	country = forms.CharField(widget=forms.Select(choices= Country_list,
		attrs={
				'class': 'form-control',
		}
	))																			#forms.Select(choices=Country_list)))

class SearchForm(forms.Form):
	search= forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'search for a scholar...'
		}
	)) 

	