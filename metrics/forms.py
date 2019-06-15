from django import forms

class IndexForm(forms.Form):
	scholar_url = forms.URLField(widget=forms.URLInput(
		attrs={
				'class': 'form-control',
				'placeholder': 'your google scholar profile url...',
		}
	))
	max_approx_publications = forms.IntegerField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
		}
	))
	country = forms.CharField(widget=forms.TextInput(
		attrs={
				'class': 'form-control',
		}
	))

class SearchForm(forms.Form):
	search= forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'search for a scholar...'
		}
	)) 